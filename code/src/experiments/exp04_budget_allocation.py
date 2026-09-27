"""EXP-04: compare B0--B6 allocation policies."""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.optimization.continuous import solve_minimax, solve_weighted_residual
from src.optimization.policies import (
    expected_corrections_allocation,
    no_subsidy,
    proportional_subsidy,
    random_subsidy,
    uniform_subsidy,
)


def run(budgets=None, seed: int = 1729) -> pd.DataFrame:
    budgets = budgets if budgets is not None else [0.0, 0.25, 0.5, 1.0, 2.0]
    baseline_fnr = np.array([0.4, 0.25])
    response = np.array([0.55, 0.8])
    risks = [lambda u, f=fnr, a=slope: f * (1.0 - min(1.0, a * u)) for fnr, slope in zip(baseline_fnr, response)]
    costs = [lambda u: u, lambda u: u]
    records = []
    for budget in budgets:
        policies = {
            "B0_no_appeal_assistance": no_subsidy(2),
            "B2_uniform": uniform_subsidy(2, budget),
            "B3_random": random_subsidy(2, budget, seed),
            "B4_expected_corrections": expected_corrections_allocation(baseline_fnr * response, budget),
            "additional_proportional_need": proportional_subsidy(baseline_fnr, budget),
        }
        welfare = solve_weighted_residual(risks, costs, [0.5, 0.5], budget, [2.0, 2.0])
        fair = solve_minimax(risks, costs, budget, [2.0, 2.0])
        policies["B5_welfare_optimum"] = welfare.allocation
        policies["B6_fairness_aware_minimax"] = fair.allocation
        if budget >= 4.0:
            policies["B1_universal_capacity"] = np.array([2.0, 2.0])
        for name, allocation in policies.items():
            residuals = np.array([fn(float(u)) for fn, u in zip(risks, allocation)])
            corrected = baseline_fnr - residuals
            records.append({
                "budget": budget,
                "policy": name,
                "u_a": allocation[0],
                "u_b": allocation[1],
                "mean_residual_fnr": residuals.mean(),
                "max_residual_fnr": residuals.max(),
                "fpr_a": 0.2,
                "fpr_b": 0.2,
                "eo_gap": abs(residuals[0] - residuals[1]),
                "equalized_odds_gap": abs(residuals[0] - residuals[1]),
                "expected_corrections": corrected.sum(),
                "corrections_per_unit_cost": corrected.sum() / allocation.sum() if allocation.sum() > 0 else 0.0,
                "resource_used": allocation.sum(),
                "social_loss": residuals.mean(),
            })
    return pd.DataFrame(records)
