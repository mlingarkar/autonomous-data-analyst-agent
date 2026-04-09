def is_ml_question(question: str) -> bool:
    """
    Detect whether the user's question sounds like a modeling/prediction request.
    """
    q = question.lower()

    keywords = [
        "predict",
        "prediction",
        "forecast",
        "model",
        "train a model",
        "machine learning",
        "ml",
        "feature importance",
        "important features",
        "which features matter",
        "regression",
    ]

    return any(keyword in q for keyword in keywords)