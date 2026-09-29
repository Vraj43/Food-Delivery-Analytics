import pytest

from src.algorithms.preprocessing.feature_selection import (
    pearson_correlation,
    select_by_target_correlation,
)


def test_perfect_positive_correlation():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    result = pearson_correlation(x, y)

    assert abs(result - 1.0) < 1e-10


def test_perfect_negative_correlation():
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]

    result = pearson_correlation(x, y)

    assert abs(result + 1.0) < 1e-10


def test_no_correlation():
    x = [1, 2, 3, 4, 5]
    y = [3, 3, 3, 3, 3]

    result = pearson_correlation(x, y)

    assert result == 0.0


def test_different_lengths():
    x = [1, 2, 3]
    y = [1, 2]

    with pytest.raises(ValueError):
        pearson_correlation(x, y)


def test_feature_selection():
    features = {
        "strong_feature": [1, 2, 3, 4, 5],
        "weak_feature": [5, 5, 5, 5, 5],
        "negative_feature": [10, 8, 6, 4, 2],
    }

    target = [2, 4, 6, 8, 10]

    result = select_by_target_correlation(
        features,
        target,
        threshold=0.5,
    )

    assert result == [
        "strong_feature",
        "negative_feature",
    ]


def test_invalid_threshold():
    features = {
        "feature": [1, 2, 3]
    }

    target = [2, 4, 6]

    with pytest.raises(ValueError):
        select_by_target_correlation(
            features,
            target,
            threshold=1.5,
        )