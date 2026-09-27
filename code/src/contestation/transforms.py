"""Analytical transformations from initial to final decision rates."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from src.models.confusion import ConfusionRates, ContestationRates


def post_contestation_rates(
    initial: ConfusionRates, contestation: ContestationRates
) -> ConfusionRates:
    """Apply Proposition 1's one-sided contestation transformation."""
    tpr = initial.tpr + initial.fnr * contestation.kappa_positive
    fpr = initial.fpr + initial.tnr * contestation.kappa_negative
    return ConfusionRates(initial.prevalence, tpr, fpr)


def post_positive_rate(
    initial: ConfusionRates, contestation: ContestationRates
) -> float:
    """Implement Corollary 1."""
    return post_contestation_rates(initial, contestation).positive_rate


def two_sided_rates(
    initial: ConfusionRates,
    kappa_positive: float,
    kappa_negative: float,
    positive_to_negative_y1: float,
    positive_to_negative_y0: float,
) -> ConfusionRates:
    """Apply Proposition 2 for a general binary two-sided kernel."""
    values = np.asarray(
        [kappa_positive, kappa_negative, positive_to_negative_y1, positive_to_negative_y0],
        dtype=float,
    )
    if np.any((values < 0.0) | (values > 1.0)):
        raise ValueError("all transition probabilities must lie in [0, 1]")
    tpr = initial.tpr * (1.0 - positive_to_negative_y1) + initial.fnr * kappa_positive
    fpr = initial.fpr * (1.0 - positive_to_negative_y0) + initial.tnr * kappa_negative
    return ConfusionRates(initial.prevalence, tpr, fpr)


def contestation_kernel(kappa: float, reverse_positive: float = 0.0) -> np.ndarray:
    """Return a row-stochastic 2x2 kernel indexed by initial/final decisions."""
    if not 0.0 <= kappa <= 1.0 or not 0.0 <= reverse_positive <= 1.0:
        raise ValueError("transition probabilities must lie in [0, 1]")
    return np.array([[1.0 - kappa, kappa], [reverse_positive, 1.0 - reverse_positive]])

