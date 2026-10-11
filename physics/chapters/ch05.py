"""Chapter 5 interface: Deformation in Solids.

The chapter's own centrepiece is the **stress–strain tester**: pick a material,
set the sample's cross-section and the load, and a full curve — with the slope
triangle, the elastic limit and the fracture point — is recomputed from scratch.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..visuals.common import freeze
from ..core import solids as S
from ..engine import (how_to, ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT, practicals,
                      WHY_IT_MATTERS,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, VIOLET, card
from ..visuals import ch05 as VIS
from . import ch05_data as D

_N = 5
P = f"c{_N}_"


def _tester() -> None:
    """The stress-strain tester: a real curve from your controls."""
    st.caption("Choose a material and a sample. Every number and the whole curve are "
               "recomputed from these controls — nothing is stored.")

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        material = st.selectbox("material", [m["name"] for m in S.MATERIALS],
                                key=f"{P}mat")
    spec = next(m for m in S.MATERIALS if m["name"] == material)
    with m2:
        length = st.number_input("length L (m)", 0.01, 10.0, 1.0, 0.05, key=f"{P}len")
    with m3:
        area_mm2 = st.number_input("cross-section (mm²)", 0.01, 5000.0, 1.0, 0.5,
                                   key=f"{P}area",
                                   help="A hair-thin wire is around 0.05 mm²; a girder is millions.")
    with m4:
        force = st.number_input("load F (N)", 0.0, 1e5, 50.0, 5.0, key=f"{P}force")

    area = area_mm2 * 1e-6
    curve = S.stress_strain_series(spec)

    stress_now = S.stress(force, area)
    strain_now = stress_now / spec["youngs_modulus"] if spec["youngs_modulus"] else 0.0
    extension = strain_now * length
    in_elastic = strain_now <= curve["elastic_strain"]
    brittle_broken = curve["brittle"] and strain_now >= curve["fracture_strain"]

    left, right = st.columns([3, 2])
    with left:
        st.markdown(VIS.stress_strain_curve(freeze(curve)), unsafe_allow_html=True)
    with right:
        if brittle_broken:
            st.error("**This sample has fractured.** The material is brittle, so it snaps "
                     "while still on the straight elastic line.")
        elif not in_elastic:
            st.warning(f"**Past the elastic limit.** The strain is {strain_now:.3g}, above "
                       f"the elastic strain of {curve['elastic_strain']:.3g}. This sample will "
                       f"**not** return to its original length.")
        else:
            st.success("**Within the elastic region.** Remove the load and this sample returns "
                       "exactly to its original length.")
        st.dataframe(pd.DataFrame([
            {"quantity": "stress σ = F/A", "value": f"{stress_now:.4g} Pa"},
            {"quantity": "strain ε = σ/Y", "value": f"{strain_now:.4g}"},
            {"quantity": "extension ΔL = εL", "value": f"{extension:.4g} m"},
            {"quantity": "Young's modulus Y", "value": f"{spec['youngs_modulus']:.3g} Pa"},
            {"quantity": "elastic strain σ/Y", "value": f"{curve['elastic_strain']:.3g}"},
            {"quantity": "stored energy ½FΔL", "value": f"{0.5 * force * extension:.4g} J"},
        ]), use_container_width=True, hide_index=True)
        if not in_elastic and not brittle_broken:
            st.caption("Past the elastic limit the stress–strain relation is no longer "
                       "σ/Y, so the extension shown is the Hooke's-law extrapolation, not the "
                       "real one.")

    st.markdown(VIS.wire_comparison(freeze(
        [{"name": m["name"], "modulus": m["youngs_modulus"]} for m in S.MATERIALS])),
        unsafe_allow_html=True)


def _bounce() -> None:
    """A bouncing mass, with the energy budget followed at every point."""
    st.caption("Drop a mass on a spring and watch the budget change between the three "
               "places energy can be: kinetic, elastic, and lost to damping.")

    c1, c2, c3 = st.columns(3)
    with c1:
        mass = st.number_input("mass m (kg)", 0.05, 5.0, 0.5, 0.05, key=f"{P}bm")
    with c2:
        k = st.number_input("spring constant k (N/m)", 10.0, 5000.0, 400.0, 10.0, key=f"{P}bk")
    with c3:
        drop = st.number_input("drop height (m)", 0.05, 3.0, 0.5, 0.05, key=f"{P}bh")

    gravity = mass * 9.8 * drop
    max_ext = math.sqrt(2 * gravity / k)
    stored = 0.5 * k * max_ext ** 2

    metric1, metric2, metric3 = st.columns(3)
    metric1.metric("Energy at release", f"{gravity:.3g} J")
    metric2.metric("Maximum compression", f"{max_ext * 100:.1f} cm")
    metric3.metric("Max elastic energy", f"{stored:.3g} J")

    n = 140
    step = max_ext / n
    xs = [i * step for i in range(n + 1)]
    energy = [0.5 * k * x * x for x in xs]
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'ENERGY STORED AS THE SPRING COMPRESSES</text>']
    left, bottom, right, top = 74, 320, 620, 48
    peak = max(energy) or 1.0
    for index, (x, e) in enumerate(zip(xs, energy)):
        px = left + (x / (max_ext or 1)) * (right - left)
        py = bottom - (e / peak) * (bottom - top)
        bar = max(2, int(2 + 26 * (e / peak)))
        colour = VIOLET if index > n * 0.55 else CYAN
        parts.append(f'<rect x="{px - bar / 2:.1f}" y="{py:.1f}" width="{bar}" '
                     f'height="{bottom - py:.1f}" fill="{colour}" opacity="0.8"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{right + 6}" y2="{bottom}" '
                 f'stroke="{MUTED}" stroke-width="2"/>')
    parts.append(f'<text x="{right + 10}" y="{bottom + 4}" fill="{MUTED}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">x</text>')
    parts.append(f'<text x="{left}" y="{top - 10}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">½kx² (J)</text>')
    parts.append(f'<text x="{left}" y="{bottom + 26}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">A mass falling h stores mg·h at maximum '
                 f'compression — the bar chart never exceeds {gravity:.3g} J, whatever k '
                 f'is.</text>')
    st.markdown(f'<svg viewBox="0 0 660 360" width="100%" '
                f'style="max-width:660px;display:block;margin:0 auto">'
                f'{"".join(parts)}</svg>', unsafe_allow_html=True)

    if k < mass * 9.8 / drop:
        st.caption("A softer spring simply compresses further to store the same energy. "
                   "That is why a trampoline is bouncy and a concrete floor is not.")


def _types() -> None:
    st.subheader("5.1 · Types of solids")
    card("The question that separates them",
         "<p>Ask whether the atoms sit in a pattern that <em>repeats</em> over long "
         "distances. If they do, the solid is crystalline; if not, it is amorphous; "
         "and if they are strung into very long chains, it is polymeric.</p>", "THE TEST")
    st.markdown(VIS.solid_types(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"class": r["class"], "order": r["order"], "melting behaviour": r["behaviour"],
         "examples": r["examples"]} for r in S.SOLID_CLASSES
    ]), use_container_width=True, hide_index=True)
    for row in S.SOLID_CLASSES:
        with st.expander(f"Why {row['class'].lower()} solids behave that way"):
            st.markdown(row["example"])
    guidance(TRY_IT, "Sugar cubes, salt and glass",
             "Candy sugar and table salt are crystalline and melt sharply. A pane of glass "
             "is amorphous and softens over a wide range — which is exactly why medieval "
             "panes are thicker at the bottom.")


def _deformation() -> None:
    how_to("numbers"),
    st.subheader("5.2 · Deformation in one dimension")
    card("Length change is a ratio, not a force",
         "<p>Strain = ΔL / L. Doubling the length doubles the extension; doubling the "
         "area halves the stress and therefore the strain. This single relationship, "
         "ΔL = FL/(AY), carries the whole station.</p>", "THE IDEA")
    st.markdown(VIS.deformation_kinds(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"symbol": row["symbol"], "means": row["means"], "unit": row["unit"]}
        for row in D.SYMBOL_TABLE
    ]), use_container_width=True, hide_index=True)

    st.subheader("Your own wire")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        L = st.number_input("L (m)", 0.1, 20.0, 2.0, 0.1, key=f"{P}dl")
    with c2:
        d = st.number_input("diameter d (mm)", 0.01, 50.0, 0.50, 0.05, key=f"{P}dd")
    with c3:
        F = st.number_input("F (N)", 0.0, 1e4, 25.0, 5.0, key=f"{P}dF")
    with c4:
        Y = st.selectbox("material", [m["name"] for m in S.MATERIALS], key=f"{P}dmat")

    spec = next(m for m in S.MATERIALS if m["name"] == Y)
    area = math.pi * (d * 1e-3 / 2) ** 2
    ext = S.length_change(F, L, area, spec["youngs_modulus"])
    st.dataframe(pd.DataFrame([
        {"step": "A = πd²/4", "value": f"{area:.4g} m²"},
        {"step": "stress F/A", "value": f"{S.stress(F, area):.4g} Pa"},
        {"step": "strain σ/Y", "value": f"{S.strain(ext, L):.4g}"},
        {"step": "extension ΔL = FL/(AY)", "value": f"{ext:.4g} m"},
        {"step": "as a percentage of L", "value": f"{100 * S.strain(ext, L):.4g} %"},
    ]), use_container_width=True, hide_index=True)
    guidance(WATCH_OUT, "Metres, not millimetres",
             "The formula needs A in m² and Y in Pa. A diameter in mm used directly gives "
             "an area a million times too large and an extension a million times too small.")


def _elastic() -> None:
    how_to("sliders"),
    st.subheader("5.3 · Elastic and plastic deformation")
    st.markdown(VIS.load_unload_trace(
        st.slider("how far do you stretch it?", 0.05, 1.0, 0.75, 0.05, key=f"{P}lu"),
        elastic_limit=0.28, yield_point=0.35), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"region": r["name"], "behaviour": r["behaviour"], "on release": r["on_returning"],
         "microstructure": r["micro"]} for r in D.REGIONS
    ]), use_container_width=True, hide_index=True)
    for row in D.REGIONS:
        with st.expander(row["name"]):
            st.markdown(f"**Behaviour.** {row['behaviour']}\n\n"
                        f"**On release.** {row['on_returning']}\n\n"
                        f"**On the graph.** {row['slopes']}\n\n"
                        f"**What is happening.** {row['micro']}")


def _stress() -> None:
    st.subheader("5.4 · Stress, strain and Young's modulus")
    st.latex(r"\sigma = \frac{F}{A}, \qquad \varepsilon = \frac{\Delta L}{L}, "
             r"\qquad Y = \frac{\sigma}{\varepsilon}")
    card("Three definitions, one graph",
         "<p>Put strain across the bottom and stress up the side, and the straight "
         "initial region has a gradient of exactly Y. Young's modulus is not a separate "
         "fact — it is the slope of the part of the curve you have already drawn.</p>",
         "THE IDEA")
    _tester()
    st.subheader("Everyday objects, explained")
    st.dataframe(pd.DataFrame([
        {"object": r["object"], "explanation": r["explanation"]} for r in D.DAILY_LIFE
    ]), use_container_width=True, hide_index=True)


def _energy() -> None:
    how_to("numbers"),
    st.subheader("5.5 · Elastic potential energy")
    st.latex(r"E = \tfrac{1}{2} F x = \tfrac{1}{2} k x^2")
    card("It is just an area",
         "<p>The force rises linearly from zero, so the graph is a straight line and the "
         "area under it is a triangle: ½ × base × height = ½Fx. Hooke's law, F = kx, turns "
         "that into ½kx². Nothing else is happening.</p>", "THE IDEA")

    f_col, x_col = st.columns(2)
    with f_col:
        fmax = st.number_input("maximum force F (N)", 0.0, 1000.0, 60.0, 5.0, key=f"{P}ef")
    with x_col:
        xmax = st.number_input("extension x (m)", 0.0, 2.0, 0.25, 0.01, key=f"{P}ex")
    k = fmax / xmax if xmax else 0.0
    st.markdown(VIS.energy_triangle(fmax, xmax), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"form": "E = ½Fx", "value": f"{S.elastic_energy_from_force(fmax, xmax):.4g} J"},
        {"form": "E = ½kx²", "value": f"{S.elastic_energy_from_k(k, xmax):.4g} J"},
        {"form": "energy density ½σε",
         "value": f"{S.energy_density(fmax, 0.5 * k * xmax):.4g} J m⁻³"},
        {"form": "implied k = F/x", "value": f"{k:.4g} N m⁻¹"},
        {"form": "average force", "value": f"{fmax / 2:.4g} N"},
    ]), use_container_width=True, hide_index=True)
    st.subheader("A bouncing mass")
    _bounce()
    guidance(EXAM_TIP, "Energy density is what actually decides the winner",
             "½σε = σ²/(2Y), so for the same working stress a material stores energy in "
             "inverse proportion to its modulus. Steel is strong and stiff and therefore "
             "stores very little; rubber stores thousands of times more per cubic metre.")


def _curve() -> None:
    how_to("numbers"),
    """5.4.2 and 5.4.3 - reading a force-extension graph and using Young's modulus."""
    st.subheader("5.4.2 & 5.4.3 · Reading the curve, and Young's modulus")
    st.latex(r"Y = \frac{\text{stress}}{\text{strain}}"
             r" = \frac{F/A}{\Delta L/L}")
    st.info("**How to use this:** the graph is drawn for the metal you pick. The straight "
            "section is the elastic region, where the gradient is Young's modulus. Drag the "
            "load and watch where the curve stops being a straight line.")
    st.markdown(VIS.load_extension_curve(), unsafe_allow_html=True)
    st.markdown("\n\n".join(f"**{b['region']}** — {b['meaning']}" for b in D.CURVE_REGIONS))

    c1, c2, c3 = st.columns(3)
    with c1:
        force = st.number_input("load F (N)", 0.0, 500.0, 120.0, 10.0, key=f"{P}5f")
    with c2:
        area = st.number_input("area A (mm²)", 0.01, 100.0, 4.0, 0.5, key=f"{P}5a")
    with c3:
        length = st.number_input("length L (m)", 0.01, 10.0, 2.0, 0.1, key=f"{P}5l")
    ext = st.number_input("measured extension ΔL (mm)", 0.0, 50.0, 0.50, 0.05, key=f"{P}5e")
    stress = force / (area * 1e-6)
    strain = (ext * 1e-3) / length
    sig = f"\\sigma = \\frac{{{force:g}}}{{{area * 1e-6:.3g}}} = {stress:.4g}"
    eps = f"\\varepsilon = \\frac{{{ext * 1e-3:.3g}}}{{{length:g}}} = {strain:.4g}"
    you = f"\\frac{{\\sigma}}{{\\varepsilon}} = {stress / strain:.5g}"
    st.latex(sig + "\\ \\mathrm{Pa}")
    st.latex(eps)
    st.latex("Y = " + you + "\\ \\mathrm{Pa}")
    st.caption("Convert the millimetres to metres before you divide. That single conversion "
               "is where almost every mark is lost in this topic.")
    guidance(EXAM_TIP, "The gradient of the straight part is Young's modulus",
             "On this graph the steep straight section and the shallow curved section have "
             "the same axes but completely different gradients. Only the straight one is "
             "Young's modulus.")


def _objects() -> None:
    """5.4.4 - stress, strain and Young's modulus in everyday objects."""
    st.subheader("5.4.4 · Stress and strain around you")
    st.write("Every solid you touch is doing one of three things: resisting a load elastically, "
             "deforming permanently, or breaking. Naming which is the whole of this outcome.")
    st.dataframe(pd.DataFrame([
        {"object": o["object"], "what happens": o["what"],
         "property exploited": o["property"]} for o in D.DAILY_OBJECTS
    ]), use_container_width=True, hide_index=True)
    for item in D.DAILY_OBJECTS:
        with st.expander(item["object"]):
            st.markdown(f"**What happens.** {item['what']}\n\n"
                        f"**Property exploited.** {item['property']}\n\n{item['explain']}")
    st.markdown("\n\n".join(f"**{c['concept']}** — {c['meaning']}"
                            for c in D.DAILY_CONCEPTS))
    guidance(WHY_IT_MATTERS, "Engineers design with these numbers",
             "A bridge cable is allowed to be strained enough to show it is working. A "
             "pressure vessel is designed to fail at twice its working pressure. Neither is "
             "accidental: both are statements about stress, strain and Young's modulus.")


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "types": _types,
    "deformation": _deformation,
    "elastic": _elastic,
    "curve": _curve,
    "objects": _objects,
    "stress": _stress,
    "energy": _energy,
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
    title="Deformation in Solids",
    blurb="Types of solids, elastic and plastic deformation, stress, strain and Young's modulus.",
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
