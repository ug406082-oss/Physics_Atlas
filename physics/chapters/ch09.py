"""Chapter 9 interface: Physical Optics.

Twenty-eight outcomes, and one mathematical heart. The **interference
explorer** at the heart of this chapter is reused for Young's slits, a single
slit, a grating and Michelson — because the bright and dark positions really do
follow the same rule in all four.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..core import optics as P9
from ..engine import (ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, card, metric_row
from ..visuals import ch09 as VIS
from . import ch09_data as D

_N = 9
P = f"c{_N}_"


def _explorer(default_geometry: str = "double") -> None:
    """The shared interference explorer."""
    st.caption("Bright where the path difference is a whole number of wavelengths, "
               "dark where it is a half number. That is the whole of this chapter.")

    g_col, l_col, d_col = st.columns(3)
    with g_col:
        geometry = st.selectbox("which experiment", ["double", "single", "grating"],
                                index=["double", "single", "grating"].index(default_geometry),
                                key=f"{P}9g{default_geometry}")
    with l_col:
        lam = st.number_input("wavelength (m)", 1e-9, 1e-3, 5.5e-7, 1e-8, format="%.2e",
                              key=f"{P}9l{default_geometry}")
    with d_col:
        delta = st.number_input("path difference (m)", -1e-6, 1e-6, lam, 1e-8,
                                format="%.2e", key=f"{P}9d{default_geometry}")
    st.markdown(VIS.interference_explorer(lam, delta, geometry), unsafe_allow_html=True)

    from ..core import waves as W8
    if geometry == "double":
        result = W8.interference_intensity(1.0, 1.0, delta, lam)
    elif geometry == "single":
        x = delta / lam if lam else 0.0
        result = {"kind": "single-slit",
                  "intensity": (math.sin(math.pi * x) / (math.pi * x) if abs(x) > 1e-12 else 1.0) ** 2}
    else:
        ratio = delta / lam if lam else 0.0
        result = {"kind": "grating", "intensity": math.cos(math.pi * ratio) ** 8}
    st.dataframe(pd.DataFrame([
        {"quantity": "path difference / wavelength", "value": f"{delta / lam:.5g}" if lam else "—"},
        {"quantity": "phase difference", "value": f"{2 * math.pi * delta / lam:.5g} rad" if lam else "—"},
        {"quantity": "relative intensity", "value": f"{result.get('intensity', 0):.5g}"},
        {"quantity": "verdict",
         "value": (W8.interference_kind(delta, lam) if geometry == "double"
                   else result.get("kind", ""))},
    ]), use_container_width=True, hide_index=True)
    guidance(EXAM_TIP, "Take the fractional part and be done",
             "0.2 lambda and 1.2 lambda give exactly the same interference, because a whole "
             "wavelength changes nothing. Compute delta/lambda, throw away the whole-number part, "
             "and you are left with the only part that matters.")


def _nature() -> None:
    st.subheader("9.1 · The nature of light, wavefronts and Huygens")
    st.markdown(VIS.wavefront_growth(), unsafe_allow_html=True)
    for item in D.WAVEFRONT_NOTES:
        with st.expander(item["question"]):
            st.markdown(item["answer"])
    st.subheader("Huygens' principle")
    st.markdown(VIS.huygens_construction(), unsafe_allow_html=True)
    st.markdown("\n\n".join(f"{index}. {step}"
                            for index, step in enumerate(D.HUYGENS_STEPS, start=1)))
    st.dataframe(pd.DataFrame([
        {"application": c["application"], "how it works": c["how"], "why": c["why"]}
        for c in D.HUYGENS_CONSEQUENCES
    ]), use_container_width=True, hide_index=True)
    st.subheader("How light was understood")
    st.dataframe(pd.DataFrame([
        {"theory": t["theory"], "claim": t["claim"], "explained": t["explained"],
         "could not explain": t["failed_for"], "verdict": t["verdict"]}
        for t in D.LIGHT_THEORIES
    ]), use_container_width=True, hide_index=True)
    for theory in D.LIGHT_THEORIES:
        with st.expander(theory["theory"]):
            st.markdown(f"**Claim.** {theory['claim']}\n\n"
                        f"**Explained.** {theory['explained']}\n\n"
                        f"**Could not explain.** {theory['failed_for']}\n\n"
                        f"**Verdict.** {theory['verdict']}")
    guidance(HONEST_LIMIT, "'Which is it?' is the wrong question",
             "Light is neither a classical wave nor a stream of classical particles. Every "
             "experiment can be predicted by one picture or the other, and no experiment "
             "distinguishes them - which is the whole content of wave-particle duality.")


def _conditions() -> None:
    st.subheader("9.2.1, 9.2.2 & 9.2.3 · Coherence and the conditions for interference")
    st.markdown(VIS.coherence_panel(), unsafe_allow_html=True)
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.COHERENCE_POINTS))
    st.subheader("The conditions, with the reason for each")
    st.dataframe(pd.DataFrame([
        {"condition": c["condition"], "why it is needed": c["why"],
         "how to achieve it": c["how"]} for c in D.INTERFERENCE_CONDITIONS
    ]), use_container_width=True, hide_index=True)
    st.markdown("**Interference.** " + "Superposition of two coherent light waves producing "
              "bright and dark fringes. Where the waves arrive in step the displacements add "
              "and the light is bright; where they arrive half a cycle out of step they cancel "
              "and the light is dark.")
    guidance(WATCH_OUT, "Same frequency is necessary but not sufficient",
             "Two sodium lamps emit at the same frequency, but their phase difference wanders "
             "many times a second. Any pattern moves faster than the eye can follow and averages "
             "to a uniform glow. Coherence means a **constant** phase difference.")


def _young() -> None:
    st.subheader("9.2.4, 9.2.5 & 9.2.6 · Young's double slit")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}" for p in D.YOUNG_POINTS))

    l_col, d_col, L_col = st.columns(3)
    with l_col:
        lam = st.number_input("wavelength (m)", 1e-9, 1e-3, 5.5e-7, 1e-8, format="%.2e",
                              key=f"{P}9yl")
    with d_col:
        sep = st.number_input("slit separation d (m)", 1e-7, 1e-2, 0.5e-3, 1e-5,
                              format="%.2e", key=f"{P}9yd")
    with L_col:
        dist = st.number_input("screen distance L (m)", 0.1, 100.0, 1.0, 0.1, key=f"{P}9yL")
    st.markdown(VIS.youngs_arrangement(lam, dist, sep), unsafe_allow_html=True)
    width = P9.fringe_width(lam, dist, sep)
    st.latex(rf"dy = \frac{{\lambda L}}{{d}} = \frac{{{lam:.3g} \times {dist:.3g}}}"
             rf"{{{sep:.3g}}} = {width:.4g}\ \text{{m}}")
    st.markdown(VIS.fringe_pattern(lam, dist, sep), unsafe_allow_html=True)

    st.dataframe(pd.DataFrame([
        {"quantity": f["quantity"], "formula": f["formula"], "note": f["note"]}
        for f in D.FRINGE_NOTES
    ]), use_container_width=True, hide_index=True)
    fringes = P9.fringe_positions(lam, dist, sep)
    st.dataframe(pd.DataFrame([
        {"order n": f["n"], "position y (m)": f"{f['y']:.4g}"} for f in fringes
    ]), use_container_width=True, hide_index=True)

    st.subheader("Solve for the unknown")
    known = st.selectbox("what do you know?", ["Fringe spacing dy", "Wavelength",
                                               "Slit separation"], key=f"{P}9yk")
    if known == "Fringe spacing dy":
        dy_in = st.number_input("fringe spacing (m)", 1e-6, 1e-1, 1.1e-3, 1e-5,
                                format="%.2e", key=f"{P}9ydy")
        st.latex(rf"dy = \frac{{\lambda L}}{{d}} \Rightarrow \lambda = "
                 rf"\frac{{dy\,d}}{{L}} = {dy_in * sep / dist:.4g}\ \text{{m}}")
    elif known == "Wavelength":
        dy_in = st.number_input("fringe spacing (m)", 1e-6, 1e-1, 1.1e-3, 1e-5,
                                format="%.2e", key=f"{P}9ydy2")
        st.latex(rf"\lambda = \frac{{dy\,d}}{{L}} = {dy_in * sep / dist:.4g}\ \text{{m}}")
    else:
        dy_in = st.number_input("fringe spacing (m)", 1e-6, 1e-1, 1.1e-3, 1e-5,
                                format="%.2e", key=f"{P}9ydy3")
        st.latex(rf"d = \frac{{\lambda L}}{{dy}} = {lam * dist / dy_in:.4g}\ \text{{m}}")
    _explorer("double")
    guidance(TRY_IT, "Make the slits closer and watch the fringes spread",
             "dy is inversely proportional to d. Doubling the separation halves the spacing, "
             "which is why a double slit with millimetre separation gives millimetre fringes on "
             "a screen a metre away.")


def _michelson() -> None:
    st.subheader("9.3 · Michelson's interferometer and gravitational waves")
    arm = st.number_input("arm length (km)", 0.1, 100.0, 4.0, 0.1, key=f"{P}9ma")
    lam = st.number_input("laser wavelength (m)", 1e-8, 1e-5, 1.064e-6, 1e-8,
                          format="%.3e", key=f"{P}9ml")
    move = st.number_input("mirror movement (m)", 0.0, 1e-6, 0.0, 1e-9, format="%.1e",
                           key=f"{P}9mm")
    st.markdown(VIS.michelson_layout(arm, 2 * move), unsafe_allow_html=True)
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.MICHELSON_POINTS))
    st.latex(rf"N = \frac{{2 \times {move:.3g}}}{{{lam:.4g}}} = {2 * move / lam:.4g}\ \text{{fringes}}")
    st.metric("Fringes crossed", f"{2 * move / lam:.4g}")
    st.caption("One fringe passes for every half-wavelength of mirror movement, because the "
               "light makes the round trip.")

    st.subheader("Gravitational waves")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.GRAVITATIONAL_NOTES))
    st.markdown(VIS.spacetime_ring(), unsafe_allow_html=True)
    st.markdown(VIS.sensitivity_scale(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"length": r["length"], "value": r["value"], "note": r["note"]}
        for r in D.INTERFEROMETER_SENSITIVITY
    ]), use_container_width=True, hide_index=True)
    strain_col = st.number_input("strain detected by LIGO", 1e-24, 1e-18, 1e-21, 1e-24,
                                  format="%.0e", key=f"{P}9ms")
    st.metric("Change in each arm", f"{strain_col * arm * 1000:.4g} m")
    st.caption("That is a few million millionths of a metre. It is detected because the arms are "
               "kilometres long and the mirrors hang in a vacuum, free of any material to drift.")
    guidance(HONEST_LIMIT, "Why the arms are kilometres, not centimetres",
             "The required strain scales directly with arm length, and nothing can provide a "
             "larger strain than nature allows. A short arm would need the wave to strain "
             "space by a larger fraction than a black-hole merger actually produces.")


def _diffraction() -> None:
    st.subheader("9.4 · Diffraction, slits and gratings")
    st.markdown("**Diffraction** is the spreading of light past an obstacle or through an "
              "opening. It is more pronounced for longer wavelengths and narrower openings, "
              "and it is unavoidable — every opening has a finite width.")
    a_col, l_col = st.columns(2)
    with a_col:
        slit = st.number_input("slit width a (m)", 1e-7, 1e-2, 1e-4, 1e-6, format="%.1e",
                               key=f"{P}9da")
    with l_col:
        lam = st.number_input("wavelength (m)", 1e-9, 1e-3, 5.5e-7, 1e-8, format="%.2e",
                              key=f"{P}9dl")
    st.markdown(VIS.diffraction_pattern(slit, lam), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"feature": f["feature"], "condition": f.get("condition", f.get("width", "")),
         "note": f["note"]} for f in D.SINGLE_SLIT_NOTES
    ]), use_container_width=True, hide_index=True)
    st.subheader("Minima, one at a time")
    order = st.slider("order m", 1, 6, 1, 1, key=f"{P}9do")
    result = P9.single_slit_minima(slit, lam, order)
    if "error" in result:
        st.error(result["error"])
    else:
        st.latex(rf"\sin\theta = \frac{{{order}\lambda}}{{a}} = "
                 rf"{result['sin_theta']:.4g} \Rightarrow \theta = {result['theta_deg']:.4g}^\circ")
        st.caption(result["note"])
    st.subheader("Diffraction gratings")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}" for p in D.GRATING_NOTES))
    d_col, g_col = st.columns(2)
    with d_col:
        spacing = st.number_input("slit spacing d (m)", 1e-7, 1e-3, 1e-6, 1e-8,
                                  format="%.1e", key=f"{P}9gd")
    with g_col:
        glam = st.number_input("wavelength (m)", 1e-9, 1e-3, 5.5e-7, 1e-8, format="%.2e",
                               key=f"{P}9gl")
    st.markdown(VIS.grating_panel(spacing, glam), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"order m": g["m"], "exists?": "yes" if g["exists"] else "no",
         "sin(theta)": f"{g['sin_theta']:.4g}" if g["exists"] else "—",
         "angle": f"{g['theta_deg']:.3g}°" if g["exists"] else "—",
         "note": g["note"]} for g in P9.grating_angles(spacing, glam)
    ]), use_container_width=True, hide_index=True)
    n_lines = st.number_input("number of ruled lines N", 100, 100000, 5000, 100, key=f"{P}9gn")
    rp = P9.grating_resolving_power(2, int(n_lines))
    st.metric("Resolving power (order 2)", f"{rp['R']:.4g}")
    st.caption(rp["separates"])
    _explorer("single")
    guidance(EXAM_TIP, "sin(theta) can never exceed 1",
             "Before you calculate, check whether the order can exist at all. If m lambda > d, "
             "there is no such maximum and writing one down loses the marks.")


def _bragg() -> None:
    st.subheader("9.5 · Bragg's law and X-ray diffraction")
    st.latex(r"2 d \sin\theta = m \lambda")
    st.markdown("**Derivation.**")
    st.markdown("\n\n".join(f"**{g['step']}** — {g['detail']}" for g in D.BRAGG_GEOMETRY))
    d_col, l_col, o_col = st.columns(3)
    with d_col:
        spacing = st.number_input("plane spacing d (m)", 1e-12, 1e-6, 5.64e-10, 1e-11,
                                  format="%.2e", key=f"{P}9bd")
    with l_col:
        lam = st.number_input("wavelength (m)", 1e-13, 1e-8, 1.54e-10, 1e-12,
                              format="%.2e", key=f"{P}9bl")
    with o_col:
        order = st.slider("order m", 1, 8, 1, 1, key=f"{P}9bo")
    st.markdown(VIS.bragg_layers(spacing, lam, order), unsafe_allow_html=True)
    result = P9.bragg_angle(spacing, lam, order)
    if "error" in result:
        st.error(result["error"])
    else:
        st.latex(rf"\theta = \sin^{{-1}}\!\left(\frac{{{order} \times {lam:.3g}}}"
                 rf"{{{2 * spacing:.3g}}}\right) = {result['theta_deg']:.4g}^\circ")
        st.metric("2θ as the detector is quoted", f"{result['twice_theta_deg']:.4g}°")
        st.caption(result["note"])
        back = P9.bragg_order(spacing, result["theta_deg"], lam)
        st.caption(f"Reading the order back out of that angle: m = {back:.4g}, which should be "
                   f"exactly {order}.")
    st.dataframe(pd.DataFrame([
        {"crystal": c["crystal"], "d (m)": f"{c['d']:.3g}", "note": c["note"]}
        for c in D.BRAGG_EXAMPLES
    ]), use_container_width=True, hide_index=True)
    st.subheader("Peak positions for this crystal")
    st.dataframe(pd.DataFrame([
        {"order m": row["m"],
         "theta": "does not exist" if "error" in row else f"{row['theta_deg']:.4g}°",
         "2theta": "—" if "error" in row else f"{row['twice_theta_deg']:.4g}°"}
        for row in P9.xray_diffraction_series(spacing, lam)
    ]), use_container_width=True, hide_index=True)
    guidance(WATCH_OUT, "θ is measured to the plane, not the normal",
             "Every Bragg answer is quoted at 2θ, because 2θ is the angle between the incident "
             "and the reflected beam. Mixing the two up is the classic error in this topic.")


def _polarisation() -> None:
    st.subheader("9.6.1 to 9.6.4 · Polarisation, and how it is produced")
    st.markdown(VIS.polarisation_types(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"type": t["type"], "vibration": t["vibration"], "appearance": t["appearance"],
         "note": t["note"]} for t in D.POLARISATION_TYPES
    ]), use_container_width=True, hide_index=True)
    st.write("**Only transverse waves can be polarised.** A longitudinal wave's particles "
              "vibrate along the direction of travel, so there is no plane of vibration to "
              "select. Sound in air cannot be polarised; light can.")
    st.markdown(VIS.polaroid_chain(90.0, second=True), unsafe_allow_html=True)
    st.latex(r"I_1 = \frac{I_0}{2}, \qquad I = I_1 \cos^2\theta")
    st.subheader("Polarisation by reflection")
    st.markdown(VIS.brewster_diagram(1.0, 1.5), unsafe_allow_html=True)
    n1_col, n2_col = st.columns(2)
    with n1_col:
        n1 = st.number_input("n of the first medium", 1.0, 3.0, 1.0, 0.05, key=f"{P}9n1")
    with n2_col:
        n2 = st.number_input("n of the second medium", 1.0, 3.0, 1.5, 0.05, key=f"{P}9n2")
    brew = P9.brewster_angle(n1, n2)
    st.latex(rf"\tan\theta_B = \frac{{{n2:g}}}{{{n1:g}}} \Rightarrow \theta_B = "
             rf"{brew['theta_b_deg']:.4g}^\circ")
    st.caption(brew["note"])
    guidance(TRY_IT, "Cross the two polarisers, then add a third",
             "Two crossed polarisers give a black view. Slip a third in at 45 degrees and light "
             "gets through again — more than with two. A filter cannot do that, so it is the "
             "clearest demonstration that polarisers work by re-orienting vibrations rather than "
             "by absorbing them.")


def _malus() -> None:
    st.subheader("9.6.5 & 9.6.6 · Malus's law")
    st.latex(r"I = I_0 \cos^2\theta")
    st.markdown(VIS.malus_curve(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"theta": f"{row['theta_deg']}°", "fraction transmitted": f"{row['fraction']:.3g}",
         "note": row["note"]} for row in D.MALUS_TABLE
    ]), use_container_width=True, hide_index=True)

    angle = st.slider("angle between the axes (°)", 0.0, 180.0, 60.0, 1.0, key=f"{P}9ma")
    i0 = st.number_input("polarised intensity entering the last polaroid (W m⁻²)",
                         0.0, 1e5, 400.0, 10.0, key=f"{P}9mi")
    st.metric("transmitted", f"{P9.malus_law(i0, angle):.4g} W m⁻²")
    st.caption(f"cos²({angle:g}°) = {math.cos(math.radians(angle)) ** 2:.4g}, so "
               f"{100 * math.cos(math.radians(angle)) ** 2:.1f} % passes.")
    triple = P9.two_polarisers(i0, 0.0, angle)
    st.dataframe(pd.DataFrame([
        {"stage": "after the first polaroid (unpolarised in)",
         "intensity": f"{triple['after_first']:.4g} W m⁻²"},
        {"stage": f"after the second ({angle:g}° apart)",
         "intensity": f"{triple['after_second']:.4g} W m⁻²"},
        {"stage": "with a third at 45°",
         "intensity": f"{triple['with_three_polarisers']:.4g} W m⁻²"},
    ]), use_container_width=True, hide_index=True)
    if triple["gain"]:
        st.success("More light gets through with three polarisers than with two. That is "
                   "impossible for simple filters, and it is the clearest proof that the "
                   "middle polariser re-orients the vibrations.")
    st.markdown("**From the table:** " + triple["note"])
    guidance(EXAM_TIP, "Two different halvings, two different reasons",
             "Unpolarised light loses half at the first polaroid — that is a fact about "
             "unpolarised input. Everything after that follows Malus's cos squared. Dropping "
             "either step is the commonest error in this topic.")


def _uses() -> None:
    st.subheader("9.6.7 · Applications of polarisation")
    st.dataframe(pd.DataFrame([
        {"application": a["application"], "how it works": a["how"], "why": a["why"]}
        for a in D.POLARISATION_USES
    ]), use_container_width=True, hide_index=True)
    for item in D.POLARISATION_USES:
        with st.expander(item["application"]):
            st.markdown(f"**How.** {item['how']}\n\n{item['why']}")
    st.write("**Name the wave property, and the application explains itself.** Glare is "
              "polarised, so it can be blocked. Vibrations can be turned, so an LCD can dim each "
              "pixel. Two images can be separated by polarisation, so the eyes can see them "
              "independently.")
    guidance(HONEST_LIMIT, "Polarising sunglasses cut glare, not brightness",
             "They remove the reflected, largely-polarised light from a horizontal surface. They "
             "do not darken the scene in general, which is why they help at the beach and do "
             "little in a forest.")


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "nature": _nature,
    "conditions": _conditions,
    "young": _young,
    "michelson": _michelson,
    "diffraction": _diffraction,
    "bragg": _bragg,
    "polarisation": _polarisation,
    "malus": _malus,
    "uses": _uses,
    "worked": lambda: worked_problems(SPEC),
    "practice": lambda: practice(SPEC),
    "tutor": lambda: ai_tutor.render(_N),
    "references": lambda: references(SPEC),
}

STATIONS = [Station(row["key"], row["label"], RENDERERS[row["key"]], row["slos"])
            for row in D.STATIONS]

SPEC = ChapterSpec(
    number=_N,
    title="Physical Optics",
    blurb="Wavefronts, interference, diffraction, Bragg's law and polarisation.",
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