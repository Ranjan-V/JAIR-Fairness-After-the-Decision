"""Stable experiment registry and standardized metric metadata."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExperimentSpec:
    module: str
    experiment_type: str
    metrics: tuple[str, ...]


SPECS = {
    "EXP-01": ExperimentSpec("src.experiments.exp01_fairness_destruction", "SYNTHETIC EXPERIMENT", ("theoretical_value", "theoretical_signed_gap", "empirical_value", "empirical_signed_gap", "absolute_error")),
    "EXP-02": ExperimentSpec("src.experiments.exp02_review_disparity", "SYNTHETIC EXPERIMENT", ("theoretical_signed_gap", "empirical_signed_gap", "absolute_error")),
    "EXP-03": ExperimentSpec("src.experiments.exp03_cost_heterogeneity", "SYNTHETIC EXPERIMENT", ("appeal_rate_a", "appeal_rate_b", "effective_correction_a", "effective_correction_b", "post_fnr_a", "post_fnr_b", "theoretical_signed_tpr_gap", "empirical_signed_tpr_gap", "absolute_error", "institutional_cost")),
    "EXP-04": ExperimentSpec("src.experiments.exp04_budget_allocation", "SYNTHETIC EXPERIMENT", ("u_a", "u_b", "mean_residual_fnr", "max_residual_fnr", "fpr_a", "fpr_b", "eo_gap", "equalized_odds_gap", "expected_corrections", "corrections_per_unit_cost", "resource_used", "social_loss")),
    "EXP-05": ExperimentSpec("src.experiments.exp05_frontier", "SYNTHETIC EXPERIMENT", ("u_a", "u_b", "mean_residual_fnr", "eo_gap", "success", "dominated")),
    "EXP-06": ExperimentSpec("src.experiments.exp06_nonidentification", "THEOREM ILLUSTRATION", ("observable_appeal_rate_world_1", "observable_appeal_rate_world_2", "observable_appellant_positive_rate_world_1", "observable_appellant_positive_rate_world_2", "oracle_fnr_world_1", "oracle_fnr_world_2", "oracle_latent_fnr_difference")),
    "EXP-07": ExperimentSpec("src.experiments.exp07_partial_identification", "SYNTHETIC EXPERIMENT", ("lower", "upper", "width", "coverage", "distance_to_interval")),
    "EXP-08": ExperimentSpec("src.experiments.exp08_random_audits", "SYNTHETIC EXPERIMENT", ("audited", "q_lower", "q_upper", "fnr_lower", "fnr_upper", "fnr_width", "oracle_true_fnr", "estimator_error", "coverage")),
    "EXP-09": ExperimentSpec("src.experiments.exp09_robustness", "ROBUSTNESS STUDY", ("predicted_pair_gap",)),
    "EXP-10": ExperimentSpec("src.experiments.exp10_boundaries", "THEOREM ILLUSTRATION", ("pre_tpr", "post_tpr", "pre_fpr", "post_fpr", "post_fnr_plus_tpr", "post_tnr_plus_fpr")),
    "THEOREM": ExperimentSpec("src.experiments.theorem_validation", "THEOREM ILLUSTRATION", ("theoretical_value", "empirical_value", "absolute_error", "lower", "upper", "oracle_truth")),
}

STAGE_EXPERIMENTS = {
    "smoke": tuple(f"EXP-{i:02d}" for i in range(1, 11)),
    "theorem": ("THEOREM",),
    "core": tuple(f"EXP-{i:02d}" for i in range(1, 9)),
    "robustness": ("EXP-09", "EXP-10"),
    "stress": ("EXP-01", "EXP-02", "EXP-03", "EXP-08", "EXP-09"),
}
