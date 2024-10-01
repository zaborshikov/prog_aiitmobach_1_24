from typing import Callable, Union


def accuracy_score(predicted: list, labels: list) -> float:
    """
    Calculating accuracy score

    in:
        predicted   (list): data that your model returns
        labels      (list): data that your model needs to return
    out:
        score      (float): accuracy score

    >>> accuracy_score([1, 1, 0, 1], [1, 1, 1, 1])
    0.75
    >>> accuracy_score([0, 1], [0, 1])
    1.0
    >>> accuracy_score([1], [0])
    0.0
    """

    size_of_data = len(labels)
    assert size_of_data == len(predicted)

    points = 0

    for i in range(size_of_data):
        points += labels[i] == predicted[i]

    score = points / size_of_data

    return score


def test(
    data: list,
    labels: list,
    func: Callable,
    input_args: dict = {},
    return_acuracy: bool = False,
    print_errors: bool = False,
) -> Union[float, list[bool]]:
    """
    Testing your model

    in:
        data    (list): data given to function
        out     (list): data
        func    (function): function for testing
        input_args  (list): input arguments for your function
        return_acuracy  (bool): return accuracy score, not list of bools
    out:
        list of bools (if True - test passed)
        OR accuracy score (if flag return_acuracy if True)

    >>> test([(1, 1), (2, 1), (2, 4)],
        [2, 3, 5], lambda a, b: a + b)
    [True, True, False]
    """

    size_of_data = len(data)
    assert size_of_data == len(labels)

    results = []

    for i in range(size_of_data):
        res = func(*data[i], **input_args)

        if print_errors:
            if res != labels[i]:
                print(f"ERROR: function returns [{res}], but need [{labels[i]}]")

        if return_acuracy:
            results.append(res)
        else:
            results.append(res == labels[i])

    if return_acuracy:
        return accuracy_score(results, labels)

    return results
