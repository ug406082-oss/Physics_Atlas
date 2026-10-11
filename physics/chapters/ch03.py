"""Chapter 3 interface: Motion in One Dimension.

Three benches belong to this chapter alone: the **motion lab**, which plots
position, velocity and acceleration together from a single set of controls; the
**collision bench**, where two bodies are launched and momentum and kinetic
energy are shown balancing — or not — across the collision; and the **work
bench**, which integrates a force–displacement profile with the trapezium rule.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..core import motion1d as M
from ..core import vectors as V
from ..engine import (how_to, ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT, practicals,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, card, metric_row
from ..visuals import ch02 as V2
from . import ch03_data as D

_N = 3
P = f"c{_N}_"


def _motion_lab() -> None:
    """Set u and a once, watch all three graphs move together."""
    st.caption("One set of controls drives all three graphs. Watch how the straight "
               "velocity graph's gradient is exactly the acceleration.")

    c1, c2, c3 = st.columns(3)
    with c1:
        u = st.number_input("initial velocity u (m s⁻¹)", -60.0, 60.0, 12.0, 1.0, key=f"{P}mu")
    with c2:
        a = st.number_input("acceleration a (m s⁻²)", -30.0, 30.0, -4.0, 0.5, key=f"{P}ma")
    with c3:
        t_max = st.number_input("time t_max (s)", 0.5, 60.0, 10.0, 0.5, key=f"{P}mt")

    series = M.kinematic_series(u, a, t_max, 200)

    tab_all, tab_s, tab_v, tab_a = st.tabs(["All three", "s–t", "v–t", "a–t"])
    with tab_all:
        st.markdown(_three_graphs(series, u, a, t_max), unsafe_allow_html=True)
    with tab_s:
        st.plotly_chart(_graph(series["t"], series["s"], "displacement s (m)", CYAN,
                               f"s = {u:g}t + ½({a:g})t²"),
                        use_container_width=True, config={"displayModeBar": False})
    with tab_v:
        st.plotly_chart(_graph(series["t"], series["v"], "velocity v (m s⁻¹)", AMBER,
                               f"v = {u:g} + ({a:g})t"),
                        use_container_width=True, config={"displayModeBar": False})
    with tab_a:
        st.plotly_chart(_graph(series["t"], series["a"], "acceleration a (m s⁻²)", GREEN,
                               f"a = {a:g} (constant)"),
                        use_container_width=True, config={"displayModeBar": False})

    st.dataframe(pd.DataFrame([
        {"quantity": "v at t_max", "value": f"{M.velocity(u, a, t_max):.4g} m s⁻¹"},
        {"quantity": "s at t_max", "value": f"{M.displacement(u, a, t_max):.4g} m"},
        {"quantity": "time to stop moving",
         "value": f"{M.time_from_velocity(u, 0, a):.4g} s" if a else "never (a = 0)"},
        {"quantity": "distance to stop",
         "value": f"{M.solve_from_uas(u, a, 0)['v']:.4g}" if a else "—"},
    ]), use_container_width=True, hide_index=True)

    st.markdown("Every quantity above comes from the same two numbers, u and a. "
                "That is the point: the three graphs are not three problems, they are one "
                "situation described three ways.", unsafe_allow_html=False)


def _graph(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def _three_graphs(series, u, a, t_max) -> str:
    """Three stacked plots drawn as one SVG."""
    w, h = 700, 540
    panel_h = 140
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'THREE GRAPHS, ONE SET OF CONTROLS</text>']
    rows = [("displacement s (m)", series["s"], CYAN),
            ("velocity v (m s⁻¹)", series["v"], AMBER),
            ("acceleration a (m s⁻²)", series["a"], GREEN)]
    left, right = 92, w - 30
    for index, (label, values, colour) in enumerate(rows):
        top = 50 + index * (panel_h + 34)
        bottom = top + panel_h
        lo, hi = min(values + [0.0]), max(values + [0.0])
        span = (hi - lo) or 1.0
        parts.append(f'<rect x="{left}" y="{top}" width="{right - left}" '
                     f'height="{panel_h}" rx="8" fill="#0b1a2c" stroke="#1b3350"/>')
        for fraction in (0.25, 0.5, 0.75):
            y = top + panel_h * fraction
            parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" '
                         f'stroke="#18304b" stroke-width="1"/>')
        zero_y = bottom - (0.0 - lo) / span * panel_h
        parts.append(f'<line x1="{left}" y1="{zero_y:.1f}" x2="{right}" y2="{zero_y:.1f}" '
                     f'stroke="{MUTED}" stroke-width="1" stroke-dasharray="3 3"/>')
        points = []
        for step, value in enumerate(values):
            px = left + (step / (len(values) - 1)) * (right - left)
            py = bottom - (value - lo) / span * panel_h
            points.append(f"{px:.1f},{py:.1f}")
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{colour}" '
                     f'stroke-width="3"/>')
        parts.append(f'<text x="20" y="{top + 20}" fill="{colour}" font-size="12" '
                     f'font-family="JetBrains Mono, monospace">{label}</text>')
        parts.append(f'<text x="{right}" y="{top + 20}" text-anchor="end" fill="{colour}" '
                     f'font-size="12" font-family="JetBrains Mono, monospace">'
                     f'{lo:.3g} … {hi:.3g}</text>')
    parts.append(f'<text x="20" y="{h - 22}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The velocity graph is a straight line whose '
                 f'gradient is a = {a:g} m s⁻². The acceleration graph is flat, because the '
                 f'acceleration is constant by assumption.</text>')
    parts.append(f'<text x="20" y="{h - 6}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">These equations assume uniform '
                 f'acceleration. Set a = 0 and they reduce to v = u and s = ut.</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;'
            f'display:block;margin:0 auto">{"".join(parts)}</svg>')


def _freefall() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("3.1.2 · Free fall")
    card("Gravity is the same for everything",
         "<p>Near the Earth's surface every body, whatever its mass, accelerates at "
         "g = 9.8 m s⁻². Heavier objects do not fall faster — their larger weight is "
         "exactly cancelled by their larger inertia.</p>", "THE IDEA")
    st.dataframe(pd.DataFrame([
        {"situation": c["situation"], "a (m s⁻²)": c["a"], "why": c["note"]}
        for c in D.KINEMATIC_LIMITS
    ]), use_container_width=True, hide_index=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        height = st.number_input("height L (m)", 0.1, 500.0, 45.0, 1.0, key=f"{P}fh")
    with c2:
        speed = st.number_input("initial speed u (m s⁻¹), downward positive", 0.0, 200.0,
                                0.0, 1.0, key=f"{P}fu")
    with c3:
        g = st.number_input("g (m s⁻²)", 0.1, 50.0, 9.8, 0.1, key=f"{P}fg")
    result = M.free_fall(height, speed, g)
    metric_row([("Time of fall", f"{result['t']:.3g} s"),
                ("Impact speed", f"{result['impact_speed']:.3g} m s⁻¹"),
                ("Speed from √(u²+2gL)", f"{math.sqrt(speed ** 2 + 2 * g * height):.3g} m s⁻¹")])
    st.markdown(_drop_diagram(height, speed), unsafe_allow_html=True)

    st.subheader("Earth, Moon and elsewhere")
    planet = st.slider("planet radius ÷ Earth's", 0.2, 4.0, 1.0, 0.05, key=f"{P}fplanet")
    g_planet = 9.8 * (1.0 / planet ** 2)
    st.metric("surface g", f"{g_planet:.3g} m s⁻²")
    st.caption(f"g falls as 1/r², so a planet {planet:g} times as wide as Earth has "
               f"{g_planet / 9.8:.3g} times its surface gravity.")

    st.subheader("Escape and orbit")
    st.dataframe(pd.DataFrame([
        {"speed (m s⁻¹)": f"{s:g}",
         "what happens": M.escape_and_orbit(6.371e6, s, 9.8)["state"]}
        for s in (5000, 7500, 7900, 8000, 11200)
    ]), use_container_width=True, hide_index=True)
    st.caption("On Earth the escape speed is about 11.2 km/s and the orbital speed at the "
               "surface about 7.9 km/s. Rocket launches work because you need far more than "
               "orbital speed to reach orbit, and still more to escape.")
    guidance(HONEST_LIMIT, "Constant g is an approximation",
             "g really falls as 1/r², so over the full 6371 km of Earth's radius it varies "
             "from 9.8 at the surface to zero at the centre. Constant-g equations are fine "
             "for a dropped ball and hopeless for a satellite.")


def _drop_diagram(height: float, speed: float) -> str:
    w, h = 260, 380
    top, ground = 46, 340
    parts = [f'<rect x="120" y="{top}" width="20" height="14" fill="{MUTED}"/>',
             f'<line x1="20" y1="{ground}" x2="240" y2="{ground}" stroke="{MUTED}" '
             f'stroke-width="2"/>',
             f'<text x="20" y="{ground + 20}" fill="{MUTED}" font-size="11" '
             f'font-family="Sora, sans-serif">height {height:g} m</text>',
             f'<text x="152" y="{top + 10}" fill="{MUTED}" font-size="11" '
             f'font-family="Sora, sans-serif">start</text>']
    for step in range(1, 7):
        fraction = (step / 6.0) ** 2
        py = top + 14 + (ground - top - 14) * fraction
        size = 9 - step * 0.6
        colour = CYAN if step < 4 else AMBER
        parts.append(f'<circle cx="{130 - 10 * step}" cy="{py:.1f}" r="{max(size, 3):.1f}" '
                     f'fill="{colour}" opacity="{1.0 - step * 0.1:.2f}"/>')
    parts.append(f'<path d="M 130 {top + 20} L 122 {top + 34} L 138 {top + 34} Z" '
                 f'fill="{ROSE}"/>')
    parts.append(f'<text x="146" y="{top + 34}" fill="{ROSE}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">g</text>')
    parts.append(f'<text x="20" y="{h - 8}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Equal drops in equal times: the spacing '
                 f'grows as t².</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;'
            f'display:block;margin:0 auto">{"".join(parts)}</svg>')


def _momentum() -> None:
    how_to("numbers"),
    st.subheader("3.2 · Conservation of linear momentum")
    card("Momentum",
         "<p><b>p = m v</b> — a vector, in kg m s⁻¹.</p>"
         "<p><b>The law:</b> if no resultant external force acts on a system, its total "
         "momentum is constant. Not approximately: exactly.</p>", "THE IDEA")

    st.subheader("Try to break it")
    c1, c2 = st.columns(2)
    with c1:
        bodies = st.number_input("number of bodies", 2, 5, 3, 1, key=f"{P}mb")
    with c2:
        rows = []
        for index in range(int(bodies)):
            cols = st.columns(3)
            with cols[0]:
                mass = st.number_input(f"body {index + 1} mass (kg)", 0.1, 100.0,
                                       2.0 + index, 0.1, key=f"{P}m{index}")
            with cols[1]:
                before = st.number_input(f"u before (m s⁻¹)", -50.0, 50.0,
                                         10.0 - 4.0 * index, 1.0, key=f"{P}bu{index}")
            with cols[2]:
                after = st.number_input(f"v after (m s⁻¹)", -50.0, 50.0,
                                        2.0 - index, 1.0, key=f"{P}av{index}")
            rows.append({"m": mass, "u": before, "v": after})
    series = M.momentum_series(rows)
    st.dataframe(pd.DataFrame([
        {"body": f"body {index + 1}", "m (kg)": r["m"],
         "p before = mu": f"{r['m'] * r['u']:.4g}", "p after = mv": f"{r['m'] * r['v']:.4g}",
         "change": f"{r['m'] * (r['v'] - r['u']):+.4g}"}
        for index, r in enumerate(rows)
    ]), use_container_width=True, hide_index=True)
    if series["conserved"]:
        st.success(f"Total momentum is unchanged at {series['before']:.4g} kg m s⁻¹. "
                   f"The bodies redistributed it; they did not create or destroy it.")
    else:
        st.error(f"Total momentum changed from {series['before']:.4g} to "
                 f"{series['after']:.4g}. Either an external force acted, or one of the "
                 f"bodies is not part of the system you meant.")

    st.subheader("Momentum in the real world")
    for example in D.MOMENTUM_EXAMPLES:
        with st.expander(example["situation"]):
            st.markdown(f"**System.** {example['system']}\n\n"
                        f"**Before.** {example['before']}\n\n"
                        f"**After.** {example['after']}\n\n"
                        f"**The lesson.** {example['lesson']}")


def _collisions() -> None:
    how_to("numbers"), how_to("sliders"),
    st.subheader("3.2 · Elastic and inelastic collisions")
    st.dataframe(pd.DataFrame([
        {"type": c["kind"], "momentum": c["momentum"], "kinetic energy": c["kinetic_energy"],
         "sound": c["sound"], "example": c["example"], "rule": c["rule"]}
        for c in D.COLLISION_TYPES
    ]), use_container_width=True, hide_index=True)

    st.subheader("The collision bench")
    kind = st.radio("What kind of collision?", ["Elastic", "Perfectly inelastic"],
                    horizontal=True, key=f"{P}ckind")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        m1 = st.number_input("m₁ (kg)", 0.1, 100.0, 2.0, 0.1, key=f"{P}c1m")
    with c2:
        u1 = st.number_input("u₁ before (m s⁻¹)", -50.0, 50.0, 10.0, 0.5, key=f"{P}c1u")
    with c3:
        m2 = st.number_input("m₂ (kg)", 0.1, 100.0, 5.0, 0.1, key=f"{P}c2m")
    with c4:
        u2 = st.number_input("u₂ before (m s⁻¹)", -50.0, 50.0, 0.0, 0.5, key=f"{P}c2u")

    result = (M.elastic_collision_1d(m1, u1, m2, u2) if kind == "Elastic"
              else M.inelastic_collision_1d(m1, u1, m2, u2))
    st.markdown(VIS_collision(m1, u1, m2, u2, result["v1"], result["v2"],
                              kind == "Elastic"),
                unsafe_allow_html=True)
    ledger = pd.DataFrame([
        {"quantity": "total momentum", "before": f"{result['momentum_before']:.4g}",
         "after": f"{result['momentum_after']:.4g}",
         "conserved?": "✓ yes" if result["momentum_conserved"] else "✗ no"},
        {"quantity": "kinetic energy", "before": f"{result['kinetic_before']:.4g} J",
         "after": f"{result['kinetic_after']:.4g} J",
         "conserved?": "✓ yes" if result["kinetic_conserved"] else
                       f"✗ no — {result['kinetic_lost']:.4g} J became heat and sound"},
    ])
    st.dataframe(ledger, use_container_width=True, hide_index=True)
    if result["momentum_conserved"]:
        st.success("Momentum balances exactly. This is always true for a closed system, "
                   "whatever else happens.")
    if not result["kinetic_conserved"]:
        st.warning(f"{result['kinetic_lost']:.4g} J of kinetic energy did not vanish — it "
                   f"became heat, sound and permanent deformation, and none of it can be "
                   f"got back.")

    st.subheader("The elastic formulas")
    st.dataframe(pd.DataFrame([
        {"result": f["result"], "formula": f["formula"], "note": f["note"]}
        for f in D.ELASTIC_FORMULAS
    ]), use_container_width=True, hide_index=True)
    guidance(TRY_IT, "Set m₁ = m₂ and watch them swap",
             "With equal masses the formulas reduce to v₁ = u₂ and v₂ = u₁. Change m₂ to "
             "twice m₁ and the reversal appears — which is what makes a squash shot work.")
    guidance(WATCH_OUT, "Negative does not mean wrong",
             "In the bench above, v₁ = −2 m s⁻¹ means the body rebounded. Always write the "
             "sign explicitly; a bare number loses the direction, which is the whole point of "
             "one-dimensional momentum.")


def VIS_collision(m1, u1, m2, u2, v1, v2, elastic):
    w, h = 660, 320
    lane = 110
    scale = 0.9
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'{"ELASTIC" if elastic else "PERFECTLY INELASTIC"} COLLISION</text>']
    for index, (label, before, after, colour) in enumerate([
            ("body 1", u1, v1, CYAN), ("body 2", u2, v2, AMBER)]):
        y = 70 + index * lane
        parts.append(f'<line x1="30" y1="{y}" x2="630" y2="{y}" stroke="#1b3350" '
                     f'stroke-width="1"/>')
        parts.append(f'<text x="30" y="{y - 14}" fill="{MUTED}" font-size="11" '
                     f'font-family="Sora, sans-serif">{label}</text>')
        bx = 330 + before * 14 * scale
        ax = 330 + after * 14 * scale
        parts.append(f'<rect x="{min(bx, ax) - 11:.1f}" y="{y - 11}" width="22" '
                     f'height="22" rx="5" fill="{colour}" opacity="0.85"/>')
        parts.append(f'<line x1="330" y1="{y - 26}" x2="330" y2="{y + 26}" stroke="{MUTED}" '
                     f'stroke-width="1.5" stroke-dasharray="4 3"/>')
        parts.append(f'<text x="338" y="{y - 22}" fill="{colour}" font-size="11" '
                     f'font-family="JetBrains Mono, monospace">'
                     f'before {before:g} → after {after:g} m s⁻¹</text>')
    parts.append(f'<text x="30" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">'
                 f'{"Both momentum and kinetic energy are conserved." if elastic else "Only momentum survives; the rest becomes heat."}'
                 f'</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;'
            f'display:block;margin:0 auto">{"".join(parts)}</svg>')


def _oblique() -> None:
    how_to("numbers"), how_to("sliders"),
    st.subheader("3.2.5 · Collisions in two dimensions")
    card("There is one direction in which this problem is easy",
         "<p>Along the line joining the centres, the collision is exactly the "
         "one-dimensional case. Across it, nothing happens at all. So split, solve, and "
         "recombine.</p>", "THE IDEA")
    st.markdown("\n\n".join(f"{i}. {step}" for i, step in enumerate(D.OBLIQUE_METHOD, 1)))

    c1, c2, c3 = st.columns(3)
    with c1:
        m1 = st.number_input("moving ball m₁ (kg)", 0.1, 50.0, 1.0, 0.1, key=f"{P}o1m")
    with c2:
        speed = st.number_input("speed (m s⁻¹)", 1.0, 50.0, 10.0, 0.5, key=f"{P}osp")
    with c3:
        restitution = st.slider("coefficient of restitution e", 0.0, 1.0, 1.0, 0.05,
                                key=f"{P}ore")
    offset = st.slider("how far apart the centres are", 0.2, 1.0, 0.5, 0.05, key=f"{P}ood")
    m2 = 2.0
    p1 = (speed, 0.0)
    p2 = (offset, -offset * 0.4)
    result = M.two_dimensional_collision(m1, p1, m2, p2, restitution)
    if "error" in result:
        st.warning(result["error"])
    else:
        st.markdown(V2.vector_arrow(p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1]),
                    unsafe_allow_html=True)
        st.dataframe(pd.DataFrame([
            {"quantity": "angle between the balls", "value": f"{result['centre_angle_deg']:.2f}°"},
            {"quantity": "v₁ after", "value": f"({result['v1'][0]:.4g}, {result['v1'][1]:.4g}) m s⁻¹"},
            {"quantity": "v₂ after", "value": f"({result['v2'][0]:.4g}, {result['v2'][1]:.4g}) m s⁻¹"},
            {"quantity": "momentum in x",
             "value": "conserved ✓" if result["momentum_conserved"] else "NOT conserved ✗"},
        ]), use_container_width=True, hide_index=True)
        st.info(f"At e = {restitution:g}: "
                f"{'a perfectly elastic bounce' if restitution == 1 else 'some energy lost to heat and deformation'}. "
                f"At e = 0 the balls would share one common velocity.")
    guidance(EXAM_TIP, "Draw the line of centres first",
             "In a real two-dimensional collision question the diagram usually tells you the "
             "answer before any arithmetic does. Mark the centres, draw the line, and the "
             "path of each ball usually becomes obvious.")


def _work() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("3.3 · Work, and the area under a force–displacement graph")
    st.latex(r"W = \mathbf{F}\cdot\mathbf{d} = Fd\cos\theta")
    st.dataframe(pd.DataFrame([
        {"θ": c["theta"], "cos θ": c["cos"], "sign": c["sign"], "meaning": c["meaning"],
         "example": c["example"]} for c in D.WORK_ANGLE_CASES
    ]), use_container_width=True, hide_index=True)

    st.subheader("The work bench")
    f_col, th_col, d_col = st.columns(3)
    with f_col:
        force = st.number_input("force F (N)", 0.0, 1000.0, 40.0, 5.0, key=f"{P}wf")
    with th_col:
        angle = st.slider("angle to the displacement (°)", 0.0, 180.0, 60.0, 5.0,
                          key=f"{P}wth")
    with d_col:
        distance = st.number_input("displacement d (m)", 0.0, 100.0, 2.0, 0.1, key=f"{P}wd")
    st.markdown(VIS_fd(force, angle, distance), unsafe_allow_html=True)

    st.markdown(VIS_fd_shapes(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"shape": c["shape"], "area": c["area"], "meaning": c["meaning"],
         "look for": c["diagram"]} for c in D.FD_CASES
    ]), use_container_width=True, hide_index=True)
    guidance(WATCH_OUT, "Negative area is real",
             "A resistive force draws the curve below the axis, and the area there is "
             "negative work. That is not a mistake in the diagram; it is exactly why the "
             "sum of a forward push and friction can be smaller than the push alone.")


def _fd(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def VIS_fd(force, angle, distance):
    w, h = 620, 320
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'AREA UNDER THE FORCE – DISPLACEMENT GRAPH</text>']
    left, bottom, right, top = 80, 270, w - 30, 54
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" '
                 f'stroke="{MUTED}" stroke-width="2"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{left}" y2="{top}" '
                 f'stroke="{MUTED}" stroke-width="2"/>')
    span = max(distance, 1e-6)
    parts.append(f'<polygon points="{left},{bottom} {right},{bottom} '
                 f'{right},{bottom - 90}" fill="{TEAL}" opacity="0.25"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom - 90}" '
                 f'stroke="{TEAL}" stroke-width="3.5"/>')
    components = force * math.cos(math.radians(angle))
    wasted = force * math.sin(math.radians(angle))
    parts.append(f'<text x="{right - 6}" y="{bottom - 100}" text-anchor="end" '
                 f'fill="{TEAL}" font-size="13" font-family="JetBrains Mono, monospace">'
                 f'F cos θ = {components:.4g} N</text>')
    parts.append(f'<text x="{right - 6}" y="{bottom + 20}" text-anchor="end" '
                 f'fill="{MUTED}" font-size="12" font-family="JetBrains Mono, monospace">'
                 f'd = {distance:g} m</text>')
    parts.append(f'<text x="{left + 12}" y="{top + 16}" fill="{ROSE}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">F sin θ = {wasted:.4g} N does '
                 f'no work at all</text>')
    parts.append(f'<rect x="{left}" y="{top + 34}" width="330" height="56" rx="10" '
                 f'fill="#0d1c30" stroke="{AMBER}" stroke-opacity="0.5"/>'
                 f'<text x="{left + 14}" y="{top + 56}" fill="{AMBER}" font-size="18" '
                 f'font-weight="800" font-family="JetBrains Mono, monospace">'
                 f'{_fd(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;'
            f'display:block;margin:0 auto">{"".join(parts)}</svg>')


def VIS_fd_shapes():
    w, h = 680, 200
    shapes = [("rectangle", CYAN, "constant force → W = Fd"),
              ("triangle", TEAL, "spring → W = ½kx²"),
              ("below axis", ROSE, "friction → negative work"),
              ("crossing", AMBER, "signed sum — parts cancel")]
    parts = [f'<text x="20" y="22" fill="{MUTED}" font-size="11" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'FOUR F–d SHAPES</text>']
    for index, (name, colour, note) in enumerate(shapes):
        x0 = 24 + index * 162
        base = 168
        parts.append(f'<line x1="{x0}" y1="{base}" x2="{x0 + 140}" y2="{base}" '
                     f'stroke="{MUTED}" stroke-width="1.5"/>')
        if name == "rectangle":
            parts.append(f'<rect x="{x0 + 20}" y="{base - 62}" width="100" height="62" '
                         f'fill="{colour}" opacity="0.3"/>'
                         f'<line x1="{x0 + 20}" y1="{base - 62}" x2="{x0 + 120}" '
                         f'y2="{base - 62}" stroke="{colour}" stroke-width="2.5"/>')
        elif name == "triangle":
            parts.append(f'<polygon points="{x0 + 20},{base} {x0 + 120},{base - 62} '
                         f'{x0 + 120},{base}" fill="{colour}" opacity="0.3"/>'
                         f'<line x1="{x0 + 20}" y1="{base}" x2="{x0 + 120}" '
                         f'y2="{base - 62}" stroke="{colour}" stroke-width="2.5"/>')
        elif name == "below axis":
            parts.append(f'<rect x="{x0 + 20}" y="{base}" width="100" height="44" '
                         f'fill="{colour}" opacity="0.3"/>'
                         f'<line x1="{x0 + 20}" y1="{base + 44}" x2="{x0 + 120}" '
                         f'y2="{base + 44}" stroke="{colour}" stroke-width="2.5"/>')
        else:
            points = (f"{x0 + 20},{base} {x0 + 55},{base - 50} {x0 + 90},{base + 38} "
                      f"{x0 + 120},{base - 26}")
            parts.append(f'<polyline points="{points}" fill="none" stroke="{colour}" '
                         f'stroke-width="2.5"/>')
        parts.append(f'<text x="{x0 + 70}" y="{base - 70}" text-anchor="middle" '
                     f'fill="{colour}" font-size="12" font-weight="700">{name}</text>')
        parts.append(f'<text x="{x0 + 70}" y="192" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="9" font-family="Sora, sans-serif">{note}</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;'
            f'display:block;margin:0 auto">{"".join(parts)}</svg>')


def _fields() -> None:
    how_to("numbers"),
    st.subheader("3.4 · Conservative and non-conservative fields")
    card("Path or no path?",
         "<p>Conserve the energy and the work between two points is the same whichever "
         "way you go. Dissipate it and the route matters.</p>", "THE IDEA")
    st.dataframe(pd.DataFrame([
        {"field": f["field"], "conservative?": "yes ✓" if f["conservative"] else "no ✗",
         "work done": f["work"], "test": f["test"], "stored as": f["potential"]}
        for f in D.FIELD_EXAMPLES
    ]), use_container_width=True, hide_index=True)

    st.subheader("Run the test yourself")
    force = st.number_input("force along the displacement (N)", -50.0, 50.0, -5.0, 1.0,
                            key=f"{P}ff")
    direct = st.number_input("direct path length (m)", 0.0, 100.0, 3.0, 0.5, key=f"{P}fd1")
    detour = st.number_input("total length of the detouring path (m)", 0.0, 200.0, 4.0,
                             0.5, key=f"{P}fd2")
    w_direct = force * direct
    w_detour = force * detour
    st.dataframe(pd.DataFrame([
        {"path": "direct", "work": f"{w_direct:.4g} J"},
        {"path": "detour", "work": f"{w_detour:.4g} J"},
        {"path": "difference", "work": f"{w_detour - w_direct:.4g} J"},
    ]), use_container_width=True, hide_index=True)
    if abs(w_detour - w_direct) < 1e-9:
        st.success("The work is the same either way, so the field is conservative. The "
                   "energy is stored and recoverable.")
    else:
        st.error(f"The two paths differ by {abs(w_detour - w_direct):.4g} J, so the field is "
                 f"non-conservative. The energy was dissipated along the way.")
    st.caption("Try a constant force of 0 N: every route gives the same work, because no "
               "energy is being moved or dissipated at all.")
    guidance(HONEST_LIMIT, "'Conservative' is about the work, not the force",
             "Gravity is a strong force and a conservative field. Friction is often weak "
             "and always non-conservative. The word describes whether the energy can be "
             "got back, not how large the force is.")


def _energy() -> None:
    how_to("numbers"),
    st.subheader("3.5 · The work-energy theorem")
    st.latex(r"W = \Delta K = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2")
    card("Split the work by force, then add",
         "<p>The net work is the sum of the work done by *every* force. In a resistive "
         "medium one of those terms is negative, and that is the whole difference between "
         "the two cases.</p>", "THE IDEA")

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        mass = st.number_input("mass m (kg)", 0.1, 100.0, 5.0, 0.5, key=f"{P}em")
    with c2:
        u = st.number_input("initial speed u (m s⁻¹)", 0.0, 100.0, 4.0, 0.5, key=f"{P}eu")
    with c3:
        v = st.number_input("final speed v (m s⁻¹)", 0.0, 100.0, 0.0, 0.5, key=f"{P}ev")
    with c4:
        distance = st.number_input("distance (m)", 0.0, 200.0, 10.0, 0.5, key=f"{P}ed")
    with c5:
        friction = st.number_input("friction force (N)", 0.0, 200.0, 10.0, 1.0, key=f"{P}ef")

    check = M.work_energy_check(mass, u, v, friction=friction)
    st.dataframe(pd.DataFrame([
        {"quantity": "initial kinetic energy", "value": f"{M.kinetic_energy(mass, u):.4g} J"},
        {"quantity": "final kinetic energy", "value": f"{M.kinetic_energy(mass, v):.4g} J"},
        {"quantity": "change in kinetic energy", "value": f"{check['delta_kinetic']:.4g} J"},
        {"quantity": "work done against friction", "value": f"{check['work_friction']:.4g} J"},
        {"quantity": "work done by the other forces",
         "value": f"{check['work_other_forces']:.4g} J"},
        {"quantity": "net work", "value": f"{check['net_work']:.4g} J"},
    ]), use_container_width=True, hide_index=True)
    if check["consistent"]:
        st.success("Net work equals the change in kinetic energy exactly. The theorem holds "
                   "with friction present as well as without it.")
    else:
        st.error("They do not agree — check that every force has been counted.")

    if friction > 0:
        needed = abs(check["delta_kinetic"]) / friction
        st.metric("Stopping distance if only friction acts", f"{needed:.3g} m")
        st.caption(f"Against {distance:g} m of travel, "
                   f"{'friction alone brings it to rest' if needed <= distance else 'friction alone would not be enough'}.")
    st.dataframe(pd.DataFrame([
        {"case": c["case"], "net work (J)": c["work"], "change in K (J)": c["delta_k"],
         "explanation": c["explanation"]} for c in D.WORK_ENERGY_WORKED
    ]), use_container_width=True, hide_index=True)
    guidance(EXAM_TIP, "The mass often cancels",
             "In W = Fd = ΔK, the mass appears on both sides. If a problem gives you a mass "
             "and then the answer does not need it, that is a strong hint the work-energy "
             "theorem is the intended route.")


def _equations() -> None:
    st.subheader("3.1 · Equations of motion")
    st.dataframe(pd.DataFrame([
        {"name": e["name"], "formula": e["formula"], "use it when": e["uses"],
         "what it says": e["says"]} for e in D.KINEMATIC_EQUATIONS
    ]), use_container_width=True, hide_index=True)
    for row in D.KINEMATIC_EQUATIONS:
        st.latex(row["formula"])
        st.latex(row["check"])
    card("Uniform acceleration is a promise",
         "<p>These three equations only hold when the acceleration is constant. That is "
         "worth saying out loud in every answer, because it is the assumption examiners "
         "check first.</p>", "THE ASSUMPTION")
    _motion_lab()
    guidance(TRY_IT, "Set a = 0",
             "With zero acceleration the first equation gives v = u and the second gives "
             "s = ut. That is just 'distance = speed × time', which is what these three "
             "equations reduce to when nothing is accelerating.")


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "equations": _equations,
    "freefall": _freefall,
    "momentum": _momentum,
    "collisions": _collisions,
    "oblique": _oblique,
    "work": _work,
    "fields": _fields,
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
    title="Motion in One Dimension",
    blurb="Equations of motion, conservation of momentum, work and the work-energy theorem.",
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
