def refusal_check(predicted):
    """
    Check whether the model appropriately refuses
    to answer an unanswerable question.
    """

    refusal_phrases = [
        "i don't know",
        "i do not know",
        "not enough information",
        "cannot determine",
        "unable to answer",
        "insufficient information"
    ]

    predicted = str(predicted).strip().lower()

    for phrase in refusal_phrases:
        if phrase in predicted:
            return 1

    return 0