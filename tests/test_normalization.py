from src.algorithms.preprocessing.normalization import (
    min_max_normalization,
)


def test_min_max_normalization():
    data = [10, 20, 30, 40, 50]

    result = min_max_normalization(data)

    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_min_max_with_negative_values():
    data = [-10, 0, 10]

    result = min_max_normalization(data)

    assert result == [0.0, 0.5, 1.0]


def test_identical_values():
    data = [5, 5, 5]

    result = min_max_normalization(data)

    assert result == [0.0, 0.0, 0.0]


def test_empty_data():
    data = []

    result = min_max_normalization(data)

    assert result == []