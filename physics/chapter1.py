"""Chapter 1 - Physical Quantities and Measurement.

The four teaching stations in this module - units and quantities, dimensions,
accuracy and precision, and uncertainty - are written by hand for Chapter 1.
The chapter shell itself (the tab bar, the outcome strip, worked problems,
practice, the tutor and the exit report) comes from :mod:`physics.engine`, so
that Chapter 1 and the nine chapters after it behave identically at the edges
while sharing nothing in the middle.
"""

from __future__ import annotations

import random

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from . import ai_tutor
from . import data as D
from .chapters import ch01_data as D_META
from . import physics_core as pc
from . import progress as P
from . import visuals as V
from .engine import (table, ChapterSpec, Station, HONEST_LIMIT, WATCH_OUT, EXAM_TIP,
                     guidance, overview_station, practice, references,
                     worked_problems)
from .theme import (AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET,
                    card, metric_row, pill, section_intro, style_fig)

_N = 1

# Which learning outcomes each station teaches. The single source of truth is
# ``chapters.ch01_data.STATIONS``, so this table and the curriculum tests can
# never drift apart.
from .chapters.ch01_data import STATIONS as _STATION_TABLE

STATION_SLOS = {row["key"]: row["slos"] for row in _STATION_TABLE}

def _quantities_and_units():
    st.subheader("1 · Physical quantities: magnitude and unit")
    card(
        "A number alone is not a measurement",
        "A physical quantity is fully described only when we state a numerical magnitude "
        "<em>and</em> a unit. Writing “the length is 5” is incomplete: 5 mm, 5 cm, 5 m and "
        "5 km are very different lengths. The unit gives meaning to the number.",
        "1.1.1",
    )

    st.markdown("##### Magnitude-and-unit builder")
    st.caption("Choose a quantity, set a magnitude, then read off the complete physical quantity.")
    builder = {
        "Length of a room": ("m", 6, 1, 20, "m"),
        "Mass of an apple": ("g", 150, 10, 500, "g"),
        "Time of a race": ("s", 12, 1, 120, "s"),
        "Speed of a car": ("m/s", 25, 1, 60, "m s⁻¹"),
        "Temperature of a room": ("K", 295, 200, 400, "K"),
    }
    choice = st.selectbox("Quantity", list(builder.keys()), key="qb_choice")
    unit_name, default, lo, hi, unit = builder[choice]
    magnitude = st.slider("Numerical magnitude", int(lo), int(hi), int(default), key="qb_mag")
    st.markdown(
        f'<div class="atlas-card"><div class="kicker">COMPLETE PHYSICAL QUANTITY</div>'
        f'<h2 style="color:#5eead4">{magnitude} <span style="color:#e2e8f0">{unit}</span></h2>'
        f"<div class='body'>The magnitude is <b>{magnitude}</b> and the unit is <b>{unit}</b>. "
        f"Changing either one changes the quantity. This is why “{magnitude}” by itself "
        f"cannot describe {choice.lower()}.</div></div>",
        unsafe_allow_html=True,
    )

    with st.expander("Why would a number without a unit be ambiguous?"):
        st.markdown(
            "Suppose someone writes only **“the length is 5”**. Depending on the unit, "
            "that could be:"
        )
        st.markdown(V.ambiguity_bars(), unsafe_allow_html=True)
        demo = pd.DataFrame([
            ["5 mm", 0.005, "a tiny screw"],
            ["5 cm", 0.05, "a short pen"],
            ["5 m", 5.0, "a classroom"],
            ["5 km", 5000.0, "a short drive"],
        ], columns=["If the unit were", "Length in metres", "Roughly the size of"])
        table(demo, use_container_width=True, hide_index=True)
        st.info("The same number describes lengths that differ by a factor of 1 000 000. "
                "The unit is not decoration — it carries the meaning.")

    st.divider()
    st.subheader("2 · Choosing appropriate values")
    card(
        "A sensible estimate is a skill",
        "For everyday and scientific work we choose a unit that keeps the number readable. "
        "Estimates are based on reasoning and experience; measured values come from an "
        "instrument. Keep the two ideas separate.",
        "1.1.2",
    )
    scenario = st.selectbox("Pick a situation", [s["thing"] for s in D.APPROPRIATE_VALUES], key="av_scen")
    scenario_data = next(s for s in D.APPROPRIATE_VALUES if s["thing"] == scenario)
    pick = st.radio("Which unit is most appropriate?", scenario_data["options"],
                    key="av_unit", index=None, horizontal=True)
    if pick is None:
        st.caption("Choose a unit to see the reasoning.")
    elif pick == scenario_data["answer"]:
        st.success(f"Best choice: {pick}. {scenario_data['reason']} "
                   f"Sensible value: {scenario_data['value']}.")
    else:
        st.warning(
            f"{pick} is not the most convenient here. {scenario_data['reason']} "
            f"The best choice for this situation is {scenario_data['answer']} "
            f"({scenario_data['value']})."
        )
    st.caption("Estimates like these are order-of-magnitude judgements, not measurements. "
               "A measured value would come from an instrument and would carry an uncertainty.")

    st.divider()
    st.subheader("3 · SI base quantities and units")
    card(
        "Only seven quantities are fundamental",
        "The SI system defines seven base quantities, each with its own base unit. "
        "Everything else in physics is built from these seven. The definitions follow the "
        "BIPM SI Brochure (9th edition).",
        "1.1.3",
    )
    st.markdown(V.si_wheel(), unsafe_allow_html=True)
    base_frame = pd.DataFrame([
        {"Base quantity": r["quantity"], "SI unit": r["unit"],
         "Symbol": r["symbol"], "Dimension": pc.dim_unicode(r["dims"]),
         "Everyday example": r["example"]}
        for r in D.SI_BASE_QUANTITIES
    ])
    table(base_frame, use_container_width=True, hide_index=True)

    st.markdown("##### Quick check: base or not?")
    base_names = {r["quantity"] for r in D.SI_BASE_QUANTITIES}
    probe = st.selectbox(
        "Is this quantity an SI base quantity?",
        ["Length", "Force", "Time", "Electric current", "Energy", "Amount of substance"],
        key="base_probe",
    )
    if probe in base_names:
        st.success(f"{probe} is one of the seven SI base quantities.")
    else:
        st.warning(f"{probe} is a derived quantity — it is built from base quantities. "
                   "The seven base quantities are length, mass, time, electric current, "
                   "thermodynamic temperature, amount of substance and luminous intensity.")

    st.markdown("##### SI prefixes (multiples and submultiples)")
    prefix_frame = pd.DataFrame([
        {"Prefix": p["name"], "Symbol": p["symbol"], "Factor": p["power"]}
        for p in D.SI_PREFIXES
    ])
    table(prefix_frame, use_container_width=True, hide_index=True, height=250)

    st.divider()
    st.subheader("4 · Derived quantities and derived units")
    card(
        "Products and quotients of base units",
        "Derived units are formed by multiplying or dividing SI base units. Some are given "
        "special names (newton, joule, pascal, watt) to keep writing simple, but each can always "
        "be written in base units. Choose a quantity to see how its unit is built.",
        "1.1.4",
    )
    names = [q["name"] for q in D.DERIVED_QUANTITIES]
    chosen_name = st.selectbox("Select a derived quantity", names, key="dqe")
    q = next(item for item in D.DERIVED_QUANTITIES if item["name"] == chosen_name)
    c1, c2 = st.columns([3, 2])
    with c1:
        card(
            f"{q['name']} — {q['symbol']}",
            f"<p>Defined as: {q['definition']}</p>"
            f"<p>Dimension: {pc.dim_unicode(q['dims'])}</p>"
            f"<p>SI unit: <b>{q['unit_symbol']}</b> ({q['unit']})</p>",
            q["category"].upper(),
        )
        for i, step in enumerate(q["steps"], start=1):
            st.markdown(f"**Step {i}.** {step}")
    with c2:
        st.markdown(
            f'<div class="atlas-card"><div class="kicker">BASE-UNIT BUILD</div>'
            f"<h3>{q['symbol']} → {q['unit_symbol']}</h3>"
            f"<div class='body'>Every derived unit can be reduced to the seven base units. "
            f"The dimensional expression {pc.dim_unicode(q['dims'])} is the recipe.</div></div>",
            unsafe_allow_html=True,
        )
        st.latex(_base_latex(q))
        st.markdown(_unit_blocks(q["unit_symbol"]), unsafe_allow_html=True)

    with st.expander("Unit conversion practice (with worked reasoning)"):
        st.markdown("**Example:** convert 90 km h⁻¹ to m s⁻¹.")
        st.latex(r"90 \times \frac{1000\ \text{m}}{3600\ \text{s}} = 25\ \text{m s}^{-1}")
        st.markdown("**Example:** convert 2.0 g cm⁻³ to kg m⁻³.")
        st.latex(r"2.0\ \frac{\text{g}}{\text{cm}^3} \times \frac{10^{-3}\ \text{kg}}{10^{-6}\ \text{m}^3}"
                 r"= 2000\ \text{kg m}^{-3}")
        st.caption("Areas and volumes scale with the square and cube of the length factor, "
                   "which is a common source of mistakes.")


def _unit_blocks(unit_symbol: str) -> str:
    """Turn a base-unit string such as 'kg m s⁻²' into a block diagram."""
    roles = {
        "kg": "mass", "g": "mass", "m": "length", "m²": "length²", "m³": "length³",
        "s": "time", "s⁻¹": "per time", "s⁻²": "per time²", "s⁻³": "per time³",
        "A": "current", "A⁻¹": "per current", "A⁻²": "per current²",
        "K": "temperature", "mol": "amount", "cd": "luminous",
    }
    core = unit_symbol.split("=")[-1].strip()
    tokens = [t for t in core.replace("·", " ").split() if t in roles]
    if not tokens:
        tokens = [core] if core else ["—"]
    parts = [(token, roles.get(token, "base unit")) for token in tokens]
    return V.unit_blocks(unit_symbol, tuple(parts))


def _base_latex(quantity):
    mapping = {
        "m²": r"\text{m}^2",
        "m³": r"\text{m}^3",
        "m s⁻¹": r"\text{m}\,\text{s}^{-1}",
        "m s⁻²": r"\text{m}\,\text{s}^{-2}",
        "N = kg m s⁻²": r"\text{N} = \text{kg}\,\text{m}\,\text{s}^{-2}",
        "kg m s⁻¹": r"\text{kg}\,\text{m}\,\text{s}^{-1}",
        "J = kg m² s⁻²": r"\text{J} = \text{kg}\,\text{m}^2\,\text{s}^{-2}",
        "W = kg m² s⁻³": r"\text{W} = \text{kg}\,\text{m}^2\,\text{s}^{-3}",
        "Pa = kg m⁻¹ s⁻²": r"\text{Pa} = \text{kg}\,\text{m}^{-1}\,\text{s}^{-2}",
        "kg m⁻³": r"\text{kg}\,\text{m}^{-3}",
        "Hz = s⁻¹": r"\text{Hz} = \text{s}^{-1}",
        "C = A s": r"\text{C} = \text{A}\,\text{s}",
        "V = kg m² s⁻³ A⁻¹": r"\text{V} = \text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-1}",
        "Ω = kg m² s⁻³ A⁻²": r"\Omega = \text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-2}",
    }
    return mapping.get(quantity["unit_symbol"], quantity["unit_symbol"])


def _dimensions():
    st.subheader("1 · The concept of dimensions")
    card(
        "Dimensions describe physical nature, not size",
        "A dimension tells you what kind of quantity something is, independent of the unit used "
        "to measure it. The fundamental dimensions of mechanics are <b>M</b> (mass), <b>L</b> "
        "(length) and <b>T</b> (time). A speed is always [L T⁻¹] whether you measure it in m s⁻¹ "
        "or km h⁻¹.",
        "1.2.1",
    )

    st.subheader("2 · Quantities in terms of dimensions")
    dim_rows = [
        ("Displacement", r"[L]", pc.dims(L=1)),
        ("Area", r"[L²]", pc.dims(L=2)),
        ("Volume", r"[L³]", pc.dims(L=3)),
        ("Speed", r"[L T⁻¹]", pc.dims(L=1, T=-1)),
        ("Acceleration", r"[L T⁻²]", pc.dims(L=1, T=-2)),
        ("Force", r"[M L T⁻²]", pc.dims(M=1, L=1, T=-2)),
        ("Momentum", r"[M L T⁻¹]", pc.dims(M=1, L=1, T=-1)),
        ("Work or energy", r"[M L² T⁻²]", pc.dims(M=1, L=2, T=-2)),
        ("Pressure", r"[M L⁻¹ T⁻²]", pc.dims(M=1, L=-1, T=-2)),
        ("Density", r"[M L⁻³]", pc.dims(M=1, L=-3)),
    ]
    table(
        pd.DataFrame([{"Quantity": name, "Dimensions": text} for name, text, _ in dim_rows]),
        use_container_width=True, hide_index=True,
    )

    st.markdown("##### Dimensional-analysis tool")
    st.caption("Select a quantity to see how its dimensions are obtained step by step.")
    analysable = D.DERIVED_QUANTITIES + [
        {"name": "Displacement", "symbol": "s", "dims": pc.dims(L=1),
         "unit_symbol": "m", "steps": ["Displacement is a length.", "[s] = [L]"]},
    ]
    pick = st.selectbox("Quantity", [a["name"] for a in analysable], key="dat_pick")
    item = next(a for a in analysable if a["name"] == pick)
    card(f"{item['name']} — {item.get('symbol','')}",
         f"<p>Dimensions: <b>{pc.dim_unicode(item['dims'])}</b></p>"
         f"<p>Unit: {item.get('unit_symbol','')}</p>",
         "DIMENSION RESULT")
    for i, step in enumerate(item["steps"], start=1):
        st.markdown(f"**Step {i}.** {step}")

    st.divider()
    st.subheader("3 · Homogeneity of physical equations")
    card(
        "Both sides must speak the same language",
        "An equation is dimensionally homogeneous when every term added or subtracted has the "
        "same dimensions, and both sides agree. Homogeneity is necessary but not sufficient: a "
        "homogeneous equation can still be physically wrong, because dimensions cannot detect a "
        "missing dimensionless factor such as 2π or ½.",
        "1.2.3 · 1.1.5",
    )
    titles = [e["title"] for e in D.HOMOGENEITY_EXAMPLES]
    chosen = st.selectbox("Choose an example to test", titles, key="hmg_pick")
    ex = next(e for e in D.HOMOGENEITY_EXAMPLES if e["title"] == chosen)
    pc.check_homogeneity([ex["lhs_dims"]], [ex["rhs_dims"]])
    vcol1, vcol2 = st.columns(2)
    with vcol1:
        card("Left-hand side", f"<p>{ex['lhs']}</p><p>Dimensions: <b>{ex['lhs_label']}</b></p>", "LHS")
    with vcol2:
        card("Right-hand side", f"<p>{ex['rhs']}</p><p>Dimensions: <b>{ex['rhs_label']}</b></p>", "RHS")
    st.latex(ex["equation_latex"])
    st.markdown(
        V.balance(ex["lhs"], ex["rhs"], ex["valid"], ex["lhs_label"], ex["rhs_label"]),
        unsafe_allow_html=True,
    )
    if ex["valid"]:
        st.markdown(f"**Verdict:** {pill('HOMOGENEOUS', 'good')}", unsafe_allow_html=True)
    else:
        st.markdown(f"**Verdict:** {pill('NOT HOMOGENEOUS', 'bad')}", unsafe_allow_html=True)
    st.markdown(ex["explanation"])
    st.markdown(
        f'<div class="atlas-card"><div class="kicker">IMPORTANT CAUTION</div>'
        "<div class='body'>Passing the dimensional test does <b>not</b> prove an equation is "
        "physically correct. It can only detect certain inconsistencies. Dimensionless factors "
        "and the actual physics must be supplied separately.</div></div>",
        unsafe_allow_html=True,
    )

    st.divider()
    st.subheader("4 · Deriving a relationship by dimensions")
    card(
        "The pendulum: from dimensions to a formula",
        "Dimensional analysis can find the form of a relationship up to a dimensionless constant. "
        "Follow the reasoning for the period of a simple pendulum, then read its limitations.",
        "1.2.4",
    )
    deriv = pc.solve_pendulum_exponents()
    step = st.slider("Reveal the derivation step by step", 0, len(deriv["steps"]), 0, key="pend_step")
    for i in range(step):
        st.markdown(f"**Step {i+1}.** {deriv['steps'][i]}")
    if step >= len(deriv["steps"]):
        st.success(f"Result: {deriv['result']}, i.e. T is proportional to √(L/g).")
    with st.expander("See the algebra written out"):
        st.latex(r"T = k\,m^{a}L^{b}g^{c}")
        st.latex(r"[T] = M^{a}\,L^{b}\,(L T^{-2})^{c} = M^{a}L^{b+c}T^{-2c}")
        st.latex(r"\text{Mass: } a = 0 \quad \text{Time: } -2c = 1 \Rightarrow c = -\tfrac12 "
                 r"\quad \text{Length: } b + c = 0 \Rightarrow b = \tfrac12")
        st.latex(r"\therefore\; T = k\sqrt{\frac{L}{g}}")
    st.warning(
        "Limitations: dimensional analysis gives T ∝ √(L/g) but cannot determine k. For small "
        "oscillations the true constant is k = 2π, so T = 2π√(L/g). The method also assumes the "
        "period depends only on m, L and g, and it cannot handle dimensionless factors on its own."
    )
    with st.expander("Second derivation: mass on a spring"):
        st.markdown("Assume T = k mᵃ k꜀ᵇ where k꜀ is the spring constant with dimensions [M T⁻²].")
        st.latex(r"[T] = M^{a}\,(M T^{-2})^{b} = M^{a+b}T^{-2b}")
        st.latex(r"a+b=0,\quad -2b=1 \Rightarrow b=-\tfrac12,\; a=\tfrac12 "
                 r"\Rightarrow T = k\sqrt{\frac{m}{k_s}}")
        st.caption("Again the dimensionless constant (2π) is not given by dimensional analysis.")


def _accuracy_precision():
    st.subheader("1 · Accuracy and precision")
    card(
        "Two different questions",
        "<b>Accuracy</b> asks: how close is a measurement to the accepted reference value? "
        "<b>Precision</b> asks: how closely do repeated measurements agree with each other? "
        "They are independent ideas.",
        "1.3.1",
    )
    quad = pd.DataFrame([
        ["Accurate and precise", "Close to the reference value", "Readings agree closely"],
        ["Accurate on average, not precise", "Mean is close to reference", "Readings are scattered"],
        ["Precise but not accurate", "Mean is offset from reference", "Readings agree closely"],
        ["Neither", "Mean is far from reference", "Readings are scattered"],
    ], columns=["Situation", "Accuracy", "Precision"])
    table(quad, use_container_width=True, hide_index=True)

    st.subheader("2 · Simulated measurement lab")
    st.markdown(
        f"{pill('SIMULATED DATA — not experimental readings', 'warn')}",
        unsafe_allow_html=True,
    )
    st.caption(
        "Adjust the reference value, a systematic offset and the random variation to see how "
        "each one changes accuracy and precision. Every point below is generated by the app, not "
        "collected from a real instrument."
    )
    c1, c2, c3, c4 = st.columns(4)
    reference = c1.number_input("Accepted reference value", value=10.00, step=0.1, format="%.2f", key="ap_ref")
    offset = c2.number_input("Systematic offset (bias)", value=0.00, step=0.1, format="%.2f", key="ap_off")
    sigma = c3.number_input("Random variation (σ)", value=0.20, min_value=0.0, step=0.05, format="%.2f", key="ap_sig")
    n = c4.slider("Number of readings", 3, 40, 12, key="ap_n")
    seed = st.number_input("Random seed", value=7, step=1, key="ap_seed")

    rng = random.Random(int(seed))
    readings = [reference + offset + rng.gauss(0, sigma) for _ in range(int(n))]
    stats = pc.summary_statistics(readings)
    mean = stats["mean"]
    bias = mean - reference
    stdev = stats["stdev"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(1, int(n) + 1)), y=readings, mode="markers",
        marker=dict(size=9, color=CYAN), name="Simulated readings"))
    fig.add_hline(y=reference, line=dict(color=GREEN, width=2, dash="dash"),
                  annotation_text="reference", annotation_position="top left")
    fig.add_hline(y=mean, line=dict(color=AMBER, width=2),
                  annotation_text="mean", annotation_position="bottom left")
    fig.update_layout(title="Simulated repeated readings (this app's data)",
                      xaxis_title="Reading number", yaxis_title="Value")
    st.plotly_chart(style_fig(fig, 340), use_container_width=True, key="c1_readings",
                     config={"displayModeBar": False})

    target_col, note_col = st.columns([1, 1])
    with target_col:
        st.markdown(V.error_target(V.freeze(readings), reference, mean, stdev), unsafe_allow_html=True)
    with note_col:
        card(
            "Read the bullseye",
            "<p>The green dot is the true reference value. Each blue dot is one simulated "
            "reading, placed at a distance equal to its error.</p>"
            "<p><b>A tight cluster</b> → precise. <b>A cluster on the centre</b> → accurate. "
            "The amber line shows how far the average sits from the centre: that is the "
            "systematic bias.</p>",
            "HOW TO READ IT",
        )

    metric_row([
        ("Mean", f"{mean:.3f}"),
        ("Mean − reference (bias)", f"{bias:+.3f}"),
        ("Spread (sample σ)", f"{stdev:.3f}"),
        ("Reference", f"{reference:.2f}"),
    ])
    if abs(bias) > max(2 * stats["stderr"], 0.02):
        st.markdown(f"**Interpretation:** the readings are shifted from the reference by about "
                    f"{abs(bias):.2f}, a systematic effect. This is an accuracy problem, and "
                    "averaging will not remove it.")
    elif stdev > 2 * abs(offset) + 0.05:
        st.markdown("**Interpretation:** the average is close to the reference, but the readings "
                    "are scattered. This is a precision problem driven by random variation.")
    else:
        st.markdown("**Interpretation:** the readings are close to the reference and close to each "
                    "other — accurate and precise for this simulated set.")
    st.caption("Systematic offset moves the whole cloud (accuracy). Random variation widens the "
               "cloud (precision). Increase the number of readings: the mean becomes more stable, "
               "but the systematic offset remains.")

    st.subheader("3 · Measuring instruments")
    st.caption(
        "Resolution is the smallest change an instrument can display. The reading uncertainty "
        "depends on the instrument, its condition and the method — there is no single universal "
        "value. The figures below are common textbook conventions and must be stated as assumptions."
    )
    inst_frame = pd.DataFrame([
        {"Instrument": i["name"], "Resolution": i["resolution"],
         "Typical reading uncertainty (assumption)": i["typical_uncertainty"],
         "Best for": i["best_for"]}
        for i in D.INSTRUMENTS
    ])
    table(inst_frame, use_container_width=True, hide_index=True)
    st.markdown("##### Zoom in on a reading")
    st.caption("Pick a smallest division and a reading. The picture shows how much of the "
               "scale one division covers — that is the resolution.")
    zoom1, zoom2 = st.columns(2)
    resolution_choices = {"1 mm": 0.001, "0.1 mm": 0.0001, "0.01 s": 0.01,
                          "1 cm": 0.01, "0.5 g": 0.5}
    zoom_res = zoom1.selectbox("Smallest division", list(resolution_choices), key="ap_res")
    zoom_reading = zoom2.number_input("Your reading", value=float(reference), step=resolution_choices[zoom_res],
                                      format="%.4f", key="ap_reading")
    st.markdown(
        V.reading_ruler(zoom_reading, resolution_choices[zoom_res], reference),
        unsafe_allow_html=True,
    )
    with st.expander("Zero error, parallax and calibration"):
        st.markdown(
            "- **Zero error:** the instrument does not read zero when it should. It shifts all "
            "readings in one direction (systematic).\n"
            "- **Parallax:** reading from an angle makes the scale appear shifted; you should read "
            "with your eye perpendicular to the scale.\n"
            "- **Calibration:** an instrument may be accurately readable in resolution but not "
            "traceable to the reference standard.\n"
            "- **Method limits:** even a perfect instrument gives poor data if the method is poor "
            "(for example, timing a single swing instead of many periods).\n\n"
            "A better instrument usually improves resolution, but it does not automatically remove "
            "systematic or method errors."
        )


def _uncertainty_and_significant_figures():
    st.subheader("1 · Why every measurement has uncertainty")
    card(
        "Uncertainty is not carelessness",
        "A measurement can never be exact. Limitations of the instrument, the method, the "
        "environment and the observer all mean that a reported value is an interval, not a point. "
        "This is why we report an uncertainty alongside a measured value.",
        "1.4.2",
    )
    sources = pd.DataFrame([
        ["Finite instrument resolution", "The scale cannot show differences smaller than its smallest division."],
        ["Variation between readings", "Repeated readings of the same quantity differ (random effect)."],
        ["Calibration limits", "The instrument may be slightly offset from the standard (systematic)."],
        ["Environmental effects", "Temperature, draughts or vibration change the measurement."],
        ["Human reading limits", "Reading a scale and reaction time when timing introduce error."],
        ["Method limitations", "The procedure itself may not fully isolate the quantity."],
    ], columns=["Source", "What it means"])
    table(sources, use_container_width=True, hide_index=True)

    vocab = pd.DataFrame([
        ["Measured value", "The best estimate you report, e.g. 20.8 m s⁻¹."],
        ["Uncertainty estimate", "An interval that expresses the range the value probably lies in."],
        ["Systematic effect", "A consistent shift in one direction; affects accuracy; not reduced by averaging."],
        ["Random variation", "Scatter between readings; affects precision; reduced by averaging."],
    ], columns=["Term", "Meaning"])
    table(vocab, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("2 · Uncertainty in a derived quantity")
    card(
        "Two standard methods",
        "For a quantity written as a product of powers, <code>Q = k·x₁ⁿ¹·x₂ⁿ²…</code>, the "
        "relative uncertainties combine in two common ways. <b>Independent (quadrature)</b> is "
        "used when the inputs vary independently and the uncertainties are small. "
        "<b>Maximum (limiting)</b> adds the fractional uncertainties, giving a larger, "
        "worst-case interval. They are different conventions — they must not be mixed silently.",
        "1.4.1",
    )
    presets = {
        "Momentum  p = m v": {"formula": r"p = m\,v", "terms": [("m", 1), ("v", 1)]},
        "Speed  v = d / t": {"formula": r"v = \dfrac{d}{t}", "terms": [("d", 1), ("t", -1)]},
        "Density  ρ = m / V": {"formula": r"\rho = \dfrac{m}{V}", "terms": [("m", 1), ("V", -1)]},
        "Area  A = l w": {"formula": r"A = l\,w", "terms": [("l", 1), ("w", 1)]},
        "Pressure  p = F / A": {"formula": r"p = \dfrac{F}{A}", "terms": [("F", 1), ("A", -1)]},
    }
    preset_name = st.selectbox("Choose a relationship", list(presets.keys()), key="unc_preset")
    preset = presets[preset_name]
    st.latex(preset["formula"])

    cols = st.columns(len(preset["terms"]))
    values = {}
    uncertainties = {}
    for col, (name, exponent) in zip(cols, preset["terms"]):
        with col:
            values[name] = st.number_input(f"{name} value", value=1.0, min_value=0.0,
                                           step=0.1, format="%.4f", key=f"unc_v_{name}")
            uncertainties[name] = st.number_input(f"{name} uncertainty", value=0.01,
                                                  min_value=0.0, step=0.01, format="%.4f",
                                                  key=f"unc_u_{name}")

    def _compute(method):
        value = 1.0
        terms = []
        for name, exponent in preset["terms"]:
            if values[name] > 0:
                value *= values[name] ** exponent
                terms.append((exponent, uncertainties[name] / values[name]))
            else:
                value = 0.0 if exponent > 0 else value
        return value, pc.propagate_product(value, terms, method)

    if any(v == 0 for v in values.values()):
        st.info("Enter nonzero values for each quantity so the relative uncertainty is defined.")
    else:
        val_q, quad = _compute("quadrature")
        _, maxim = _compute("maximum")
        metric_row([
            ("Calculated value", f"{val_q:.4g}"),
            ("Independent uncertainty", f"± {quad['absolute']:.3g}"),
            ("Independent %", f"{quad['percentage']:.2f} %"),
            ("Maximum uncertainty", f"± {maxim['absolute']:.3g}"),
            ("Maximum %", f"{maxim['percentage']:.2f} %"),
        ])
        st.markdown(
            f"**Independent (quadrature):** ΔQ/Q = √(Σ(nᵢ·Δxᵢ/xᵢ)²) = "
            f"{quad['relative']:.4f}, so ΔQ = {quad['absolute']:.3g} and the result is "
            f"Q = {val_q:.4g} ± {quad['absolute']:.3g}."
        )
        st.markdown(
            f"**Maximum (limiting):** ΔQ/Q = Σ|nᵢ·Δxᵢ/xᵢ| = {maxim['relative']:.4f}, so "
            f"ΔQ = {maxim['absolute']:.3g} and the result is Q = {val_q:.4g} ± {maxim['absolute']:.3g}."
        )
        st.caption("The maximum method always gives the larger interval. State which convention "
                   "your curriculum expects and apply it consistently. Both results are computed "
                   "by this app and labelled as such.")
        st.markdown(
            V.uncertainty_number_line(val_q, quad["absolute"]), unsafe_allow_html=True)

    with st.expander("Worked example: momentum uncertainty, one line at a time"):
        st.markdown("Let m = 2.0 kg ± 0.1 kg and v = 3.0 m s⁻¹ ± 0.1 m s⁻¹.")
        st.latex(r"p = mv = 2.0 \times 3.0 = 6.0\ \text{kg m s}^{-1}")
        st.latex(r"\frac{\Delta m}{m} = \frac{0.1}{2.0} = 0.050, \qquad "
                 r"\frac{\Delta v}{v} = \frac{0.1}{3.0} = 0.0333")
        st.latex(r"\frac{\Delta p}{p} = \sqrt{0.050^2 + 0.0333^2} = 0.060 "
                 r"\Rightarrow \Delta p = 6.0 \times 0.060 = 0.36")
        st.markdown("So p = 6.0 ± 0.4 kg m s⁻¹ (independent method). The maximum method gives "
                    "0.050 + 0.0333 = 0.0833, i.e. Δp = 0.5 kg m s⁻¹.")

    st.divider()
    st.subheader("3 · Significant figures")
    card(
        "Precision as written",
        "Significant figures record how precisely a value was written. They are read from the "
        "written form, not from a number that has already been rounded by the computer. "
        "Use the tool below to inspect any value.",
        "1.4.1",
    )
    sf_col1, sf_col2 = st.columns([3, 2])
    with sf_col1:
        text_value = st.text_input("Enter a value exactly as written",
                                   value="0.00250", key="sf_text")
        result = pc.analyse_significant_figures(text_value)
        if not result["valid"]:
            st.error(result["note"])
        else:
            st.markdown(
                f'<div class="atlas-card"><div class="kicker">SIGNIFICANT FIGURES</div>'
                f"<h2 style='color:#5eead4'>{result['count']}</h2>"
                f"<div class='body'>{result['note']}</div></div>",
                unsafe_allow_html=True,
            )
            st.markdown(V.sigfig_highlight(text_value), unsafe_allow_html=True)
    with sf_col2:
        st.markdown("**Rules of thumb**")
        st.markdown(
            "- All nonzero digits are significant.\n"
            "- Leading zeros are never significant.\n"
            "- Zeros between nonzero digits are significant.\n"
            "- Trailing zeros after a decimal point are significant.\n"
            "- Trailing zeros in a whole number are ambiguous (e.g. 1500).\n"
            "- In scientific notation, only the mantissa counts."
        )

    st.markdown("##### Rounding a computed result")
    rc1, rc2, rc3 = st.columns(3)
    number = rc1.number_input("Computed value", value=8.55, step=0.01, format="%.6f", key="sf_val")
    digits = rc2.slider("Keep significant figures", 1, 8, 2, key="sf_digits")
    rc3.metric("Rounded", pc.format_to_sig_figs(number, digits))
    st.caption("In multiplication and division, the result keeps the fewest significant figures of "
               "the inputs. Retain extra 'guard' digits during intermediate steps and round only at "
               "the end. Report uncertainty and significant figures consistently.")

    with st.expander("Worked examples in significant figures"):
        st.markdown("- 0.00250 has **3** significant figures (leading zeros do not count).")
        st.markdown("- 1500 written without a decimal point is **ambiguous**; write 1.500 × 10³ "
                    "to show 4 significant figures.")
        st.markdown("- 2.5 × 3.42 = 8.55 → **8.6** (2 significant figures, limited by 2.5).")
        st.markdown("- 100.0 ÷ 3.00 = 33.333… → **33.3** (3 significant figures).")


STATIONS = [
    Station("overview", "🗺️ Your route & outcomes",
            lambda: overview_station(SPEC), [s["id"] for s in D.SLOS]),
    Station("quantities", "📏 Units & quantities", _quantities_and_units,
            STATION_SLOS["quantities"]),
    Station("dimensions", "🧭 Dimensions", _dimensions, STATION_SLOS["dimensions"]),
    Station("accuracy", "🎯 Accuracy & precision", _accuracy_precision,
            STATION_SLOS["accuracy"]),
    Station("uncertainty", "➕ Uncertainty & sig figs",
            _uncertainty_and_significant_figures, STATION_SLOS["uncertainty"]),
    Station("worked", "🧮 Worked problems",
            lambda: worked_problems(SPEC), STATION_SLOS["worked"]),
    Station("practice", "🧠 Practice",
            lambda: practice(SPEC), STATION_SLOS["practice"]),
    Station("tutor", "🤖 Atlas Tutor (offline AI)",
            lambda: ai_tutor.render(_N), STATION_SLOS["tutor"]),
    Station("references", "📚 References",
            lambda: references(SPEC), []),
]

SPEC = ChapterSpec(
    number=_N,
    title="Physical Quantities and Measurement",
    blurb="Magnitudes and units, the SI system, dimensions, accuracy, precision and uncertainty.",
    tag=D_META.TAG,
    intro=D_META.INTRO,
    stations=STATIONS,
    slos=D.SLOS,
    key_prefix="c1_",
    big_ideas=D_META.BIG_IDEAS,
    worked_problems=D.WORKED_PROBLEMS,
    practice_questions=D.PRACTICE_QUESTIONS,
    references=D.REFERENCES,
    tutor=ai_tutor.render,
    route=D_META.ROUTE,
    honesty_pills=[
        ("Established scientific definitions", "info"),
        ("Curriculum conventions", "warn"),
        ("Simulated teaching data", "mute"),
        ("Values computed by this app", "good"),
    ],
    notes=[
        (WATCH_OUT,
         "A dimensionally correct equation can still be wrong",
         "Dimensional analysis can only tell you that a formula is <em>possible</em>. "
         "It can never give you a dimensionless constant, and it cannot tell "
         "sin(theta) from tan(theta). Chapter 4 is a live example: every projectile "
         "relation here is dimensionally sound, and only the experiment settles the "
         "value of 45°."),
        (EXAM_TIP,
         "Three marks for a unit, every time",
         "Examining boards award marks for writing the unit even when the number is "
         "wrong. Write the unit in every line of working, and check it at the end "
         "against the quantity you were asked for — not against the numbers you were "
         "given."),
        (HONEST_LIMIT,
         "Resolution is not the same as uncertainty",
         "A metre rule graduated in millimetres has a resolution of 1 mm, but the "
         "uncertainty of a single reading is usually taken as about ±0.5 mm at best, "
         "and usually more once you allow for how you place the zero mark and read "
         "between the lines."),
    ],
)


def render() -> None:
    """Build the Chapter 1 world."""
    from . import engine
    engine.render(SPEC)


def station_count() -> int:
    return len(STATIONS)
