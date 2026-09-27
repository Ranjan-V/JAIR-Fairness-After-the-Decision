"""Local-file adapter for a user-prepared German Credit CSV."""

from __future__ import annotations

import pandas as pd

from .common import require_local_file, split_features


def load_german_credit(path, group_column: str, label_column: str = "credit_risk"):
    frame = pd.read_csv(require_local_file(path))
    return split_features(frame, label_column, group_column)

