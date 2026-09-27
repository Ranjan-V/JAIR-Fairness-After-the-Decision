"""Train/validation/test real prediction with semisynthetic contestation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.datasets.adult import load_adult
from src.datasets.german_credit import load_german_credit
from src.datasets.real_pipeline import (
    apply_group_thresholds,
    build_classifier,
    equal_opportunity_thresholds,
    simulate_contestation,
)
from src.fairness.metrics import group_metrics, pairwise_gaps
from src.utils.manifest import RunManifest


LOADERS = {"adult": load_adult, "german": load_german_credit}


def _sequence_map(groups, values):
    if not values:
        raise ValueError("contestation sequence cannot be empty")
    return {group: float(values[min(i, len(values) - 1)]) for i, group in enumerate(sorted(groups))}


def _contestation_scenarios(settings: dict) -> list[dict]:
    scenarios = settings.get("contestation_scenarios")
    if scenarios:
        return list(scenarios)
    return [{
        "name": "primary",
        "alpha_positive_sequence": settings["alpha_positive_sequence"],
        "alpha_negative_sequence": settings["alpha_negative_sequence"],
        "rho_positive_sequence": settings["rho_positive_sequence"],
        "rho_negative_sequence": settings["rho_negative_sequence"],
    }]


def run_one_dataset(dataset: dict, model_name: str, seed: int, settings: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    name = dataset["name"]
    if name not in LOADERS:
        raise ValueError(f"unsupported dataset {name!r}")
    x, y, groups = LOADERS[name](dataset["path"], group_column=dataset["group_column"], label_column=dataset["label_column"])
    test_fraction = float(settings.get("test_fraction", 0.2))
    validation_fraction = float(settings.get("validation_fraction", 0.2))
    stratify = y.astype(str) + "::" + groups.astype(str)
    x_dev, x_test, y_dev, y_test, g_dev, g_test = train_test_split(x, y, groups, test_size=test_fraction, random_state=seed, stratify=stratify)
    validation_relative = validation_fraction / (1.0 - test_fraction)
    dev_stratify = y_dev.astype(str) + "::" + g_dev.astype(str)
    x_train, x_val, y_train, y_val, _, g_val = train_test_split(x_dev, y_dev, g_dev, test_size=validation_relative, random_state=seed + 1, stratify=dev_stratify)
    classifier = build_classifier(x_train, model_name, seed)
    classifier.fit(x_train, y_train)
    validation_scores = classifier.predict_proba(x_val)[:, 1]
    test_scores = classifier.predict_proba(x_test)[:, 1]
    if settings.get("calibrate_equal_opportunity", True):
        thresholds = equal_opportunity_thresholds(y_val, validation_scores, g_val)
        d0 = apply_group_thresholds(test_scores, g_test, thresholds)
    else:
        thresholds = {group: 0.5 for group in np.unique(g_test.astype(str))}
        d0 = (test_scores >= 0.5).astype(int)
    names = sorted(np.unique(g_test.astype(str)))
    alpha_plus = _sequence_map(names, settings["alpha_positive_sequence"])
    alpha_minus = _sequence_map(names, settings["alpha_negative_sequence"])
    rho_plus = _sequence_map(names, settings["rho_positive_sequence"])
    rho_minus = _sequence_map(names, settings["rho_negative_sequence"])
    scenario_name = str(settings.get("_scenario_name", "primary"))
    parameter_json = json.dumps({
        "contestation_scenario": scenario_name,
        "alpha_positive": alpha_plus,
        "alpha_negative": alpha_minus,
        "rho_positive": rho_plus,
        "rho_negative": rho_minus,
    }, sort_keys=True)
    parameter_key = hashlib.sha256(parameter_json.encode("utf-8")).hexdigest()[:16]
    cases = simulate_contestation(y_test, d0, g_test, alpha_plus, alpha_minus, rho_plus, rho_minus, seed)
    cases.insert(0, "dataset", name)
    cases.insert(1, "model", model_name)
    cases.insert(2, "seed", seed)
    cases.insert(3, "contestation_scenario", scenario_name)
    pre = group_metrics(cases["y"], cases["d0"], cases["group"])
    post = group_metrics(cases["y"], cases["d1"], cases["group"])
    rows = []
    for stage, values in (("pre", pre), ("post", post)):
        for group, metrics in values.items():
            for metric, value in metrics.items():
                rows.append({"experiment_id": "REALDATA", "experiment_type": "SEMISYNTHETIC REAL-DATA EXPERIMENT", "dataset": name, "model": model_name, "seed": seed, "group": group, "decision_stage": stage, "method": "group_threshold_calibrated" if settings.get("calibrate_equal_opportunity", True) else "threshold_0.5", "contestation_scenario": scenario_name, "parameter_key": parameter_key, "parameter_json": parameter_json, "metric": metric, "value": value})
        for metric, value in pairwise_gaps(values).items():
            rows.append({"experiment_id": "REALDATA", "experiment_type": "SEMISYNTHETIC REAL-DATA EXPERIMENT", "dataset": name, "model": model_name, "seed": seed, "group": "ALL", "decision_stage": stage, "method": "group_threshold_calibrated" if settings.get("calibrate_equal_opportunity", True) else "threshold_0.5", "contestation_scenario": scenario_name, "parameter_key": parameter_key, "parameter_json": parameter_json, "metric": metric, "value": value})
        if len(names) == 2:
            first, second = names
            for metric, value in (
                ("signed_equal_opportunity_gap", values[first]["tpr"] - values[second]["tpr"]),
                ("signed_fpr_gap", values[first]["fpr"] - values[second]["fpr"]),
            ):
                rows.append({"experiment_id": "REALDATA", "experiment_type": "SEMISYNTHETIC REAL-DATA EXPERIMENT", "dataset": name, "model": model_name, "seed": seed, "group": f"{first}_minus_{second}", "decision_stage": stage, "method": "group_threshold_calibrated" if settings.get("calibrate_equal_opportunity", True) else "threshold_0.5", "contestation_scenario": scenario_name, "parameter_key": parameter_key, "parameter_json": parameter_json, "metric": metric, "value": value})
    for group, threshold in thresholds.items():
        rows.append({"experiment_id": "REALDATA", "experiment_type": "SEMISYNTHETIC REAL-DATA EXPERIMENT", "dataset": name, "model": model_name, "seed": seed, "group": group, "decision_stage": "frozen_policy", "method": "validation_selected_threshold", "contestation_scenario": scenario_name, "parameter_key": parameter_key, "parameter_json": parameter_json, "metric": "decision_threshold", "value": threshold})
    return cases, pd.DataFrame(rows)


def run_configured_realdata(config: dict, output_override: str | None, resume: bool, force: bool) -> None:
    settings = config.get("realdata", {})
    root = Path(output_override or config["output_dir"])
    if not root.is_absolute():
        root = Path(__file__).resolve().parents[2] / root
    manifest = RunManifest(root / "run_manifest.json")
    config_hash = hashlib.sha256(json.dumps(config, sort_keys=True).encode("utf-8")).hexdigest()[:16]
    datasets = settings.get("datasets", [])
    if not datasets:
        manifest.skip("REALDATA__NOT_CONFIGURED", {"experiment_id": "REALDATA", "config_hash": config_hash, "seed": None, "parameter_combination": {}}, "No dataset paths configured; add them to a local config file.")
        return
    for dataset in datasets:
        for model in settings.get("models", ["logistic"]):
            for scenario in _contestation_scenarios(settings):
                scenario_name = str(scenario["name"])
                if not scenario_name.replace("_", "").isalnum():
                    raise ValueError(f"unsafe contestation scenario name {scenario_name!r}")
                scenario_settings = {**settings, **scenario, "_scenario_name": scenario_name}
                for seed in config["seeds"]:
                    run_id = f"REALDATA__{dataset['name']}__{model}__{scenario_name}__seed_{seed}"
                    metadata = {"experiment_id": "REALDATA", "config_hash": config_hash, "seed": seed, "parameter_combination": {"dataset": dataset["name"], "model": model, "contestation_scenario": scenario_name}, "output_filenames": []}
                    if resume and not force and manifest.is_complete(run_id, config_hash):
                        continue
                    manifest.start(run_id, metadata)
                    try:
                        cases, metrics = run_one_dataset(dataset, model, seed, scenario_settings)
                        raw_dir = root / "raw" / "realdata"
                        standard_dir = root / "standardized" / "realdata"
                        raw_dir.mkdir(parents=True, exist_ok=True)
                        standard_dir.mkdir(parents=True, exist_ok=True)
                        stem = f"{dataset['name']}__{model}__{scenario_name}__seed_{seed}"
                        cases_path = raw_dir / f"{stem}.csv"
                        metrics_path = standard_dir / f"{stem}.csv"
                        cases.to_csv(cases_path, index=False)
                        metrics.to_csv(metrics_path, index=False)
                        manifest.finish(run_id, [str(cases_path), str(metrics_path)])
                    except Exception as error:
                        manifest.fail(run_id, repr(error))
                        raise
