"""Validated population-rate containers."""

from __future__ import annotations

from dataclasses import dataclass


def _probability(name: str, value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must lie in [0, 1], got {value}")
    return value


@dataclass(frozen=True)
class ConfusionRates:
    """Group-conditional rates plus base rate.

    Implements the notation used in Proposition 1 and Corollary 1.
    """

    prevalence: float
    tpr: float
    fpr: float

    def __post_init__(self) -> None:
        for name in ("prevalence", "tpr", "fpr"):
            object.__setattr__(self, name, _probability(name, getattr(self, name)))

    @property
    def fnr(self) -> float:
        return 1.0 - self.tpr

    @property
    def tnr(self) -> float:
        return 1.0 - self.fpr

    @property
    def positive_rate(self) -> float:
        return self.prevalence * self.tpr + (1.0 - self.prevalence) * self.fpr


@dataclass(frozen=True)
class ContestationRates:
    """Appeal and conditional reversal probabilities by true-label stratum."""

    alpha_positive: float
    alpha_negative: float
    rho_positive: float
    rho_negative: float

    def __post_init__(self) -> None:
        for name in (
            "alpha_positive",
            "alpha_negative",
            "rho_positive",
            "rho_negative",
        ):
            object.__setattr__(self, name, _probability(name, getattr(self, name)))

    @property
    def kappa_positive(self) -> float:
        return self.alpha_positive * self.rho_positive

    @property
    def kappa_negative(self) -> float:
        return self.alpha_negative * self.rho_negative

