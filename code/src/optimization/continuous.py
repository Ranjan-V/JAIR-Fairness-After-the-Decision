"""Continuous resource allocation for Theorems 9--11."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize


@dataclass(frozen=True)
class AllocationResult:
    allocation: np.ndarray
    residuals: np.ndarray
    resource_used: float
    objective: float
    success: bool
    message: str


def _validate_problem(n: int, budget: float, upper_bounds: Sequence[float]) -> np.ndarray:
    bounds = np.asarray(upper_bounds, dtype=float)
    if len(bounds) != n or np.any(bounds < 0.0):
        raise ValueError("upper_bounds must be nonnegative and match group count")
    if budget < 0.0:
        raise ValueError("budget must be nonnegative")
    return bounds


def solve_minimax(
    residual_functions: Sequence[Callable[[float], float]],
    cost_functions: Sequence[Callable[[float], float]],
    budget: float,
    upper_bounds: Sequence[float],
) -> AllocationResult:
    """Solve Theorem 10's minimax epigraph program using SLSQP.

    Convex guarantees require the caller to supply functions satisfying the
    theorem assumptions; scipy cannot certify those assumptions.
    """
    n = len(residual_functions)
    if len(cost_functions) != n:
        raise ValueError("one cost function is required per group")
    ub = _validate_problem(n, budget, upper_bounds)
    initial_risk = max(fn(0.0) for fn in residual_functions)
    x0 = np.r_[np.zeros(n), initial_risk]
    bounds = [(0.0, float(v)) for v in ub] + [(0.0, 1.0)]
    constraints = [{
        "type": "ineq",
        "fun": lambda x: budget - sum(c(float(x[i])) for i, c in enumerate(cost_functions)),
    }]
    for i, risk in enumerate(residual_functions):
        constraints.append({"type": "ineq", "fun": lambda x, i=i, risk=risk: x[-1] - risk(float(x[i]))})
    result = minimize(lambda x: float(x[-1]), x0, method="SLSQP", bounds=bounds, constraints=constraints)
    allocation = np.asarray(result.x[:-1], dtype=float)
    residuals = np.asarray([fn(float(u)) for fn, u in zip(residual_functions, allocation)], dtype=float)
    used = float(sum(fn(float(u)) for fn, u in zip(cost_functions, allocation)))
    return AllocationResult(allocation, residuals, used, float(np.max(residuals)), bool(result.success), str(result.message))


def solve_weighted_residual(
    residual_functions: Sequence[Callable[[float], float]],
    cost_functions: Sequence[Callable[[float], float]],
    weights: Sequence[float],
    budget: float,
    upper_bounds: Sequence[float],
) -> AllocationResult:
    """Solve Theorem 11's separable welfare objective."""
    n = len(residual_functions)
    if len(cost_functions) != n:
        raise ValueError("one cost function is required per group")
    ub = _validate_problem(n, budget, upper_bounds)
    w = np.asarray(weights, dtype=float)
    if len(w) != n or np.any(w < 0.0) or w.sum() <= 0.0:
        raise ValueError("weights must be nonnegative, matched, and not all zero")
    w = w / w.sum()
    constraint = {
        "type": "ineq",
        "fun": lambda u: budget - sum(c(float(u[i])) for i, c in enumerate(cost_functions)),
    }
    objective = lambda u: float(sum(w[i] * residual_functions[i](float(u[i])) for i in range(n)))
    result = minimize(objective, np.zeros(n), method="SLSQP", bounds=[(0.0, float(v)) for v in ub], constraints=[constraint])
    allocation = np.asarray(result.x, dtype=float)
    residuals = np.asarray([fn(float(u)) for fn, u in zip(residual_functions, allocation)], dtype=float)
    used = float(sum(fn(float(u)) for fn, u in zip(cost_functions, allocation)))
    return AllocationResult(allocation, residuals, used, float(objective(allocation)), bool(result.success), str(result.message))

