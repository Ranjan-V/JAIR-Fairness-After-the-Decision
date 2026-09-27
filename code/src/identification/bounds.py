"""Sharp intervals implementing Theorem 14 and Proposition 7."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Interval:
    lower: float
    upper: float

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("lower endpoint exceeds upper endpoint")

    @property
    def width(self) -> float:
        return self.upper - self.lower


def _fnr(s: float, m: float, z: float, rho: float) -> float:
    denominator = s + m + z
    if denominator <= 0.0:
        raise ValueError("FNR is undefined when the group has no positives")
    return (m * (1.0 - rho) + z) / denominator


def fnr_identification_interval(s: float, m: float, n: float, rho: float) -> Interval:
    """Sharp no-assumption interval from Theorem 14."""
    if min(s, m, n) < 0.0 or not 0.0 <= rho <= 1.0:
        raise ValueError("masses must be nonnegative and rho in [0, 1]")
    if s + m == 0.0:
        if n == 0.0:
            raise ValueError("FNR is undefined in every compatible world")
        # At z=0 the positive stratum is empty; for every compatible world
        # with z>0, all positives are uncorrected adverse non-appellants.
        return Interval(1.0, 1.0)
    return Interval(_fnr(s, m, 0.0, rho), _fnr(s, m, n, rho))


def propensity_bounded_interval(
    s: float,
    m: float,
    n: float,
    rho: float,
    alpha_lower: float,
    alpha_upper: float,
) -> Interval:
    """Sharp interval under Proposition 7's propensity bounds."""
    if not 0.0 < alpha_lower <= alpha_upper <= 1.0:
        raise ValueError("require 0 < alpha_lower <= alpha_upper <= 1")
    if m <= 0.0:
        raise ValueError("Proposition 7 requires positive appealed-positive mass m")
    z_lower = max(0.0, m * (1.0 - alpha_upper) / alpha_upper)
    z_upper = min(n, m * (1.0 - alpha_lower) / alpha_lower)
    if z_lower > z_upper:
        raise ValueError("propensity restriction is incompatible with observed masses")
    return Interval(_fnr(s, m, z_lower, rho), _fnr(s, m, z_upper, rho))


def signed_gap_interval(a: Interval, b: Interval) -> Interval:
    return Interval(a.lower - b.upper, a.upper - b.lower)


def absolute_gap_interval(a: Interval, b: Interval) -> Interval:
    lower = 0.0 if max(a.lower, b.lower) <= min(a.upper, b.upper) else min(abs(a.lower - b.upper), abs(b.lower - a.upper))
    upper = max(abs(a.lower - b.upper), abs(a.upper - b.lower))
    return Interval(lower, upper)
