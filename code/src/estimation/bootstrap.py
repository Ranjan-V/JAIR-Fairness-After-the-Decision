"""Deterministic-seed stratified bootstrap utilities."""

from __future__ import annotations

from collections.abc import Callable

import numpy as np


def stratified_bootstrap(
    values: np.ndarray,
    strata: np.ndarray,
    statistic: Callable[[np.ndarray, np.ndarray], float],
    repetitions: int,
    seed: int,
) -> np.ndarray:
    values = np.asarray(values)
    strata = np.asarray(strata)
    if len(values) != len(strata) or repetitions <= 0:
        raise ValueError("invalid bootstrap inputs")
    rng = np.random.default_rng(seed)
    unique = np.unique(strata)
    estimates = np.empty(repetitions, dtype=float)
    for b in range(repetitions):
        sampled_parts = []
        sampled_strata = []
        for group in unique:
            indices = np.flatnonzero(strata == group)
            selected = rng.choice(indices, size=len(indices), replace=True)
            sampled_parts.append(values[selected])
            sampled_strata.append(strata[selected])
        estimates[b] = statistic(np.concatenate(sampled_parts), np.concatenate(sampled_strata))
    return estimates

