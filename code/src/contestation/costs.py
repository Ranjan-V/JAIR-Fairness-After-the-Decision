"""Cost distributions and endogenous threshold appeal behavior.

Implements Propositions 4--5 and provides inverse CDFs used by Proposition 6.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np
from scipy.special import expit, logit


class CostDistribution(Protocol):
    def cdf(self, x: np.ndarray | float) -> np.ndarray | float: ...
    def ppf(self, p: np.ndarray | float) -> np.ndarray | float: ...


@dataclass(frozen=True)
class UniformCost:
    upper: float

    def __post_init__(self) -> None:
        if self.upper <= 0:
            raise ValueError("upper must be positive")

    def cdf(self, x):
        return np.clip(np.asarray(x, dtype=float) / self.upper, 0.0, 1.0)

    def ppf(self, p):
        p = _check_probability_array(p)
        return self.upper * p


@dataclass(frozen=True)
class ExponentialCost:
    rate: float

    def __post_init__(self) -> None:
        if self.rate <= 0:
            raise ValueError("rate must be positive")

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        return np.where(x < 0.0, 0.0, -np.expm1(-self.rate * x))

    def ppf(self, p):
        p = _check_probability_array(p)
        return -np.log1p(-p) / self.rate


@dataclass(frozen=True)
class LogisticCost:
    location: float
    scale: float

    def __post_init__(self) -> None:
        if self.scale <= 0:
            raise ValueError("scale must be positive")

    def cdf(self, x):
        return expit((np.asarray(x, dtype=float) - self.location) / self.scale)

    def ppf(self, p):
        p = _check_probability_array(p)
        return self.location + self.scale * logit(p)


@dataclass(frozen=True)
class ParetoCost:
    scale: float
    shape: float

    def __post_init__(self) -> None:
        if self.scale <= 0 or self.shape <= 0:
            raise ValueError("scale and shape must be positive")

    def cdf(self, x):
        x = np.asarray(x, dtype=float)
        safe = np.maximum(x, self.scale)
        values = 1.0 - (self.scale / safe) ** self.shape
        return np.where(x < self.scale, 0.0, values)

    def ppf(self, p):
        p = _check_probability_array(p)
        return self.scale * (1.0 - p) ** (-1.0 / self.shape)


def _check_probability_array(p):
    values = np.asarray(p, dtype=float)
    if np.any((values < 0.0) | (values > 1.0)):
        raise ValueError("probabilities must lie in [0, 1]")
    return values


def appeal_probability(
    distribution: CostDistribution, perceived_value: float, subsidy: float
) -> float:
    """Return F(perceived_value + subsidy), Proposition 4."""
    if subsidy < 0:
        raise ValueError("subsidy must be nonnegative")
    return float(distribution.cdf(perceived_value + subsidy))


def heterogeneous_appeal_probability(
    distribution: CostDistribution,
    perceived_values: np.ndarray,
    subsidy: float,
) -> float:
    """Monte Carlo plug-in for E[F(V+u)] under conditional independence."""
    if subsidy < 0:
        raise ValueError("subsidy must be nonnegative")
    values = np.asarray(perceived_values, dtype=float)
    if values.size == 0:
        raise ValueError("perceived_values cannot be empty")
    return float(np.mean(distribution.cdf(values + subsidy)))
