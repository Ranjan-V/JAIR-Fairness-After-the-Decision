"""Random-audit estimators for Theorem 15 and Propositions 8--9."""

from __future__ import annotations

import math

from src.identification.bounds import Interval


def hoeffding_audit_interval(positives: int, audited: int, delta: float = 0.05) -> Interval:
    if audited <= 0 or not 0 <= positives <= audited:
        raise ValueError("require 0 <= positives <= audited and audited > 0")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie in (0, 1)")
    estimate = positives / audited
    radius = math.sqrt(math.log(2.0 / delta) / (2.0 * audited))
    return Interval(max(0.0, estimate - radius), min(1.0, estimate + radius))


def simultaneous_audit_intervals(counts: dict[str, tuple[int, int]], delta: float = 0.05) -> dict[str, Interval]:
    """Bonferroni/Hoeffding intervals from Proposition 9."""
    if not counts:
        raise ValueError("counts cannot be empty")
    adjusted = delta / len(counts)
    return {group: hoeffding_audit_interval(pos, total, adjusted) for group, (pos, total) in counts.items()}


def propagate_q_interval_to_fnr(
    q_interval: Interval, s: float, m: float, nonappellant_mass: float, rho: float
) -> Interval:
    from src.identification.bounds import _fnr

    return Interval(
        _fnr(s, m, nonappellant_mass * q_interval.lower, rho),
        _fnr(s, m, nonappellant_mass * q_interval.upper, rho),
    )

