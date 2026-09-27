import math

import numpy as np

from src.optimization.continuous import solve_weighted_residual


def test_symmetric_interior_kkt_matches_closed_form():
    risks = [lambda u: math.exp(-u), lambda u: math.exp(-u)]
    costs = [lambda u: u, lambda u: u]
    result = solve_weighted_residual(risks, costs, [0.5, 0.5], budget=1.0, upper_bounds=[2.0, 2.0])
    assert result.success
    assert np.allclose(result.allocation, [0.5, 0.5], atol=1e-5)
    marginal_a = 0.5 * math.exp(-result.allocation[0])
    marginal_b = 0.5 * math.exp(-result.allocation[1])
    assert math.isclose(marginal_a, marginal_b, rel_tol=1e-5, abs_tol=1e-7)

