import math

from src.contestation.costs import UniformCost, appeal_probability
from src.contestation.transforms import post_contestation_rates, two_sided_rates
from src.fairness.metrics import demographic_parity_increment
from src.identification.worlds import equivalent_world_pair
from src.models.confusion import ConfusionRates, ContestationRates


def test_ce3_equal_kappa_breaks_demographic_parity():
    a = ConfusionRates(0.8, 0.5, 0.0)
    b = ConfusionRates(0.2, 1.0, 0.25)
    assert math.isclose(a.positive_rate, b.positive_rate)
    assert demographic_parity_increment(a, 0.5, 0.0) != demographic_parity_increment(b, 0.5, 0.0)


def test_ce4_unequal_kappas_can_preserve_demographic_parity():
    common = ConfusionRates(0.5, 0.5, 0.5)
    assert demographic_parity_increment(common, 1.0, 0.0) == demographic_parity_increment(common, 0.0, 1.0)


def test_ce5_equal_policy_unequal_effective_access():
    assert appeal_probability(UniformCost(2.0), 0.5, 0.0) == 0.25
    assert appeal_probability(UniformCost(1.0), 0.5, 0.0) == 0.5


def test_ce8_review_quality_offsets_access():
    assert 0.5 * 1.0 == 1.0 * 0.5


def test_ce9_perfect_reviewer_does_not_fix_access():
    initial = ConfusionRates(0.5, 0.5, 0.2)
    a = post_contestation_rates(initial, ContestationRates(1.0, 0.0, 1.0, 0.0))
    b = post_contestation_rates(initial, ContestationRates(0.0, 0.0, 1.0, 0.0))
    assert a.tpr == 1.0 and b.tpr == 0.5


def test_ce11_correct_negative_appeals_create_false_positives():
    final = post_contestation_rates(ConfusionRates(0.5, 0.5, 0.0), ContestationRates(0.0, 0.5, 0.0, 0.4))
    assert math.isclose(final.fpr, 0.2)


def test_ce15_identical_logs_different_latent_fnr():
    first, second = equivalent_world_pair(0.5, 0.5, 0.0, 1.0)
    assert first.observable_signature() == second.observable_signature()
    assert first.final_fnr_under_perfect_review() != second.final_fnr_under_perfect_review()


def test_ce19_two_sided_appeal_invalidates_one_sided_identity():
    final = two_sided_rates(ConfusionRates(0.5, 1.0, 0.0), 0.0, 0.0, 0.5, 0.0)
    assert final.tpr == 0.5


def test_boundaries_universal_and_harmful_reviewer():
    initial = ConfusionRates(0.5, 0.6, 0.2)
    universal_perfect = post_contestation_rates(initial, ContestationRates(1.0, 1.0, 1.0, 0.0))
    universal_harmful = post_contestation_rates(initial, ContestationRates(1.0, 1.0, 0.0, 1.0))
    assert universal_perfect.tpr == 1.0 and universal_perfect.fpr == initial.fpr
    assert universal_harmful.tpr == initial.tpr and universal_harmful.fpr == 1.0

