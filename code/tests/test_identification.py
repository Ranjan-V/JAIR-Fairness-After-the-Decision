import math

import pytest

from src.identification.bounds import Interval, absolute_gap_interval, fnr_identification_interval, propensity_bounded_interval
from src.identification.worlds import equivalent_world_pair


def test_theorem_13_observational_equivalence():
    first, second = equivalent_world_pair(0.5, 0.5, 0.0, 1.0)
    assert first.observable_signature() == second.observable_signature()
    assert first.final_fnr_under_perfect_review() == 0.0
    assert math.isclose(second.final_fnr_under_perfect_review(), 2.0 / 3.0)


def test_theorem_14_sharp_bounds_contain_truth():
    interval = fnr_identification_interval(s=0.2, m=0.1, n=0.4, rho=0.8)
    true_z = 0.16
    truth = (0.1 * 0.2 + true_z) / (0.2 + 0.1 + true_z)
    assert interval.lower <= truth <= interval.upper


def test_theorem_14_latent_only_positive_boundary():
    interval = fnr_identification_interval(s=0.0, m=0.0, n=0.8, rho=1.0)
    assert interval.lower == interval.upper == 1.0


def test_theorem_14_all_zero_positive_mass_is_undefined():
    with pytest.raises(ValueError, match="undefined"):
        fnr_identification_interval(s=0.0, m=0.0, n=0.0, rho=1.0)


def test_propensity_information_weakly_shrinks_interval():
    broad = fnr_identification_interval(0.2, 0.1, 0.4, 0.8)
    narrow = propensity_bounded_interval(0.2, 0.1, 0.4, 0.8, 0.2, 0.8)
    assert narrow.width <= broad.width


def test_proposition_7_requires_positive_appealed_positive_mass():
    with pytest.raises(ValueError, match="positive appealed-positive mass"):
        propensity_bounded_interval(0.2, 0.0, 0.4, 0.8, 0.2, 0.8)


def test_absolute_gap_interval_overlap_and_separation():
    assert absolute_gap_interval(Interval(0.1, 0.4), Interval(0.3, 0.5)).lower == 0.0
    assert absolute_gap_interval(Interval(0.1, 0.2), Interval(0.5, 0.6)).lower == 0.3
