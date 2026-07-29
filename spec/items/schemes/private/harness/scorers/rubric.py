def rubric_score(score):
    """
    Validate a rubric-based score.
    Expected score range: 0 to 4.
    """

    try:
        score = int(score)

        if 0 <= score <= 4:
            return score

        return 0

    except ValueError:
        return 0