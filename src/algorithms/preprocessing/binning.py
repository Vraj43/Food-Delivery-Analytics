from statistics import median
from typing import List


def create_bins(data: List[float], bin_size: int) -> List[List[float]]:
    """
    Divide sorted data into equal-sized bins.

    Parameters
    ----------
    data : List[float]
        Numerical dataset.
    bin_size : int
        Number of values in each bin.

    Returns
    -------
    List[List[float]]
        Binned data.
    """

    if bin_size <= 0:
        raise ValueError("bin_size must be greater than 0")

    if not data:
        return []

    sorted_data = sorted(data)

    return [
        sorted_data[i:i + bin_size]
        for i in range(0, len(sorted_data), bin_size)
    ]


def smooth_by_mean(bins: List[List[float]]) -> List[List[float]]:
    """Replace every value in a bin with the bin mean."""

    smoothed = []

    for current_bin in bins:
        mean_value = sum(current_bin) / len(current_bin)
        smoothed.append([mean_value] * len(current_bin))

    return smoothed


def smooth_by_median(bins: List[List[float]]) -> List[List[float]]:
    """Replace every value in a bin with the bin median."""

    smoothed = []

    for current_bin in bins:
        median_value = median(current_bin)
        smoothed.append([median_value] * len(current_bin))

    return smoothed


def smooth_by_boundaries(bins: List[List[float]]) -> List[List[float]]:
    """
    Replace each value with the closest boundary
    of its bin.
    """

    smoothed = []

    for current_bin in bins:
        lower = current_bin[0]
        upper = current_bin[-1]

        new_bin = []

        for value in current_bin:
            if abs(value - lower) <= abs(value - upper):
                new_bin.append(lower)
            else:
                new_bin.append(upper)

        smoothed.append(new_bin)

    return smoothed