"""Tight analytical disparity bounds from Theorem 6."""

from __future__ import annotations


def attainable_signed_tpr_gap(tpr_a: float, tpr_b: float) -> tuple[float, float]:
    """Return the tight interval over unrestricted effective corrections."""
    for value in (tpr_a, tpr_b):
        if not 0.0 <= value <= 1.0:
            raise ValueError("TPRs must lie in [0, 1]")
    return tpr_a - 1.0, 1.0 - tpr_b


def attainable_absolute_gap(tpr_a: float, tpr_b: float) -> tuple[float, float]:
    lower, upper = attainable_signed_tpr_gap(tpr_a, tpr_b)
    min_abs = 0.0 if lower <= 0.0 <= upper else min(abs(lower), abs(upper))
    max_abs = max(abs(lower), abs(upper))
    return min_abs, max_abs

