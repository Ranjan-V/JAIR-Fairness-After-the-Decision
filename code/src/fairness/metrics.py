"""Predictive, group-fairness, and contestability metrics."""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np

from src.models.confusion import ConfusionRates


def group_metrics(y_true, decisions, groups) -> dict[str, dict[str, float]]:
    """Compute confusion rates without silently defining empty-condition rates."""
    y = np.asarray(y_true, dtype=int)
    d = np.asarray(decisions, dtype=int)
    g = np.asarray(groups)
    if not (len(y) == len(d) == len(g)):
        raise ValueError("inputs must have equal length")
    result: dict[str, dict[str, float]] = {}
    for group in np.unique(g):
        mask = g == group
        positive = mask & (y == 1)
        negative = mask & (y == 0)
        if positive.sum() == 0 or negative.sum() == 0:
            raise ValueError(f"group {group!r} lacks a label stratum")
        tpr = float(np.mean(d[positive] == 1))
        fpr = float(np.mean(d[negative] == 1))
        accuracy = float(np.mean(d[mask] == y[mask]))
        result[str(group)] = {
            "n": int(mask.sum()),
            "prevalence": float(np.mean(y[mask])),
            "accuracy": accuracy,
            "tpr": tpr,
            "fnr": 1.0 - tpr,
            "fpr": fpr,
            "tnr": 1.0 - fpr,
            "positive_rate": float(np.mean(d[mask] == 1)),
        }
    return result


def pairwise_gaps(metrics: Mapping[str, Mapping[str, float]]) -> dict[str, float]:
    """Return maximum pairwise absolute gaps across any number of groups."""
    if len(metrics) < 2:
        raise ValueError("at least two groups are required")
    def span(key: str) -> float:
        values = [float(item[key]) for item in metrics.values()]
        return max(values) - min(values)
    eo = span("tpr")
    fpr = span("fpr")
    return {
        "equal_opportunity_gap": eo,
        "fpr_gap": fpr,
        "equalized_odds_gap": max(eo, fpr),
        "demographic_parity_gap": span("positive_rate"),
    }


def signed_tpr_gap_after(
    tpr_a: float, tpr_b: float, kappa_a: float, kappa_b: float
) -> float:
    """Implement Theorem 5's exact signed gap."""
    return (tpr_a - tpr_b) + (1.0 - tpr_a) * kappa_a - (1.0 - tpr_b) * kappa_b


def demographic_parity_increment(rates: ConfusionRates, kappa_plus: float, kappa_minus: float) -> float:
    """Return the weighted increment in Theorem 4."""
    return (
        rates.prevalence * rates.fnr * kappa_plus
        + (1.0 - rates.prevalence) * rates.tnr * kappa_minus
    )

