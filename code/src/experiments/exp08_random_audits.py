"""EXP-08: audit-rate versus interval width."""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.estimation.audit import hoeffding_audit_interval, propagate_q_interval_to_fnr
from src.identification.bounds import fnr_identification_interval


def run(n_nonappellants: int = 10000, true_q: float = 0.4, rates=None, seeds=None, seed: int = 1729) -> pd.DataFrame:
    rates = rates if rates is not None else [0.0, 0.001, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20]
    seeds = seeds if seeds is not None else [seed]
    records = []
    for rate in rates:
        for seed in seeds:
            if rate == 0.0:
                interval = fnr_identification_interval(s=0.2, m=0.1, n=0.4, rho=0.8)
                true_fnr = (0.1 * 0.2 + 0.4 * true_q) / (0.2 + 0.1 + 0.4 * true_q)
                records.append({"audit_rate": rate, "seed": seed, "audited": 0, "q_lower": 0.0, "q_upper": 1.0, "fnr_lower": interval.lower, "fnr_upper": interval.upper, "fnr_width": interval.width, "oracle_true_fnr": true_fnr, "estimator_error": float("nan"), "coverage": interval.lower <= true_fnr <= interval.upper})
                continue
            rng = np.random.default_rng(seed)
            audited = int(rng.binomial(n_nonappellants, rate))
            if audited == 0:
                continue
            positives = int(rng.binomial(audited, true_q))
            q_interval = hoeffding_audit_interval(positives, audited)
            fnr_interval = propagate_q_interval_to_fnr(q_interval, s=0.2, m=0.1, nonappellant_mass=0.4, rho=0.8)
            true_fnr = (0.1 * 0.2 + 0.4 * true_q) / (0.2 + 0.1 + 0.4 * true_q)
            q_hat = positives / audited
            fnr_hat = (0.1 * 0.2 + 0.4 * q_hat) / (0.2 + 0.1 + 0.4 * q_hat)
            records.append({"audit_rate": rate, "seed": seed, "audited": audited, "q_lower": q_interval.lower, "q_upper": q_interval.upper, "fnr_lower": fnr_interval.lower, "fnr_upper": fnr_interval.upper, "fnr_width": fnr_interval.width, "oracle_true_fnr": true_fnr, "estimator_error": abs(fnr_hat - true_fnr), "coverage": fnr_interval.lower <= true_fnr <= fnr_interval.upper})
    return pd.DataFrame(records)
