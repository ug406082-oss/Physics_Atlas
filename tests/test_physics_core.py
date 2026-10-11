"""Validation tests for the scientific helpers in Physics Atlas.

Run with:  pytest -q
These tests exercise the pure functions and check the internal consistency of
the static scientific data. They do not require Streamlit.
"""

import math

import pytest

from physics import data as D
from physics import physics_core as pc


def test_dimension_algebra():
    length = pc.dims(L=1)
    time = pc.dims(T=1)
    speed = pc.div_dims(length, time)
    assert speed == pc.dims(L=1, T=-1)
    accel = pc.div_dims(speed, time)
    assert accel == pc.dims(L=1, T=-2)
    area = pc.mul_dims(length, length)
    assert area == pc.dims(L=2)
    assert pc.pow_dims(length, 3) == pc.dims(L=3)
    assert pc.is_dimensionless(pc.div_dims(length, length))


def test_dim_unicode_is_exact():
    assert pc.dim_unicode(pc.dims(L=1)) == "[L]"
    assert pc.dim_unicode(pc.dims(L=1, T=-1)) == "[L T⁻¹]"
    assert pc.dim_unicode(pc.dims(M=1, L=1, T=-2)) == "[M L T⁻²]"
    assert pc.dim_unicode(pc.dims(M=1, L=-1, T=-2)) == "[M L⁻¹ T⁻²]"
    assert pc.dim_unicode(pc.dims()) == "[dimensionless]"


def test_force_and_energy_dimensions_from_definitions():
    force = pc.mul_dims(pc.dims(M=1), pc.dims(L=1, T=-2))
    assert force == pc.dims(M=1, L=1, T=-2)
    energy = pc.mul_dims(force, pc.dims(L=1))
    assert energy == pc.dims(M=1, L=2, T=-2)


def test_homogeneity_of_valid_equations():
    assert pc.check_homogeneity([pc.dims(L=1)], [pc.dims(L=1)])["homogeneous"]
    assert pc.check_homogeneity([pc.dims(L=1, T=-1)], [pc.dims(L=1, T=-1)])["homogeneous"]


def test_homogeneity_of_invalid_equation():
    result = pc.check_homogeneity([pc.dims(L=1, T=-1)], [pc.dims(L=1)])
    assert not result["homogeneous"]


def test_pendulum_derivation():
    deriv = pc.solve_pendulum_exponents()
    assert deriv["a"] == 0
    assert deriv["b"] == pytest.approx(0.5)
    assert deriv["c"] == pytest.approx(-0.5)
    assert "sqrt(L / g)" in deriv["result"]


@pytest.mark.parametrize("text,expected", [
    ("0.00250", 3),
    ("250", 2),
    ("2.5", 2),
    ("10.0", 3),
    ("0.050", 2),
    ("1.20e5", 3),
    ("1.20x10^5", 3),
    ("0.0001", 1),
    ("5.00", 3),
])
def test_significant_figures(text, expected):
    assert pc.analyse_significant_figures(text)["count"] == expected


def test_significant_figures_ambiguity():
    result = pc.analyse_significant_figures("1500")
    assert result["ambiguous"] is True
    assert result["count"] == 2
    result2 = pc.analyse_significant_figures("1500.")
    assert result2["ambiguous"] is False
    assert result2["count"] == 4


def test_significant_figures_invalid_input():
    assert pc.analyse_significant_figures("abc")["valid"] is False
    assert pc.analyse_significant_figures("")["valid"] is False


def test_rounding_to_significant_figures():
    assert pc.format_to_sig_figs(8.55, 2) == "8.6"
    assert pc.format_to_sig_figs(33.3333, 3) == "33.3"
    assert pc.round_to_sig_figs(6000.0, 3) == 6000.0
    assert pc.round_to_sig_figs(0.0367, 2) == pytest.approx(0.037)
    assert pc.format_to_sig_figs(20.0, 2) == "20"


def test_uncertainty_helpers():
    assert pc.fractional_uncertainty(0.5, 20.0) == pytest.approx(0.025)
    assert pc.percentage_uncertainty(0.5, 20.0) == pytest.approx(2.5)
    assert pc.fractional_uncertainty(1.0, 0.0) == math.inf


def test_momentum_uncertainty_quadrature():
    rel = pc.relative_uncertainty_quadrature([(1, 0.1 / 2.0), (1, 0.1 / 3.0)])
    assert rel == pytest.approx(0.0600, abs=0.0005)
    result = pc.propagate_product(6.0, [(1, 0.05), (1, 0.0333333)], "quadrature")
    assert result["absolute"] == pytest.approx(0.36, abs=0.01)


def test_momentum_uncertainty_maximum_is_larger():
    quad = pc.relative_uncertainty_quadrature([(1, 0.05), (1, 0.0333)])
    maxim = pc.relative_uncertainty_maximum([(1, 0.05), (1, 0.0333)])
    assert maxim > quad
    assert maxim == pytest.approx(0.0833, abs=0.001)


def test_uncertainty_with_negative_exponent():
    rel = pc.relative_uncertainty_quadrature([(1, 0.004), (-1, 0.0166667)])
    assert rel == pytest.approx(0.0171, abs=0.0005)


def test_combine_absolute_uncertainties():
    assert pc.uncertainty_from_absolute_terms([0.3, 0.4], "quadrature") == pytest.approx(0.5)
    assert pc.uncertainty_from_absolute_terms([0.3, 0.4], "maximum") == pytest.approx(0.7)


def test_summary_statistics():
    stats = pc.summary_statistics([1.0, 2.0, 3.0, 4.0])
    assert stats["mean"] == pytest.approx(2.5)
    assert stats["n"] == 4
    assert stats["stdev"] == pytest.approx(1.29099, abs=1e-4)


def test_volume_and_density():
    volume = pc.volume_of_sphere(6.0e-3)
    assert volume == pytest.approx(1.131e-7, rel=1e-2)
    assert pc.density(2.0, 4.0) == pytest.approx(0.5)
    assert pc.density(1.0, 0.0) == math.inf


def test_convert_prefix():
    assert pc.convert_prefix(1.0, 1e3, 1e-3) == pytest.approx(1e6)
    with pytest.raises(ValueError):
        pc.convert_prefix(1.0, 1.0, 0.0)


def test_safe_divide():
    assert pc.safe_divide(10, 2) == 5
    assert pc.safe_divide(10, 0) is None


def test_si_base_quantities_are_correct():
    expected = {
        "Length": ("metre", "m"), "Mass": ("kilogram", "kg"), "Time": ("second", "s"),
        "Electric current": ("ampere", "A"), "Thermodynamic temperature": ("kelvin", "K"),
        "Amount of substance": ("mole", "mol"), "Luminous intensity": ("candela", "cd"),
    }
    assert len(D.SI_BASE_QUANTITIES) == 7
    for row in D.SI_BASE_QUANTITIES:
        assert row["unit"], row
        assert row["symbol"] == expected[row["quantity"]][1]
        assert row["unit"] == expected[row["quantity"]][0]


def test_every_base_quantity_has_a_single_base_dimension():
    for row in D.SI_BASE_QUANTITIES:
        assert len(pc.normalise_dims(row["dims"])) == 1


def test_derived_quantity_dimensions_are_consistent():
    lookup = {q["name"]: q["dims"] for q in D.DERIVED_QUANTITIES}
    assert lookup["Area"] == pc.dims(L=2)
    assert lookup["Volume"] == pc.dims(L=3)
    assert lookup["Speed and velocity"] == pc.dims(L=1, T=-1)
    assert lookup["Acceleration"] == pc.dims(L=1, T=-2)
    assert lookup["Force"] == pc.dims(M=1, L=1, T=-2)
    assert lookup["Momentum"] == pc.dims(M=1, L=1, T=-1)
    assert lookup["Work and energy"] == pc.dims(M=1, L=2, T=-2)
    assert lookup["Pressure"] == pc.dims(M=1, L=-1, T=-2)
    assert lookup["Density"] == pc.dims(M=1, L=-3)
    assert lookup["Frequency"] == pc.dims(T=-1)


def test_derived_quantity_definitions_match_dimensions():
    for q in D.DERIVED_QUANTITIES:
        recomputed = None
        if q["name"] == "Force":
            recomputed = pc.mul_dims(pc.dims(M=1), pc.dims(L=1, T=-2))
        elif q["name"] == "Work and energy":
            recomputed = pc.mul_dims(pc.dims(M=1, L=1, T=-2), pc.dims(L=1))
        elif q["name"] == "Pressure":
            recomputed = pc.div_dims(pc.dims(M=1, L=1, T=-2), pc.dims(L=2))
        elif q["name"] == "Density":
            recomputed = pc.div_dims(pc.dims(M=1), pc.dims(L=3))
        elif q["name"] == "Speed and velocity":
            recomputed = pc.div_dims(pc.dims(L=1), pc.dims(T=1))
        if recomputed is not None:
            assert recomputed == q["dims"], q["name"]


def test_homogeneity_examples_are_internally_consistent():
    for example in D.HOMOGENEITY_EXAMPLES:
        result = pc.check_homogeneity([example["lhs_dims"]], [example["rhs_dims"]])
        assert result["homogeneous"] == example["valid"], example["title"]


def test_chapter_list_has_ten_entries():
    assert len(D.CHAPTERS) == 10
    assert D.CHAPTERS[0]["title"] == "Physical Quantities and Measurement"
    assert [c["number"] for c in D.CHAPTERS] == list(range(1, 11))
    assert all("module" in c for c in D.CHAPTERS)


def test_a_chapter_is_available_only_once_its_modules_exist():
    """The picker must never offer a chapter whose files are missing."""
    import importlib

    for chapter in D.CHAPTERS:
        try:
            importlib.import_module(f"physics.chapters.{chapter['module']}_data")
            available = True
        except ModuleNotFoundError:
            available = False
        assert chapter["available"] == available, chapter["number"]


def test_thirteen_slos_present():
    assert len(D.SLOS) == 13
    ids = [s["id"] for s in D.SLOS]
    assert ids == ["1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.1.5",
                   "1.2.1", "1.2.2", "1.2.3", "1.2.4", "1.3.1", "1.3.2",
                   "1.4.1", "1.4.2"]
    for slo in D.SLOS:
        assert slo["taught"] and slo["activity"] and slo["check"]


def test_practice_answers_are_valid():
    for q in D.PRACTICE_QUESTIONS:
        assert q["type"] in ("mcq", "numeric")
        if q["type"] == "mcq":
            assert 0 <= q["answer"] < len(q["options"])
            assert len(set(q["options"])) == len(q["options"])
        else:
            assert isinstance(q["answer"], (int, float))
            assert q["tolerance"] >= 0


def test_worked_problem_answers_are_computable():
    assert pc.density(0.2400, 4.00e-5) == pytest.approx(6000.0, rel=1e-9)
    v = pc.safe_divide(250.0, 12.0)
    assert v == pytest.approx(20.8333, abs=1e-3)
    area = 12.5 * 8.0
    rel = 0.1 / 12.5 + 0.1 / 8.0
    assert area * rel == pytest.approx(2.05, abs=0.01)


def test_all_references_have_urls():
    assert len(D.REFERENCES) >= 4
    for ref in D.REFERENCES:
        assert ref["url"].startswith("http")
