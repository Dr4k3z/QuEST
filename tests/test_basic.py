import quest


def test_add() -> None:
    assert quest.add(2, 3) == 5


def test_add_10_times() -> None:
    assert quest.add_10_times(2, 3) == 50
