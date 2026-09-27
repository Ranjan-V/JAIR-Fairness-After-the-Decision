"""Build the final E6 interval figure from the audited paired summary only."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "artifacts" / "reproducibility_audit_2026-09-26" / "e6" / "e6_paired_summary.csv"
OUTPUT = ROOT / "paper" / "jair" / "figures" / "FIG-05_signed_eo_change.pdf"
PREVIEW = ROOT / "paper" / "jair" / "figures" / "FIG-05_signed_eo_change.png"

MODELS = ["logistic", "gradient_boosting", "random_forest"]
MODEL_LABELS = ["Logistic", "Gradient\nboosting", "Random\nforest"]
SCENARIOS = [
    "moderate_first_group",
    "strong_first_group",
    "moderate_second_group",
    "strong_second_group",
]
LABELS = ["Moderate female", "Strong female", "Moderate male", "Strong male"]
MARKERS = ["o", "s", "^", "D"]
SHADES = ["0.15", "0.45", "0.15", "0.45"]
OFFSETS = [-0.24, -0.08, 0.08, 0.24]


def main() -> None:
    frame = pd.read_csv(SOURCE)
    frame = frame[
        (frame["metric"] == "signed_equal_opportunity_gap")
        & frame["contestation_scenario"].isin(SCENARIOS)
    ].copy()

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 8.5,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "legend.fontsize": 7.5,
        "pdf.fonttype": 42,
    })
    fig, axes = plt.subplots(1, 2, figsize=(7.05, 3.25), constrained_layout=True)

    for panel, (axis, dataset, title) in enumerate(zip(axes, ["adult", "german"], ["Adult", "German Credit"])):
        subset = frame[frame["dataset"] == dataset]
        for scenario_index, scenario in enumerate(SCENARIOS):
            means, lower, upper = [], [], []
            for model in MODELS:
                row = subset[(subset["model"] == model) & (subset["contestation_scenario"] == scenario)].iloc[0]
                means.append(row["delta_mean"])
                lower.append(row["delta_mean"] - row["delta_ci95_lower"])
                upper.append(row["delta_ci95_upper"] - row["delta_mean"])
            x = [index + OFFSETS[scenario_index] for index in range(3)]
            axis.errorbar(
                x,
                means,
                yerr=[lower, upper],
                fmt=MARKERS[scenario_index],
                color=SHADES[scenario_index],
                markerfacecolor="white" if scenario_index % 2 else SHADES[scenario_index],
                markeredgewidth=0.9,
                markersize=4.8,
                elinewidth=1.0,
                capsize=2.4,
                label=LABELS[scenario_index],
            )
        axis.axhline(0, color="0.55", linewidth=0.8, linestyle="--", zorder=0)
        axis.set_xticks(range(3), MODEL_LABELS)
        axis.set_xlim(-0.55, 2.55)
        axis.grid(axis="y", color="0.88", linewidth=0.6)
        axis.set_title(f"{chr(65 + panel)}. {title}", loc="left", fontweight="bold")
        axis.set_ylabel(r"Signed EO change  $\Delta_{post}-\Delta_{pre}$")
        axis.text(0.02, 0.03, "Female advantage up\nMale advantage down", transform=axis.transAxes,
                  va="bottom", ha="left", fontsize=7.2, color="0.25")
    axes[0].set_ylim(-0.22, 0.22)
    axes[1].set_ylim(-0.105, 0.105)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=4, frameon=False, handletextpad=0.4, columnspacing=1.0)
    fig.savefig(OUTPUT, bbox_inches="tight")
    fig.savefig(PREVIEW, dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
