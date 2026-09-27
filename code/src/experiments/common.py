"""Shared experiment reporting helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.fairness.metrics import group_metrics, pairwise_gaps


def summarize_decisions(frame: pd.DataFrame) -> dict:
    pre = group_metrics(frame["y"], frame["d0"], frame["group"])
    post = group_metrics(frame["y"], frame["d1"], frame["group"])
    contestability = {}
    for group, part in frame.groupby("group", sort=True):
        adverse = part[part["d0"] == 0]
        appealed = adverse[adverse["appeal"] == 1]
        contestability[str(group)] = {
            "appeal_rate_among_adverse": float(adverse["appeal"].mean()) if len(adverse) else float("nan"),
            "reversal_rate_among_appeals": float(appealed["review_reversal"].mean()) if len(appealed) else float("nan"),
            "appeals_processed": int(appealed.shape[0]),
            "successful_corrections": int(((appealed["y"] == 1) & (appealed["review_reversal"] == 1)).sum()),
            "false_reversals": int(((appealed["y"] == 0) & (appealed["review_reversal"] == 1)).sum()),
        }
    return {"pre": pre, "post": post, "pre_gaps": pairwise_gaps(pre), "post_gaps": pairwise_gaps(post), "contestation": contestability}


def write_records(records: list[dict], output: str | Path) -> None:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.json_normalize(records).to_csv(path, index=False)

