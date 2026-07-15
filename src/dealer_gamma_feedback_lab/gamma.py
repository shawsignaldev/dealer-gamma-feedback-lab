def feedback_gain(gamma: float, beta: float, shock: float) -> float:
    return round(abs(gamma) * abs(beta) * abs(shock), 6)

def stability_label(gain: float, threshold: float = 1.0) -> str:
    return "unstable" if gain >= threshold else "stable"
