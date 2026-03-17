def detect_bottleneck(penalties, df):
    """
    Determines the largest performance bottleneck.
    """

    arithmetic_count = len(df[df["category"] == "Arithmetic"])

    scores = {
        "Memory Latency": penalties["memory_penalty"],
        "Data Hazards": penalties["data_hazard"],
        "Branch Penalties": penalties["branch_penalty"],
        "Arithmetic Pressure": arithmetic_count
    }

    bottleneck = max(scores, key=scores.get)

    return bottleneck, scores