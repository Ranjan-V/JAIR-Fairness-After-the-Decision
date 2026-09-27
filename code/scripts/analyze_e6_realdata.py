"""Paired-seed audit for the E6 semisynthetic real-data gate.

This script consumes the standardized REALDATA CSV files and reports confidence
intervals for pre/post metrics and their paired changes.  It does not rerun a
classifier or a contestation simulation.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import pandas as pd
from scipy.stats import t


KEYS = ["dataset", "model", "contestation_scenario"]
EXPECTED_DATASETS = {"adult", "german"}
EXPECTED_MODELS = {"logistic", "gradient_boosting", "random_forest"}
EXPECTED_SCENARIOS = {
    "equal_access",
    "moderate_first_group",
    "moderate_second_group",
    "strong_first_group",
    "strong_second_group",
}


def _mean_ci(values: pd.Series) -> tuple[int, float, float, float, float]:
    clean = pd.to_numeric(values, errors="coerce").dropna()
    n = int(clean.size)
    if not n:
        return 0, math.nan, math.nan, math.nan, math.nan
    mean = float(clean.mean())
    sd = float(clean.std(ddof=1)) if n > 1 else 0.0
    half = float(t.ppf(0.975, n - 1) * sd / math.sqrt(n)) if n > 1 else 0.0
    return n, mean, sd, mean - half, mean + half


def _load(input_dir: Path) -> pd.DataFrame:
    paths = sorted(input_dir.glob("*.csv"))
    if len(paths) != 600:
        raise ValueError(f"Expected 600 real-data CSVs; found {len(paths)} in {input_dir}")
    frame = pd.concat((pd.read_csv(path) for path in paths), ignore_index=True)
    observed = {
        "datasets": set(frame["dataset"].dropna().unique()),
        "models": set(frame["model"].dropna().unique()),
        "scenarios": set(frame["contestation_scenario"].dropna().unique()),
        "seeds": set(pd.to_numeric(frame["seed"], errors="raise").astype(int).unique()),
    }
    expected_seeds = set(range(1729, 1749))
    expected = {
        "datasets": EXPECTED_DATASETS,
        "models": EXPECTED_MODELS,
        "scenarios": EXPECTED_SCENARIOS,
        "seeds": expected_seeds,
    }
    for key, expected_values in expected.items():
        if observed[key] != expected_values:
            raise ValueError(f"Unexpected {key}: {sorted(observed[key])}; expected {sorted(expected_values)}")
    combinations = frame[[*KEYS, "seed"]].drop_duplicates()
    if len(combinations) != 600 or combinations.duplicated().any():
        raise ValueError("Dataset/model/scenario/seed design is incomplete or duplicated")
    return frame


def _paired_summary(frame: pd.DataFrame, group: str, metric: str) -> pd.DataFrame:
    selected = frame[(frame["group"] == group) & (frame["metric"] == metric)].copy()
    wide = selected.pivot_table(
        index=[*KEYS, "seed"], columns="decision_stage", values="value", aggfunc="first"
    ).reset_index()
    if not {"pre", "post"}.issubset(wide.columns):
        raise ValueError(f"Missing pre/post values for {group}/{metric}")
    wide["delta"] = wide["post"] - wide["pre"]
    records: list[dict[str, object]] = []
    for key, part in wide.groupby(KEYS, sort=True):
        record: dict[str, object] = dict(zip(KEYS, key, strict=True))
        record.update({"group": group, "metric": metric})
        for column in ("pre", "post", "delta"):
            n, mean, sd, lower, upper = _mean_ci(part[column])
            record.update(
                {
                    f"{column}_n": n,
                    f"{column}_mean": mean,
                    f"{column}_sd": sd,
                    f"{column}_ci95_lower": lower,
                    f"{column}_ci95_upper": upper,
                }
            )
        record["delta_positive_fraction"] = float((part["delta"] > 0).mean())
        record["delta_negative_fraction"] = float((part["delta"] < 0).mean())
        delta_sd = float(part["delta"].std(ddof=1))
        record["paired_effect_size_dz"] = (
            float(part["delta"].mean()) / delta_sd if delta_sd > 0 else math.nan
        )
        records.append(record)
    return pd.DataFrame.from_records(records)


def _weighted_accuracy_summary(frame: pd.DataFrame) -> pd.DataFrame:
    groups = frame[~frame["group"].isin(["ALL", "Female_minus_Male"])]
    selected = groups[groups["metric"].isin(["n", "accuracy"])]
    wide = selected.pivot_table(
        index=[*KEYS, "seed", "group", "decision_stage"],
        columns="metric",
        values="value",
        aggfunc="first",
    ).reset_index()
    wide["correct"] = wide["n"] * wide["accuracy"]
    overall = (
        wide.groupby([*KEYS, "seed", "decision_stage"], as_index=False)
        .agg(correct=("correct", "sum"), n=("n", "sum"))
    )
    overall["value"] = overall["correct"] / overall["n"]
    synthetic = overall.assign(group="ALL", metric="overall_accuracy")
    return _paired_summary(synthetic, "ALL", "overall_accuracy")


def _write_markdown(summary: pd.DataFrame, target: Path) -> None:
    eo = summary[(summary["group"] == "ALL") & (summary["metric"] == "equal_opportunity_gap")]
    lines = [
        "# E6 paired-seed analysis",
        "",
        "All intervals are two-sided 95% Student-t intervals across the 20 paired seeds.",
        "Positive delta means the absolute equal-opportunity gap increased after contestation.",
        "",
        "| Dataset | Model | Scenario | Pre EO gap | Post EO gap | Paired change (95% CI) | Positive seeds |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in eo.sort_values(KEYS).itertuples(index=False):
        lines.append(
            f"| {row.dataset} | {row.model} | {row.contestation_scenario} "
            f"| {row.pre_mean:.4f} | {row.post_mean:.4f} "
            f"| {row.delta_mean:+.4f} [{row.delta_ci95_lower:+.4f}, {row.delta_ci95_upper:+.4f}] "
            f"| {row.delta_positive_fraction:.0%} |"
        )
    lines.extend(["", "## Variability comparison", ""])
    for dataset, part in eo.groupby("dataset"):
        unequal = part[part["contestation_scenario"] != "equal_access"]
        lines.append(
            f"- **{dataset}:** median paired-change SD {unequal['delta_sd'].median():.4f}; "
            f"range {unequal['delta_sd'].min():.4f}--{unequal['delta_sd'].max():.4f}."
        )
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    frame = _load(args.input_dir.resolve())
    summaries = [
        _paired_summary(frame, "ALL", metric)
        for metric in ("equal_opportunity_gap", "fpr_gap", "equalized_odds_gap", "demographic_parity_gap")
    ]
    summaries.extend(
        _paired_summary(frame, "Female_minus_Male", metric)
        for metric in ("signed_equal_opportunity_gap", "signed_fpr_gap")
    )
    summaries.append(_weighted_accuracy_summary(frame))
    summary = pd.concat(summaries, ignore_index=True)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_dir / "e6_paired_summary.csv"
    markdown_path = args.output_dir / "E6_PAIRED_ANALYSIS.md"
    metadata_path = args.output_dir / "e6_analysis_metadata.json"
    summary.to_csv(csv_path, index=False)
    _write_markdown(summary, markdown_path)
    metadata = {
        "source_csv_count": 600,
        "datasets": sorted(EXPECTED_DATASETS),
        "models": sorted(EXPECTED_MODELS),
        "scenarios": sorted(EXPECTED_SCENARIOS),
        "seeds": list(range(1729, 1749)),
        "confidence_interval": "two-sided 95% Student-t interval across paired seeds",
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(csv_path)
    print(markdown_path)


if __name__ == "__main__":
    main()
