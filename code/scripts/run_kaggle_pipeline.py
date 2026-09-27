"""Thin one-click Kaggle launcher; delegates all research logic."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml


def _call(arguments: list[str]) -> None:
    subprocess.run([sys.executable, *arguments], check=True)


def _output_root(code_root: Path, config_path: str | None, override: str | None, mode: str) -> Path:
    if override:
        root = Path(override)
    else:
        default = "smoke.yaml" if mode == "smoke" else "full.yaml"
        path = Path(config_path) if config_path else code_root / "configs" / default
        config = yaml.safe_load(path.read_text(encoding="utf-8"))
        root = Path(config["output_dir"])
    return root if root.is_absolute() else code_root / root


def _write_output_inventory(output_root: Path) -> Path:
    """Write recursive artifact counts after a pipeline stage.

    Real-data outputs are nested below ``standardized/realdata``.  Counting
    only CSVs immediately below ``standardized`` incorrectly reports zero.
    """
    standardized_root = output_root / "standardized"
    realdata_root = standardized_root / "realdata"
    payload = {
        "artifact_count": sum(path.is_file() for path in output_root.rglob("*")),
        "standardized_csv_count": sum(1 for _ in standardized_root.rglob("*.csv")),
        "realdata_csv_count": sum(1 for _ in realdata_root.rglob("*.csv")),
        "counting_rule": "recursive",
    }
    target = output_root / "output_inventory.json"
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=["validate", "smoke", "theorem", "core", "robustness", "realdata", "aggregate", "full"])
    parser.add_argument("--config")
    parser.add_argument("--output-dir")
    parser.add_argument("--n-jobs", type=int, default=2)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    code_root = Path(__file__).resolve().parents[1]
    common = [str(code_root / "run_experiments.py")]
    if args.config:
        common += ["--config", args.config]
    if args.output_dir:
        common += ["--output-dir", args.output_dir]
    common += ["--n-jobs", str(args.n_jobs)]
    if args.resume:
        common.append("--resume")
    if args.mode == "validate":
        _call(["-m", "pytest", "-q", str(code_root / "tests")])
        return
    stages = {
        "smoke": ["smoke"], "theorem": ["theorem"], "core": ["core"],
        "robustness": ["robustness"], "realdata": ["realdata"],
        "aggregate": ["aggregate", "figures"],
        "full": ["theorem", "core", "robustness", "realdata", "aggregate", "figures"],
    }[args.mode]
    for stage in stages:
        _call([*common, "--stage", stage])
    output_root = _output_root(code_root, args.config, args.output_dir, args.mode)
    print(_write_output_inventory(output_root))


if __name__ == "__main__":
    main()
