import numpy as np

from src.fairness.operators import preserves_linear_constraint


def test_operator_preservation_and_failure():
    fairness = np.array([[1.0, -1.0]])
    compatible = np.diag([0.7, 0.7])
    assert preserves_linear_constraint(fairness, compatible)
    incompatible = np.diag([0.2, 0.7])
    assert not preserves_linear_constraint(fairness, incompatible)
