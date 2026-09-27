"""Dedicated numerical illustrations of proved mathematical results.

These routines are labeled THEOREM ILLUSTRATION. Numerical agreement is a
software check and illustration, never a proof.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.contestation.costs import UniformCost, appeal_probability
from src.identification.bounds import fnr_identification_interval
from src.identification.worlds import equivalent_world_pair
from src.optimization.closed_form import minimum_subsidy
from src.optimization.discrete import knapsack_dynamic_program
from src.fairness.metrics import demographic_parity_increment
from src.models.confusion import ConfusionRates
from src.fairness.operators import preserves_linear_constraint


def _rate_draw(rng: np.random.Generator, n: int, initial_positive_rate: float, kappa: float) -> float:
    initial_positive = int(rng.binomial(n, initial_positive_rate))
    transitioned = int(rng.binomial(n - initial_positive, kappa))
    return (initial_positive + transitioned) / n


def run(sample_sizes=None, seed: int = 1729, **_ignored) -> pd.DataFrame:
    sample_sizes = sample_sizes or [1_000, 10_000, 100_000, 1_000_000]
    rng = np.random.default_rng(seed)
    rows: list[dict] = []
    for n in sample_sizes:
        # Proposition 1: both label strata.
        for label, initial, alpha, rho in [(1, 0.7, 0.4, 0.8), (0, 0.2, 0.3, 0.1)]:
            kappa = alpha * rho
            theoretical = initial + (1.0 - initial) * kappa
            empirical = _rate_draw(rng, n, initial, kappa)
            rows.append(_row("Proposition 1", f"rate_y{label}", n, theoretical, empirical))

        # Theorem 2: preservation and exact violation.
        tpr = 0.65
        preserved_a = _rate_draw(rng, n, tpr, 0.3)
        preserved_b = _rate_draw(rng, n, tpr, 0.3)
        rows.append(_row("Theorem 2", "preservation_gap", n, 0.0, abs(preserved_a - preserved_b)))
        unequal_a = _rate_draw(rng, n, tpr, 0.6)
        unequal_b = _rate_draw(rng, n, tpr, 0.1)
        predicted_gap = (1.0 - tpr) * 0.5
        rows.append(_row("Theorem 5", "nonpreservation_gap", n, predicted_gap, abs(unequal_a - unequal_b)))

        # Theorem 8: common policy, strictly ordered Uniform CDFs.
        alpha_a = appeal_probability(UniformCost(2.0), 0.5, 0.0)
        alpha_b = appeal_probability(UniformCost(1.0), 0.5, 0.0)
        predicted_signed = (1.0 - tpr) * 0.8 * (alpha_a - alpha_b)
        observed_a = _rate_draw(rng, n, tpr, alpha_a * 0.8)
        observed_b = _rate_draw(rng, n, tpr, alpha_b * 0.8)
        rows.append(_row("Theorem 8", "group_blind_impossibility", n, predicted_signed, observed_a - observed_b))

    # Exact/non-sampling checks appear once with n=0.
    first, second = equivalent_world_pair(0.5, 0.5, 0.0, 1.0)
    rows.append(_row("Theorem 13", "observable_signature_distance", 0, 0.0, float(first.observable_signature() != second.observable_signature())))
    rows.append(_row("Corollary 5", "latent_fnr_difference", 0, 2.0 / 3.0, second.final_fnr_under_perfect_review() - first.final_fnr_under_perfect_review()))
    interval = fnr_identification_interval(0.2, 0.1, 0.4, 0.8)
    truth = (0.1 * 0.2 + 0.16) / (0.2 + 0.1 + 0.16)
    rows.append({**_row("Theorem 14", "sharp_bound_coverage", 0, 1.0, float(interval.lower <= truth <= interval.upper)), "lower": interval.lower, "upper": interval.upper, "oracle_truth": truth})
    subsidy = minimum_subsidy(UniformCost(2.0), 0.0, 0.5, 1.0, 0.25)
    rows.append(_row("Proposition 6", "closed_form_subsidy", 0, 1.0, subsidy))
    knapsack = knapsack_dynamic_program([10, 20, 30], [60, 100, 120], 50)
    rows.append(_row("Theorem 12", "knapsack_optimum", 0, 220.0, knapsack.total_value))
    dp_a = ConfusionRates(0.8, 0.5, 0.0)
    dp_b = ConfusionRates(0.2, 1.0, 0.25)
    dp_increment_gap = demographic_parity_increment(dp_a, 0.5, 0.0) - demographic_parity_increment(dp_b, 0.5, 0.0)
    rows.append(_row("Theorem 4", "equal_kappa_dp_increment_gap", 0, 0.2, dp_increment_gap))
    fairness_map = np.array([[1.0, -1.0]])
    compatible_operator = np.diag([0.7, 0.7])
    incompatible_operator = np.diag([0.2, 0.7])
    rows.append(_row("Theorem 1", "compatible_linear_operator", 0, 1.0, float(preserves_linear_constraint(fairness_map, compatible_operator))))
    rows.append(_row("Theorem 1", "incompatible_linear_operator", 0, 0.0, float(preserves_linear_constraint(fairness_map, incompatible_operator))))
    return pd.DataFrame(rows)


def _row(theorem_id: str, scenario: str, n: int, theoretical: float, empirical: float) -> dict:
    return {
        "theorem_id": theorem_id,
        "scenario": scenario,
        "n": n,
        "theoretical_value": theoretical,
        "empirical_value": empirical,
        "absolute_error": abs(empirical - theoretical),
    }
