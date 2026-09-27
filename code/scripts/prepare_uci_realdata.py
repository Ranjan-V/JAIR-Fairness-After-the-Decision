"""Prepare the official UCI Adult and German Credit files for EXP-REALDATA.

This script performs deterministic schema conversion only. It does not
download data. The semisynthetic contestation mechanism is applied later by
``src.experiments.realdata_semisynthetic``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd


ADULT_COLUMNS = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income",
]

GERMAN_COLUMNS = [
    "checking_status",
    "duration_months",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_status",
    "employment_status",
    "installment_rate",
    "personal_status_sex",
    "other_debtors",
    "residence_years",
    "property",
    "age_years",
    "other_installment_plans",
    "housing",
    "existing_credits",
    "job",
    "dependents",
    "telephone",
    "foreign_worker",
    "credit_risk",
]

FEMALE_GERMAN_CODES = {"A92", "A95"}
MALE_GERMAN_CODES = {"A91", "A93", "A94"}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def prepare_adult(raw_dir: Path) -> pd.DataFrame:
    train = pd.read_csv(
        raw_dir / "adult.data",
        names=ADULT_COLUMNS,
        skipinitialspace=True,
        na_values="?",
    )
    test = pd.read_csv(
        raw_dir / "adult.test",
        names=ADULT_COLUMNS,
        skipinitialspace=True,
        na_values="?",
        comment="|",
    )
    frame = pd.concat([train, test], ignore_index=True)
    frame["income"] = (
        frame["income"].astype(str).str.strip().str.rstrip(".").eq(">50K").astype(int)
    )
    frame["sex"] = frame["sex"].astype(str).str.strip()
    if len(frame) != 48_842 or set(frame["income"]) != {0, 1}:
        raise ValueError("Adult conversion failed row-count or label validation")
    if set(frame["sex"]) != {"Female", "Male"}:
        raise ValueError("Adult conversion produced unexpected sex groups")
    return frame


def prepare_german(raw_dir: Path) -> pd.DataFrame:
    frame = pd.read_csv(
        raw_dir / "german.data",
        sep=r"\s+",
        names=GERMAN_COLUMNS,
    )
    codes = set(frame["personal_status_sex"].astype(str))
    expected = FEMALE_GERMAN_CODES | MALE_GERMAN_CODES
    if not codes <= expected:
        raise ValueError(f"German conversion found undocumented sex codes: {sorted(codes - expected)}")
    frame["sex"] = frame["personal_status_sex"].map(
        lambda value: "Female" if value in FEMALE_GERMAN_CODES else "Male"
    )
    # UCI uses 1=good and 2=bad. The favorable decision is therefore 1.
    frame["credit_risk"] = frame["credit_risk"].eq(1).astype(int)
    frame = frame.drop(columns=["personal_status_sex"])
    if len(frame) != 1_000 or set(frame["credit_risk"]) != {0, 1}:
        raise ValueError("German conversion failed row-count or label validation")
    if set(frame["sex"]) != {"Female", "Male"}:
        raise ValueError("German conversion produced unexpected sex groups")
    return frame


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--uci-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    root = args.uci_root.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)

    adult = prepare_adult(root / "adult")
    german = prepare_german(root / "german")
    adult_path = output / "adult.csv"
    german_path = output / "german_credit.csv"
    adult.to_csv(adult_path, index=False)
    german.to_csv(german_path, index=False)

    metadata = {
        "adult": {
            "citation": "Becker, B. & Kohavi, R. (1996). Adult. UCI ML Repository.",
            "doi": "10.24432/C5XW20",
            "license": "CC BY 4.0",
            "rows": len(adult),
            "prepared_sha256": _sha256(adult_path),
        },
        "german": {
            "citation": "Hofmann, H. (1994). Statlog (German Credit Data). UCI ML Repository.",
            "doi": "10.24432/C5NC77",
            "license": "CC BY 4.0",
            "rows": len(german),
            "prepared_sha256": _sha256(german_path),
        },
        "schema_note": "Sex is the protected group. Labels encode favorable outcomes as 1.",
    }
    (output / "provenance.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
