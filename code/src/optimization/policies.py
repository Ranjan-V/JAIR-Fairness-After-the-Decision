"""Allocation baselines B0--B6."""

from __future__ import annotations

import numpy as np


def no_subsidy(groups: int) -> np.ndarray:
    return np.zeros(groups)


def uniform_subsidy(groups: int, budget: float) -> np.ndarray:
    if groups <= 0 or budget < 0:
        raise ValueError("invalid group count or budget")
    return np.full(groups, budget / groups)


def proportional_subsidy(weights, budget: float) -> np.ndarray:
    weights = np.asarray(weights, dtype=float)
    if budget < 0 or np.any(weights < 0.0) or weights.sum() <= 0.0:
        raise ValueError("invalid weights or budget")
    return budget * weights / weights.sum()


def random_subsidy(groups: int, budget: float, seed: int) -> np.ndarray:
    if groups <= 0 or budget < 0:
        raise ValueError("invalid group count or budget")
    shares = np.random.default_rng(seed).dirichlet(np.ones(groups))
    return budget * shares


def expected_corrections_allocation(marginal_corrections, budget: float) -> np.ndarray:
    """B4: allocate all divisible budget to the best initial correction return."""
    values = np.asarray(marginal_corrections, dtype=float)
    if budget < 0 or values.size == 0:
        raise ValueError("invalid inputs")
    result = np.zeros_like(values)
    result[int(np.argmax(values))] = budget
    return result

