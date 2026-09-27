"""EXP-09: structured robustness and one-factor sensitivity designs."""

from __future__ import annotations

import pandas as pd

from src.contestation.costs import ExponentialCost, LogisticCost, ParetoCost, UniformCost, appeal_probability


def _gap(tpr: float, rho: float, alpha_a: float, alpha_b: float) -> float:
    return (1.0 - tpr) * rho * abs(alpha_a - alpha_b)


def run(seed: int = 1729, **_ignored) -> pd.DataFrame:
    records = []
    baseline = dict(prevalence=0.5, tpr=0.7, fpr=0.2, review_success=0.8, alpha_a=0.7, alpha_b=0.3, benefit=1.0, subsidy=0.5, group_proportion_a=0.5, number_of_groups=2)
    for tpr in [0.4, 0.7, 0.95]:
        for rho in [0.4, 0.8, 1.0]:
            row = {**baseline, "factor": "tpr_x_review", "factor_value": f"{tpr}:{rho}", "tpr": tpr, "review_success": rho}
            row["predicted_pair_gap"] = _gap(tpr, rho, row["alpha_a"], row["alpha_b"])
            records.append(row)
    one_factor = {
        "group_proportion_a": [0.05, 0.2, 0.5, 0.8, 0.95],
        "prevalence": [0.1, 0.3, 0.5, 0.7, 0.9],
        "tpr": [0.4, 0.55, 0.7, 0.85, 0.95],
        "fpr": [0.05, 0.2, 0.4],
        "review_success": [0.2, 0.4, 0.6, 0.8, 1.0],
        "benefit": [0.25, 0.5, 1.0, 2.0],
        "subsidy": [0.0, 0.25, 0.5, 1.0, 2.0],
        "number_of_groups": [2, 3, 5, 10],
    }
    for factor, values in one_factor.items():
        for value in values:
            row = {**baseline, factor: value, "factor": factor, "factor_value": value}
            row["predicted_pair_gap"] = _gap(row["tpr"], row["review_success"], row["alpha_a"], row["alpha_b"])
            records.append(row)
    families = {
        "uniform": (UniformCost(2.0), UniformCost(1.0)),
        "exponential": (ExponentialCost(0.5), ExponentialCost(1.0)),
        "logistic": (LogisticCost(1.0, 0.5), LogisticCost(0.5, 0.5)),
        "pareto": (ParetoCost(1.0, 1.5), ParetoCost(1.0, 3.0)),
    }
    for family, (dist_a, dist_b) in families.items():
        value = baseline["benefit"] * 0.5
        alpha_a = appeal_probability(dist_a, value, baseline["subsidy"])
        alpha_b = appeal_probability(dist_b, value, baseline["subsidy"])
        row = {**baseline, "factor": "cost_family_heterogeneity", "factor_value": family, "cost_family": family, "alpha_a": alpha_a, "alpha_b": alpha_b}
        row["predicted_pair_gap"] = _gap(row["tpr"], row["review_success"], alpha_a, alpha_b)
        records.append(row)
    return pd.DataFrame(records)
