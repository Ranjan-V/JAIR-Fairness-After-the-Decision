"""Build JAIR/EXPERIMENT_RESULTS_SUMMARY.md from actual manifests and outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


def _aggregate_status(root: Path) -> tuple[str, list[str]]:
    manifest_path = root / "run_manifest.json"
    if not manifest_path.exists():
        return "NOT_RUN", []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    statuses = pd.Series([item.get("status", "UNKNOWN") for item in manifest.get("runs", {}).values()]).value_counts()
    summary = ", ".join(f"{key}={value}" for key, value in statuses.items()) or "MISSING"
    failures = [run_id for run_id, item in manifest.get("runs", {}).items() if item.get("status") == "FAILED"]
    return summary, failures


def _metric_summary(path: Path, metrics: list[str]) -> str:
    if not path.exists():
        return "NOT_RUN"
    frame = pd.read_csv(path)
    if frame.empty:
        return "MISSING"
    subset = frame[frame["metric"].isin(metrics)]
    if subset.empty:
        return "MISSING"
    lines = []
    for metric, part in subset.groupby("metric"):
        values = pd.to_numeric(part["mean"], errors="coerce").dropna()
        lines.append(f"- {metric}: rows={len(part)}, range=[{values.min():.6g}, {values.max():.6g}]" if len(values) else f"- {metric}: MISSING")
    return "\n".join(lines)


def build(output_root: Path, project_root: Path) -> Path:
    aggregate = output_root / "aggregate"
    run_status, failures = _aggregate_status(output_root)
    validation_path = output_root / "validation_report.json"
    validation = json.loads(validation_path.read_text(encoding="utf-8")) if validation_path.exists() else None
    text = [
        "# Experiment results summary",
        "",
        "> Generated only from files present on disk. Missing stages are labeled NOT_RUN or MISSING.",
        "",
        "## Successful and failed runs",
        "",
        run_status,
        "",
        f"Failed run IDs: {', '.join(failures) if failures else ('none recorded' if run_status != 'NOT_RUN' else 'NOT_RUN')}",
        "",
        "## Theorem agreement",
        "",
        _metric_summary(aggregate / "theorem_validation.csv", ["absolute_error"]),
        "",
        "## Primary synthetic metrics",
        "",
        _metric_summary(aggregate / "core_synthetic.csv", ["empirical_value", "absolute_error", "post_fnr_a", "post_fnr_b", "eo_gap"]),
        "",
        "## Resource-allocation comparisons",
        "",
        _metric_summary(aggregate / "resource_allocation.csv", ["eo_gap", "mean_residual_fnr", "resource_used", "social_loss"]),
        "",
        "## Identification and auditing",
        "",
        _metric_summary(aggregate / "identification.csv", ["width", "coverage", "oracle_latent_fnr_difference"]),
        "",
        _metric_summary(aggregate / "auditing.csv", ["fnr_width", "coverage", "estimator_error"]),
        "",
        "## Robustness",
        "",
        _metric_summary(aggregate / "robustness.csv", ["predicted_pair_gap"]),
        "",
        "## Semisynthetic real-data results",
        "",
        _metric_summary(aggregate / "realdata.csv", ["equal_opportunity_gap", "equalized_odds_gap", "accuracy"]),
        "",
        "## Validation warnings",
        "",
        ("NOT_RUN" if validation is None else f"Status: {validation.get('status', 'MISSING')}\n\nErrors: {validation.get('errors', [])}\n\nWarnings: {validation.get('warnings', [])}"),
        "",
        "## Interpretation guardrails",
        "",
        "- Numerical theorem illustrations are not proofs.",
        "- Real-data contestation is semisynthetic, not observed appeal behavior.",
        "- Ranges above are descriptive inventory summaries, not claims of superiority.",
        "- Consult seed-level outputs and confidence intervals before drawing conclusions.",
    ]
    target = project_root / "EXPERIMENT_RESULTS_SUMMARY.md"
    target.write_text("\n".join(text) + "\n", encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    project_root = Path(__file__).resolve().parents[2]
    print(build(Path(args.output_dir).resolve(), project_root))


if __name__ == "__main__":
    main()

