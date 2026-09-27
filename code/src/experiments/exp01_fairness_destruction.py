"""EXP-01: sampled fairness destruction with exact Theorem 2 predictions."""

from __future__ import annotations

import pandas as pd
import numpy as np


def run(
    tpr: float = 0.7,
    review_success: float = 0.8,
    grid=None,
    n: int = 100_000,
    seed: int = 1729,
) -> pd.DataFrame:
    """Simulate equal initial TPR and sweep unequal appeal access.

    ``n`` is the number of true-positive-stratum cases per group and parameter
    pair. Sampling uses binomial sufficient statistics rather than materializing
    individual records.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    grid = grid if grid is not None else [i / 20 for i in range(21)]
    rng = np.random.default_rng(seed)
    records = []
    for alpha_a in grid:
        for alpha_b in grid:
            kappa_a = alpha_a * review_success
            kappa_b = alpha_b * review_success
            signed = (1.0 - tpr) * (kappa_a - kappa_b)
            tp_a, tp_b = rng.binomial(n, tpr, size=2)
            corrected_a = rng.binomial(n - tp_a, kappa_a)
            corrected_b = rng.binomial(n - tp_b, kappa_b)
            empirical_signed = (tp_a + corrected_a) / n - (tp_b + corrected_b) / n
            records.append({
                "alpha_a": alpha_a,
                "alpha_b": alpha_b,
                "kappa_a": kappa_a,
                "kappa_b": kappa_b,
                "theoretical_value": abs(signed),
                "theoretical_signed_gap": signed,
                "empirical_value": abs(empirical_signed),
                "empirical_signed_gap": empirical_signed,
                "absolute_error": abs(empirical_signed - signed),
                "n_per_group": n,
            })
    return pd.DataFrame(records)
