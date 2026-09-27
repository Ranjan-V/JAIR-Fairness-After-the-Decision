import math

from src.contestation.costs import ExponentialCost, LogisticCost, ParetoCost, UniformCost, appeal_probability
from src.optimization.closed_form import minimum_subsidy, required_appeal_probability
from src.optimization.continuous import solve_minimax, solve_weighted_residual
from src.optimization.discrete import knapsack_dynamic_program


def test_closed_form_cdf_inverse_pairs():
    distributions = [UniformCost(2.0), ExponentialCost(1.5), LogisticCost(0.5, 1.2), ParetoCost(1.0, 2.0)]
    for distribution in distributions:
        for p in (0.1, 0.5, 0.9):
            assert math.isclose(float(distribution.cdf(distribution.ppf(p))), p, rel_tol=1e-10, abs_tol=1e-10)


def test_procedural_symmetry_counterexample():
    alpha_a = appeal_probability(UniformCost(2.0), 0.5, 0.0)
    alpha_b = appeal_probability(UniformCost(1.0), 0.5, 0.0)
    assert alpha_a == 0.25
    assert alpha_b == 0.5


def test_minimum_subsidy_hits_target():
    distribution = UniformCost(2.0)
    subsidy = minimum_subsidy(distribution, perceived_value=0.0, fnr=0.5, review_success=1.0, epsilon=0.25)
    assert subsidy == 1.0
    assert required_appeal_probability(0.5, 1.0, 0.25) == 0.5


def test_knapsack_regression_against_ratio_greedy():
    result = knapsack_dynamic_program([10, 20, 30], [60, 100, 120], 50)
    assert result.selected == (1, 2)
    assert result.total_value == 220.0
    assert result.total_cost <= 50


def test_continuous_optimizers_respect_budget_and_bounds():
    risks = [lambda u: 0.4 * (1.0 - 0.5 * u), lambda u: 0.3 * (1.0 - 0.4 * u)]
    costs = [lambda u: u, lambda u: u]
    for result in (
        solve_minimax(risks, costs, budget=0.5, upper_bounds=[1.0, 1.0]),
        solve_weighted_residual(risks, costs, [0.5, 0.5], budget=0.5, upper_bounds=[1.0, 1.0]),
    ):
        assert result.success
        assert result.resource_used <= 0.5 + 1e-7
        assert all(0.0 <= value <= 1.0 for value in result.allocation)

