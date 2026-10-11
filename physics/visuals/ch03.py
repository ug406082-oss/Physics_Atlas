"""Chapter 3 diagrams: graphs of motion, the drop, collisions and force diagrams.

These used to be built inline in ``ch03.py``, which meant they were never
memoised and bypassed the shared wrapper's overflow protection. They now live
here like every other chapter's diagrams, behind ``@cached`` and ``wrap``.
"""

from __future__ import annotations

import math

from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, para, wrap

__all__ = ["three_graphs", "drop_diagram", "collision", "fd_shapes",
           "fd_chart", "graph_card"]

@cached


def graph_card(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def three_graphs(series, u, a, t_max) -> str:
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
    return wrap("".join(parts), w, h)




@cached
def drop_diagram(height: float, speed: float) -> str:
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
    return wrap("".join(parts), w, h)


def collision(m1, u1, m2, u2, v1, v2, elastic):
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
    return wrap("".join(parts), w, h)


def _fd_row(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def fd_chart(force, angle, distance):
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
                 f'{_fd_row(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return wrap("".join(parts), w, h)


def fd_shapes():
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
    return wrap("".join(parts), w, h)

@cached


def graph_card(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def three_graphs(series, u, a, t_max) -> str:
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
    return wrap("".join(parts), w, h)


def drop_diagram(height: float, speed: float) -> str:
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
    return wrap("".join(parts), w, h)


def collision(m1, u1, m2, u2, v1, v2, elastic):
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
    return wrap("".join(parts), w, h)


def _fd_row(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def fd_chart(force, angle, distance):
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
                 f'{_fd_row(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return wrap("".join(parts), w, h)


def fd_shapes():
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
    return wrap("".join(parts), w, h)

@cached


def graph_card(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def three_graphs(series, u, a, t_max) -> str:
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
    return wrap("".join(parts), w, h)


def drop_diagram(height: float, speed: float) -> str:
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
    return wrap("".join(parts), w, h)


def collision(m1, u1, m2, u2, v1, v2, elastic):
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
    return wrap("".join(parts), w, h)


def _fd_row(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def fd_chart(force, angle, distance):
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
                 f'{_fd_row(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return wrap("".join(parts), w, h)


def fd_shapes():
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
    return wrap("".join(parts), w, h)

@cached


def graph_card(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def three_graphs(series, u, a, t_max) -> str:
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
    return wrap("".join(parts), w, h)


def drop_diagram(height: float, speed: float) -> str:
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
    return wrap("".join(parts), w, h)


def collision(m1, u1, m2, u2, v1, v2, elastic):
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
    return wrap("".join(parts), w, h)


def _fd_row(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def fd_chart(force, angle, distance):
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
                 f'{_fd_row(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return wrap("".join(parts), w, h)


def fd_shapes():
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
    return wrap("".join(parts), w, h)

@cached


def graph_card(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def three_graphs(series, u, a, t_max) -> str:
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
    return wrap("".join(parts), w, h)


def drop_diagram(height: float, speed: float) -> str:
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
    return wrap("".join(parts), w, h)


def collision(m1, u1, m2, u2, v1, v2, elastic):
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
    return wrap("".join(parts), w, h)


def _fd_row(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def fd_chart(force, angle, distance):
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
                 f'{_fd_row(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return wrap("".join(parts), w, h)


def fd_shapes():
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
    return wrap("".join(parts), w, h)

@cached


def graph_card(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def three_graphs(series, u, a, t_max) -> str:
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
    return wrap("".join(parts), w, h)


def drop_diagram(height: float, speed: float) -> str:
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
    return wrap("".join(parts), w, h)


def collision(m1, u1, m2, u2, v1, v2, elastic):
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
    return wrap("".join(parts), w, h)


def _fd_row(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def fd_chart(force, angle, distance):
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
                 f'{_fd_row(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return wrap("".join(parts), w, h)


def fd_shapes():
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
    return wrap("".join(parts), w, h)

@cached


def graph_card(xs, ys, ylabel, colour, title):
    import plotly.graph_objects as go
    from ..theme import style_fig
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=list(xs), y=list(ys), mode="lines",
                                line=dict(color=colour, width=3)))
    figure.add_hline(y=0, line=dict(color=MUTED, width=1))
    figure.update_layout(title=title, xaxis=dict(title="t (s)"), yaxis=dict(title=ylabel))
    return style_fig(figure, 300)


def three_graphs(series, u, a, t_max) -> str:
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
    return wrap("".join(parts), w, h)


def drop_diagram(height: float, speed: float) -> str:
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
    return wrap("".join(parts), w, h)


def collision(m1, u1, m2, u2, v1, v2, elastic):
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
    return wrap("".join(parts), w, h)


def _fd_row(force, angle, distance):
    return (f"W = {force:g} × {distance:g} × cos({angle:g}°) = "
            f"{force * distance * math.cos(math.radians(angle)):.4g} J")


def fd_chart(force, angle, distance):
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
                 f'{_fd_row(force, angle, distance)}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only the component along the displacement '
                 f'does work, so the height of the graph is F cos θ, not F.</text>')
    return wrap("".join(parts), w, h)


def fd_shapes():
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
    return wrap("".join(parts), w, h)
