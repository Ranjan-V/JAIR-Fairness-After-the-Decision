from src.estimation.audit import hoeffding_audit_interval, propagate_q_interval_to_fnr, simultaneous_audit_intervals


def test_audit_interval_contains_estimate():
    interval = hoeffding_audit_interval(40, 100)
    assert interval.lower <= 0.4 <= interval.upper


def test_more_audits_narrow_hoeffding_radius_at_same_fraction():
    small = hoeffding_audit_interval(40, 100)
    large = hoeffding_audit_interval(400, 1000)
    assert large.width < small.width


def test_monotone_propagation():
    q = hoeffding_audit_interval(40, 100)
    fnr = propagate_q_interval_to_fnr(q, s=0.2, m=0.1, nonappellant_mass=0.4, rho=0.8)
    assert 0.0 <= fnr.lower <= fnr.upper <= 1.0


def test_simultaneous_intervals_for_all_groups():
    result = simultaneous_audit_intervals({"A": (40, 100), "B": (50, 100)})
    assert set(result) == {"A", "B"}

