from src.contestation.transforms import post_contestation_rates
from src.models.confusion import ConfusionRates, ContestationRates


def test_all_grid_outputs_are_legal_probabilities_and_complements():
    grid = [0.0, 0.25, 0.5, 0.75, 1.0]
    for prevalence in grid:
        for tpr in grid:
            for fpr in grid:
                initial = ConfusionRates(prevalence, tpr, fpr)
                for alpha in grid:
                    final = post_contestation_rates(initial, ContestationRates(alpha, alpha, 0.75, 0.25))
                    assert all(0.0 <= value <= 1.0 for value in (final.tpr, final.fnr, final.fpr, final.tnr, final.positive_rate))
                    assert abs(final.tpr + final.fnr - 1.0) < 1e-12
                    assert abs(final.fpr + final.tnr - 1.0) < 1e-12


def test_perfect_classifier_under_all_legal_appeal_rates():
    for alpha_plus in [0.0, 0.5, 1.0]:
        for alpha_minus in [0.0, 0.5, 1.0]:
            final = post_contestation_rates(ConfusionRates(0.5, 1.0, 0.0), ContestationRates(alpha_plus, alpha_minus, 1.0, 0.0))
            assert final.tpr == 1.0 and final.fpr == 0.0

