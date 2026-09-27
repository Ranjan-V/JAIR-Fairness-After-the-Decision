"""Local-file adapter for the UCI Adult-style CSV schema."""

from __future__ import annotations

import pandas as pd

from .common import require_local_file, split_features


def load_adult(path, group_column: str = "sex", label_column: str = "income"):
    """Load a user-provided CSV; never downloads data.

    The caller is responsible for documenting source/license and normalizing
    the label to 0/1 before training if their file uses textual labels.
    """
    frame = pd.read_csv(require_local_file(path), skipinitialspace=True)
    return split_features(frame, label_column, group_column)

