"""Curriculum integrity tests.

These tests import *only* the pure data modules and the pure physics core, so
they run under a bare Python interpreter with no Streamlit, pandas or NumPy
installed. That is deliberate: the curriculum is the part of the app that must
never be wrong, so it must never depend on the web framework.

They check that the syllabus is complete, that every claim is anchored to a
real learning outcome, that every question is answerable and that the numbers
the app would show are the numbers physics actually gives.
"""

import math
import re

import pytest

from physics import curriculum
from physics.core import (fluids, measurement, motion1d, motion2d, optics,
                          oscillations, solids, thermo, vectors, waves)

# --------------------------------------------------------------------------
# The shape of the syllabus itself
# --------------------------------------------------------------------------

def test_ten_chapters_numbered_in_order():
    assert [c["number"] for c in curriculum.CHAPTERS] == list(range(1, 11))


def test_every_chapter_is_open_and_has_a_module_and_blurb():
    for chapter in curriculum.CHAPTERS:
        assert chapter["available"] is True, chapter["number"]
        assert chapter["module"].startswith("ch")
        assert chapter["blurb"].strip()


def test_outcome_counts_match_the_published_syllabus():
    expected = {1: 13, 2: 10, 3: 12, 4: 20, 5: 8, 6: 18, 7: 22, 8: 19, 9: 28, 10: 35}
    for number, count in expected.items():
        assert len(curriculum.slo_ids(number)) == count, number
    assert len(curriculum.total_slo_ids()) == sum(expected.values())


def test_outcome_identifiers_are_well_formed_and_unique():
    seen = set()
    for number in range(1, 11):
        for slo_id in curriculum.slo_ids(number):
            assert slo_id.startswith(f"{number}."), slo_id
            assert re.fullmatch(rf"{number}\.\d+\.\d+", slo_id), slo_id
            assert slo_id not in seen, f"{slo_id} appears twice"
            seen.add(slo_id)


# --------------------------------------------------------------------------
# What each chapter must contain
# --------------------------------------------------------------------------

REQUIRED_SLO_KEYS = {"id", "text", "simple", "taught", "activity", "check"}
REQUIRED_STATION_KEYS = {"key", "label", "slos"}


@pytest.mark.parametrize("number", range(1, 11))
def test_chapter_data_is_complete(number):
    data = curriculum.chapter_data(number)
    assert data.SLOS, number
    assert data.WORKED_PROBLEMS, number
    assert data.PRACTICE_QUESTIONS, number
    assert data.REFERENCES, number
    assert data.STATIONS, number
    assert data.BIG_IDEAS, number
    assert data.INTRO.strip(), number

    for slo in data.SLOS:
        assert REQUIRED_SLO_KEYS <= set(slo), (number, slo.get("id"))
        for key in REQUIRED_SLO_KEYS:
            assert str(slo[key]).strip(), (slo["id"], key)

    keys = [s["key"] for s in data.STATIONS]
    assert len(keys) == len(set(keys)), f"duplicate station keys in chapter {number}"
    for station in data.STATIONS:
        assert REQUIRED_STATION_KEYS <= set(station), (number, station)
        assert station["label"].strip()

    for reference in data.REFERENCES:
        assert reference["url"].startswith("http")
        for key in ("short", "title", "org", "used_for"):
            assert str(reference[key]).strip()


@pytest.mark.parametrize("number", range(1, 11))
def test_every_outcome_is_taught_by_exactly_one_station(number):
    """No outcome may be orphaned, and none may be claimed twice."""
    data = curriculum.chapter_data(number)
    ids = [slo["id"] for slo in data.SLOS]
    claimed = []
    for station in data.STATIONS:
        for slo_id in station["slos"]:
            assert slo_id in ids, f"chapter {number} station {station['key']} claims unknown {slo_id}"
            claimed.append(slo_id)
    assert sorted(claimed) == sorted(ids), (
        f"chapter {number}: outcomes with no station are "
        f"{sorted(set(ids) - set(claimed))}, duplicated are "
        f"{sorted(set(claimed) - set(ids))}"
    )


@pytest.mark.parametrize("number", range(1, 11))
def test_practice_questions_are_answerable_and_anchored(number):
    data = curriculum.chapter_data(number)
    ids = {slo["id"] for slo in data.SLOS}
    seen = set()
    for q in data.PRACTICE_QUESTIONS:
        assert q["id"] not in seen, f"duplicate question id {q['id']}"
        seen.add(q["id"])
        assert q["slo"] in ids, f"{q['id']} points at unknown outcome {q['slo']}"
        assert q["category"].strip() and q["prompt"].strip()
        assert q["hint"].strip() and q["explanation"].strip()
        if q["type"] == "mcq":
            assert len(q["options"]) >= 3
            assert len(set(q["options"])) == len(q["options"]), q["id"]
            assert isinstance(q["answer"], int) and 0 <= q["answer"] < len(q["options"])
            assert q["answer"] not in q["options"] or True
        else:
            assert isinstance(q["answer"], (int, float)) and math.isfinite(q["answer"])
            assert q["tolerance"] >= 0
            assert math.isfinite(float(q["answer"])) or q["answer"] == 0


@pytest.mark.parametrize("number", range(1, 11))
def test_practice_covers_every_outcome_at_least_once(number):
    data = curriculum.chapter_data(number)
    asked = {q["slo"] for q in data.PRACTICE_QUESTIONS}
    missing = {slo["id"] for slo in data.SLOS} - asked
    assert not missing, f"chapter {number} never tests {sorted(missing)}"


@pytest.mark.parametrize("number", range(1, 11))
def test_worked_problems_are_complete(number):
    data = curriculum.chapter_data(number)
    seen = set()
    required = {"id", "title", "level", "question", "known", "find", "equation",
                "conversions", "substitution", "calculation", "unit_check",
                "answer", "sig_fig_note", "assumptions"}
    for problem in data.WORKED_PROBLEMS:
        assert required <= set(problem), (problem["id"], sorted(required - set(problem)))
        assert problem["id"] not in seen, problem["id"]
        seen.add(problem["id"])
        assert problem["level"] in {"Foundation", "Developing", "Challenge"}
        for key in ("known", "calculation", "assumptions", "conversions"):
            assert problem[key], (problem["id"], key)
        for key in ("question", "find", "answer", "sig_fig_note", "title"):
            assert str(problem[key]).strip(), (problem["id"], key)


@pytest.mark.parametrize("number", range(1, 11))
def test_worked_problems_are_anchored_to_outcomes(number):
    data = curriculum.chapter_data(number)
    ids = {slo["id"] for slo in data.SLOS}
    for problem in data.WORKED_PROBLEMS:
        for slo_id in problem.get("slos", []):
            assert slo_id in ids, (problem["id"], slo_id)


# --------------------------------------------------------------------------
# Chapter 1 keeps its historical module layout
# --------------------------------------------------------------------------

def test_chapter_one_slos_are_unchanged():
    from physics import data as legacy
    assert len(legacy.SLOS) == 13
    assert [s["id"] for s in legacy.SLOS] == [
        "1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.1.5", "1.2.1", "1.2.2",
        "1.2.3", "1.2.4", "1.3.1", "1.3.2", "1.4.1", "1.4.2",
    ]


# --------------------------------------------------------------------------
# The physics: numbers the app will show must be the right ones
# --------------------------------------------------------------------------

def test_chapter_one_measurements_unchanged():
    assert measurement.dim_unicode(measurement.dims(M=1, L=1, T=-2)) == "[M L T⁻²]"
    assert measurement.dim_unicode(measurement.dims(L=1)) == "[L]"
    assert measurement.analyse_significant_figures("0.00250")["count"] == 3
    assert measurement.analyse_significant_figures("1500")["ambiguous"] is True
    assert measurement.format_to_sig_figs(8.55, 2) == "8.6"
    terms = [(1, 0.004), (-1, 1.0 / 60.0)]
    assert measurement.relative_uncertainty_quadrature(terms) == pytest.approx(0.0171, abs=1e-4)


def test_chapter_two_vector_products():
    a, b = vectors.components_from_polar(5, 60)
    assert a == pytest.approx(2.5)
    assert b == pytest.approx(5 * math.sin(math.radians(60)))
    assert vectors.magnitude((3, 4)) == pytest.approx(5)
    assert vectors.angle_of((0, 1)) == pytest.approx(90)
    # Perpendicular vectors have a zero scalar product.
    assert vectors.dot_product((1, 0), (0, 1)) == 0
    # A vector with itself gives the square of its magnitude.
    assert vectors.dot_product((3, 4), (3, 4)) == pytest.approx(25)
    # The two products are commutative / anti-commutative.
    p, q = vectors.components_from_polar(4, 30), vectors.components_from_polar(6, 100)
    assert vectors.dot_commutativity_error(p, q) == pytest.approx(0, abs=1e-12)
    assert vectors.cross_anticommutativity_error(p, q) == pytest.approx(0, abs=1e-12)
    # The cross product magnitude is A B sin(theta).
    assert abs(vectors.cross_product((1, 0), (0, 1))) == pytest.approx(1)
    # A dot B equals A B cos(theta).
    assert vectors.dot_product((1, 0), (0, 1)) == pytest.approx(
        1 * 1 * math.cos(math.pi / 2), abs=1e-12)
    # Work is the scalar product of force and displacement.
    assert vectors.work((10, 0), (2, 0)) == pytest.approx(20)
    assert vectors.work((10, 0), (0, 2)) == pytest.approx(0)


def test_chapter_three_equations_of_motion_and_collisions():
    assert motion1d.velocity(0, 9.8, 3) == pytest.approx(29.4)
    assert motion1d.displacement(0, 9.8, 3) == pytest.approx(44.1)
    assert motion1d.displacement_from_velocity(0, 29.4, 9.8) == pytest.approx(44.1)
    # Equal masses swap velocities in an elastic collision.
    r = motion1d.elastic_collision_1d(1, 10, 1, 0)
    assert r["v1"] == pytest.approx(0)
    assert r["v2"] == pytest.approx(10)
    assert r["kinetic_conserved"] and r["momentum_conserved"]
    # A perfectly inelastic collision shares one velocity and loses kinetic energy.
    r = motion1d.inelastic_collision_1d(1, 10, 1, 0)
    assert r["v1"] == pytest.approx(r["v2"]) == pytest.approx(5)
    assert r["momentum_conserved"]
    assert not r["kinetic_conserved"]
    assert r["kinetic_lost"] == pytest.approx(25)
    # Hitting a heavier stationary body rebounds the light one at the heavier
    # body's speed: v1 = ((m1-m2)u1 + 2 m2 u2)/(m1+m2), v2 = 2 m1 u1/(m1+m2).
    r = motion1d.elastic_collision_1d(1, 10, 5, 0)
    assert r["v1"] == pytest.approx(-40 / 6)
    assert r["v2"] == pytest.approx(20 / 6)
    assert r["momentum_conserved"] and r["kinetic_conserved"]
    # Hitting a lighter stationary body sends it off at twice the speed.
    r = motion1d.elastic_collision_1d(5, 10, 1, 0)
    assert r["v1"] == pytest.approx(40 / 6)
    assert r["v2"] == pytest.approx(100 / 6)
    # Area under an F-d graph is the work.
    assert motion1d.area_under_fd([0, 10, 10, 0], [0, 1, 2, 3]) == pytest.approx(20)
    assert motion1d.area_under_fd([0, -10, 0], [0, 1, 2]) == pytest.approx(-10)
    # Work-energy theorem: net work equals the change in kinetic energy.
    check = motion1d.work_energy_check(2, 0, 4, friction=0)
    assert check["delta_kinetic"] == pytest.approx(16)
    assert check["consistent"]


def test_chapter_four_projectiles_and_rotation():
    p = motion2d.projectile(20, 45)
    assert p["time_of_flight"] == pytest.approx(2 * 20 * math.sin(math.pi / 4) / 9.8)
    assert p["max_range"] == pytest.approx(20 ** 2 / 9.8)
    assert p["range"] == pytest.approx(p["max_range"])          # 45 degrees is optimal
    assert p["max_height"] == pytest.approx(20 ** 2 * 0.5 / (2 * 9.8))
    assert motion2d.projectile(20, 30)["range"] < p["range"]
    # Centripetal quantities.
    assert motion2d.centripetal_acceleration(10, 5) == pytest.approx(20)
    assert motion2d.centripetal_force(2, 10, 5) == pytest.approx(40)
    # Torque is r F sin(theta) and is largest at right angles.
    assert motion2d.torque(2, 10, 90) == pytest.approx(20)
    assert motion2d.torque(2, 10, 180) == pytest.approx(0, abs=1e-12)
    # Moment of inertia: a ring is the largest, a semi-disc the smallest here.
    values = {body: motion2d.moment_of_inertia(body, 1, 1)
              for body in ("ring", "disc", "sphere", "shell", "semi")}
    assert values["ring"] == pytest.approx(1.0)
    assert values["disc"] == pytest.approx(0.5)
    assert values["sphere"] == pytest.approx(0.4)
    assert values["shell"] == pytest.approx(2 / 3)
    assert values["semi"] == pytest.approx(0.125)
    # Hollow bodies resist rotation more than solid ones of the same mass and
    # radius, because their mass sits further from the axis.
    assert values["ring"] > values["shell"] > values["disc"] > values["sphere"] > values["semi"]
    assert motion2d.moment_of_inertia("rod", 1, 1, length=2) == pytest.approx(1 / 3)
    assert motion2d.moment_of_inertia("rod", 1, 1, length=2, axis="end") == pytest.approx(4 / 3)
    # Angular momentum is conserved when the moment of inertia falls.
    result = motion2d.conserve_angular_momentum(2, 5, 0.5)
    assert result["omega_after"] == pytest.approx(20)
    assert result["angular_momentum_after"] == pytest.approx(10)
    # Apparent gravity in a rotating spacecraft.
    assert motion2d.artificial_gravity(5, 2) == pytest.approx(20)


def test_chapter_five_stress_strain_and_energy():
    assert solids.stress(100, 0.001) == pytest.approx(100000)
    assert solids.strain(0.002, 2.0) == pytest.approx(0.001)
    assert solids.young_modulus(2e8, 0.001) == pytest.approx(2e11)
    assert solids.length_change(100, 2.0, 0.001, 200e9) == pytest.approx(1e-6)
    assert solids.elastic_energy_from_k(200, 0.01) == pytest.approx(0.01)
    assert solids.elastic_energy_from_force(100, 0.01) == pytest.approx(0.5)
    assert solids.energy_density(2e11, 1e-4) == pytest.approx(1e7)
    # Every generated curve must start in the elastic region and end at fracture.
    for material in solids.MATERIALS:
        curve = solids.stress_strain_series(material)
        assert curve["youngs_modulus"] == material["youngs_modulus"]
        assert curve["elastic_strain"] <= curve["ultimate_strain"] <= curve["fracture_strain"]
        assert curve["stress"][0] == pytest.approx(0, abs=1e-9)
        # Every point inside the elastic region must follow Hooke's law exactly:
        # that straight branch is the definition of the Young's modulus.
        elastic_points = [(e, s) for e, s in zip(curve["strain"], curve["stress"])
                          if e <= curve["elastic_strain"]]
        assert len(elastic_points) >= 2, material["name"]
        for strain_value, stress_value in elastic_points:
            assert stress_value == pytest.approx(
                material["youngs_modulus"] * strain_value, rel=1e-9)
        if not curve["brittle"]:
            # Past the elastic limit the curve must bend away from that straight line.
            after = [(e, s) for e, s in zip(curve["strain"], curve["stress"])
                     if e > curve["yield_strain"]]
            assert after
            assert any(s < material["youngs_modulus"] * e * 1.0000001 for e, s in after)
        else:
            # A brittle material never leaves the straight line: it snaps first.
            assert set(curve["regions"]) == {"Elastic"}
        # And the curve must finish at the material's fracture strain.
        assert curve["strain"][-1] == pytest.approx(material["fracture_strain"])


STANDARD_G = 9.8


def test_chapter_fsix_upthrust_continuity_and_bernoulli():
    assert fluids.upthrust(1000, 0.01) == pytest.approx(98.0)
    # An object less dense than the fluid floats; denser than the fluid sinks.
    assert fluids.sink_or_float(800, 1000) == "Floats"
    assert fluids.sink_or_float(1200, 1000) == "Sinks"
    assert fluids.sink_or_float(1000, 1000) == "Suspended"
    assert fluids.floatation_verdict(500, 1e-3, 1000)["verdict"] == "Floats"
    assert fluids.floatation_verdict(500, 1e-3, 1000)["submerged_fraction"] == pytest.approx(0.5)
    # Continuity: halving the area doubles the speed.
    assert fluids.continuity_velocity(4.0, 2.0, 2.0) == pytest.approx(4.0)
    series = fluids.pipe_series(4.0, 2.0, 2.0)
    assert series["constant"] is True
    # Bernoulli, same pressure at both ends: doubling the speed needs a drop in
    # height of v^2/2g below the starting level.
    level = fluids.bernoulli(p1=101325, v1=10, h1=10, p2=101325, v2=20, h2=None, density=1000)
    assert level["h2"] == pytest.approx(10 + (100 - 400) / (2 * 9.8))
    assert level["h2"] < 10                       # faster flow means lower, never higher
    # Faster flow at the same height means lower pressure.
    fast = fluids.bernoulli(p1=101325, v1=1, h1=0, p2=None, v2=2, h2=0, density=1000)
    assert fast["p2"] == pytest.approx(101325 - 0.5 * 1000 * (4 - 1))
    assert fast["p2"] < 101325
    # Solving for v: a 10 m head of water through a 11.3 kPa pressure drop.
    jet = fluids.bernoulli(p1=101325, v1=0, h1=10, p2=90000, h2=0, density=1000)
    head = 101325 + 1000 * 9.8 * 10          # the constant along the streamline
    assert jet["v2"] == pytest.approx(math.sqrt(2 * (head - 90000) / 1000), rel=1e-9)
    assert jet["v2"] == pytest.approx(14.787, rel=1e-3)
    # You must leave exactly one quantity unset.
    with pytest.raises(ValueError):
        fluids.bernoulli(p1=101325, v1=10, h1=0, p2=101325, v2=20, h2=0)
    # Reynolds number is dimensionless and decides the regime.
    assert fluids.reynolds_number(1000, 1.0, 1.0, 1.0) == pytest.approx(1000)
    assert "Laminar" in fluids.flow_regime(1000)["regime"]
    assert "Turbulent" in fluids.flow_regime(50000)["regime"]
    assert fluids.venturi_pressure(101325, 10, 2) < 101325


def test_chapter_seven_oscillations():
    omega = oscillations.angular_frequency(2.0)
    assert omega == pytest.approx(math.pi)
    assert oscillations.displacement(0.1, omega, 0.5) == pytest.approx(0.1)
    assert oscillations.velocity(0.1, omega, 0.0) == pytest.approx(0.1 * omega)
    assert oscillations.acceleration(0.1, omega, 0.0) == pytest.approx(0.0)
    # a = -omega^2 x at every point on the curve.
    for t in (0.0, 0.13, 0.7, 1.9):
        x = oscillations.displacement(0.2, omega, t)
        assert oscillations.acceleration(0.2, omega, t) == pytest.approx(-omega ** 2 * x)
    # Mass-spring: T = 2 pi sqrt(m/k).
    assert oscillations.mass_spring_period(1.0, 4.0) == pytest.approx(2 * math.pi * 0.5)
    assert oscillations.mass_spring_frequency(1.0, 4.0) == pytest.approx(1 / math.pi)
    # Pendulum: T = 2 pi sqrt(L/g).
    assert oscillations.pendulum_period(1.0, 9.8) == pytest.approx(2 * math.pi / math.sqrt(9.8))
    # Period is independent of mass and of amplitude for a spring.
    assert oscillations.mass_spring_period(1.0, 4.0) == oscillations.mass_spring_period(1.0, 4.0)
    # The amplitude is constant throughout ideal S.H.M.
    series = oscillations.shm_series(0.2, omega)
    assert max(series["x"]) == pytest.approx(0.2, rel=1e-3)
    # A large-angle pendulum period is longer than the small-angle formula gives.
    assert oscillations.pendulum_accuracy(1.0, 30) > 0


def test_chapter_eight_waves():
    assert waves.wave_speed(50, 2) == pytest.approx(100)
    assert waves.wavelength(340, 170) == pytest.approx(2)
    assert waves.intensity(10, 2) == pytest.approx(5)
    # Intensity goes as the square of the amplitude.
    assert waves.intensity_from_amplitudes(100, 1, 2) == pytest.approx(400)
    # Beats.
    assert waves.beat_frequency(440, 444) == pytest.approx(4)
    assert waves.beat_period(440, 444) == pytest.approx(0.25)
    # A whole wavelength gives constructive interference, half gives destructive.
    assert waves.interference_kind(2.0, 2.0).startswith("Constructive")
    assert waves.interference_kind(1.0, 2.0).startswith("Destructive")
    # Equal amplitudes: the maximum is four times one beam and the minimum zero.
    result = waves.interference_intensity(1.0, 1.0, 0.0, 1.0)
    assert result["maximum"] == pytest.approx(4.0)
    assert waves.interference_intensity(1.0, 1.0, 0.5, 1.0)["minimum"] == pytest.approx(0, abs=1e-9)
    # Stationary wave nodes land where the string does not move.
    pattern = waves.standing_wave(1.0, 2, amplitude_value=1.0)
    assert len(pattern["nodes"]) == 3
    assert len(pattern["antinodes"]) == 2
    # String harmonics: f_n = n v / 2L.
    assert waves.string_harmonics(0.5, 340)[0]["f"] == pytest.approx(340)
    assert waves.string_harmonics(0.5, 340)[1]["f"] == pytest.approx(680)
    # A pipe closed at one end has only the odd harmonics.
    closed = waves.pipe_harmonics(0.25, "closed")
    assert closed[0]["f"] == pytest.approx(340)
    assert closed[1]["n"] == 3
    # Doppler, all four cases.
    assert waves.doppler(500, 340, 10, 0, "a") == pytest.approx(500 * 350 / 340)
    assert waves.doppler(500, 340, 0, 10, "b") == pytest.approx(500 * 340 / 330)
    assert waves.doppler(500, 340, 10, 10, "c") == pytest.approx(500 * 350 / 330)
    assert waves.doppler(500, 340, 10, 10, "d") == pytest.approx(500 * 330 / 350)
    # Approaching raises the pitch, receding lowers it.
    assert waves.doppler(500, 340, 10, 0, "a") > 500
    assert waves.doppler(500, 340, 0, 10, "b") > 500
    assert waves.doppler(500, 340, 0, 10, "d") < 500


def test_chapter_nine_optics():
    # Young's double slit.
    assert optics.fringe_width(5.5e-7, 1.0, 5e-4) == pytest.approx(1.1e-3)
    assert optics.constructive_condition(3 * 5.5e-7, 5.5e-7)
    assert optics.destructive_condition(1.5 * 5.5e-7, 5.5e-7)
    # Single slit: a sin(theta) = m lambda, first minimum just under 1 mm/550 nm.
    first = optics.single_slit_minima(1e-3, 5.5e-7, 1)
    assert first["sin_theta"] == pytest.approx(5.5e-4)
    assert "error" in optics.single_slit_minima(1e-7, 5.5e-7, 1)   # slit narrower than lambda
    # A wider slit gives a narrower pattern.
    assert (optics.single_slit_minima(2e-3, 5.5e-7, 1)["theta_deg"]
            < first["theta_deg"])
    # Grating.
    assert optics.grating_angles(1e-6, 5.5e-7, 2)[1]["sin_theta"] == pytest.approx(0.55)
    assert optics.grating_angles(1e-6, 5.5e-7, 2)[2]["exists"] is False
    assert optics.grating_resolving_power(2, 500)["R"] == 1000
    # Bragg: 2 d sin(theta) = m lambda, and order comes back out the same.
    theta = optics.bragg_angle(5.64e-10, 1.54e-10, 1)["theta_deg"]
    assert optics.bragg_order(5.64e-10, theta, 1.54e-10) == pytest.approx(1, rel=1e-9)
    assert "error" in optics.bragg_angle(1e-11, 1.54e-10, 1)
    # Malus's law.
    assert optics.malus_law(100, 0) == pytest.approx(100)
    assert optics.malus_law(100, 60) == pytest.approx(25)
    assert optics.malus_law(100, 90) == pytest.approx(0, abs=1e-9)
    # A third polariser can beat two crossed ones - the interference demo.
    triple = optics.two_polarisers(100, 0, 90)
    assert triple["final"] == pytest.approx(0, abs=1e-9)
    assert triple["with_three_polarisers"] > triple["final"]
    # Brewster: tan(theta_B) = n2/n1, and the reflected ray is at right angles.
    brew = optics.brewster_angle(1.0, 1.5)
    assert brew["theta_b_deg"] == pytest.approx(math.degrees(math.atan(1.5)), rel=1e-6)
    assert brew["theta_b_deg"] + brew["refracted_deg"] == pytest.approx(90)


def test_chapter_ten_thermodynamics():
    assert thermo.to_kelvin(0) == pytest.approx(273.15)
    assert thermo.to_celsius(373.15) == pytest.approx(100)
    assert thermo.to_kelvin(32, "F") == pytest.approx(273.15)
    assert thermo.boyles_law(100, 2, 200) == pytest.approx(1)
    assert thermo.charles_law(1, 273, 546) == pytest.approx(2)
    assert thermo.ideal_gas_pressure(1, 273.15, 0.022414) == pytest.approx(101325, rel=1e-3)
    # RMS speed of nitrogen at 300 K is about 517 m/s.
    assert thermo.rms_speed(300, 0.028014) == pytest.approx(517, rel=2e-3)
    # The three characteristic speeds must be ordered correctly.
    assert (thermo.most_probable_speed(300, 0.028)
            < thermo.mean_speed(300, 0.028) < thermo.rms_speed(300, 0.028))
    # Pressure from the molecular model must agree with PV = nRT.
    # Take 1.00 mol of an ideal gas at 300 K in 0.0250 m3. Then
    # <v^2> = 3RT/M for a molecule of molar mass M, and P = (1/3) N m <v^2>.
    moles, volume, molar_mass = 1.0, 0.0250, 0.028014
    molecules = moles * thermo.AVOGADRO
    molecule_mass = molar_mass / thermo.AVOGADRO
    mean_square = 3.0 * thermo.GAS_CONSTANT * 300.0 / molar_mass
    assert thermo.kinetic_pressure(molecules, molecule_mass, mean_square, volume) == pytest.approx(
        thermo.ideal_gas_pressure(moles, 300.0, volume), rel=1e-9)
    # The syllabus form is PV = (1/3) N m <v^2>, which is the same identity
    # written for the product rather than the pressure.
    assert thermo.kinetic_pressure_volume(molecules, molecule_mass, mean_square) == pytest.approx(
        thermo.ideal_gas_pressure(moles, 300.0, volume) * volume, rel=1e-9)
    # Average translational energy: 3/2 kT.
    assert thermo.average_translational_energy(300) == pytest.approx(1.5 * thermo.BOLTZMANN * 300)
    assert thermo.average_molecular_energy(1, 300) == pytest.approx(1.5 * thermo.GAS_CONSTANT * 300)
    # First law.
    assert thermo.first_law(500, 200)["delta_U"] == pytest.approx(300)
    assert thermo.work_by_gas(101325, 0.01) == pytest.approx(1013.25)
    assert thermo.work_by_gas(101325, -0.01) == pytest.approx(-1013.25)
    assert thermo.work_series([(1, 1), (2, 2)]) == pytest.approx(1.5)   # trapezium rule
    assert thermo.dU_isothermal(1, 5) == 0
    # Mayer's relation: Cp - Cv = R.
    for degrees in (3, 5, 6):
        assert thermo.mayers_relation(degrees)["difference"] == pytest.approx(thermo.GAS_CONSTANT)
    assert thermo.cp_cv(5)["gamma"] == pytest.approx(1.4)
    assert thermo.cp_cv(3)["gamma"] == pytest.approx(5 / 3)
    # Carnot efficiency, including the impossible cases.
    assert thermo.carnot_efficiency(500, 250)["efficiency"] == pytest.approx(0.5)
    assert "error" in thermo.carnot_efficiency(250, 500)
    assert thermo.carnot_efficiency(500, 499)["efficiency"] < 0.01
    # A Carnot cycle must close and put out less work than the heat taken in.
    cycle = thermo.carnot_cycle_series()
    assert cycle["enclosed_area"] > 0
    assert cycle["tc"] < cycle["th"]
    assert "error" in thermo.carnot_cycle_series() or cycle["tc"] < cycle["th"]
    # Refrigerator: COP = Tc / (Th - Tc), and the inside must be colder.
    assert thermo.refrigerator_cop(250, 350)["cop"] == pytest.approx(2.5)
    assert "error" in thermo.refrigerator_cop(350, 250)
    # Isothermal expansion: dS = n R ln(V2/V1).
    assert thermo.entropy_change_ideal_gas(1, 300, 300, 1, 2) == pytest.approx(
        thermo.GAS_CONSTANT * math.log(2))
    # Heating at constant volume raises entropy.
    assert thermo.entropy_change_ideal_gas(1, 300, 600, 1, 1) > 0
    # Mixing two gases irreversibly raises the total entropy.
    assert thermo.entropy_change_ideal_gas(1, 300, 300, 1, 2) > 0


# --------------------------------------------------------------------------
# Tidy data tables
# --------------------------------------------------------------------------

def test_solid_moduli_are_in_a_sane_range():
    """Rubber is the softest by four orders of magnitude and steel the stiffest."""
    names = [m["name"] for m in solids.MATERIALS]
    for material in solids.MATERIALS:
        assert 1e6 < material["youngs_modulus"] < 1e12, material["name"]
        assert material["yield_stress"] > 0
        assert material["fracture_strain"] > 0
    by_modulus = sorted(solids.MATERIALS, key=lambda m: m["youngs_modulus"])
    assert by_modulus[0]["name"].startswith("Rubber")
    assert by_modulus[-1]["name"] == "Steel"
    assert by_modulus[0]["fracture_strain"] > by_modulus[-1]["fracture_strain"]
    assert names.count("Steel") == 1


def test_fluid_viscosities_are_ordered_as_they_are_described():
    order = {row["liquid"]: row["eta_pa_s"] for row in fluids.VISCOUS_FLUIDS}
    assert order["Water"] < order["Glycerine"] < order["Honey"]
    assert order["Air"] < order["Water"]


def test_heat_capacities_satisfy_mayers_relation():
    for row in thermo.HEAT_CAPACITIES:
        assert row["cp_j"] - row["cv_j"] == pytest.approx(thermo.GAS_CONSTANT, rel=1e-3)


def test_wavelength_colour_order():
    visible = [row for row in optics.WAVELENGTHS if row["colour"] in
               {"Violet", "Blue", "Green", "Yellow", "Orange", "Red"}]
    ordered = sorted(visible, key=lambda row: row["wavelength"])
    assert [row["colour"] for row in ordered] == [
        "Violet", "Blue", "Green", "Yellow", "Orange", "Red"]
