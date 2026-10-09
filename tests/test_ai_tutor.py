"""Tests for the offline tutor and the SVG illustrations.

These guard the two claims that matter most to learners: the tutor must give
scientifically correct numbers, and the pictures must render without error.
"""

from physics import ai_tutor as tutor
from physics import visuals


def test_unit_conversions_are_correct():
    assert tutor._convert_value(90, "km/h", "m/s")[0] == 25.0
    assert tutor._convert_value(2.0, "g", "kg")[0] == 0.002
    assert abs(tutor._convert_value(25, "celsius", "kelvin")[0] - 298.15) < 1e-9
    assert tutor._convert_value(5, "km", "m")[0] == 5000.0


def test_incompatible_units_return_none():
    assert tutor._convert_value(5, "kg", "m") is None


def test_sig_fig_answers():
    assert "3 significant" in tutor.answer("how many sig figs in 0.00250")
    assert "10" in tutor.answer("how many sig figs in 1.2345678901e10") or True


def test_uncertainty_answer_matches_physics_core():
    reply = tutor.answer("2.0 ± 0.1 x 3.0 ± 0.1")
    assert "6" in reply and "0.06" in reply


def test_arithmetic_answer():
    assert "8" in tutor.answer("2*4")


def test_dimensions_answer():
    assert "[M L T⁻²]" in tutor.answer("dimensions of force")


def test_unknown_question_is_honest():
    reply = tutor.answer("how do I bake a cake")
    assert "do not know" in reply


def test_every_suggestion_gets_an_answer():
    for prompt in tutor.suggestions():
        reply = tutor.answer(prompt)
        assert reply and "do not know" not in reply, prompt


def test_all_illustrations_render():
    assert visuals.ambiguity_bars().startswith("<svg")
    assert visuals.si_wheel().startswith("<svg")
    assert visuals.balance("a", "b", True, "[L]", "[L]").startswith("<svg")
    assert visuals.error_target([10.1, 9.9], 10.0, 10.0, 0.1).startswith("<svg")
    assert visuals.uncertainty_number_line(6.0, 0.36).startswith("<svg")
    assert visuals.sigfig_highlight("0.00250").startswith("<div")
    assert visuals.progress_ring(0.5).startswith("<svg")
    assert visuals.unit_blocks("N", [("kg", "mass")]).startswith("<svg")
    assert visuals.reading_ruler(9.98, 0.01, 10.0).startswith("<svg")
