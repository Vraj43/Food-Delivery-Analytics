from typing import List


def equal_width_discretization(
    data: List[float],
    num_bins: int
) -> List[int]:
    """
    Discretize numerical data using equal-width binning.

    Each value is assigned to a bin numbered from 0
    to num_bins - 1.

    Parameters
    ----------
    data : List[float]
        Numerical dataset.
    num_bins : int
        Number of bins.

    Returns
    -------
    List[int]
        Bin index assigned to each value.
    """

    if not data:
        return []

    if num_bins <= 0:
        raise ValueError("num_bins must be greater than 0")

    minimum = min(data)
    maximum = max(data)

    if minimum == maximum:
        return [0] * len(data)

    bin_width = (maximum - minimum) / num_bins

    result = []

    for value in data:
        bin_index = int((value - minimum) / bin_width)

        # Maximum value can produce num_bins,
        # so place it in the final bin.
        if bin_index >= num_bins:
            bin_index = num_bins - 1

        result.append(bin_index)

    return result