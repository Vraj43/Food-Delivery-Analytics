from typing import List


def min_max_normalization(data: List[float]) -> List[float]:
    """
    Normalize numerical data to the range [0, 1]
    using Min-Max normalization.

    Formula:
        x' = (x - min) / (max - min)

    Parameters
    ----------
    data : List[float]
        Numerical dataset.

    Returns
    -------
    List[float]
        Normalized dataset.
    """

    if not data:
        return []

    minimum = min(data)
    maximum = max(data)

    # If all values are identical, normalization
    # cannot use the standard formula.
    if minimum == maximum:
        return [0.0] * len(data)

    return [
        (value - minimum) / (maximum - minimum)
        for value in data
    ]