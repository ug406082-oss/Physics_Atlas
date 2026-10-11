"""Chapter 8 interface: Waves.

Three instruments of its own: the **two-wave bench**, where any pair of sources
can be superposed and the sum watched emerge; the **stationary-wave bench** for
strings and air columns; and the **Doppler explorer**, where all four cases of
the syllabus can be set up and read off in numbers.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..core import waves as W
from ..engine import (how_to, ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT, practicals,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, card, metric_row
from ..visuals import ch08 as VIS
from . import ch08_data as D

_N = 8
P = f"c{_N}_"


def _two_wave_bench() -> None:
    """The shared bench used by the superposition, interference and beats stations."""
    st.caption("Two waves and their sum. When the frequencies match, the sum is a single "
               "clean wave; when they differ, you get the beats you hear.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        a1 = st.number_input("amplitude of A", 0.0, 3.0, 1.0, 0.1, key=f"{P}wa1")
    with c2:
        f1 = st.number_input("frequency of A (cycles across the graph)", 0.5, 12.0, 3.0,
                             0.5, key=f"{P}wf1")
    with c3:
        a2 = st.number_input("amplitude of B", 0.0, 3.0, 1.0, 0.1, key=f"{P}wa2")
    with c4:
        f2 = st.number_input("frequency of B", 0.5, 12.0, 3.5, 0.5, key=f"{P}wf2")

    st.markdown(VIS.two_wave_bench(a1, f1, a2, f2), unsafe_allow_html=True)
    if math.isclose(f1, f2, rel_tol=1e-9):
        st.success("Equal frequencies: the sum is a single wave of amplitude "
                   f"{a1 + a2:.3g}. Two sounds in step are disproportionately loud.")
    else:
        st.info(f"Differing frequencies: you will hear {abs(f1 - f2):.3g} beats per unit time. "
                f"Switch to the Beats station for the full picture.")
    series = W.superposition_series([
        {"A": a1, "f": f1, "lambda": 1.0},
        {"A": a2, "f": f2, "lambda": 1.0}], 1.0)
    st.dataframe(pd.DataFrame([
        {"quantity": "resultant at x = 0",
         "value": f"{series['sum'][0]:.4g}"},
        {"quantity": "largest resultant",
         "value": f"{max(series['sum']):.4g}"},
        {"quantity": "smallest resultant",
         "value": f"{min(series['sum']):.4g}"},
        {"quantity": "would-be sum of amplitudes", "value": f"{a1 + a2:.4g}"},
    ]), use_container_width=True, hide_index=True)


def _progressive() -> None:
    how_to("numbers"),
    st.subheader("8.1.1 & 8.1.2 · Progressive waves and the energy they carry")
    card("Energy goes; matter stays",
         "<p>Every particle of the medium oscillates about a fixed point while the pattern "
         "travels away from the source. A cork on a pond bobs up and down and drifts only "
         "slightly; a floating boat is thrown back to the shore after the waves have gone "
         "past.</p>", "THE IDEA")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.PROGRESSIVE_POINTS))
    st.markdown(VIS.progressive_trace(0.6, 1.0), unsafe_allow_html=True)

    st.subheader("Read every feature off the graph")
    amp = st.number_input("amplitude (m)", 0.01, 10.0, 0.60, 0.05, key=f"{P}gamp")
    lam = st.number_input("wavelength (m)", 0.1, 20.0, 2.0, 0.1, key=f"{P}wlam")
    st.markdown(VIS.wave_graph_annotated(amp, lam), unsafe_allow_html=True)
    guidance(WATCH_OUT, "Amplitude is half the crest-to-trough height",
             "The diagram draws the full peak-to-peak distance, so if a real graph shows 6 cm "
             "crest to trough the amplitude is 3 cm. This is the single most common mark loss "
             "in wave questions.")


def _intensity() -> None:
    how_to("numbers"), how_to("sliders"),
    st.subheader("8.1.3 · Intensity")
    st.latex(r"I = \frac{P}{A}, \qquad I \propto A^2")
    st.dataframe(pd.DataFrame([
        {"situation": c["situation"], "what changes": c["change"], "why": c["why"]}
        for c in D.INTENSITY_CASES
    ]), use_container_width=True, hide_index=True)

    mode = st.radio("What do you want to calculate?", ["From power and area",
                                                       "From the amplitude change"],
                    horizontal=True, key=f"{P}imode")
    if mode == "From power and area":
        p_col, a_col = st.columns(2)
        with p_col:
            power = st.number_input("power P (W)", 0.0, 1e5, 12.0, 1.0, key=f"{P}iP")
        with a_col:
            area = st.number_input("area A (m²)", 1e-6, 1e5, 2.0, 0.5, key=f"{P}iA")
        st.metric("intensity", f"{W.intensity(power, area):.4g} W m⁻²")
    else:
        i0_col, a0_col, a1_col = st.columns(3)
        with i0_col:
            i0 = st.number_input("original intensity (W m⁻²)", 0.0, 1e4, 8.0, 0.5, key=f"{P}iI0")
        with a0_col:
            amp0 = st.number_input("original amplitude (m)", 0.0, 10.0, 0.20, 0.05, key=f"{P}iA0")
        with a1_col:
            amp1 = st.number_input("new amplitude (m)", 0.0, 10.0, 0.40, 0.05, key=f"{P}iA1")
        new = W.intensity_from_amplitudes(i0, amp0, amp1)
        st.metric("new intensity", f"{new:.4g} W m⁻²")
        st.caption(f"A factor of {(amp1 / amp0) ** 2:.3g} in amplitude is a factor of "
                   f"{(amp1 / amp0) ** 2:.3g} in intensity.")
    guidance(EXAM_TIP, "Intensity goes as amplitude squared, always",
             "Doubling the amplitude quadruples the intensity. This is why a wave twice as "
             "large is not twice as 'loud' — loudness is roughly logarithmic, which is why "
             "decibels exist at all.")


def _waveequation() -> None:
    how_to("numbers"), how_to("sliders"),
    st.subheader("8.1.4 · v = fλ")
    st.latex(r"v = f\lambda")
    known = st.radio("Which quantity do you know?", ["Speed", "Frequency", "Wavelength"],
                     horizontal=True, key=f"{P}wk")
    c1, c2, c3 = st.columns(3)
    with c1:
        v_in = st.number_input("v (m s⁻¹)", 0.01, 3e8, 340.0, 1.0, key=f"{P}wv")
    with c2:
        f_in = st.number_input("f (Hz)", 0.01, 1e9, 440.0, 1.0, key=f"{P}wf")
    with c3:
        lam_in = st.number_input("lambda (m)", 1e-9, 1e3, 0.77, 0.01, key=f"{P}wl")
    if known == "Speed":
        result = W.wavelength(v_in, f_in)
        st.metric("wavelength", f"{result:.4g} m")
    elif known == "Frequency":
        result = W.wavelength(v_in, f_in)
        st.metric("wavelength", f"{result:.4g} m")
    else:
        result = W.wave_speed(f_in, lam_in)
        st.metric("speed", f"{result:.4g} m s⁻¹")
    st.dataframe(pd.DataFrame([
        {"quantity": "v", "value": f"{v_in:g} m s⁻¹"},
        {"quantity": "f", "value": f"{f_in:g} Hz"},
        {"quantity": "lambda = v/f", "value": f"{W.wavelength(v_in, f_in):.4g} m"},
        {"quantity": "check: f lambda", "value": f"{W.wave_speed(f_in, W.wavelength(v_in, f_in)):.4g} m s⁻¹"},
    ]), use_container_width=True, hide_index=True)
    if abs(W.wave_speed(f_in, W.wavelength(v_in, f_in)) - v_in) < 1e-6:
        st.success("The three are consistent — f lambda returns the speed you started with.")
    for item in D.WAVE_EQUATION_NOTES:
        with st.expander(item["question"]):
            st.markdown(item["answer"])
    guidance(TRY_IT, "Compare the same note in air and in water",
             "Set v to 340 and then 1500 with f fixed at 440. The frequency — and so the pitch — "
             "does not move, but the wavelength nearly doubles. Frequency belongs to the "
             "source; speed and wavelength belong to the medium.")


def _types() -> None:
    how_to("numbers"),
    st.subheader("8.2.1 & 8.2.2 · Transverse and longitudinal waves")
    st.markdown(VIS.particle_motion(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"property": r["property"], "transverse": r["transverse"],
         "longitudinal": r["longitudinal"]} for r in D.TRANSVERSE_DETAIL
    ]), use_container_width=True, hide_index=True)
    quiz = st.selectbox("Classify each", ["Light", "Sound in air", "S-waves in rock",
                                          "Waves on a rope", "Sound in a steel rod",
                                          "P-waves in rock"],
                        key=f"{P}tq")
    answer = {"Light": "transverse", "Sound in air": "longitudinal",
              "S-waves in rock": "transverse", "Waves on a rope": "transverse",
              "Sound in a steel rod": "longitudinal", "P-waves in rock": "longitudinal"}[quiz]
    st.markdown(f"**{quiz}** is **{answer}**.")
    st.markdown(VIS.wave_graph_annotated(0.6, 2.0), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"feature": "crest", "transverse": "yes", "longitudinal": "no"},
        {"feature": "trough", "transverse": "yes", "longitudinal": "no"},
        {"feature": "compression", "transverse": "no", "longitudinal": "yes"},
        {"feature": "rarefaction", "transverse": "no", "longitudinal": "yes"},
        {"feature": "high pressure region", "transverse": "no", "longitudinal": "yes"},
    ]), use_container_width=True, hide_index=True)


def _superposition() -> None:
    how_to("numbers"),
    st.subheader("8.3.1, 8.3.2 & 8.3.3 · Superposition, interference and phase")
    card("The resultant displacement is the sum",
         "<p>Add the displacements point by point. That is the whole principle — and it is "
         "reversible, so the waves reappear unchanged on the other side.</p>", "THE IDEA")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.SUPERPOSITION_POINTS))
    _two_wave_bench()

    st.subheader("Explore the interference pattern")
    d_col, l_col = st.columns(2)
    with d_col:
        delta = st.number_input("path difference (m)", 0.0, 10.0, 0.5, 0.05, key=f"{P}id")
    with l_col:
        lam = st.number_input("wavelength (m)", 0.01, 10.0, 1.0, 0.05, key=f"{P}il")
    st.markdown(VIS.interference_map(delta, lam), unsafe_allow_html=True)
    result = W.interference_intensity(1.0, 1.0, delta, lam)
    st.dataframe(pd.DataFrame([
        {"quantity": "path difference / wavelength", "value": f"{delta / lam:.4g}"},
        {"quantity": "phase difference", "value": f"{result['phase']:.4g} rad"},
        {"quantity": "kind", "value": result["kind"]},
        {"quantity": "resultant intensity (for equal beams of 1)",
         "value": f"{result['intensity']:.4g}"},
        {"quantity": "maximum", "value": f"{result['maximum']:.4g}"},
        {"quantity": "minimum", "value": f"{result['minimum']:.4g}"},
    ]), use_container_width=True, hide_index=True)
    st.dataframe(pd.DataFrame([
        {"case": n["case"], "phase": n["phase"], "kind": n["kind"], "why": n["why"]}
        for n in D.INTERFERENCE_NOTES
    ]), use_container_width=True, hide_index=True)
    st.subheader("Phase difference")
    st.latex(r"\Delta\phi = \frac{2\pi}{\lambda}\times(\text{path difference})")
    st.caption(f"At a path difference of {delta:g} m and a wavelength of {lam:g} m, "
               f"Δφ = 2π × {delta / lam:.4g} = **{result['phase']:.4g} rad**.")
    guidance(EXAM_TIP, "A whole wavelength changes nothing",
             "Only the fractional part of the path difference matters. Adding a whole number "
             "of wavelengths leaves the interference exactly as it was — which is why a sound "
             "does not get louder every metre you move along a corridor.")


def _beats() -> None:
    how_to("numbers"),
    st.subheader("8.3.4 · Beats")
    st.latex(r"f_{\text{beat}} = |f_1 - f_2|, \qquad T_{\text{beat}} = \frac{1}{f_{\text{beat}}}")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.BEAT_POINTS))
    f1_col, f2_col, d_col = st.columns(3)
    with f1_col:
        f1 = st.number_input("f₁ (Hz)", 100.0, 2000.0, 440.0, 1.0, key=f"{P}bf1")
    with f2_col:
        f2 = st.number_input("f₂ (Hz)", 100.0, 2000.0, 444.0, 1.0, key=f"{P}bf2")
    with d_col:
        duration = st.number_input("time shown (s)", 0.1, 5.0, 0.6, 0.1, key=f"{P}bd")
    st.markdown(VIS.beat_panel(f1, f2, duration), unsafe_allow_html=True)
    metric_row([("beat frequency", f"{W.beat_frequency(f1, f2):.4g} Hz"),
                ("beat period", f"{W.beat_period(f1, f2):.4g} s"),
                ("beats in the window", f"{W.beat_frequency(f1, f2) * duration:.3g}"),
                ("mean pitch", f"{(f1 + f2) / 2:.4g} Hz")])
    if abs(f1 - f2) < 1:
        st.success("Those are within 1 Hz, so the beats are slow enough to follow with your "
                   "head. That is what makes this effect so useful for tuning.")
    st.dataframe(pd.DataFrame([
        {"quantity": "|f₁ − f₂|", "value": f"{W.beat_frequency(f1, f2):.4g} Hz"},
        {"quantity": "1/f_beat", "value": f"{W.beat_period(f1, f2):.4g} s"},
        {"quantity": "path difference for a half cycle",
         "value": f"{1 / (2 * ((f1 + f2) / 2)) * 0:.4g} m (uses the mean frequency)"},
    ]), use_container_width=True, hide_index=True)
    guidance(HONEST_LIMIT, "Beats need two nearly equal frequencies",
             "If the two sounds are more than about 10 Hz apart, the beat is faster than the "
             "ear can follow as a distinct rhythm and the note simply sounds slightly rough. "
             "It is the slow version that is musically useful.")


def _stationary() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("8.4 · Stationary waves")
    card("Two waves, opposite ways",
         "<p>Identical waves travelling towards each other superpose into a pattern that does "
         "not travel. The energy stays put, oscillating between two stores.</p>", "THE IDEA")
    st.markdown("\n\n".join(f"**{p['point']}** — {p['detail']}"
                            for p in D.STANDING_WAVE_POINTS))

    l_col, m_col = st.columns(2)
    with l_col:
        L = st.number_input("length (m)", 0.01, 20.0, 1.0, 0.05, key=f"{P}sl")
    with m_col:
        mode = st.slider("mode n", 1, 8, 3, 1, key=f"{P}sm")
    st.markdown(VIS.stationary_bench(L, mode), unsafe_allow_html=True)
    pattern = W.node_positions(L, mode)
    st.dataframe(pd.DataFrame([
        {"quantity": "nodes", "value": f"{len(pattern['nodes'])} at "
                                     + ", ".join(f"{x:.4g}" for x in pattern["nodes"])},
        {"quantity": "antinodes", "value": f"{len(pattern['antinodes'])} at "
                                            + ", ".join(f"{x:.4g}" for x in pattern["antinodes"])},
        {"quantity": "half-wavelength segments", "value": f"{pattern['segments']}"},
        {"quantity": "node definition", "value": pattern["node_definition"]},
        {"quantity": "antinode definition", "value": pattern["antinode_definition"]},
    ]), use_container_width=True, hide_index=True)

    st.subheader("Strings and air columns")
    st.markdown(VIS.pipe_bench(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"column": c["column"], "end condition": c["end condition"],
         "f_n": c["f_n"], "allowed": c["allowed"], "note": c["note"]}
        for c in D.COLUMN_RULES
    ]), use_container_width=True, hide_index=True)

    v_col, count_col, kind_col = st.columns(3)
    with v_col:
        speed = st.number_input("wave speed (m s⁻¹)", 1.0, 1e5, 340.0, 10.0, key=f"{P}sv")
    with count_col:
        n = st.slider("how many harmonics", 1, 8, 5, 1, key=f"{P}sn")
    with kind_col:
        kind = st.selectbox("column type", ["closed", "open"], key=f"{P}sk")
    harmonics = (W.pipe_harmonics(L, kind, speed, n) if kind == "closed"
                 else W.pipe_harmonics(L, "open", speed, n))
    st.dataframe(pd.DataFrame([
        {"n": h["n"], "mode": h["mode"], "frequency (Hz)": f"{h['f']:.4g}",
         "lambda (m)": f"{h['lambda']:.4g}"} for h in harmonics
    ]), use_container_width=True, hide_index=True)
    if kind == "closed":
        st.warning("Only the odd harmonics exist in a closed column — that is why a stopped "
                   "pipe sounds an octave below and noticeably hollow.")
    strings = W.string_harmonics(L, speed, n)
    st.dataframe(pd.DataFrame([
        {"n": s["n"], "frequency (Hz)": f"{s['f']:.4g}", "lambda (m)": f"{s['lambda']:.4g}"}
        for s in strings
    ]), use_container_width=True, hide_index=True)
    guidance(EXAM_TIP, "Count half wavelengths, and count the end condition first",
             "A node at each end means the length holds a whole number of half wavelengths: "
             "f = nv/2L. A node at one end and an antinode at the other means a whole number "
             "of quarter wavelengths: f = (2n−1)v/4L. Get the end condition right and the "
             "arithmetic almost writes itself.")


def _doppler() -> None:
    how_to("numbers"),
    st.subheader("8.5.1, 8.5.2 & 8.5.3 · The Doppler effect")
    card("It is a wavelength argument, not a speed argument",
         "<p>A moving source crams its wavefronts together in front and spreads them out "
         "behind. The medium's speed never changes — the spacing the observer meets does.</p>",
         "THE IDEA")
    st.dataframe(pd.DataFrame([
        {"case": r["case"], "situation": r["title"], "formula": r["formula"],
         "signs": r["sign"], "what changes": r["picture"]} for r in D.DOPPLER_SUMMARY
    ]), use_container_width=True, hide_index=True)

    f_col, v_col = st.columns(2)
    with f_col:
        f = st.number_input("emitted frequency f (Hz)", 1.0, 20000.0, 440.0, 1.0, key=f"{P}df")
    with v_col:
        speed = st.number_input("speed of the wave v (m s⁻¹)", 1.0, 3e8, 340.0, 1.0,
                                key=f"{P}dv")
    case = st.selectbox("Which case?", ["a", "b", "c", "d"], key=f"{P}dc")
    so_col, oo_col = st.columns(2)
    with so_col:
        v_s = st.number_input("source speed vₛ (m s⁻¹)", -500.0, 500.0, 0.0, 5.0, key=f"{P}ds")
    with oo_col:
        v_o = st.number_input("observer speed v₀ (m s⁻¹)", -500.0, 500.0, 0.0, 5.0, key=f"{P}do")
    st.markdown(VIS.doppler_explorer(f, speed, abs(v_o), abs(v_s), case), unsafe_allow_html=True)

    result = W.doppler(f, speed, abs(v_o), abs(v_s), case)
    st.latex(f"f' = {result:.4g}\\,\\text{{Hz}}")
    st.dataframe(pd.DataFrame([
        {"quantity": "emitted f", "value": f"{f:.4g} Hz"},
        {"quantity": "apparent f'", "value": f"{result:.4g} Hz"},
        {"quantity": "shift", "value": f"{result - f:+.4g} Hz"},
        {"quantity": "percentage", "value": f"{100 * (result / f - 1):+.3g} %"},
        {"quantity": "verdict", "value": W.doppler_shift(f, result)["verdict"]},
    ]), use_container_width=True, hide_index=True)
    if abs(W.doppler(f, speed, 0.0, 0.0, case) - f) < 1e-9:
        st.success("Sanity check passed: with both speeds zero the formula returns f exactly, "
                   "so the signs are consistent.")
    else:
        st.error("The formula does not return f when nothing is moving — the signs are wrong.")
    if result > f:
        st.success("Rising pitch: the source and observer are closing the gap.")
    elif result < f:
        st.info("Falling pitch: they are separating.")
    guidance(EXAM_TIP, "Two checks, five seconds each",
             "Set v₀ = vₛ = 0 and confirm f′ = f. Then confirm that an approaching pair gives "
             "a frequency *above* f. Between them they catch almost every sign error in this "
             "topic.")


def _lightshift() -> None:
    how_to("sliders"),
    st.subheader("8.5.4 & 8.5.5 · Doppler in light, and its applications")
    lam = st.slider("observed wavelength (nm)", 380.0, 750.0, 620.0, 1.0, key=f"{P}slx")
    st.markdown(VIS.spectrum_shift(lam * 1e-9), unsafe_allow_html=True)
    st.markdown(VIS.round_trip(30.0), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"application": a["application"], "how it works": a["how"],
         "why it works": a["why_it_works"]} for a in D.DOPPLER_APPLICATIONS
    ]), use_container_width=True, hide_index=True)
    st.latex(r"f' = f\frac{v + v_o}{v - v_s}")
    st.caption("The same four relations apply to light, because they depend only on the wave "
               "picture and not on sound specifically. Only the value of v changes — to "
               "3 × 10⁸ m s⁻¹, which makes the ordinary shifts immeasurably small except "
               "for astronomical distances.")
    guidance(HONEST_LIMIT, "Why light shifts are so tiny at everyday speeds",
             "Because the speed of light is so enormous, a pedestrian moving at 1.5 m s⁻¹ "
             "shifts visible light by about 1.5 parts in 10⁶ — undetectable without "
             "interferometry. It is the enormous distances of astronomy that make redshift "
             "measurable at all.")


def _modern() -> None:
    st.subheader("8.6.1 · Waves in the modern world")
    card("Name the wave property, and the application explains itself",
         "<p>Every modern use of waves exploits exactly one property — reflection, time of "
         "flight, focusing, or the way speed depends on the medium.</p>", "THE METHOD")
    st.dataframe(pd.DataFrame([
        {"field": r["field"], "wave": r["wave"], "property exploited": r["property used"],
         "detail": r["detail"]} for r in D.MODERN_USES_TABLE
    ]), use_container_width=True, hide_index=True)
    for row in D.MODERN_USES_TABLE:
        with st.expander(row["field"]):
            st.markdown(f"**Wave.** {row['wave']}\n\n"
                        f"**Property used.** {row['property used']}\n\n"
                        f"{row['detail']}")
    guidance(WATCH_OUT, "S-waves cannot travel through liquid",
             "That single fact proved that the outer core of the Earth is liquid. Since "
             "seismic stations worldwide continued to receive S-waves, whatever the wave was "
             "travelling through had to be able to support a transverse vibration.")


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "progressive": _progressive,
    "intensity": _intensity,
    "waveequation": _waveequation,
    "types": _types,
    "superposition": _superposition,
    "beats": _beats,
    "stationary": _stationary,
    "doppler": _doppler,
    "lightshift": _lightshift,
    "modern": _modern,
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
    title="Waves",
    blurb="Wave motion and energy, superposition, beats, stationary waves and the Doppler effect.",
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