def exact_match(expected, predicted):
    """
    Check whether the expected answer
    and predicted answer are exactly the same.
    """

    expected = str(expected).strip().lower()
    predicted = str(predicted).strip().lower()

    if expected == predicted:
        return 1

    return 0