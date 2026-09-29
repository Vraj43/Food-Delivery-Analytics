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
    
def z_score_normalization(data: List[float]) -> List[float]:
    """
    Normalize numerical data using Z-Score normalization.

    Formula:
        z = (x - mean) / standard_deviation

    Parameters
    ----------
    data : List[float]
        Numerical dataset.

    Returns
    -------
    List[float]
        Z-score normalized dataset.
    """

    if not data:
        return []

    mean_value = sum(data) / len(data)

    variance = sum(
        (value - mean_value) ** 2
        for value in data
    ) / len(data)

    standard_deviation = variance ** 0.5

    # If all values are identical, standard deviation is zero.
    if standard_deviation == 0:
        return [0.0] * len(data)

    return [
        (value - mean_value) / standard_deviation
        for value in data
    ]