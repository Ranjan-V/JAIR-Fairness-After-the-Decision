import math

from src.fairness.bounds import attainable_absolute_gap, attainable_signed_tpr_gap
from src.fairness.metrics import demographic_parity_increment, signed_tpr_gap_after
from src.models.confusion import ConfusionRates


def test_theorem_2_preservation_and_counterexample():
    assert signed_tpr_gap_after(0.5, 0.5, 0.3, 0.3) == 0.0
    assert signed_tpr_gap_after(0.5, 0.5, 1.0, 0.0) == 0.5


def test_perfect_classifier_boundary():
    assert signed_tpr_gap_after(1.0, 1.0, 1.0, 0.0) == 0.0


def test_theorem_4_dp_counterexample():
    a = ConfusionRates(0.8, 0.5, 0.0)
    b = ConfusionRates(0.2, 1.0, 0.25)
    assert math.isclose(a.positive_rate, b.positive_rate)
    assert not math.isclose(demographic_parity_increment(a, 0.5, 0.0), demographic_parity_increment(b, 0.5, 0.0))


def test_theorem_6_tight_interval():
    signed = attainable_signed_tpr_gap(0.7, 0.4)
    absolute = attainable_absolute_gap(0.7, 0.4)
    assert math.isclose(signed[0], -0.3) and math.isclose(signed[1], 0.6)
    assert math.isclose(absolute[0], 0.0) and math.isclose(absolute[1], 0.6)
