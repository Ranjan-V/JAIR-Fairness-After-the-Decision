"""Validate actual result files against structural and theorem-driven checks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


PROBABILITY_METRIC_TOKENS = ("rate", "tpr", "fnr", "fpr", "tnr", "coverage", "gap", "lower", "upper")


def validate(root: Path, expected_seeds: list[int] | None = None) -> dict:
    files = sorted((root / "standardized").rglob("*.csv"))
    errors, warnings = [], []
    if not files:
        return {"status": "FAIL", "errors": ["no standardized outputs"], "warnings": []}
    frame = pd.concat((pd.read_csv(path) for path in files), ignore_index=True, sort=False)
    required = {"experiment_id", "experiment_type", "seed", "metric", "value"}
    missing = required - set(frame)
    if missing:
        errors.append(f"missing required columns: {sorted(missing)}")
    # A real-data file contains the same metric for the pre- and
    # post-contestation decisions. ``decision_stage`` is therefore part of the
    # experimental identity whenever it is present.
    duplicate_keys = [
        column
        for column in (
            "experiment_id",
            "seed",
            "parameter_key",
            "decision_stage",
            "metric",
            "dataset",
            "group",
            "model",
            "method",
        )
        if column in frame
    ]
    if frame.duplicated(duplicate_keys).any():
        errors.append("duplicate standardized result rows")
    numeric = pd.to_numeric(frame["value"], errors="coerce")
    allowed_nan = (frame["experiment_id"] == "EXP-08") & (frame["metric"] == "estimator_error")
    if (numeric.isna() & ~allowed_nan).any():
        errors.append("unexpected NaN or nonnumeric metric value")
    if np.isinf(numeric.dropna()).any():
        errors.append("infinite metric value")
    probability = frame["metric"].astype(str).map(lambda name: any(token in name.lower() for token in PROBABILITY_METRIC_TOKENS))
    invalid_probability = probability & numeric.notna() & ((numeric < -1e-10) | (numeric > 1.0 + 1e-10))
    # Signed gaps are allowed in [-1,1].
    signed = frame["metric"].astype(str).str.contains("signed")
    invalid_probability &= ~signed
    if invalid_probability.any():
        errors.append("probability-like metrics outside [0,1]")
    allocation = frame[frame["experiment_id"] == "EXP-04"].copy()
    if not allocation.empty and "budget" in allocation:
        used = allocation[allocation["metric"] == "resource_used"]
        if (pd.to_numeric(used["value"]) > pd.to_numeric(used["budget"]) + 1e-7).any():
            errors.append("allocation budget violation")
    coverage = frame[frame["metric"] == "coverage"]
    if not coverage.empty and not set(pd.to_numeric(coverage["value"].dropna()).unique()).issubset({0.0, 1.0}):
        errors.append("coverage values are not binary")
    exp10_files = list((root / "raw" / "exp-10").glob("*.csv"))
    for path in exp10_files:
        boundary = pd.read_csv(path)
        if not np.allclose(boundary["post_fnr_plus_tpr"], 1.0) or not np.allclose(boundary["post_tnr_plus_fpr"], 1.0):
            errors.append(f"impossible confusion rates in {path}")
    if expected_seeds is not None:
        observed = set(pd.to_numeric(frame["seed"], errors="coerce").dropna().astype(int))
        missing_seeds = set(expected_seeds) - observed
        if missing_seeds:
            warnings.append(f"missing seeds: {sorted(missing_seeds)}")
    return {"status": "PASS" if not errors else "FAIL", "errors": errors, "warnings": warnings, "files_checked": [str(path) for path in files]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--expected-seeds", nargs="*", type=int)
    parser.add_argument(
        "--report-path",
        help="Optional report destination, allowing read-only validation of an archived output tree.",
    )
    args = parser.parse_args()
    root = Path(args.output_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)
    report = validate(root, args.expected_seeds)
    target = Path(args.report_path).resolve() if args.report_path else root / "validation_report.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
