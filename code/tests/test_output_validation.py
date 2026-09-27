from __future__ import annotations

import pandas as pd

from scripts.validate_outputs import validate


def _realdata_row(stage: str) -> dict:
    return {
        "experiment_id": "REALDATA",
        "experiment_type": "SEMISYNTHETIC REAL-DATA EXPERIMENT",
        "seed": 1729,
        "metric": "equal_opportunity_gap",
        "value": 0.1,
        "dataset": "adult",
        "group": "ALL",
        "model": "logistic",
        "method": "group_threshold_calibrated",
        "decision_stage": stage,
    }


def test_validator_distinguishes_pre_and_post_decision_stages(tmp_path):
    target = tmp_path / "standardized" / "realdata"
    target.mkdir(parents=True)
    pd.DataFrame([_realdata_row("pre"), _realdata_row("post")]).to_csv(
        target / "result.csv", index=False
    )

    report = validate(tmp_path)

    assert report["status"] == "PASS"
    assert report["errors"] == []


def test_validator_still_rejects_true_duplicates(tmp_path):
    target = tmp_path / "standardized" / "realdata"
    target.mkdir(parents=True)
    row = _realdata_row("post")
    pd.DataFrame([row, row]).to_csv(target / "result.csv", index=False)

    report = validate(tmp_path)

    assert report["status"] == "FAIL"
    assert "duplicate standardized result rows" in report["errors"]
