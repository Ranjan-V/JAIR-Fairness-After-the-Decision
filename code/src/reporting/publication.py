"""Generate paper-ready data tables and deterministic figures from real outputs."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def _load(root: Path, filename: str) -> pd.DataFrame:
    path = root / "aggregate" / filename
    if not path.exists():
        raise FileNotFoundError(f"required aggregate is missing: {path}")
    frame = pd.read_csv(path)
    if "parameter_json" in frame:
        parsed = frame["parameter_json"].fillna("{}").map(json.loads).apply(pd.Series)
        for column in parsed:
            if column not in frame:
                frame[column] = parsed[column]
    return frame


def _save(fig, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def _write_table(frame: pd.DataFrame, stem: Path) -> None:
    stem.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(stem.with_suffix(".csv"), index=False)
    stem.with_suffix(".tex").write_text(frame.to_latex(index=False, escape=True, float_format=lambda value: f"{value:.4g}"), encoding="utf-8")


def build_all_figures_and_tables(root: Path) -> list[Path]:
    root = root.resolve()
    figures = root / "figures"
    tables = root / "tables"
    written: list[Path] = []

    theorem = _load(root, "theorem_validation.csv")
    table01 = theorem[theorem["metric"] == "absolute_error"]
    _write_table(table01, tables / "TABLE-01_theory_verification")
    written.extend([tables / "TABLE-01_theory_verification.csv", tables / "TABLE-01_theory_verification.tex"])

    core = _load(root, "core_synthetic.csv")
    table02 = core[(core["experiment_id"] == "EXP-01") & core["metric"].isin(["theoretical_value", "empirical_value", "absolute_error"])]
    _write_table(table02, tables / "TABLE-02_access_heterogeneity")
    allocation = _load(root, "resource_allocation.csv")
    _write_table(allocation, tables / "TABLE-03_resource_allocation")
    identification = _load(root, "identification.csv")
    _write_table(identification, tables / "TABLE-04_partial_identification")
    realdata = _load(root, "realdata.csv")
    _write_table(realdata, tables / "TABLE-05_semisynthetic_realdata")

    exp01 = core[(core["experiment_id"] == "EXP-01") & (core["metric"] == "empirical_value")].copy()
    if not exp01.empty:
        exp01["contestability_gap"] = exp01["kappa_a"] - exp01["kappa_b"]
        view = exp01.groupby("contestability_gap", as_index=False)["mean"].mean().sort_values("contestability_gap")
        fig, ax = plt.subplots(figsize=(6, 4)); ax.plot(view["contestability_gap"], view["mean"], marker="o")
        ax.set(xlabel="Effective contestability gap", ylabel="Post-contestation EO gap")
        _save(fig, figures / "FIG-01_contestability_gap.png")

    exp03 = core[(core["experiment_id"] == "EXP-03") & core["metric"].isin(["post_fnr_a", "post_fnr_b"])].copy()
    if not exp03.empty:
        fig, ax = plt.subplots(figsize=(7, 4))
        for (family, metric), part in exp03.groupby(["family_pair", "metric"]):
            ax.plot(part["subsidy"], part["mean"], label=f"{family}: {metric}")
        ax.set(xlabel="Common assistance", ylabel="Post-contestation FNR"); ax.legend(fontsize=6)
        _save(fig, figures / "FIG-02_equal_policy_heterogeneous_costs.png")

    frontier = core[(core["experiment_id"] == "EXP-05") & core["metric"].isin(["mean_residual_fnr", "eo_gap"])]
    if not frontier.empty:
        pivot = frontier.pivot_table(index=["parameter_key", "lambda", "budget"], columns="metric", values="mean", aggfunc="first").reset_index()
        fig, ax = plt.subplots(figsize=(6, 4))
        for penalty, part in pivot.groupby("lambda"):
            ax.plot(part["mean_residual_fnr"], part["eo_gap"], marker=".", label=f"lambda={penalty}")
        ax.set(xlabel="Aggregate residual loss", ylabel="Fairness disparity"); ax.legend(fontsize=7)
        _save(fig, figures / "FIG-03_fairness_utility_frontier.png")

    nonid = identification[identification["experiment_id"] == "EXP-06"]
    if not nonid.empty:
        view = nonid.groupby("metric", as_index=False)["mean"].mean()
        fig, ax = plt.subplots(figsize=(8, 4)); ax.bar(view["metric"], view["mean"])
        ax.tick_params(axis="x", rotation=55); ax.set(ylabel="Value", title="Same observables, different oracle quantities")
        _save(fig, figures / "FIG-04_observational_equivalence.png")

    auditing = _load(root, "auditing.csv")
    audit_width = auditing[auditing["metric"] == "fnr_width"] if "metric" in auditing else pd.DataFrame()
    if not audit_width.empty and "audit_rate" in audit_width:
        audit_width = audit_width.sort_values("audit_rate")
    if not audit_width.empty:
        fig, ax = plt.subplots(figsize=(6, 4)); ax.plot(audit_width["audit_rate"], audit_width["mean"], marker="o")
        ax.set_xscale("symlog", linthresh=0.001); ax.set(xlabel="Random-audit rate", ylabel="FNR interval width")
        _save(fig, figures / "FIG-05_audit_rate_interval_width.png")

    theorem_pair = theorem[theorem["metric"].isin(["theoretical_value", "empirical_value"])] if "metric" in theorem else pd.DataFrame()
    if not theorem_pair.empty:
        pivot = theorem_pair.pivot_table(index=["parameter_key", "scenario", "n"], columns="metric", values="mean", aggfunc="first").dropna().reset_index()
        fig, ax = plt.subplots(figsize=(5, 5)); ax.scatter(pivot["theoretical_value"], pivot["empirical_value"], alpha=0.7)
        limits = [min(pivot["theoretical_value"].min(), pivot["empirical_value"].min()), max(pivot["theoretical_value"].max(), pivot["empirical_value"].max())]
        ax.plot(limits, limits, linestyle="--", color="black"); ax.set(xlabel="Theory", ylabel="Simulation")
        _save(fig, figures / "FIG-06_theory_vs_simulation.png")

    real_gap = realdata[realdata["metric"] == "equal_opportunity_gap"] if "metric" in realdata else pd.DataFrame()
    if not real_gap.empty:
        index = ["dataset", "model"]
        if "contestation_scenario" in real_gap:
            index.append("contestation_scenario")
        pivot = real_gap.pivot_table(index=index, columns="decision_stage", values="mean", aggfunc="first").reset_index()
        fig, ax = plt.subplots(figsize=(max(8, 0.65 * len(pivot)), 5)); positions = np.arange(len(pivot)); width = 0.35
        ax.bar(positions - width / 2, pivot.get("pre", np.nan), width, label="Pre-contestation")
        ax.bar(positions + width / 2, pivot.get("post", np.nan), width, label="Post-contestation")
        labels = pivot["dataset"] + " / " + pivot["model"]
        if "contestation_scenario" in pivot:
            labels = labels + " / " + pivot["contestation_scenario"]
        ax.set_xticks(positions, labels, rotation=55, ha="right"); ax.set_ylabel("EO gap"); ax.legend()
        _save(fig, figures / "FIG-07_semisynthetic_pre_post.png")

    robustness = _load(root, "robustness.csv")
    heat = robustness[robustness["metric"] == "predicted_pair_gap"] if "metric" in robustness else pd.DataFrame()
    if not heat.empty:
        matrix = heat.pivot_table(index="tpr", columns="review_success", values="mean", aggfunc="mean")
        fig, ax = plt.subplots(figsize=(6, 4)); image = ax.imshow(matrix.values, aspect="auto", origin="lower")
        ax.set_xticks(range(len(matrix.columns)), [str(v) for v in matrix.columns]); ax.set_yticks(range(len(matrix.index)), [str(v) for v in matrix.index])
        ax.set(xlabel="Review success", ylabel="Initial TPR"); fig.colorbar(image, ax=ax, label="Predicted EO gap")
        _save(fig, figures / "FIG-08_robustness_heatmap.png")
    return written
