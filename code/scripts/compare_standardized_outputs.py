"""Compare two standardized output trees by parsed content, not CSV bytes.

This avoids false mismatches caused only by platform-specific line endings.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def _paths(root: Path, exclude_subdir: set[str]) -> dict[str, Path]:
    return {
        str(path.relative_to(root)).replace("\\", "/"): path
        for path in root.rglob("*.csv")
        if not set(path.relative_to(root).parts).intersection(exclude_subdir)
    }


def compare(
    reference: Path,
    candidate: Path,
    atol: float,
    rtol: float,
    exclude_subdir: set[str],
    ignore_columns: set[str],
) -> dict:
    reference_files = _paths(reference, exclude_subdir)
    candidate_files = _paths(candidate, exclude_subdir)
    missing = sorted(set(reference_files) - set(candidate_files))
    unexpected = sorted(set(candidate_files) - set(reference_files))
    mismatches: list[dict[str, object]] = []
    max_abs_difference = 0.0

    for relative in sorted(set(reference_files) & set(candidate_files)):
        expected = pd.read_csv(reference_files[relative])
        observed = pd.read_csv(candidate_files[relative])
        if list(expected.columns) != list(observed.columns) or expected.shape != observed.shape:
            mismatches.append(
                {
                    "file": relative,
                    "reason": "schema_or_shape",
                    "reference_shape": list(expected.shape),
                    "candidate_shape": list(observed.shape),
                }
            )
            continue
        file_errors: list[str] = []
        for column in expected.columns:
            if column in ignore_columns:
                continue
            left, right = expected[column], observed[column]
            left_numeric = pd.to_numeric(left, errors="coerce")
            right_numeric = pd.to_numeric(right, errors="coerce")
            numeric_mask = left_numeric.notna() | right_numeric.notna()
            if numeric_mask.any():
                if not np.array_equal(left_numeric.isna(), right_numeric.isna()):
                    file_errors.append(f"{column}: missingness differs")
                    continue
                finite = left_numeric.notna() & right_numeric.notna()
                if finite.any():
                    left_values = left_numeric[finite].to_numpy(dtype=float)
                    right_values = right_numeric[finite].to_numpy(dtype=float)
                    differences = np.abs(left_values - right_values)
                    max_abs_difference = max(max_abs_difference, float(differences.max(initial=0.0)))
                    if not np.allclose(
                        left_values, right_values, atol=atol, rtol=rtol
                    ):
                        file_errors.append(f"{column}: numeric values differ")
            else:
                left_text = left.fillna("<NA>").astype(str)
                right_text = right.fillna("<NA>").astype(str)
                if not left_text.equals(right_text):
                    file_errors.append(f"{column}: text values differ")
        if file_errors:
            mismatches.append({"file": relative, "reason": "; ".join(file_errors)})

    return {
        "status": "PASS" if not (missing or unexpected or mismatches) else "FAIL",
        "reference_file_count": len(reference_files),
        "candidate_file_count": len(candidate_files),
        "missing_files": missing,
        "unexpected_files": unexpected,
        "content_mismatches": mismatches,
        "max_absolute_numeric_difference": max_abs_difference,
        "absolute_tolerance": atol,
        "relative_tolerance": rtol,
        "ignored_columns": sorted(ignore_columns),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--report-path", required=True, type=Path)
    parser.add_argument("--atol", type=float, default=1e-12)
    parser.add_argument("--rtol", type=float, default=1e-12)
    parser.add_argument("--exclude-subdir", action="append", default=[])
    parser.add_argument("--ignore-column", action="append", default=[])
    args = parser.parse_args()
    report = compare(
        args.reference.resolve(),
        args.candidate.resolve(),
        args.atol,
        args.rtol,
        set(args.exclude_subdir),
        set(args.ignore_column),
    )
    args.report_path.parent.mkdir(parents=True, exist_ok=True)
    args.report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
