"""Closed-form target budgets from Proposition 6."""

from __future__ import annotations

import numpy as np

from src.contestation.costs import CostDistribution


def required_appeal_probability(fnr: float, review_success: float, epsilon: float) -> float:
    if not 0.0 <= fnr <= 1.0 or not 0.0 <= review_success <= 1.0 or epsilon < 0.0:
        raise ValueError("invalid probability or target")
    if fnr <= epsilon:
        return 0.0
    if review_success == 0.0:
        return float("inf")
    probability = (1.0 - epsilon / fnr) / review_success
    return float(probability) if probability <= 1.0 else float("inf")


def minimum_subsidy(
    distribution: CostDistribution,
    perceived_value: float,
    fnr: float,
    review_success: float,
    epsilon: float,
) -> float:
    """Minimum nonnegative assistance for one group, Proposition 6."""
    p = required_appeal_probability(fnr, review_success, epsilon)
    if not np.isfinite(p):
        return float("inf")
    threshold = float(distribution.ppf(p))
    return max(0.0, threshold - perceived_value)


def minimum_budget(subsidies, cost_functions) -> float:
    subsidies = list(map(float, subsidies))
    functions = list(cost_functions)
    if len(subsidies) != len(functions):
        raise ValueError("one cost function is required per subsidy")
    if any(not np.isfinite(value) for value in subsidies):
        return float("inf")
    return float(sum(fn(value) for fn, value in zip(functions, subsidies)))

