"""EXP-02: isolate heterogeneous review quality at fixed appeal propensity."""

from __future__ import annotations

import pandas as pd
import numpy as np


def run(tpr: float = 0.7, appeal_probability: float = 0.5, grid=None, n: int = 100_000, seed: int = 1729) -> pd.DataFrame:
    grid = grid if grid is not None else [i / 20 for i in range(21)]
    rng = np.random.default_rng(seed)
    records = []
    for rho_a in grid:
        for rho_b in grid:
            predicted = (1.0 - tpr) * appeal_probability * (rho_a - rho_b)
            tp_a, tp_b = rng.binomial(n, tpr, size=2)
            corrected_a = rng.binomial(n - tp_a, appeal_probability * rho_a)
            corrected_b = rng.binomial(n - tp_b, appeal_probability * rho_b)
            empirical = (tp_a + corrected_a) / n - (tp_b + corrected_b) / n
            records.append({"rho_a": rho_a, "rho_b": rho_b, "appeal_probability": appeal_probability, "theoretical_signed_gap": predicted, "empirical_signed_gap": empirical, "absolute_error": abs(empirical - predicted), "n_per_group": n})
    return pd.DataFrame(records)
