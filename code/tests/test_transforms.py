import math

from src.contestation.transforms import post_contestation_rates, post_positive_rate, two_sided_rates
from src.models.confusion import ConfusionRates, ContestationRates


def test_proposition_1_identities():
    initial = ConfusionRates(prevalence=0.4, tpr=0.7, fpr=0.2)
    appeal = ContestationRates(0.5, 0.25, 0.8, 0.1)
    final = post_contestation_rates(initial, appeal)
    assert math.isclose(final.fnr, initial.fnr * (1.0 - appeal.kappa_positive))
    assert math.isclose(final.fpr, initial.fpr + initial.tnr * appeal.kappa_negative)
    assert math.isclose(final.tpr + final.fnr, 1.0)
    assert math.isclose(final.fpr + final.tnr, 1.0)


def test_corollary_1_positive_rate():
    initial = ConfusionRates(0.3, 0.6, 0.1)
    appeal = ContestationRates(0.4, 0.2, 0.75, 0.1)
    expected = initial.positive_rate + 0.3 * initial.fnr * appeal.kappa_positive + 0.7 * initial.tnr * appeal.kappa_negative
    assert math.isclose(post_positive_rate(initial, appeal), expected)


def test_zero_appeals_identity():
    initial = ConfusionRates(0.5, 0.65, 0.15)
    final = post_contestation_rates(initial, ContestationRates(0.0, 0.0, 1.0, 1.0))
    assert final == initial


def test_two_sided_boundary_breaks_one_sided_identity():
    initial = ConfusionRates(0.5, 1.0, 0.0)
    final = two_sided_rates(initial, 0.0, 0.0, 0.5, 0.0)
    assert final.tpr == 0.5

