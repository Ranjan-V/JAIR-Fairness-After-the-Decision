"""Manual command-line runner for EXP-01 through EXP-10."""

from __future__ import annotations

import argparse
import importlib
from pathlib import Path


MODULES = {
    "EXP-01": "src.experiments.exp01_fairness_destruction",
    "EXP-02": "src.experiments.exp02_review_disparity",
    "EXP-03": "src.experiments.exp03_cost_heterogeneity",
    "EXP-04": "src.experiments.exp04_budget_allocation",
    "EXP-05": "src.experiments.exp05_frontier",
    "EXP-06": "src.experiments.exp06_nonidentification",
    "EXP-07": "src.experiments.exp07_partial_identification",
    "EXP-08": "src.experiments.exp08_random_audits",
    "EXP-09": "src.experiments.exp09_robustness",
    "EXP-10": "src.experiments.exp10_boundaries",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment", choices=MODULES)
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()
    frame = importlib.import_module(MODULES[args.experiment]).run()
    output = Path(args.output_dir) / f"{args.experiment.lower()}.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False)
    print(f"wrote {output}")


if __name__ == "__main__":
    main()

