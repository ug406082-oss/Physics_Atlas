"""Chapter 2 interface: Scalars and Vectors.

Four teaching stations written for this chapter alone. The shell — tabs, mastery
meter, worked problems, practice, tutor, references — comes from
:mod:`physics.engine`.

Two interactive tools are built here that no other chapter has: a **vector
sandpit** where two vectors are set with sliders and the resultant, its
components and both products update live, and a **product dial** that rotates
one vector through a full turn while the dot and cross products trace out
against each other.
"""

from __future__ import annotations

import math

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from .. import ai_tutor
from ..core import vectors as V
from ..engine import (ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, card, pill, style_fig
from ..visuals import ch02 as VIS
from . import ch02_data as D

_N = 2
P = f"c{_N}_"


def _arrow_sandbox() -> None:
    """The vector sandpit: set two vectors, watch everything downstream."""
    st.caption("Set two vectors with the sliders. The components, the resultant and both "
               "products are recomputed from the formulas every time you move anything.")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        mag_a = st.number_input("|A|", 0.0, 20.0, 6.0, 0.5, key=f"{P}maga")
        ang_a = st.slider("direction of A (°)", 0.0, 360.0, 25.0, 5.0, key=f"{P}anga")
    with col2:
        mag_b = st.number_input("|B|", 0.0, 20.0, 4.0, 0.5, key=f"{P}magb")
        ang_b = st.slider("direction of B (°)", 0.0, 360.0, 120.0, 5.0, key=f"{P}angb")
    with col3:
        add = st.checkbox("Add A + B", value=True, key=f"{P}add")
        subtract = st.checkbox("Also show A − B", value=False, key=f"{P}sub")
    with col4:
        ratio = st.slider("scale of the drawing", 12.0, 60.0, 40.0, 2.0, key=f"{P}scale")

    a = V.components_from_polar(mag_a, ang_a)
    b = V.components_from_polar(mag_b, ang_b)

    left, right = st.columns([3, 2])
    with left:
        traces = []
        traces.append(go.Scatter(x=[0, a[0]], y=[0, a[1]], mode="lines+markers",
                                 line=dict(color=CYAN, width=5),
                                 marker=dict(size=9), name="A", hoverinfo="skip"))
        traces.append(go.Scatter(x=[a[0], a[0] + b[0]], y=[a[1], a[1] + b[1]],
                                 mode="lines", line=dict(color=AMBER, width=5),
                                 name="B", hoverinfo="skip"))
        if add:
            traces.append(go.Scatter(x=[0, a[0] + b[0]], y=[0, a[1] + b[1]],
                                     mode="lines+markers",
                                     line=dict(color=GREEN, width=6),
                                     marker=dict(size=10), name="A + B",
                                     hoverinfo="skip"))
        if subtract:
            traces.append(go.Scatter(x=[0, a[0] - b[0]], y=[0, a[1] - b[1]],
                                     mode="lines", line=dict(color=ROSE, width=4,
                                                             dash="dash"),
                                     name="A − B", hoverinfo="skip"))
        span = max(mag_a, mag_b, V.magnitude(a) + V.magnitude(b), 1.0) * ratio / 10.0 + 0.4
        traces.append(go.Scatter(x=[-span, span], y=[0, 0], mode="lines",
                                 line=dict(color=MUTED, width=1), showlegend=False,
                                 hoverinfo="skip"))
        traces.append(go.Scatter(x=[0, 0], y=[-span, span], mode="lines",
                                 line=dict(color=MUTED, width=1), showlegend=False,
                                 hoverinfo="skip"))
        fig = go.Figure(data=traces)
        fig.update_layout(
            title="Head-to-tail: the resultant is the straight line from start to finish",
            xaxis=dict(title="x", range=[-span, span], constrain="domain"),
            yaxis=dict(title="y", range=[-span, span], scaleanchor="x",
                       scaleratio=1, constrain="domain"))
        st.plotly_chart(style_fig(fig, 380), use_container_width=True,
                        config={"displayModeBar": False})
    with right:
        total = V.add(a, b)
        difference = V.subtract(a, b)
        rows = [
            {"quantity": "A", "x": f"{a[0]:.3g}", "y": f"{a[1]:.3g}",
             "|A|": f"{V.magnitude(a):.4g}", "θ": f"{V.angle_of(a):.1f}°"},
            {"quantity": "B", "x": f"{b[0]:.3g}", "y": f"{b[1]:.3g}",
             "|B|": f"{V.magnitude(b):.4g}", "θ": f"{V.angle_of(b):.1f}°"},
            {"quantity": "A + B", "x": f"{total[0]:.4g}", "y": f"{total[1]:.4g}",
             "|A+B|": f"{V.magnitude(total):.4g}", "θ": f"{V.angle_of(total):.1f}°"},
            {"quantity": "A − B", "x": f"{difference[0]:.4g}", "y": f"{difference[1]:.4g}",
             "|A−B|": f"{V.magnitude(difference):.4g}", "θ": f"{V.angle_of(difference):.1f}°"},
        ]
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        st.markdown(VIS.vector_arrow(a[0], a[1], b[0], b[1]), unsafe_allow_html=True)


def _component_workbench() -> None:
    """Resolve a single vector and rebuild it from its parts."""
    st.caption("Change the magnitude and the direction. The right-hand column is always "
               "recomputed from the components, never stored.")

    m_col, a_col, t_col = st.columns(3)
    with m_col:
        mag = st.number_input("magnitude A", 0.0, 20.0, 8.0, 0.5, key=f"{P}cmag")
    with a_col:
        ang = st.slider("angle θ from +x (°)", 0.0, 360.0, 55.0, 1.0, key=f"{P}cang")
    with t_col:
        target = st.number_input("the magnitude I claim it should have", 0.0, 20.0,
                                 8.0, 0.5, key=f"{P}ctarget",
                                 help="Try a deliberately wrong number and see the check fail.")

    ax, ay = V.components_from_polar(mag, ang)
    rebuilt = math.hypot(ax, ay)

    col_a, col_b = st.columns([3, 2])
    with col_a:
        st.markdown(VIS.component_rectangle(mag, ang), unsafe_allow_html=True)
    with col_b:
        st.dataframe(pd.DataFrame([
            {"step": "Ax = A cos θ", "value": f"{ax:.4g}"},
            {"step": "Ay = A sin θ", "value": f"{ay:.4g}"},
            {"step": "√(Ax² + Ay²)", "value": f"{rebuilt:.4g}"},
            {"step": "θ from tan⁻¹(Ay/Ax)", "value": f"{V.angle_of((ax, ay)):.2f}°"},
        ]), use_container_width=True, hide_index=True)
        if math.isclose(rebuilt, target, rel_tol=1e-3):
            st.success(f"The components rebuild to {rebuilt:.4g}, which matches your claim "
                       f"of {target:g}.")
        else:
            st.error(f"The components rebuild to {rebuilt:.4g}, not {target:g}. "
                     f"Squaring and adding components always returns the square of the "
                     f"magnitude, so a mismatch means the components are wrong.")


def _product_dial(kind: str) -> None:
    """The shared dial behind both products: rotate B through a full turn."""
    st.caption("Vector A is held fixed and vector B turns through a full circle. Watch which "
               "part of the turn each product picks out.")

    c1, c2, c3 = st.columns(3)
    with c1:
        mag_a = st.number_input("|A|", 1.0, 12.0, 5.0, 0.5, key=f"{P}{kind}maga")
    with c2:
        mag_b = st.number_input("|B|", 1.0, 12.0, 4.0, 0.5, key=f"{P}{kind}magb")
    with c3:
        angle = st.slider("angle between them θ (°)", 0.0, 360.0, 55.0, 1.0,
                          key=f"{P}{kind}ang")

    a = (mag_a, 0.0)
    b = V.components_from_polar(mag_b, angle)
    dot = V.dot_product(a, b)
    cross = V.cross_product(a, b)
    theta = V.angle_between(a, b)

    fig_col, read_col = st.columns([3, 2])
    with fig_col:
        if kind == "dot":
            st.markdown(VIS.shadow_dial(angle, mag_a, mag_b), unsafe_allow_html=True)
        else:
            st.markdown(VIS.cross_plane(angle, mag_a, mag_b), unsafe_allow_html=True)

        # Both products plotted against the same axis, so the phase shift shows.
        xs = [i for i in range(361)]
        dots = [mag_a * mag_b * math.cos(math.radians(t)) for t in xs]
        crosses = [mag_a * mag_b * math.sin(math.radians(t)) for t in xs]
        figure = go.Figure()
        figure.add_trace(go.Scatter(x=xs, y=dots, mode="lines",
                                    line=dict(color=VIOLET, width=3),
                                    name="A · B = AB cos θ"))
        figure.add_trace(go.Scatter(x=xs, y=crosses, mode="lines",
                                    line=dict(color=TEAL, width=3, dash="dash"),
                                    name="|A × B| = AB sin θ"))
        figure.add_vline(x=angle, line=dict(color=AMBER, width=2))
        figure.add_hline(y=0, line=dict(color=MUTED, width=1))
        figure.update_layout(
            title="Both products against θ: the sine leads the cosine by 90°",
            xaxis=dict(title="θ (degrees)"), yaxis=dict(title="value"))
        st.plotly_chart(style_fig(figure, 300), use_container_width=True,
                        config={"displayModeBar": False})

    with read_col:
        if kind == "dot":
            sign = "positive" if dot > 0 else "negative" if dot < 0 else "zero"
            st.metric("A · B", f"{dot:.3f}")
            st.caption(f"{sign} — θ = {theta:.1f}°, and cos {angle:g}° = "
                       f"{math.cos(math.radians(angle)):.4f}")
            st.markdown(VIS.project_shadow(angle, mag_a, mag_b), unsafe_allow_html=True)
        else:
            sense = V.cross_direction(cross)
            st.metric("|A × B|", f"{abs(cross):.3f}")
            st.caption(f"Points {sense}. θ = {theta:.1f}°.")
            try:
                torque_case = math.degrees(math.atan2(cross, dot))
                st.caption(f"As a torque, {abs(cross):.2f} N m would turn the body "
                           f"{'anticlockwise' if cross > 0 else 'clockwise'} — "
                           f"{torque_case:.0f}° away from the direction of A.")
            except ValueError:
                pass


def _sweep() -> None:
    """Table of the two products as one vector turns."""
    st.caption("Every angle from 0° to 180°. Notice which product is zero, and where.")
    mag_a = st.number_input("|A|", 1.0, 12.0, 5.0, 0.5, key=f"{P}swmaga")
    mag_b = st.number_input("|B|", 1.0, 12.0, 4.0, 0.5, key=f"{P}swmagb")
    rows = []
    for theta in (0, 30, 60, 90, 120, 150, 180):
        radians = math.radians(theta)
        rows.append({
            "θ": f"{theta}°",
            "A · B": f"{mag_a * mag_b * math.cos(radians):+.2f}",
            "|A × B|": f"{mag_a * mag_b * math.sin(radians):.2f}",
            "A + B": f"{math.hypot(mag_a + mag_b * math.cos(radians), mag_b * math.sin(radians)):.2f}",
            "A − B": f"{math.hypot(mag_a - mag_b * math.cos(radians), mag_b * math.sin(radians)):.2f}",
            "note": ("parallel — largest dot, zero cross" if theta == 0
                     else "perpendicular — zero dot, largest cross" if theta == 90
                     else "opposite — most negative dot, zero cross" if theta == 180
                     else ""),
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


# --------------------------------------------------------------------------
# Stations
# --------------------------------------------------------------------------

def _kind() -> None:
    st.subheader("2.1 · Scalar or vector?")
    card("The test that never fails",
         "<p>Ask: <em>would a compass or a clock tell me which way?</em> If the answer "
         "needs a direction to be complete, it is a vector. If not, it is a scalar.</p>",
         "START HERE")

    tab_a, tab_b, tab_c = st.tabs(["Scalars", "Vectors", "Try classifying"])
    with tab_a:
        st.dataframe(pd.DataFrame(D.SCALARS), use_container_width=True, hide_index=True)
    with tab_b:
        st.dataframe(pd.DataFrame(D.VECTORS), use_container_width=True, hide_index=True)
    with tab_c:
        pick = st.selectbox("Choose a situation", [row["item"] for row in D.CLASSIFY_THESE],
                            key=f"{P}cls")
        row = next(r for r in D.CLASSIFY_THESE if r["item"] == pick)
        st.markdown(f"**{row['item']}**")
        guess = st.radio("Is it a scalar or a vector?",
                         ["Scalar", "Vector"], key=f"{P}clsans", horizontal=True,
                         index=None)
        if guess is None:
            st.caption("Make a choice and the reasoning appears.")
        elif guess.lower() == row["answer"]:
            st.success(f"Correct. {row['why']}")
        else:
            st.warning(f"Not quite — this one is a {row['answer']}. {row['why']}")

    st.divider()
    st.markdown(VIS.scalar_vector_strip(), unsafe_allow_html=True)

    guidance(WATCH_OUT, "Adding vectors is not adding numbers",
             "10 N east plus 10 N east is 20 N east, because the two are in the same "
             "direction. 10 N east plus 10 N north is not 20 N of anything — it is "
             "14.1 N at 45°. That is the entire reason components exist.")
    guidance(EXAM_TIP, "Momentum is always in the direction of the velocity",
             "p = m v, and m is a positive scalar, so it cannot flip the direction. A "
             "ball thrown upwards has upward momentum on the way up and, once it is "
             "falling, downward momentum — never sideways.")


def _components() -> None:
    st.subheader("2.2 · Rectangular components")
    card("Why components work at all",
         "<p>Two vectors in the same direction add like numbers. Two at an angle do "
         "not — but their <em>components</em> are signed numbers along fixed axes, and "
         "signed numbers do add like numbers. So break everything up, add the pieces, "
         "and rebuild once at the end.</p>", "THE IDEA")

    st.dataframe(pd.DataFrame(D.COMPONENT_RULES), use_container_width=True,
                 hide_index=True)

    st.subheader("The vector sandpit")
    _arrow_sandbox()

    st.subheader("Rebuilding a vector from its components")
    _component_workbench()

    st.subheader("Reading real component numbers")
    rows = []
    for case in D.COMPONENT_LAB:
        rows.append({"situation": case["setup"], "Ax": case["ax"], "Ay": case["ay"],
                     "|A|": case["magnitude"], "θ": f'{case["angle"]:.2f}°'})
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    for case in D.COMPONENT_LAB:
        with st.expander(case["setup"]):
            st.markdown(case["explain"])

    st.subheader("Adding two vectors — the procedure")
    for index, step in enumerate(D.RESULTANT_STEPS, start=1):
        st.markdown(f"**{index}.** {step}")

    st.subheader("The parallelogram rule")
    m1, a1, m2, a2 = st.columns(4)
    with m1:
        pa = st.number_input("|A|", 1.0, 15.0, 6.0, 0.5, key=f"{P}pma")
    with a1:
        qa = st.slider("angle of A (°)", 0.0, 360.0, 30.0, 5.0, key=f"{P}paa")
    with m2:
        pb = st.number_input("|B|", 1.0, 15.0, 4.0, 0.5, key=f"{P}pmb")
    with a2:
        qb = st.slider("angle of B (°)", 0.0, 360.0, 95.0, 5.0, key=f"{P}pab")
    st.markdown(VIS.resultant_parallelogram(pa, qa, pb, qb), unsafe_allow_html=True)

    guidance(TRY_IT, "Set A at 0° and B at 90°",
             "The resultant becomes exactly √(A² + B²), and the triangle is a right one. "
             "Now set B to 10° instead and watch the result approach A + B. The angle "
             "between the two vectors is what decides how much they reinforce.")
    guidance(HONEST_LIMIT, "atan2, not atan",
             "If you ever write code for this, use atan2(Ay, Ax) rather than atan(Ay/Ax). "
             "The plain tangent cannot tell you which quadrant you are in, so a vector "
             "at 225° and one at 45° give the same tangent but opposite answers.")


def _dot() -> None:
    st.subheader("2.3 · The scalar product")
    st.latex(r"\mathbf{A}\cdot\mathbf{B} = A_xB_x + A_yB_y = AB\cos\theta")
    card("The shadow definition",
         "<p>A·B is the length of the shadow that B casts on the direction of A, taken "
         "with a sign. That is why it is a plain number, and why the sign matters: a "
         "positive result means the two push the same way along A, a negative result "
         "means they oppose.</p>", "THE IDEA")

    st.dataframe(pd.DataFrame(D.PRODUCT_CONTRAST), use_container_width=True,
                 hide_index=True)

    st.subheader("The dial")
    _product_dial("dot")

    st.subheader("Properties")
    for prop in D.DOT_PROPERTIES:
        with st.expander(f"{prop['name']} — {prop['statement']}"):
            st.markdown(prop["proof"])

    st.subheader("Where it shows up: work")
    st.latex(r"W = \mathbf{F}\cdot\mathbf{d} = Fd\cos\theta")
    st.dataframe(pd.DataFrame(D.WORK_APPLICATIONS), use_container_width=True,
                 hide_index=True)
    f_col, d_col, t_col = st.columns(3)
    with f_col:
        force = st.number_input("force F (N)", 0.0, 500.0, 50.0, 5.0, key=f"{P}wf")
    with d_col:
        distance = st.number_input("displacement d (m)", 0.0, 100.0, 6.0, 0.5, key=f"{P}wd")
    with t_col:
        angle = st.slider("angle between them (°)", 0.0, 180.0, 40.0, 5.0, key=f"{P}wth")
    work = force * distance * math.cos(math.radians(angle))
    st.metric("Work done", f"{work:.1f} J")
    if work > 0:
        st.success("Positive: the force has a component along the motion, so energy is "
                   "being added to the system.")
    elif work < 0:
        st.error("Negative: the force opposes the motion, so energy is being removed.")
    else:
        st.warning("Zero: the force is perpendicular to the motion, so it changes the "
                   "direction of travel without changing the speed.")

    guidance(WATCH_OUT, "Work is a scalar even though it is built from two vectors",
             "F and d are both vectors, but F·d is a plain number measured in joules. "
             "Compare it with torque, which uses the cross product and comes out with a "
             "direction. Same two ingredients, different product, different answer.")


def _cross() -> None:
    st.subheader("2.4 · The vector product")
    st.latex(r"\mathbf{A}\times\mathbf{B} = AB\sin\theta\,\hat{\mathbf{n}}")
    card("The area definition",
         "<p>|A × B| = AB sin θ is exactly the area of the parallelogram that A and B "
         "enclose. The direction is normal to that parallelogram, fixed by the "
         "right-hand rule. In the xy plane that means straight out of the page (⊙) or "
         "straight into it (⊗).</p>", "THE IDEA")

    st.subheader("The dial")
    _product_dial("cross")

    st.subheader("Properties")
    for prop in D.CROSS_PROPERTIES:
        with st.expander(f"{prop['name']} — {prop['statement']}"):
            st.markdown(prop["proof"])

    st.subheader("The right-hand rule, step by step")
    st.markdown(
        "1. Point the fingers of your right hand along **A**.\n"
        "2. Curl them towards **B**, through the smaller angle.\n"
        "3. Your thumb now points along **A × B**.\n\n"
        "If the curl from A to B is anticlockwise, the thumb points out of the page (⊙). "
        "If it is clockwise, the thumb points into the page (⊗)."
    )

    st.subheader("Where it shows up: torque")
    st.latex(r"\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}, \qquad \tau = rF\sin\theta")
    st.dataframe(pd.DataFrame(D.TORQUE_APPLICATIONS), use_container_width=True,
                 hide_index=True)
    r_col, f_col, p_col = st.columns(3)
    with r_col:
        arm = st.number_input("moment arm r (m)", 0.0, 2.0, 0.4, 0.05, key=f"{P}tr")
    with f_col:
        applied = st.number_input("force F (N)", 0.0, 500.0, 30.0, 5.0, key=f"{P}tf")
    with p_col:
        phi = st.slider("angle between r and F (°)", 0.0, 180.0, 70.0, 1.0, key=f"{P}tphi")
    tau = arm * applied * math.sin(math.radians(phi))
    st.metric("|τ|", f"{abs(tau):.2f} N m")
    st.markdown(VIS.torque_arc(arm, phi, arm, applied, handle_deg=0.0),
                unsafe_allow_html=True)
    if abs(tau) < 1e-9:
        st.warning("Zero: the force acts along the arm, so nothing turns. This is why a "
                   "hinge placed at the edge of a door makes the door hard to close.")
    else:
        st.success(f"The force turns the body {'anticlockwise' if tau > 0 else 'clockwise'} "
                   f"about the pivot. The perpendicular component, "
                   f"{applied * abs(math.cos(math.radians(phi))):.1f} N, is the part doing "
                   f"the turning.")

    st.subheader("Both products at a glance")
    _sweep()

    guidance(WATCH_OUT, "The order of the vectors matters here, and only here",
             "A × B = −(B × A), but A · B = B · A. Reverse the order of a cross product "
             "and you have reversed the direction of a torque — which is the whole "
             "difference between tightening and loosening a bolt.")


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------

RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "kind": _kind,
    "components": _components,
    "dot": _dot,
    "cross": _cross,
    "worked": lambda: worked_problems(SPEC),
    "practice": lambda: practice(SPEC),
    "tutor": lambda: ai_tutor.render(_N),
    "references": lambda: references(SPEC),
}

STATIONS = [Station(row["key"], row["label"], RENDERERS[row["key"]], row["slos"])
            for row in D.STATIONS]

SPEC = ChapterSpec(
    number=_N,
    title="Scalars and Vectors",
    blurb="Scalars versus vectors, rectangular components, scalar and vector products.",
    tag=D.TAG,
    intro=D.INTRO,
    stations=STATIONS,
    slos=D.SLOS,
    key_prefix=P,
    big_ideas=D.BIG_IDEAS,
    worked_problems=D.WORKED_PROBLEMS,
    practice_questions=D.PRACTICE_QUESTIONS,
    references=D.REFERENCES,
    tutor=ai_tutor.render,
    route=D.ROUTE,
    honesty_pills=D.HONESTY_PILLS,
    notes=D.NOTES,
)


def render() -> None:
    from .. import engine
    engine.render(SPEC)


def station_count() -> int:
    return len(STATIONS)
