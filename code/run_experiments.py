"""Resumable master runner for every experimental stage.

This file is prepared for manual execution and was not run during packaging.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import sys
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import pandas as pd
import yaml

CODE_ROOT = Path(__file__).resolve().parent
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from src.experiments.registry import SPECS, STAGE_EXPERIMENTS
from src.utils.manifest import RunManifest


def _hash_config(config: dict) -> str:
    encoded = json.dumps(config, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def _run_module(module_name: str, kwargs: dict) -> pd.DataFrame:
    return importlib.import_module(module_name).run(**kwargs)


def _parameter_key(row: pd.Series) -> str:
    payload = json.dumps({key: _jsonable(value) for key, value in row.items()}, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def _jsonable(value):
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def _standardize(frame: pd.DataFrame, experiment_id: str, seed: int, profile: str, config_hash: str) -> pd.DataFrame:
    spec = SPECS[experiment_id]
    frame = frame.copy()
    if "seed" in frame.columns:
        frame = frame.drop(columns=["seed"])
    parameter_columns = [column for column in frame.columns if column not in spec.metrics]
    parameter_json = frame[parameter_columns].apply(
        lambda row: json.dumps({key: _jsonable(value) for key, value in row.items()}, sort_keys=True), axis=1
    )
    frame.insert(0, "parameter_json", parameter_json)
    frame.insert(0, "parameter_key", parameter_json.map(lambda value: hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]))
    id_vars = [column for column in frame.columns if column not in spec.metrics]
    long = frame.melt(id_vars=id_vars, value_vars=[m for m in spec.metrics if m in frame], var_name="metric", value_name="value")
    # Heterogeneous theorem rows contain metrics that are structurally absent rather
    # than measured as NaN.  Do not emit those artificial tidy rows.  EXP-08's
    # estimator error is the one intentional missing value: no estimate exists
    # when a random audit samples nobody, and the validator handles it explicitly.
    intentional_missing = (experiment_id == "EXP-08") & (long["metric"] == "estimator_error")
    long = long[long["value"].notna() | intentional_missing].copy()
    long["value"] = long["value"].map(lambda value: int(value) if isinstance(value, bool) else value)
    long.insert(0, "experiment_id", experiment_id)
    long.insert(1, "experiment_type", spec.experiment_type)
    long.insert(2, "seed", seed)
    long.insert(3, "configuration", profile)
    long.insert(4, "config_hash", config_hash)
    for column, default in (("dataset", "synthetic"), ("group", "ALL"), ("model", "not_applicable"), ("method", "not_applicable")):
        if column not in long:
            long[column] = default
    return long


def _resolve_config(args) -> tuple[Path, dict]:
    default_name = "smoke.yaml" if args.stage == "smoke" else "stress.yaml" if args.stage == "stress" else "full.yaml"
    path = Path(args.config) if args.config else CODE_ROOT / "configs" / default_name
    config = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise ValueError("configuration root must be a mapping")
    return path, config


def _resolved_output_root(config: dict, override: str | None) -> Path:
    root = Path(override or config["output_dir"])
    return root if root.is_absolute() else CODE_ROOT / root


def _run_one(experiment_id: str, seed: int, kwargs: dict, profile: str, config_hash: str, output_root: Path) -> tuple[str, list[str]]:
    spec = SPECS[experiment_id]
    frame = _run_module(spec.module, {**kwargs, "seed": seed})
    raw_dir = output_root / "raw" / experiment_id.lower()
    standard_dir = output_root / "standardized" / experiment_id.lower()
    raw_dir.mkdir(parents=True, exist_ok=True)
    standard_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"seed_{seed}.csv"
    standard_path = standard_dir / f"seed_{seed}.csv"
    frame.to_csv(raw_path.with_suffix(".csv.tmp"), index=False)
    raw_path.with_suffix(".csv.tmp").replace(raw_path)
    _standardize(frame, experiment_id, seed, profile, config_hash).to_csv(standard_path.with_suffix(".csv.tmp"), index=False)
    standard_path.with_suffix(".csv.tmp").replace(standard_path)
    return f"{experiment_id}__seed_{seed}", [str(raw_path), str(standard_path)]


def run_stage(args, config: dict) -> None:
    profile = str(config["profile"])
    output_root = _resolved_output_root(config, args.output_dir)
    config_hash = _hash_config(config)
    seeds = [args.seed] if args.seed is not None else list(config["seeds"])
    n_jobs = args.n_jobs if args.n_jobs is not None else int(config.get("n_jobs", 1))
    manifest = RunManifest(output_root / "run_manifest.json")
    experiment_ids = STAGE_EXPERIMENTS[args.stage]
    tasks = []
    for experiment_id in experiment_ids:
        kwargs = dict(config.get("theorem", {})) if experiment_id == "THEOREM" else dict(config.get("experiments", {}).get(experiment_id, {}))
        for seed in seeds:
            run_id = f"{experiment_id}__seed_{seed}"
            metadata = {"experiment_id": experiment_id, "config_hash": config_hash, "seed": seed, "parameter_combination": kwargs, "output_filenames": []}
            if args.resume and not args.force and manifest.is_complete(run_id, config_hash):
                continue
            manifest.start(run_id, metadata)
            tasks.append((experiment_id, seed, kwargs, run_id))
    if n_jobs <= 1:
        for experiment_id, seed, kwargs, run_id in tasks:
            try:
                _, outputs = _run_one(experiment_id, seed, kwargs, profile, config_hash, output_root)
                manifest.finish(run_id, outputs)
            except Exception:
                manifest.fail(run_id, traceback.format_exc())
                raise
    else:
        with ProcessPoolExecutor(max_workers=n_jobs) as pool:
            futures = {pool.submit(_run_one, exp, seed, kwargs, profile, config_hash, output_root): run_id for exp, seed, kwargs, run_id in tasks}
            for future in as_completed(futures):
                run_id = futures[future]
                try:
                    _, outputs = future.result()
                    manifest.finish(run_id, outputs)
                except Exception:
                    manifest.fail(run_id, traceback.format_exc())
                    raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True, choices=["smoke", "theorem", "core", "robustness", "realdata", "aggregate", "figures", "stress", "all"])
    parser.add_argument("--config")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--output-dir")
    parser.add_argument("--n-jobs", type=int)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    _, config = _resolve_config(args)
    if args.force and args.resume:
        raise SystemExit("choose at most one of --resume and --force")
    if args.stage in STAGE_EXPERIMENTS:
        run_stage(args, config)
        return
    if args.stage == "realdata":
        from src.experiments.realdata_semisynthetic import run_configured_realdata
        run_configured_realdata(config, args.output_dir, args.resume, args.force)
    elif args.stage == "aggregate":
        from src.reporting.aggregation import aggregate_all
        aggregate_all(_resolved_output_root(config, args.output_dir))
    elif args.stage == "figures":
        from src.reporting.publication import build_all_figures_and_tables
        build_all_figures_and_tables(_resolved_output_root(config, args.output_dir))
    elif args.stage == "all":
        for stage in ("theorem", "core", "robustness"):
            args.stage = stage
            run_stage(args, config)
        from src.experiments.realdata_semisynthetic import run_configured_realdata
        run_configured_realdata(config, args.output_dir, args.resume, args.force)
        from src.reporting.aggregation import aggregate_all
        from src.reporting.publication import build_all_figures_and_tables
        root = _resolved_output_root(config, args.output_dir)
        aggregate_all(root)
        build_all_figures_and_tables(root)


if __name__ == "__main__":
    main()
