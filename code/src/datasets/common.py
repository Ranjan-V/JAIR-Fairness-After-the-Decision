"""Shared validation and preprocessing for local real-data adapters."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def require_local_file(path: str | Path) -> Path:
    resolved = Path(path).expanduser().resolve()
    if not resolved.is_file():
        raise FileNotFoundError(
            f"Dataset not found at {resolved}. Downloading is intentionally disabled; "
            "follow code/data/README.md."
        )
    return resolved


def split_features(frame: pd.DataFrame, label: str, group: str):
    if label not in frame or group not in frame:
        raise ValueError("label and group columns must exist")
    y = frame[label].astype(int)
    g = frame[group].astype(str)
    x = frame.drop(columns=[label, group])
    return x, y, g

