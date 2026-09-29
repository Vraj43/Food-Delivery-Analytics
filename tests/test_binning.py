from src.algorithms.preprocessing.binning import (
    create_bins,
    smooth_by_mean,
    smooth_by_median,
    smooth_by_boundaries,
)


def test_create_bins():
    data = [4, 8, 15, 21, 25, 28]

    bins = create_bins(data, 3)

    assert bins == [
        [4, 8, 15],
        [21, 25, 28],
    ]


def test_mean_smoothing():
    bins = [
        [4, 8, 15],
        [21, 25, 28],
    ]

    result = smooth_by_mean(bins)

    assert result[0] == [9.0, 9.0, 9.0]


def test_median_smoothing():
    bins = [
        [4, 8, 15],
        [21, 25, 28],
    ]

    result = smooth_by_median(bins)

    assert result[0] == [8, 8, 8]


def test_boundary_smoothing():
    bins = [
        [4, 8, 15],
        [21, 25, 28],
    ]

    result = smooth_by_boundaries(bins)

    assert result[0] == [4, 4, 15]