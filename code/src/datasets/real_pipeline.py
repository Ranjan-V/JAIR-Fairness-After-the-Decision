"""Lightweight real-classification plus semisynthetic contestation harness."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier


def build_classifier(x: pd.DataFrame, model: str, seed: int):
    categorical = list(x.select_dtypes(exclude=[np.number]).columns)
    numeric = [column for column in x.columns if column not in categorical]
    transform = ColumnTransformer([
        ("numeric", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
        ("categorical", Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("one_hot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), categorical),
    ])
    estimators = {
        "logistic": LogisticRegression(max_iter=1000, random_state=seed),
        "tree": DecisionTreeClassifier(max_depth=8, min_samples_leaf=20, random_state=seed),
        "gradient_boosting": HistGradientBoostingClassifier(max_iter=200, max_leaf_nodes=31, learning_rate=0.05, random_state=seed),
        "random_forest": RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_leaf=10, n_jobs=1, random_state=seed),
    }
    if model not in estimators:
        raise ValueError(f"unknown model {model!r}")
    return Pipeline([("transform", transform), ("model", estimators[model])])


def equal_opportunity_thresholds(y, scores, groups, reference_threshold: float = 0.5) -> dict[str, float]:
    """Choose group thresholds on validation data to approximate a common TPR.

    This is an experimental control, not the proposed contribution. Thresholds
    must be frozen before test evaluation.
    """
    y = np.asarray(y, dtype=int)
    scores = np.asarray(scores, dtype=float)
    groups = np.asarray(groups).astype(str)
    positive = y == 1
    if positive.sum() == 0:
        raise ValueError("validation set has no positive labels")
    target = float(np.mean(scores[positive] >= reference_threshold))
    grid = np.linspace(0.01, 0.99, 99)
    thresholds = {}
    for group in np.unique(groups):
        mask = positive & (groups == group)
        if mask.sum() == 0:
            raise ValueError(f"validation group {group!r} has no positives")
        rates = np.asarray([np.mean(scores[mask] >= threshold) for threshold in grid])
        thresholds[group] = float(grid[int(np.argmin(np.abs(rates - target)))])
    return thresholds


def apply_group_thresholds(scores, groups, thresholds: dict[str, float]) -> np.ndarray:
    scores = np.asarray(scores, dtype=float)
    groups = np.asarray(groups).astype(str)
    missing = set(np.unique(groups)) - set(thresholds)
    if missing:
        raise ValueError(f"missing frozen thresholds for groups: {sorted(missing)}")
    return np.asarray([score >= thresholds[group] for score, group in zip(scores, groups)], dtype=int)


def simulate_contestation(
    y,
    d0,
    groups,
    alpha_positive: dict[str, float],
    alpha_negative: dict[str, float],
    rho_positive: dict[str, float],
    rho_negative: dict[str, float],
    seed: int,
) -> pd.DataFrame:
    """Add semisynthetic appeal/review outcomes to real test predictions."""
    rng = np.random.default_rng(seed)
    y = np.asarray(y, dtype=int)
    d0 = np.asarray(d0, dtype=int)
    groups = np.asarray(groups).astype(str)
    appeal = np.zeros(len(y), dtype=int)
    reversal = np.zeros(len(y), dtype=int)
    for group in np.unique(groups):
        mask = (groups == group) & (d0 == 0)
        alpha = np.where(y[mask] == 1, alpha_positive[group], alpha_negative[group])
        appeal[mask] = rng.binomial(1, alpha)
        reviewed = mask & (appeal == 1)
        rho = np.where(y[reviewed] == 1, rho_positive[group], rho_negative[group])
        reversal[reviewed] = rng.binomial(1, rho)
    d1 = np.where(reversal == 1, 1, d0)
    return pd.DataFrame({"y": y, "d0": d0, "group": groups, "appeal": appeal, "review_reversal": reversal, "d1": d1})
