"""EXP-10: explicit boundary-case table for regression tests."""

from __future__ import annotations

import pandas as pd

from src.contestation.transforms import post_contestation_rates
from src.models.confusion import ConfusionRates, ContestationRates


def run(seed: int = 1729, **_ignored) -> pd.DataFrame:
    cases = {
        "perfect_classifier": (ConfusionRates(0.5, 1.0, 0.0), ContestationRates(1.0, 1.0, 1.0, 1.0)),
        "perfect_reviewer": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(0.5, 0.5, 1.0, 0.0)),
        "zero_appeals": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(0.0, 0.0, 1.0, 1.0)),
        "universal_appeals": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(1.0, 1.0, 0.8, 0.1)),
        "zero_review_accuracy": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(1.0, 1.0, 0.0, 0.0)),
        "harmful_reviewer": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(1.0, 1.0, 0.0, 1.0)),
        "very_large_budget_universal_access": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(1.0, 1.0, 0.8, 0.1)),
        "equal_effective_correction": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(0.5, 0.5, 0.8, 0.1)),
        "extreme_group_imbalance": (ConfusionRates(0.01, 0.6, 0.2), ContestationRates(0.5, 0.5, 0.8, 0.1)),
        "equal_appeal_cost_proxy": (ConfusionRates(0.5, 0.6, 0.2), ContestationRates(0.5, 0.5, 0.8, 0.1)),
    }
    records = []
    for name, (initial, contestation) in cases.items():
        final = post_contestation_rates(initial, contestation)
        records.append({"case": name, "pre_tpr": initial.tpr, "post_tpr": final.tpr, "pre_fpr": initial.fpr, "post_fpr": final.fpr, "post_fnr_plus_tpr": final.fnr + final.tpr, "post_tnr_plus_fpr": final.tnr + final.fpr})
    return pd.DataFrame(records)
