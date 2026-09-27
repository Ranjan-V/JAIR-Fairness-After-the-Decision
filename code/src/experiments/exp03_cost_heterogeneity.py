"""EXP-03: equal policy under heterogeneous cost distributions."""

from __future__ import annotations

import pandas as pd
import numpy as np

from src.contestation.costs import ExponentialCost, LogisticCost, ParetoCost, UniformCost, appeal_probability


def run(subsidies=None, perceived_value: float = 0.5, review_success: float = 0.8, tpr: float = 0.7, n: int = 100_000, seed: int = 1729) -> pd.DataFrame:
    subsidies = subsidies if subsidies is not None else [i / 20 for i in range(41)]
    rng = np.random.default_rng(seed)
    families = {
        "uniform_A_vs_B": (UniformCost(2.0), UniformCost(1.0)),
        "exponential_A_vs_B": (ExponentialCost(0.5), ExponentialCost(1.0)),
        "logistic_A_vs_B": (LogisticCost(1.0, 0.5), LogisticCost(0.5, 0.5)),
        "pareto_A_vs_B": (ParetoCost(1.0, 1.5), ParetoCost(1.0, 3.0)),
    }
    records = []
    for name, (dist_a, dist_b) in families.items():
        for subsidy in subsidies:
            alpha_a = appeal_probability(dist_a, perceived_value, subsidy)
            alpha_b = appeal_probability(dist_b, perceived_value, subsidy)
            gap = (1.0 - tpr) * review_success * (alpha_a - alpha_b)
            false_denials_a, false_denials_b = rng.binomial(n, 1.0 - tpr, size=2)
            appeals_a = rng.binomial(false_denials_a, alpha_a)
            appeals_b = rng.binomial(false_denials_b, alpha_b)
            corrected_a = rng.binomial(appeals_a, review_success)
            corrected_b = rng.binomial(appeals_b, review_success)
            final_fnr_a = (false_denials_a - corrected_a) / n
            final_fnr_b = (false_denials_b - corrected_b) / n
            empirical_signed_tpr_gap = final_fnr_b - final_fnr_a
            records.append({
                "family_pair": name,
                "subsidy": subsidy,
                "formal_policy_equal": True,
                "appeal_rate_a": appeals_a / false_denials_a if false_denials_a else 0.0,
                "appeal_rate_b": appeals_b / false_denials_b if false_denials_b else 0.0,
                "effective_correction_a": corrected_a / false_denials_a if false_denials_a else 0.0,
                "effective_correction_b": corrected_b / false_denials_b if false_denials_b else 0.0,
                "post_fnr_a": final_fnr_a,
                "post_fnr_b": final_fnr_b,
                "theoretical_signed_tpr_gap": gap,
                "empirical_signed_tpr_gap": empirical_signed_tpr_gap,
                "absolute_error": abs(empirical_signed_tpr_gap - gap),
                "institutional_cost": subsidy * (appeals_a + appeals_b),
                "n_per_group": n,
            })
    return pd.DataFrame(records)
