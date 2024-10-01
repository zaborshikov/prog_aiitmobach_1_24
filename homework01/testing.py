from typing import Callable, Union, List, Optional, Dict


def accuracy_score(predicted: List, labels: List) -> float:
    """
    Calculate the accuracy score.

    Args:
        predicted (List[int]): Data that your model returns.
        labels (List[int]): Data that your model needs to return.

    Returns:
        float: Accuracy score.

    Examples:
        >>> accuracy_score([1, 1, 0, 1], [1, 1, 1, 1])
        0.75
        >>> accuracy_score([0, 1], [0, 1])
        1.0
        >>> accuracy_score([1], [0])
        0.0
    """
    size_of_data = len(labels)
    assert size_of_data == len(predicted)
    assert predicted and labels

    points = sum(1 for i in range(size_of_data) if labels[i] == predicted[i])
    score = points / size_of_data

    return score


def test(
    data: List[tuple],
    labels: List[int],
    func: Callable,
    input_args: Optional[Dict] = None,
    return_accuracy: bool = False,
    print_errors: bool = False,
) -> Union[float, List[bool]]:
    """
    Testing your model

    Args:
        data (List[tuple]): Data given to function.
        labels (List[int]): Expected output data.
        func (Callable): Function for testing.
        input_args (Optional[Dict]): Input arguments for your function.
        return_accuracy (bool): Return accuracy score, not list of bools.
        print_errors (bool): Print errors if any.

    Returns:
        Union[float, List[bool]]: List of bools (if True - test passed)
        or accuracy score (if flag return_accuracy is True).

    Examples:
        >>> test([(1, 1), (2, 1), (2, 4)], [2, 3, 4], lambda a, b: a + b)
        [True, True, False]
        >>> test([(1, 1), (2, 1)], [2, 3], lambda a, b: a + b,
            return_accuracy=True)
        1.0
    """

    if input_args is None:
        input_args = {}

    size_of_data = len(data)
    assert size_of_data == len(labels)

    results = []

    for i, d in enumerate(data):
        try:
            result = func(*d, **input_args)
            results.append(result == labels[i])
        except Exception as e:
            if print_errors:
                print(f"Error in test case {i}: {e}")
            results.append(False)

    if return_accuracy:
        return sum(results) / len(results)

    return results
