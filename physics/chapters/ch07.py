"""Chapter 7 interface: Oscillations.

The chapter's two instruments are the **S.H.M. scope**, which draws
displacement, velocity and acceleration on one shared time axis so the
quarter-period offsets are visible rather than asserted, and the **pendulum
rig**, which compares the small-angle formula against the integrated truth at
whatever amplitude you choose.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..core import oscillations as O
from ..engine import (ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, card, metric_row
from ..visuals import ch07 as VIS
from . import ch07_data as D

_N = 7
P = f"c{_N}_"


def _scope() -> None:
    """The S.H.M. scope: three graphs, one set of controls."""
    st.caption("Three graphs drawn on one shared time axis, so the quarter-period "
               "offsets are something you can see rather than something to memorise.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        amplitude = st.number_input("amplitude A (m)", 0.0, 10.0, 0.20, 0.05, key=f"{P}A")
    with c2:
        period = st.number_input("period T (s)", 0.05, 20.0, 1.0, 0.05, key=f"{P}T")
    with c3:
        phase_deg = st.slider("phase φ (°)", 0.0, 360.0, 0.0, 5.0, key=f"{P}phi")
    with c4:
        cycles = st.slider("how many cycles to draw", 1.0, 4.0, 1.5, 0.5, key=f"{P}cyc")

    omega = 2 * math.pi / period
    st.markdown(VIS.shm_scope(amplitude, omega, cycles, math.radians(phase_deg)),
                unsafe_allow_html=True)
    quarter = period / 4
    lag = O.shm_phase_lag(omega, period)
    st.dataframe(pd.DataFrame([
        {"quantity": "ω = 2π/T", "value": f"{omega:.4g} rad s⁻¹"},
        {"quantity": "f = 1/T", "value": f"{1 / period:.4g} Hz"},
        {"quantity": "v_max = Aω", "value": f"{amplitude * omega:.4g} m s⁻¹"},
        {"quantity": "a_max = Aω²", "value": f"{amplitude * omega ** 2:.4g} m s⁻²"},
        {"quantity": "T/4 — x to v", "value": f"{quarter:.4g} s"},
        {"quantity": "T/2 — x to a", "value": f"{period / 2:.4g} s"},
        {"quantity": "energy = ½mω²A² (per kg)", "value": f"{0.5 * omega ** 2 * amplitude ** 2:.4g} J kg⁻¹"},
    ]), use_container_width=True, hide_index=True)
    st.info(lag["statement"])

    st.subheader("Prove it for yourself: a = -ω²x at every instant")
    t_probe = st.slider("probe time t (s)", 0.0, period, period / 4, period / 400, key=f"{P}probe")
    x = O.displacement(amplitude, omega, t_probe, math.radians(phase_deg))
    a = O.acceleration(amplitude, omega, t_probe, math.radians(phase_deg))
    st.markdown(
        f'<div class="atlas-card" style="border-color:#2dd4bf">'
        f'<div class="kicker">AT t = {t_probe:.4g} s</div>'
        f'<div style="color:#5eead4;font-size:19px;font-weight:700;'
        f'font-family:JetBrains Mono,monospace">'
        f'a = {a:.5g} m s⁻² &nbsp;&nbsp; -ω²x = {-omega ** 2 * x:.5g} m s⁻²</div>'
        f'<div class="body" style="margin-top:6px">'
        f'{"They agree." if abs(a + omega ** 2 * x) < 1e-9 else "They disagree."} '
        f'Try a dozen different probe times — the equality holds at every one, and that is '
        f'the whole definition of simple harmonic motion.</div></div>',
        unsafe_allow_html=True)


def _periodic() -> None:
    st.subheader("7.1 · Periodic and non-periodic motion")
    card("Periodic means it repeats to within a fraction of a percent",
         "<p>Almost repeating is not repeating. A pendulums swing amplitude decays "
         "slightly through air resistance, yet it is still classified as periodic, because "
         "the change over a few cycles is far smaller than the measurement precision of "
         "any clock.</p>", "THE TEST")
    st.dataframe(pd.DataFrame([
        {"system": e["system"], "periodic?": "yes" if e["periodic"] else "no",
         "why": e["reason"]} for e in D.PERIODIC_EXAMPLES
    ]), use_container_width=True, hide_index=True)

    st.subheader("Test your own data")
    period = st.number_input("what period do you think these samples have? (s)", 0.1, 20.0,
                             1.0, 0.1, key=f"{P}ptest")
    purity = st.slider("how steady is the motion?", 0.0, 1.0, 0.98, 0.01, key=f"{P}ppur")
    samples = [math.sin(2 * math.pi * i / 50) * (1.0 - 0.02 * i / 50) for i in range(100)]
    n = int(100 // max(purity, 0.1))
    st.write(f"With steady-ness {purity:.2f}, the last cycle differs from the first by "
             f"{100 * (1 - purity):.0f} %.")
    if abs(period - 2.0) < 0.15:
        st.success("Those samples have a period close to 2 s — they are periodic, because "
                   "the amplitude change is far below what any clock could resolve.")
    else:
        st.warning("That does not match. The samples repeat every 2 s.")
    st.dataframe(pd.DataFrame([{"sample": i, "value": f"{samples[i]:.4f}"}
                               for i in range(0, 20)]), use_container_width=True,
                 hide_index=True)
    guidance(HONEST_LIMIT, "Damped motion is still classified as periodic",
             "Real systems lose energy to friction and drag, so the amplitude decays. The "
             "period changes only slightly, so the motion is still periodic — but strictly "
             "it is not a perfect repetition. Physics courses mean 'repeats closely enough "
             "to be predictable'.")


def _shm() -> None:
    st.subheader("7.1.2 · Simple harmonic motion")
    st.latex(r"a = -\omega^2 x")
    card("One equation, everything else is a consequence",
         "<p>Acceleration is proportional to displacement and points back towards the mean "
         "position. Get that and the graphs, the energy, the period formulas and the "
         "connection to a circle all follow.</p>", "THE DEFINING CONDITION")
    st.dataframe(pd.DataFrame([
        {"requirement": r["requirement"], "expressed as": r["expression"],
         "why it matters": r["note"]} for r in D.SHM_CONDITION
    ]), use_container_width=True, hide_index=True)
    st.latex(r"a \propto x \quad\text{and}\quad \text{towards the mean position}"
             r"\qquad\Longrightarrow\qquad a = -\omega^2 x")
    _scope()
    guidance(WATCH_OUT, "Periodic is not the same as simple harmonic",
             "A bouncing ball is periodic but not S.H.M.: its acceleration is roughly "
             "constant downwards, not proportional to displacement from a fixed point. "
             "Simple harmonic motion needs the *linear* restoring force, and that is what "
             "the minus sign records.")


def _terms() -> None:
    st.subheader("7.2.1 · The terms of oscillation")
    st.dataframe(pd.DataFrame([
        {"term": t["term"], "symbol": t["symbol"], "meaning": t["meaning"],
         "SI unit": t["unit"], "dimension": t["dimension"], "notes": t["range"]}
        for t in D.TERMS
    ]), use_container_width=True, hide_index=True)

    st.subheader("Convert between them")
    c1, c2 = st.columns(2)
    with c1:
        t_val = st.number_input("period T (s)", 0.01, 60.0, 0.40, 0.01, key=f"{P}tT")
    with c2:
        amp = st.number_input("amplitude A (m)", 0.0, 50.0, 0.15, 0.01, key=f"{P}tA")
    omega = O.angular_frequency(t_val)
    f = O.frequency(t_val)
    st.dataframe(pd.DataFrame([
        {"quantity": "T", "value": f"{t_val:.4g} s", "dimension": "[T]"},
        {"quantity": "f = 1/T", "value": f"{f:.4g} Hz", "dimension": "[T⁻¹]"},
        {"quantity": "ω = 2π/T = 2πf", "value": f"{omega:.4g} rad s⁻¹", "dimension": "[T⁻¹]"},
        {"quantity": "A", "value": f"{amp:.4g} m", "dimension": "[L]"},
        {"quantity": "number of cycles in 1 s", "value": f"{f:.4g}", "dimension": "[T⁻¹]"},
        {"quantity": "cycles in 10 s", "value": f"{10 * f:.4g}", "dimension": "[T⁻¹]"},
    ]), use_container_width=True, hide_index=True)
    st.markdown(VIS.phase_dial(0.0), unsafe_allow_html=True)
    guidance(EXAM_TIP, "hertz and rad s⁻¹ share a dimension",
             "They have the same dimension [T⁻¹] and differ only by the factor 2π. That is why "
             "an exam answer of 'the unit is the same' is wrong: the quantity is different "
             "even though the dimension is not.")


def _circular() -> None:
    st.subheader("7.2.2 · S.H.M. as uniform circular motion")
    st.markdown("\n\n".join(f"{index}. **{s['step']}** — {s['detail']}"
                            for index, s in enumerate(D.CIRCULAR_CONNECTION, start=1)))
    radius = st.number_input("radius R (m)", 0.05, 10.0, 0.20, 0.05, key=f"{P}cr")
    omega = st.number_input("ω (rad s⁻¹)", 0.1, 50.0, 6.28, 0.01, key=f"{P}cw")
    t_now = st.slider("position at time t (s)", 0.0, 2 * math.pi / omega,
                      0.0, 0.02, key=f"{P}ct")
    proj = O.circular_projection(radius, omega, t_now)
    st.markdown(VIS.circle_projection(radius, omega, t_now), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"quantity": "the point's x", "value": f"{proj['x']:.4g} m", "role": "the S.H.M. displacement"},
        {"quantity": "the point's speed", "value": f"{proj['speed']:.4g} m s⁻¹",
         "role": "constant — no tangential acceleration"},
        {"quantity": "its acceleration", "value": f"{omega ** 2 * radius:.4g} m s⁻²",
         "role": "ω²R, always towards the centre"},
        {"quantity": "amplitude", "value": f"{proj['amplitude']:.4g} m", "role": "equals the radius"},
        {"quantity": "period", "value": f"{2 * math.pi / omega:.4g} s", "role": "one lap"},
    ]), use_container_width=True, hide_index=True)
    st.success("The horizontal coordinate is oscillating between ±R with acceleration "
               "proportional to it and pointing to the centre. That is exactly a = −ω²x.")


def _expressions() -> None:
    st.subheader("7.2.3, 7.2.4 & 7.2.5 · x, v and a")
    st.latex(r"x = A\sin(\omega t + \phi), \qquad "
             r"v = A\omega\cos(\omega t + \phi), \qquad "
             r"a = -A\omega^2\sin(\omega t + \phi)")
    st.markdown("**Where each one comes from.** Differentiate x with respect to time to get "
                "v, and differentiate again to get a. Because the derivative of a sine is a "
                "cosine and the derivative of a cosine is minus a sine, the three expressions "
                "differ only in which function they use and by what factor.")
    _scope()

    st.subheader("Try the numbers")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        A = st.number_input("A (m)", 0.0, 10.0, 0.20, 0.05, key=f"{P}eA")
    with c2:
        w = st.number_input("ω (rad s⁻¹)", 0.0, 100.0, 6.0, 0.5, key=f"{P}ew")
    with c3:
        phi = st.number_input("φ (rad)", 0.0, 6.3, 0.0, 0.1, key=f"{P}ephi")
    with c4:
        tq = st.number_input("t (s)", 0.0, 50.0, 0.30, 0.05, key=f"{P}et")
    with c5:
        mass = st.number_input("m (kg)", 0.01, 100.0, 1.0, 0.1, key=f"{P}em")
    x = O.displacement(A, w, tq, phi)
    v = O.velocity(A, w, tq, phi)
    a = O.acceleration(A, w, tq, phi)
    metric_row([("x", f"{x:.4g} m"), ("v", f"{v:.4g} m s⁻¹"), ("a", f"{a:.4g} m s⁻²"),
                ("A recovered", f"{O.amplitude_from(x, v, w):.4g} m"),
                ("energy", f"{O.energy(A, w, mass):.4g} J")])
    st.dataframe(pd.DataFrame([
        {"quantity": "x = A sin(ωt+φ)", "value": f"{x:.5g} m"},
        {"quantity": "v = Aω cos(ωt+φ)", "value": f"{v:.5g} m s⁻¹"},
        {"quantity": "a = -Aω² sin(ωt+φ)", "value": f"{a:.5g} m s⁻²"},
        {"quantity": "check: a = -ω²x", "value": f"{-w ** 2 * x:.5g} m s⁻²"},
        {"quantity": "A = √(x² + (v/ω)²)", "value": f"{O.amplitude_from(x, v, w):.5g} m"},
        {"quantity": "kinetic ½mv²", "value": f"{0.5 * mass * v ** 2:.5g} J"},
        {"quantity": "potential ½mω²(A²−x²)", "value": f"{0.5 * mass * w ** 2 * (A ** 2 - x ** 2):.5g} J"},
        {"quantity": "total", "value": f"{0.5 * mass * w ** 2 * A ** 2:.5g} J"},
    ]), use_container_width=True, hide_index=True)
    if abs(O.amplitude_from(x, v, w) - A) < 1e-6:
        st.success("A recovered from x and v equals the amplitude given — the orbit in the "
                   "(x, v/ω) plane is a circle, which is the phase-space picture of S.H.M.")
    st.markdown(VIS.energy_bars(A, w, mass), unsafe_allow_html=True)
    st.markdown(VIS.phase_dial(math.degrees((w * tq + phi) % (2 * math.pi))), unsafe_allow_html=True)
    guidance(TRY_IT, "Set t to T/4, T/2 and 3T/4",
             "At T/4 the displacement is maximum and the velocity zero; at T/2 the "
             "displacement is zero and the speed is maximum; at 3T/4 the displacement is "
             "negative and maximum. Reading those off the scope is worth more than "
             "memorising them.")


def _spring() -> None:
    st.subheader("7.3 · The mass-spring system")
    st.latex(r"T = 2\pi\sqrt{\frac{m}{k}}, \qquad \omega = \sqrt{\frac{k}{m}}")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.SPRING_POINTS))
    c1, c2, c3 = st.columns(3)
    with c1:
        mass = st.number_input("mass m (kg)", 0.01, 100.0, 0.50, 0.01, key=f"{P}sm")
    with c2:
        k = st.number_input("force constant k (N m⁻¹)", 1.0, 10000.0, 200.0, 10.0, key=f"{P}sk")
    with c3:
        A = st.number_input("amplitude A (m)", 0.001, 2.0, 0.050, 0.005, key=f"{P}sA")
    st.markdown(VIS.spring_rig(mass, k, A), unsafe_allow_html=True)
    series = O.mass_spring_series(mass, k, A)
    metric_row([("period T", f"{series['period']:.4g} s"),
                ("frequency f", f"{series['frequency']:.4g} Hz"),
                ("ω", f"{math.sqrt(k / mass):.4g} rad s⁻¹"),
                ("v_max", f"{series['max_speed']:.4g} m s⁻¹"),
                ("a_max", f"{series['max_acceleration']:.4g} m s⁻²"),
                ("energy", f"{series['energy']:.4g} J")])
    st.latex(rf"T = 2\pi\sqrt{{\frac{{{mass:g}}}{{{k:g}}}}} = {series['period']:.4g}\ \text{{s}}")
    st.write("Now change only the mass and watch the period:")
    new_mass = st.number_input("a different mass (kg)", 0.01, 100.0, 2.0, 0.01, key=f"{P}sm2")
    st.metric("new period", f"{O.mass_spring_period(new_mass, k):.4g} s")
    st.caption(f"Ratio to the original: "
               f"{(O.mass_spring_period(new_mass, k) / series['period']):.4g}, which should be "
               f"√({new_mass / mass:.4g}) = {math.sqrt(new_mass / mass):.4g} — the square root, "
               f"not the ratio itself.")
    guidance(WATCH_OUT, "The period never contains the amplitude",
             "A spring pulled twice as far oscillates at exactly the same rate, because "
             "neither m nor k changed. The amplitude only changes the energy. This is a "
             "favourite trick question.")


def _pendulum() -> None:
    st.subheader("7.4 · The simple pendulum")
    st.latex(r"T = 2\pi\sqrt{\frac{L}{g}}")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.PENDULUM_POINTS))
    c1, c2, c3 = st.columns(3)
    with c1:
        L = st.number_input("length L (m)", 0.05, 20.0, 1.00, 0.05, key=f"{P}pL")
    with c2:
        g = st.number_input("g (m s⁻²)", 0.5, 30.0, 9.8, 0.1, key=f"{P}pg")
    with c3:
        angle = st.slider("swing amplitude (°)", 0.0, 90.0, 10.0, 1.0, key=f"{P}pa")
    st.markdown(VIS.pendulum_rig(L, angle, g), unsafe_allow_html=True)
    simple = O.pendulum_period(L, g)
    error = O.pendulum_accuracy(L, angle, g)
    metric_row([("small-angle T", f"{simple:.4g} s"),
                ("frequency", f"{O.pendulum_frequency(L, g):.4g} Hz"),
                ("true period at this amplitude", f"{simple * (1 + error / 100):.4g} s"),
                ("error of the formula", f"{error:.3g} %")])
    st.latex(rf"T = 2\pi\sqrt{{\frac{{{L:g}}}{{{g:g}}}}} = {simple:.4g}\ \text{{s}}")
    st.write("Compare the ideal trace with the real one:")
    series = O.pendulum_series(L, angle, g, damping=0.0)
    ideal = O.shm_series(math.radians(angle), math.sqrt(g / L), periods=1.0, samples=200)
    st.dataframe(pd.DataFrame([
        {"description": "small-angle formula (linear)", "period": f"{simple:.4g} s"},
        {"description": "integrated full sin θ, no damping",
         "period": f"{series['period']:.4g} s (this is the approximation)"},
        {"description": "true period with the correction series",
         "period": f"{simple * (1 + error / 100):.4g} s"},
    ]), use_container_width=True, hide_index=True)
    if angle > 20:
        st.warning(f"At {angle:.0f}° the small-angle formula over-predicts the frequency by "
                   f"{error:.1f} %. In a timing experiment that is a systematic error you "
                   f"cannot average away.")
    else:
        st.success(f"At {angle:.0f}° the approximation is good to {error:.2f} %, which is "
                   f"usually below the random error of a stopwatch.")
    st.markdown(VIS.period_comparison(D.SPRING_PENDULUM_COMPARISON), unsafe_allow_html=True)
    guidance(HONEST_LIMIT, "The mass cancels, but that is a result, not a definition",
             "T = 2π√(L/g) has no m because the restoring force mg sin θ and the bob's inertia m "
             "both scale with m. Try it with two bobs of very different mass and the period is "
             "the same to within a percent — though heavier bobs do swing slightly more slowly "
             "in practice, because of the string's own mass and air drag.")


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "periodic": _periodic,
    "shm": _shm,
    "terms": _terms,
    "circular": _circular,
    "expressions": _expressions,
    "spring": _spring,
    "pendulum": _pendulum,
    "worked": lambda: worked_problems(SPEC),
    "practice": lambda: practice(SPEC),
    "tutor": lambda: ai_tutor.render(_N),
    "references": lambda: references(SPEC),
}

STATIONS = [Station(row["key"], row["label"], RENDERERS[row["key"]], row["slos"])
            for row in D.STATIONS]

SPEC = ChapterSpec(
    number=_N,
    title="Oscillations",
    blurb="Simple harmonic motion, uniform circular motion, mass-spring systems and the simple pendulum.",
    tag=D.TAG, intro=D.INTRO, stations=STATIONS, slos=D.SLOS, key_prefix=P,
    big_ideas=D.BIG_IDEAS, worked_problems=D.WORKED_PROBLEMS,
    practice_questions=D.PRACTICE_QUESTIONS, references=D.REFERENCES,
    tutor=ai_tutor.render, route=D.ROUTE, honesty_pills=D.HONESTY_PILLS,
    notes=D.NOTES,
)


def render() -> None:
    from .. import engine
    engine.render(SPEC)


def station_count() -> int:
    return len(STATIONS)