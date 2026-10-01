"""Plot future experiment outputs; does not fabricate results."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _save(fig, path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(target, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_gap_vs_access(frame: pd.DataFrame, output: str | Path) -> None:
    fig, ax = plt.subplots(figsize=(6, 4))
    subset = frame[frame["alpha_b"] == frame["alpha_b"].min()].sort_values("alpha_a")
    ax.plot(subset["alpha_a"] - subset["alpha_b"], subset["predicted_absolute_gap"], marker="o")
    ax.set(xlabel="Appeal-propensity gap", ylabel="Absolute post-contestation EO gap")
    _save(fig, output)


def plot_fairness_budget(frame: pd.DataFrame, output: str | Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    for policy, part in frame.groupby("policy"):
        ax.plot(part["budget"], part["eo_gap"], marker="o", label=policy)
    ax.set(xlabel="Budget", ylabel="Equal-opportunity gap")
    ax.legend(fontsize=7)
    _save(fig, output)


def plot_frontier(frame: pd.DataFrame, output: str | Path) -> None:
    fig, ax = plt.subplots(figsize=(6, 4))
    for penalty, part in frame.groupby("lambda"):
        ax.plot(part["mean_residual_fnr"], part["eo_gap"], marker=".", label=f"lambda={penalty}")
    ax.set(xlabel="Mean residual FNR", ylabel="EO gap")
    ax.legend()
    _save(fig, output)


def plot_audit_width(frame: pd.DataFrame, output: str | Path) -> None:
    summary = frame.groupby("audit_rate", as_index=False)["fnr_width"].agg(["mean", "std"]).reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.errorbar(summary["audit_rate"], summary["mean"], yerr=summary["std"].fillna(0.0), marker="o")
    ax.set(xlabel="Random-audit rate", ylabel="FNR interval width")
    _save(fig, output)

