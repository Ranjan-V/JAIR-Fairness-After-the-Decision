from src.datasets.synthetic import GroupConfig, SyntheticConfig, generate_population
from src.experiments.common import summarize_decisions


def test_generator_schema_and_bounds():
    config = SyntheticConfig(
        n=1000,
        seed=7,
        groups={
            "A": GroupConfig(0.5, 0.5, 0.7, 0.2),
            "B": GroupConfig(0.5, 0.5, 0.7, 0.2),
        },
    )
    frame = generate_population(config)
    assert len(frame) == 1000
    assert set(frame["appeal"].unique()).issubset({0, 1})
    assert (frame.loc[frame["d0"] == 1, "appeal"] == 0).all()
    assert ((frame["d1"] >= frame["d0"])).all()


def test_summary_contains_pre_and_post_metrics():
    config = SyntheticConfig(
        n=2000,
        seed=11,
        groups={
            "A": GroupConfig(0.5, 0.5, 0.7, 0.2),
            "B": GroupConfig(0.5, 0.5, 0.7, 0.2),
        },
    )
    summary = summarize_decisions(generate_population(config))
    assert {"pre", "post", "pre_gaps", "post_gaps", "contestation"} <= set(summary)

