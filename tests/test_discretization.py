import pytest

from src.algorithms.preprocessing.discretization import (
    equal_width_discretization,
)


def test_equal_width_discretization():
    data = [10, 20, 30, 40, 50]

    result = equal_width_discretization(data, 4)

    assert result == [0, 1, 2, 3, 3]


def test_equal_width_with_negative_values():
    data = [-10, 0, 10, 20]

    result = equal_width_discretization(data, 3)

    assert result == [0, 1, 2, 2]


def test_identical_values():
    data = [5, 5, 5]

    result = equal_width_discretization(data, 3)

    assert result == [0, 0, 0]


def test_empty_data():
    result = equal_width_discretization([], 3)

    assert result == []


def test_invalid_number_of_bins():
    with pytest.raises(ValueError):
        equal_width_discretization([10, 20, 30], 0)