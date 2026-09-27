"""EXP-07: identification width under propensity and review knowledge."""

from __future__ import annotations

import pandas as pd

from src.identification.bounds import fnr_identification_interval, propensity_bounded_interval


def run(seed: int = 1729, **_ignored) -> pd.DataFrame:
    records = []
    s, m, n = 0.2, 0.1, 0.4
    true_z = 0.16
    for rho in [0.5, 0.8, 1.0]:
        base = fnr_identification_interval(s, m, n, rho)
        truth = (m * (1.0 - rho) + true_z) / (s + m + true_z)
        records.append({"assumption": "none", "rho": rho, "alpha_lower": 0.0, "alpha_upper": 1.0, "lower": base.lower, "upper": base.upper, "width": base.width, "oracle_truth": truth, "coverage": base.lower <= truth <= base.upper, "distance_to_interval": 0.0 if base.lower <= truth <= base.upper else min(abs(truth - base.lower), abs(truth - base.upper))})
        for lower, upper in [(0.1, 0.9), (0.2, 0.8), (0.4, 0.6)]:
            try:
                interval = propensity_bounded_interval(s, m, n, rho, lower, upper)
            except ValueError:
                continue
            records.append({"assumption": "bounded_propensity", "rho": rho, "alpha_lower": lower, "alpha_upper": upper, "lower": interval.lower, "upper": interval.upper, "width": interval.width, "oracle_truth": truth, "coverage": interval.lower <= truth <= interval.upper, "distance_to_interval": 0.0 if interval.lower <= truth <= interval.upper else min(abs(truth - interval.lower), abs(truth - interval.upper))})
    return pd.DataFrame(records)
