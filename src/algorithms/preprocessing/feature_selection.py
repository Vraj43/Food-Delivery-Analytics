from typing import Dict, List


def pearson_correlation(
    x: List[float],
    y: List[float]
) -> float:
    """
    Calculate Pearson correlation coefficient
    between two numerical variables.

    Formula:

        r = covariance(x, y) /
            (standard_deviation_x * standard_deviation_y)

    Returns a value between -1 and 1.
    """

    if len(x) != len(y):
        raise ValueError("Both datasets must have the same length")

    if not x:
        raise ValueError("Datasets cannot be empty")

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    numerator = sum(
        (x_value - mean_x) * (y_value - mean_y)
        for x_value, y_value in zip(x, y)
    )

    sum_squared_x = sum(
        (x_value - mean_x) ** 2
        for x_value in x
    )

    sum_squared_y = sum(
        (y_value - mean_y) ** 2
        for y_value in y
    )

    denominator = (
        sum_squared_x * sum_squared_y
    ) ** 0.5

    # Correlation is undefined when one variable
    # has no variation.
    if denominator == 0:
        return 0.0

    return numerator / denominator


def select_by_target_correlation(
    features: Dict[str, List[float]],
    target: List[float],
    threshold: float = 0.3
) -> List[str]:
    """
    Select features based on their absolute
    Pearson correlation with the target.

    Parameters
    ----------
    features : Dict[str, List[float]]
        Dictionary containing feature names and values.

    target : List[float]
        Target variable.

    threshold : float
        Minimum absolute correlation required.

    Returns
    -------
    List[str]
        Selected feature names.
    """

    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    selected = []

    for feature_name, values in features.items():
        correlation = pearson_correlation(values, target)

        if abs(correlation) >= threshold:
            selected.append(feature_name)

    return selected