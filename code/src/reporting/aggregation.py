"""Aggregate actual standardized outputs without hardcoded results."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


OUTPUT_GROUPS = {
    "theorem_validation.csv": {"THEOREM", "EXP-10"},
    "core_synthetic.csv": {"EXP-01", "EXP-02", "EXP-03", "EXP-05"},
    "resource_allocation.csv": {"EXP-04"},
    "identification.csv": {"EXP-06", "EXP-07"},
    "auditing.csv": {"EXP-08"},
    "realdata.csv": {"REALDATA"},
    "robustness.csv": {"EXP-09"},
}


def _read_standardized(root: Path) -> pd.DataFrame:
    files = sorted((root / "standardized").rglob("*.csv"))
    if not files:
        raise FileNotFoundError(f"no standardized result CSVs under {root / 'standardized'}")
    return pd.concat((pd.read_csv(path) for path in files), ignore_index=True, sort=False)


def aggregate_all(root: Path) -> list[Path]:
    root = root.resolve()
    frame = _read_standardized(root)
    frame["value"] = pd.to_numeric(frame["value"], errors="coerce")
    keys = [column for column in ("experiment_id", "experiment_type", "configuration", "dataset", "group", "model", "method", "decision_stage", "contestation_scenario", "parameter_key", "parameter_json", "metric") if column in frame]
    aggregate = frame.groupby(keys, dropna=False)["value"].agg(["count", "mean", "std"]).reset_index()
    aggregate["standard_error"] = aggregate["std"] / aggregate["count"].pow(0.5)
    aggregate["ci95_lower"] = aggregate["mean"] - 1.96 * aggregate["standard_error"]
    aggregate["ci95_upper"] = aggregate["mean"] + 1.96 * aggregate["standard_error"]
    target = root / "aggregate"
    target.mkdir(parents=True, exist_ok=True)
    written = []
    for filename, experiments in OUTPUT_GROUPS.items():
        subset = aggregate[aggregate["experiment_id"].isin(experiments)]
        path = target / filename
        subset.to_csv(path, index=False)
        written.append(path)
    return written
