def rubric_score(reference_answer, predicted_answer):
    """
    Rubric based scoring for open answers.
    Score:
    4 = Strong match
    2 = Partial match
    0 = Incorrect
    """

    reference = reference_answer.lower()
    prediction = predicted_answer.lower()

    keywords = []

    for word in reference.split():
        if len(word) > 4:
            keywords.append(word)

    matched = 0

    for word in keywords:
        if word in prediction:
            matched += 1

    if matched >= 5:
        return 4

    elif matched >= 2:
        return 2

    else:
        return 0