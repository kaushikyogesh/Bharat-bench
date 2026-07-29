def numeric_tolerance(expected, predicted, tolerance=0.01):
    """
    Check whether a predicted numerical answer
    is within the acceptable tolerance range.
    """

    try:
        expected = float(expected)
        predicted = float(predicted)

        difference = abs(expected - predicted)

        if difference <= tolerance:
            return 1

        return 0

    except ValueError:
        return 0