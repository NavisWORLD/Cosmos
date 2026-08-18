from cosmos.tools.reality_bridge_processor import lottery_random_baseline, moving_average, persistence_baseline


def test_prediction_baselines_are_deterministic():
    assert persistence_baseline([1, 2, 3]) == 3.0
    assert moving_average([1, 2, 3, 4], 2) == 3.5
    a = lottery_random_baseline(1, 69, 5, "universe-seed")
    b = lottery_random_baseline(1, 69, 5, "universe-seed")
    assert a == b
    assert len(set(a)) == 5
