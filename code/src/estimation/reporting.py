"""Across-seed summaries and transparent effect sizes."""

from __future__ import annotations

import math

import pandas as pd


def summarize_seeds(frame: pd.DataFrame, group_columns: list[str], metric: str) -> pd.DataFrame:
    """Return count, mean, SD, SE, and normal-approximation 95% CI."""
    grouped = frame.groupby(group_columns, dropna=False)[metric]
    result = grouped.agg(["count", "mean", "std"]).reset_index()
    result["standard_error"] = result["std"] / result["count"].pow(0.5)
    result["ci95_lower"] = result["mean"] - 1.96 * result["standard_error"]
    result["ci95_upper"] = result["mean"] + 1.96 * result["standard_error"]
    return result


def standardized_mean_difference(a, b) -> float:
    """Cohen-style standardized difference with pooled sample variance."""
    a = pd.Series(a, dtype=float).dropna()
    b = pd.Series(b, dtype=float).dropna()
    if len(a) < 2 or len(b) < 2:
        raise ValueError("each sample needs at least two observations")
    pooled = math.sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
    if pooled == 0.0:
        return 0.0 if a.mean() == b.mean() else math.copysign(float("inf"), a.mean() - b.mean())
    return float((a.mean() - b.mean()) / pooled)
