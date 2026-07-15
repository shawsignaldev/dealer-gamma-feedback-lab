from dealer_gamma_feedback_lab.gamma import feedback_gain, stability_label

def test_feedback_gain_scales_gamma_beta_and_shock() -> None:
    assert feedback_gain(gamma=2.0, beta=1.5, shock=0.1) == 0.3

def test_stability_label_flags_high_gain() -> None:
    assert stability_label(1.2) == "unstable"
    assert stability_label(0.7) == "stable"
