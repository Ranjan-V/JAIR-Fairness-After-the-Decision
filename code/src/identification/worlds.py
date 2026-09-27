"""Observationally equivalent latent worlds from Theorem 13."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LatentWorld:
    appeal_rate: float
    appellant_positive_rate: float
    nonappellant_positive_rate: float

    def __post_init__(self) -> None:
        for value in (
            self.appeal_rate,
            self.appellant_positive_rate,
            self.nonappellant_positive_rate,
        ):
            if not 0.0 <= value <= 1.0:
                raise ValueError("all rates must lie in [0, 1]")

    def observable_signature(self) -> tuple[float, float]:
        """The ordinary log cannot include the third latent parameter."""
        return self.appeal_rate, self.appellant_positive_rate

    def final_fnr_under_perfect_review(self) -> float:
        a = self.appeal_rate
        p = self.appellant_positive_rate
        q = self.nonappellant_positive_rate
        denominator = a * p + (1.0 - a) * q
        if denominator == 0.0:
            raise ValueError("FNR undefined in a world with no positives")
        return (1.0 - a) * q / denominator


def equivalent_world_pair(a: float, p: float, q1: float, q2: float) -> tuple[LatentWorld, LatentWorld]:
    first = LatentWorld(a, p, q1)
    second = LatentWorld(a, p, q2)
    if first.observable_signature() != second.observable_signature():
        raise AssertionError("construction error")
    return first, second

