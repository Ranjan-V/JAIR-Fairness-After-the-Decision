"""EXP-05: fairness--utility frontier over budget and penalty weight."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize


def run(budgets=None, lambdas=None, seed: int = 1729, **_ignored) -> pd.DataFrame:
    budgets = budgets if budgets is not None else np.linspace(0.0, 2.0, 21)
    lambdas = lambdas if lambdas is not None else [0.0, 0.25, 1.0, 4.0]
    risk_a = lambda u: 0.4 * np.exp(-0.5 * u)
    risk_b = lambda u: 0.25 * np.exp(-0.9 * u)
    records = []
    for budget in budgets:
        for penalty in lambdas:
            objective = lambda u: 0.5 * (risk_a(u[0]) + risk_b(u[1])) + penalty * abs(risk_a(u[0]) - risk_b(u[1]))
            result = minimize(objective, [budget / 2, budget / 2], method="SLSQP", bounds=[(0.0, budget), (0.0, budget)], constraints=[{"type": "ineq", "fun": lambda u, b=budget: b - u.sum()}])
            ra, rb = risk_a(result.x[0]), risk_b(result.x[1])
            records.append({"budget": budget, "lambda": penalty, "u_a": result.x[0], "u_b": result.x[1], "mean_residual_fnr": 0.5 * (ra + rb), "eo_gap": abs(ra - rb), "success": bool(result.success)})
    frame = pd.DataFrame(records)
    dominated = []
    for index, row in frame.iterrows():
        alternatives = frame.drop(index)
        weakly_better = (alternatives["mean_residual_fnr"] <= row["mean_residual_fnr"] + 1e-12) & (alternatives["eo_gap"] <= row["eo_gap"] + 1e-12) & (alternatives["budget"] <= row["budget"] + 1e-12)
        strictly_better = (alternatives["mean_residual_fnr"] < row["mean_residual_fnr"] - 1e-12) | (alternatives["eo_gap"] < row["eo_gap"] - 1e-12) | (alternatives["budget"] < row["budget"] - 1e-12)
        dominated.append(bool((weakly_better & strictly_better).any()))
    frame["dominated"] = dominated
    return frame
