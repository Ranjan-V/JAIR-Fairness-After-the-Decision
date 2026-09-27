"""Configurable synthetic population for theorem-verification experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class GroupConfig:
    proportion: float
    prevalence: float
    tpr: float
    fpr: float
    cost_family: str = "uniform"
    cost_params: tuple[float, ...] = (1.0,)
    perceived_benefit: float = 1.0
    perceived_success: float = 0.5
    review_positive: float = 0.8
    review_negative: float = 0.05
    subsidy: float = 0.0


@dataclass(frozen=True)
class SyntheticConfig:
    n: int
    groups: Mapping[str, GroupConfig]
    seed: int = 0
    feature_count: int = 4
    perceived_noise: float = 0.1
    rare_high_cost_probability: float = 0.0
    rare_high_cost_multiplier: float = 10.0


def _validate(config: SyntheticConfig) -> None:
    if config.n <= 0 or config.feature_count < 0:
        raise ValueError("n must be positive and feature_count nonnegative")
    total = sum(item.proportion for item in config.groups.values())
    if not np.isclose(total, 1.0):
        raise ValueError("group proportions must sum to one")
    for name, item in config.groups.items():
        probabilities = [item.proportion, item.prevalence, item.tpr, item.fpr,
                         item.review_positive, item.review_negative]
        if any(not 0.0 <= value <= 1.0 for value in probabilities):
            raise ValueError(f"invalid probability in group {name}")
        if item.subsidy < 0.0:
            raise ValueError("subsidy must be nonnegative")


def _sample_cost(rng: np.random.Generator, family: str, params: tuple[float, ...], size: int) -> np.ndarray:
    if family == "uniform":
        return rng.uniform(0.0, params[0], size=size)
    if family == "exponential":
        return rng.exponential(1.0 / params[0], size=size)
    if family == "logistic":
        return rng.logistic(params[0], params[1], size=size)
    if family == "pareto":
        return params[0] * (1.0 + rng.pareto(params[1], size=size))
    if family == "truncated_normal":
        return np.maximum(0.0, rng.normal(params[0], params[1], size=size))
    raise ValueError(f"unknown cost family: {family}")


def generate_population(config: SyntheticConfig) -> pd.DataFrame:
    """Generate initial decisions, endogenous appeals, and fallible review.

    Sampling is independent conditional on configured rates.  This function is
    never called at import time.
    """
    _validate(config)
    rng = np.random.default_rng(config.seed)
    names = np.asarray(list(config.groups))
    probabilities = np.asarray([config.groups[name].proportion for name in names])
    groups = rng.choice(names, size=config.n, p=probabilities)
    frame = pd.DataFrame({"group": groups})
    for j in range(config.feature_count):
        frame[f"x{j}"] = rng.normal(0.0, 1.0, size=config.n)
    y = np.zeros(config.n, dtype=int)
    d0 = np.zeros(config.n, dtype=int)
    costs = np.zeros(config.n)
    perceived = np.zeros(config.n)
    subsidies = np.zeros(config.n)
    review_probability = np.zeros(config.n)
    for name, item in config.groups.items():
        mask = groups == name
        count = int(mask.sum())
        y[mask] = rng.binomial(1, item.prevalence, size=count)
        positive_probability = np.where(y[mask] == 1, item.tpr, item.fpr)
        d0[mask] = rng.binomial(1, positive_probability)
        group_cost = _sample_cost(rng, item.cost_family, item.cost_params, count)
        if config.rare_high_cost_probability > 0.0:
            rare = rng.random(count) < config.rare_high_cost_probability
            group_cost[rare] *= config.rare_high_cost_multiplier
        costs[mask] = group_cost
        base_value = item.perceived_benefit * item.perceived_success
        perceived[mask] = np.maximum(0.0, base_value + rng.normal(0.0, config.perceived_noise, count))
        subsidies[mask] = item.subsidy
        review_probability[mask] = np.where(y[mask] == 1, item.review_positive, item.review_negative)
    appeal = ((d0 == 0) & (costs <= perceived + subsidies)).astype(int)
    reversal = rng.binomial(1, review_probability) * appeal
    d1 = np.where(reversal == 1, 1, d0)
    frame = frame.assign(
        y=y,
        d0=d0,
        cost=costs,
        perceived_value=perceived,
        subsidy=subsidies,
        appeal=appeal,
        review_reversal=reversal,
        d1=d1,
    )
    return frame

