"""Chapter 6 interface: Fluids Dynamics.

Two benches of its own: the **Archimedes bench**, where an object and a fluid can
be chosen and the force balance is drawn live, and the **pipe simulator**, which
tapers a pipe and tracks continuity — and, at constant height, the pressure —
all the way along it.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..visuals.common import freeze
from ..core import fluids as F
from ..engine import (how_to, ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT, practicals,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, VIOLET, card
from ..visuals import ch06 as VIS
from . import ch06_data as D

_N = 6
P = f"c{_N}_"

OBJECTS = [
    {"name": "Oak block", "density": 750.0, "note": "Wood, and famously buoyant"},
    {"name": "Ice", "density": 917.0, "note": "Floats in water — which is why lakes freeze from the top"},
    {"name": "Aluminium can", "density": 2700.0, "note": "Sinks in water, floats in mercury"},
    {"name": "Iron nail", "density": 7800.0, "note": "Sinks in water, floats in mercury"},
    {"name": "Empty plastic bottle", "density": 950.0, "note": "Plastic itself would float"},
    {"name": "Solid glass marble", "density": 2500.0, "note": "Heavy for its size"},
]


def _bench() -> None:
    how_to("numbers"),
    """The Archimedes bench."""
    st.caption("Pick an object and a fluid. The verdict, the forces and the submerged "
               "fraction are all recomputed from the densities.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        obj = st.selectbox("object", [o["name"] for o in OBJECTS], key=f"{P}obj")
    with c2:
        fluid = st.selectbox("fluid", [f["name"] for f in F.FLUIDS], key=f"{P}fli")
    spec = next(o for o in OBJECTS if o["name"] == obj)
    fl = next(f for f in F.FLUIDS if f["name"] == fluid)
    with c3:
        volume = st.number_input("volume (cm³)", 0.1, 1e6, 500.0, 10.0, key=f"{P}vol")
    with c4:
        drag = st.number_input("drag force (N)", 0.0, 500.0, 0.0, 5.0, key=f"{P}drag",
                               help="A resistive force, as in a viscous fluid. It never "
                                    "changes whether the body floats, only whether it reaches "
                                    "equilibrium quickly.")

    cubic = volume * 1e-6
    verdict = F.floatation_verdict(spec["density"], cubic, fl["density"])
    left, right = st.columns([3, 2])
    with left:
        st.markdown(VIS.archimedes_bench(spec["density"], fl["density"], cubic),
                    unsafe_allow_html=True)
    with right:
        st.dataframe(pd.DataFrame([
            {"step": "weight W = ρVg", "value": f"{verdict['weight']:.4g} N"},
            {"step": "maximum upthrust ρgV", "value": f"{verdict['maximum_upthrust']:.4g} N"},
            {"step": "submerged fraction", "value": f"{verdict['submerged_fraction'] * 100:.1f} %"},
            {"step": "verdict", "value": verdict["verdict"]},
            {"step": "if drag present, net upthrust",
             "value": f"{verdict['maximum_upthrust'] * verdict['submerged_fraction'] - drag:.4g} N"},
        ]), use_container_width=True, hide_index=True)
        st.info(verdict["reason"])
        st.caption(f"{spec['name']}: ρ = {spec['density']:.4g} kg m⁻³ — {spec['note']}")
        st.caption(f"{fluid}: ρ = {fl['density']:.4g} kg m⁻³ — {fl['note']}")
        if drag:
            st.warning("With a drag force present, the body only floats at a depth where "
                       "upthrust exactly balances weight plus drag. It will sink deeper than "
                       "it would in an ideal fluid.")

    st.subheader("The three cases, in full")
    st.dataframe(pd.DataFrame([
        {"condition": c["case"], "verdict": c["verdict"], "submerged": c["submerged"],
         "why": c["reason"]} for c in D.FLOATATION_CASES
    ]), use_container_width=True, hide_index=True)
    guidance(EXAM_TIP, "g cancels from every floatation question",
             "For a floating body, ρ_f g V_d = ρ_b g V, and g divides straight out. That is "
             "why the submerged fraction is just the ratio of the densities, and why a block "
             "floats the same fraction of its depth in water on Earth and on the Moon.")


def _ships() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("6.1.5 · Why ships float")
    card("It is not that steel is light",
         "<p>Steel is about 7.8 times denser than water, so a solid block of it would sink "
         "immediately. What makes a ship float is that its hull is <em>hollow</em>: it "
         "excludes a huge volume of water from a modest mass of steel.</p>", "THE IDEA")

    m_col, sea_col = st.columns(2)
    with m_col:
        mass = st.number_input("ship mass including cargo (kg)", 1e4, 5e8, 2.0e7, 1e6,
                               key=f"{P}smass")
    with sea_col:
        sea = st.selectbox("sea", ["Sea water", "Fresh water"],
                           key=f"{P}ssea")
    density = 1025.0 if sea == "Sea water" else 1000.0
    info = F.ship_displacement(mass, 9.8, density)

    st.markdown(VIS.hull_diagram(info["displaced_volume"], mass), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"quantity": "displaced volume V", "value": f"{info['displaced_volume']:.4g} m³"},
        {"quantity": "displaced mass", "value": f"{info['displaced_mass']:.4g} kg"},
        {"quantity": "upthrust", "value": f"{info['upthrust']:.4g} N"},
        {"quantity": "ship weight", "value": f"{mass * 9.8:.4g} N"},
        {"quantity": "sea density", "value": f"{density} kg m⁻³"},
    ]), use_container_width=True, hide_index=True)
    st.success(info["why"])

    st.subheader("How deep must the hull reach?")
    draft = st.slider("waterline area (m²) — the size of the ship's waterplane",
                      50.0, 5000.0, 800.0, 50.0, key=f"{P}draft")
    depth = info["displaced_volume"] / draft
    st.metric("Required draft", f"{depth:.2f} m")
    st.caption("This is the real design trade-off: a small waterplane needs a deep draft, "
               "which is why wide cargo ships float shallow and narrow boats stand tall.")

    guidance(WATCH_OUT, "Cargo changes the answer, not the material",
             "Loading a ship does not make the steel denser. It adds mass, so it increases "
             "the weight, so it increases the volume of water that must be displaced and the "
             "ship settles deeper. In a river a ship floats higher than the same ship at sea.")


def _flow() -> None:
    how_to("numbers"), how_to("sliders"),
    st.subheader("6.2 · Streamline and turbulent flow")
    st.latex(r"\mathrm{Re} = \frac{\rho v L}{\eta}")
    card("Reynolds' number decides",
         "<p>It is dimensionless, which is a useful check on its own. It compares the "
         "inertia of the fluid with its viscosity: when inertia wins, the fluid keeps going "
         "straight past an obstacle and layers mix; when viscosity wins, swirls are smoothed "
         "out and the layers stay parallel.</p>", "THE IDEA")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        rho = st.selectbox("fluid", [f["name"] for f in F.FLUIDS], index=1, key=f"{P}fname")
    with c2:
        v = st.slider("speed (m s⁻¹)", 0.01, 50.0, 2.0, 0.1, key=f"{P}fvel")
    with c3:
        length = st.number_input("characteristic length — pipe diameter (mm)", 0.1, 2000.0,
                                 50.0, 5.0, key=f"{P}flen")
    with c4:
        eta = st.number_input("dynamic viscosity η (Pa s)", 1e-6, 100.0, 1.0e-3, 1e-4,
                              format="%.2e", key=f"{P}feta")
    fl = next(f for f in F.FLUIDS if f["name"] == rho)
    result = F.reynolds_flow(fl["density"], v, length * 1e-3, eta)
    st.markdown(VIS.flow_regime_strip(result["re"], result["regime"]),
                unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"quantity": "Reynolds number", "value": f"{result['re']:.4g}"},
        {"quantity": "regime", "value": result["regime"]},
        {"quantity": "laminar below", "value": f"Re ≤ {F.REYNOLDS_LIMITS['laminar']:.0f}"},
        {"quantity": "turbulent above", "value": f"Re ≥ {F.REYNOLDS_LIMITS['turbulent']:.0f}"},
    ]), use_container_width=True, hide_index=True)
    st.info(result["note"])
    st.dataframe(pd.DataFrame([
        {"factor": f["factor"], "effect": f["direction"], "why": f["why"]}
        for f in D.TURBULENCE_FACTORS
    ]), use_container_width=True, hide_index=True)
    guidance(HONEST_LIMIT, "Streamline drawings fail in turbulent flow",
             "A streamline diagram is only trustworthy where layers really do stay on top of "
             "each other. Once Re passes about 2000 the fluid mixes and the neat parallel "
             "lines in a textbook figure describe nothing that actually happens.")


def _continuity() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("6.3 · The equation of continuity")
    st.latex(r"A_1 v_1 = A_2 v_2")
    card("Fluids do not compress, so the volume per second is fixed",
         "<p>In one second the same volume must pass every cross-section of the pipe. So if "
         "the pipe narrows, the fluid must move faster. That single sentence is the whole "
         "equation.</p>", "THE IDEA")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        a1 = st.number_input("wide area A₁ (cm²)", 0.01, 1e4, 8.0, 0.5, key=f"{P}ca1")
    with c2:
        v1 = st.number_input("speed v₁ (m s⁻¹)", 0.01, 100.0, 2.0, 0.1, key=f"{P}cv1")
    with c3:
        a2 = st.number_input("narrow area A₂ (cm²)", 0.01, 1e4, 2.0, 0.1, key=f"{P}ca2")
    with c4:
        v2 = st.slider("new speed at the narrow end (m s⁻¹)", 0.1, 200.0, 8.0, 0.1,
                       key=f"{P}cv2")

    series = F.pipe_series(a1 * 1e-4, a2 * 1e-4, v1)
    predicted = F.continuity_velocity(a1 * 1e-4, v1, a2 * 1e-4)
    st.markdown(VIS.pipe_continuity(freeze(series)), unsafe_allow_html=True)

    st.subheader("Check your answer")
    m1, m2 = st.columns(2)
    with m1:
        st.metric("continuity predicts v₂", f"{predicted:.4g} m s⁻¹")
    with m2:
        if abs(v2 - predicted) / max(predicted, 1e-9) < 0.02:
            st.success("Your answer matches continuity.")
        else:
            st.error(f"Your answer of {v2:g} m/s does not match. The area has changed by a "
                     f"factor of {a1 / a2:.4g}, so the speed must change by that factor: "
                     f"v₂ = {a1 / a2:.4g} × {v1:g} = {predicted:.4g} m/s.")
    st.markdown(VIS.bernoulli_profile(101325.0, v1, 101325.0, predicted), unsafe_allow_html=True)

    st.subheader("Squeezing a rubber pipe")
    card("The everyday case",
         "<p>Squeeze one end of a soft pipe and the cross-section there shrinks. The same "
         "volume per second must get through a smaller opening, so the water there speeds "
         "up. Release the squeeze and it slows again. Nothing has changed about the amount "
         "of water coming out of the open end — only the speed at the narrow point.</p>",
         "WHY THE TEXTBOOK ASKS ABOUT IT")
    st.dataframe(pd.DataFrame([
        {"quantity": "volume flow rate Q = A₁v₁", "value": f"{F.continuity_area(a1 * 1e-4, v1):.4g} m³ s⁻¹"},
        {"quantity": "time for 1 litre to pass",
         "value": f"{F.continuity_time(1e-3, a1 * 1e-4, v1)['time']:.3g} s"},
        {"quantity": "speed if area halved", "value": f"{F.continuity_velocity(a1 * 1e-4, v1, a1 * 2e-4):.4g} m s⁻¹"},
    ]), use_container_width=True, hide_index=True)
    guidance(TRY_IT, "Halve the diameter, not the area",
             "Area goes as the square of the diameter, so halving the diameter quarters the "
             "area and quadruples the speed. Try A₂ = A₁/4 above and watch the predicted "
             "speed jump by four, not by two.")


def _bernoulli() -> None:
    how_to("numbers"),
    st.subheader("6.4 · Bernoulli's equation")
    st.latex(r"P + \tfrac{1}{2}\rho v^2 + \rho g h = \text{constant}")
    st.dataframe(pd.DataFrame([
        {"term": r["term"], "name": r["name"], "meaning": r["meaning"], "note": r["note"]}
        for r in D.BERNOULLI_QUANTITIES
    ]), use_container_width=True, hide_index=True)
    card("Three stores, one total",
         "<p>The equation says energy per unit volume is conserved along a streamline. "
         "Nothing is gained and nothing is lost — energy just moves between the three "
         "stores: pressure, motion and height.</p>", "THE IDEA")

    st.subheader("Solve it")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        p1 = st.number_input("P₁ (Pa)", 0.0, 1e7, 101325.0, 1000.0, key=f"{P}bp1")
    with c2:
        v1 = st.number_input("v₁ (m s⁻¹)", 0.0, 200.0, 10.0, 0.5, key=f"{P}bv1")
    with c3:
        h1 = st.number_input("h₁ (m)", -100.0, 1000.0, 0.0, 0.5, key=f"{P}bh1")
    with c4:
        v2 = st.number_input("v₂ (m s⁻¹)", 0.0, 200.0, 20.0, 0.5, key=f"{P}bv2")
    with c5:
        rho = st.selectbox("fluid", [f["name"] for f in F.FLUIDS], index=1, key=f"{P}brho")
    fl = next(f for f in F.FLUIDS if f["name"] == rho)

    solved = F.bernoulli(p1, v1, h1, p2=p1, v2=v2, h2=None, density=fl["density"])
    st.markdown(VIS.bernoulli_profile(p1, v1, solved["p2"], v2, fl["density"]),
                unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"term": "P", "at point 1": f"{p1:.4g} Pa", "at point 2": f"{solved['p2']:.4g} Pa"},
        {"term": "½ρv²", "at point 1": f"{0.5 * fl['density'] * v1 ** 2:.4g} Pa",
         "at point 2": f"{0.5 * fl['density'] * v2 ** 2:.4g} Pa"},
        {"term": "ρgh", "at point 1": f"{fl['density'] * 9.8 * h1:.4g} Pa",
         "at point 2": f"{fl['density'] * 9.8 * solved['h2']:.4g} Pa"},
        {"term": "TOTAL", "at point 1": f"{solved['constant']:.4g} Pa",
         "at point 2": f"{solved['constant']:.4g} Pa"},
    ]), use_container_width=True, hide_index=True)
    if solved["p2"] < 0:
        st.error("A negative pressure is a sign that these two states cannot be joined by a "
                 "streamline: the energy per unit volume would be negative there. The speeds "
                 "are too far apart for the height difference available.")
    elif solved["p2"] < p1:
        st.success("The pressure fell, because the fluid sped up. That is the whole of the "
                   "Bernoulli effect: speed and pressure trade against each other.")
    else:
        st.info("The pressure rose, because the fluid slowed down. The energy that was in the "
                "motion has gone back into pressure.")


def _applications() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("6.4.3 · Bernoulli in the real world")
    st.dataframe(pd.DataFrame([
        {"device": a["device"], "mechanism": a["mechanism"], "effect": a["effect"],
         "without it": a["without_it"]} for a in D.BERNOULLI_APPLICATIONS
    ]), use_container_width=True, hide_index=True)
    for a in D.BERNOULLI_APPLICATIONS:
        with st.expander(a["device"]):
            st.markdown(f"**Mechanism.** {a['mechanism']}\n\n"
                        f"**Effect.** {a['effect']}\n\n"
                        f"**If it were not there.** {a['without_it']}")

    st.subheader("Work out the jet speed yourself")
    diff = st.slider("pressure difference across the nozzle (Pa)", 0.0, 200000.0,
                     30000.0, 1000.0, key=f"{P}adi")
    st.markdown(VIS.atomizer_diagram(diff), unsafe_allow_html=True)
    speed = F.atomiser_speed(diff)
    st.metric("jet speed", f"{speed:.3g} m s⁻¹")
    st.caption("A 30 kPa difference — about 0.3 atmospheres — is enough to make a fast jet "
               "and lift liquid several centimetres up a tube.")

    st.subheader("Magnus force on a spinning ball")
    m1, m2, m3 = st.columns(3)
    with m1:
        sp = st.number_input("ball speed (m s⁻¹)", 0.0, 200.0, 30.0, 1.0, key=f"{P}msp")
    with m2:
        circ = st.number_input("circulation Γ (m² s⁻¹)", 0.0, 2.0, 0.1, 0.01, key=f"{P}mcirc")
    with m3:
        app = st.number_input("spin rate factor", 0.0, 5.0, 1.0, 0.1, key=f"{P}mfac")
    force = F.magnus_lift(sp, circ * app)
    st.metric("Magnus force", f"{force:.3g} N")
    st.caption("The force curves the path towards the slow-air side, in the direction of the "
               "spin. Golf balls are dimpled so that this effect is strong and repeatable.")


def _viscosity() -> None:
    how_to("numbers"), how_to("sliders"),
    st.subheader("6.5 · Viscous fluids and fluid friction")
    st.latex(r"F_{\text{drag}} = 6\pi\eta r v \quad\text{(for a small sphere, slowly)}")
    card("Viscosity is resistance to internal shear",
         "<p>It is not a measure of how heavy the fluid is. Honey is not heavy, it is "
         "viscous — its layers will not slide past one another easily. That is why a bubble "
         "rises slowly through glycerine and quickly through water.</p>", "THE IDEA")
    st.dataframe(pd.DataFrame([
        {"liquid": r["liquid"], "η (Pa s)": f"{r['eta_pa_s']:.3g}",
         "relative to water": r["relative"], "what you notice": r["feel"]}
        for r in F.VISCOUS_FLUIDS
    ]), use_container_width=True, hide_index=True)
    st.markdown(VIS.viscosity_ladder(freeze(F.VISCOUS_FLUIDS)), unsafe_allow_html=True)

    st.subheader("The retarding force")
    c1, c2, c3 = st.columns(3)
    with c1:
        radius = st.number_input("sphere radius r (mm)", 0.1, 100.0, 5.0, 0.5, key=f"{P}vr")
    with c2:
        speed = st.slider("speed v (m s⁻¹)", 0.0, 50.0, 2.0, 0.1, key=f"{P}vv")
    with c3:
        eta = st.selectbox("fluid", [f["name"] for f in F.FLUIDS], index=1, key=f"{P}veta")
    fl = next(f for f in F.FLUIDS if f["name"] == eta)
    drag = F.drag_relation(fl["density"], fl["viscosity"], radius * 1e-3, speed)
    st.dataframe(pd.DataFrame([
        {"quantity": "drag force", "value": f"{drag['force']:.4g} N"},
        {"quantity": "Reynolds number", "value": f"{drag['reynolds']:.4g}"},
        {"quantity": "flow around the sphere", "value": drag["regime"]},
    ]), use_container_width=True, hide_index=True)
    st.info(drag["note"])

    st.subheader("The same ball in two fluids")
    st.write(F.drag_ratio(1420.0, 20.0, 1.2, 1.8e-5, radius * 1e-3, max(speed, 0.1))["note"])
    guidance(WATCH_OUT, "Density and viscosity are independent",
             "A light, thick liquid and a heavy, runny one feel nothing alike. Viscosity "
             "decides the drag; density decides the upthrust. Honey is both dense and thick, "
             "which is why it feels doubly resistant.")


def _superfluidity() -> None:
    st.subheader("6.5 · Superfluidity — the limit of zero viscosity")
    st.markdown(VIS.superfluidity_panel(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"property": r["property"], "evidence": r["evidence"],
         "explanation": r["explanation"]} for r in F.superfluidity()
    ]), use_container_width=True, hide_index=True)
    guidance(HONEST_LIMIT, "Superfluidity is a quantum effect, not just a very small viscosity",
             "Helium does not simply become 'less sticky'. Below 2.2 K its atoms pair up and "
             "cooperate, and their circulation is locked to whole multiples of a fixed "
             "quantum. That is why the swirl never dies down and why the fountain effect "
             "behaves so differently from ordinary convection.")


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "upthrust": _bench,
    "ships": _ships,
    "flow": _flow,
    "continuity": _continuity,
    "bernoulli": _bernoulli,
    "applications": _applications,
    "viscosity": _viscosity,
    "superfluidity": _superfluidity,
    "worked": lambda: worked_problems(SPEC),
    "practice": lambda: practice(SPEC),
    "tutor": lambda: ai_tutor.render(_N),
    "practical": lambda: practicals(SPEC),
    "references": lambda: references(SPEC),
}

STATIONS = [Station(row["key"], row["label"], RENDERERS[row["key"]], row["slos"])
            for row in D.STATIONS]

SPEC = ChapterSpec(
    number=_N,
    title="Fluids Dynamics",
    blurb="Upthrust and floatation, streamline and turbulent flow, continuity and Bernoulli's equation.",
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
