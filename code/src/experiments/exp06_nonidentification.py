"""EXP-06: observationally equivalent worlds with different latent fairness."""

from __future__ import annotations

import pandas as pd

from src.identification.worlds import equivalent_world_pair


def run(a: float = 0.5, p: float = 0.5, **_ignored) -> pd.DataFrame:
    records = []
    for q1, q2 in [(0.0, 0.25), (0.0, 0.5), (0.0, 1.0), (0.25, 1.0)]:
        first, second = equivalent_world_pair(a, p, q1, q2)
        fnr1 = first.final_fnr_under_perfect_review() if a * p + (1 - a) * q1 > 0 else float("nan")
        fnr2 = second.final_fnr_under_perfect_review()
        records.append({
            "observable_appeal_rate_world_1": a,
            "observable_appeal_rate_world_2": a,
            "observable_appellant_positive_rate_world_1": p,
            "observable_appellant_positive_rate_world_2": p,
            "observable_signature_equal": first.observable_signature() == second.observable_signature(),
            "oracle_nonappellant_positive_rate_world_1": q1,
            "oracle_nonappellant_positive_rate_world_2": q2,
            "oracle_fnr_world_1": fnr1,
            "oracle_fnr_world_2": fnr2,
            "oracle_latent_fnr_difference": abs(fnr2 - fnr1),
        })
    return pd.DataFrame(records)
