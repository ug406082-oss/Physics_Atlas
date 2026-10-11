"""Chapter 2 diagrams: scalars and vectors.

Every figure here is drawn for this chapter alone, in the same hand-written SVG
style as the rest of the library.
"""

from __future__ import annotations

import math

from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import MONO as _MONO, SANS as _SANS, cached, wrap
from .common import label as _label

__all__ = ["scalar_vector_strip", "vector_arrow", "component_rectangle",
           "resultant_parallelogram", "component_resultant",
           "dot_projection", "cross_parallelogram", "right_hand_rule", "angle_arc", "shadow_dial",
           "cross_plane", "torque_arc", "project_shadow"]


def _arrow(x0: float, y0: float, x1: float, y1: float, colour: str,
           width: float = 3, head: float = 12, dash: str = "", opacity: float = 1.0) -> str:
    """One arrow with a proper head, drawn from (x0, y0) to (x1, y1)."""
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy) or 1.0
    ux, uy = dx / length, dy / length
    # Stop the shaft short so the head sits neatly on the tip.
    sx, sy = x1 - ux * head * 0.8, y1 - uy * head * 0.8
    px, py = -uy, ux
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{sx:.1f}" y2="{sy:.1f}" '
        f'stroke="{colour}" stroke-width="{width}" stroke-linecap="round"{dash_attr} '
        f'opacity="{opacity}"/>'
        f'<polygon points="{x1:.1f},{y1:.1f} '
        f'{x1 - ux * head + px * head * 0.5:.1f},{y1 - uy * head + py * head * 0.5:.1f} '
        f'{x1 - ux * head - px * head * 0.5:.1f},{y1 - uy * head - py * head * 0.5:.1f}" '
        f'fill="{colour}" opacity="{opacity}"/>'
    )


def _axes(cx: float, cy: float, span: float, colour: str = MUTED,
          labels: bool = True) -> str:
    """A pair of labelled x and y axes through (cx, cy)."""
    parts = [
        _arrow(cx - span, cy, cx + span, cy, colour, 1.6, 9, opacity=0.8),
        _arrow(cx, cy + span * 0.62, cx, cy - span * 0.62, colour, 1.6, 9, opacity=0.8),
    ]
    if labels:
        parts.append(
            f'<text x="{cx + span + 4:.0f}" y="{cy + 5:.0f}" fill="{MUTED}" '
            f'font-size="15" font-family="JetBrains Mono, monospace">x</text>'
            f'<text x="{cx + 6:.0f}" y="{cy - span * 0.62 - 6:.0f}" fill="{MUTED}" '
            f'font-size="15" font-family="JetBrains Mono, monospace">y</text>'
        )
    return "".join(parts)


@cached
def scalar_vector_strip() -> str:
    """The same number, once without a direction and once with one.

    This is the whole point of Chapter 2 in one picture: 5 is not a vector, and
    5 newtons only becomes one when you say which way it acts.
    """
    w, h = 680, 250
    rows = [
        ("5", "just a number", MUTED, None),
        ("5 m s⁻¹", "a speed — size only", CYAN, None),
        ("5 m s⁻¹ due north", "a velocity — size and direction", TEAL, 90),
        ("5 m s⁻¹ due east", "a different velocity entirely", AMBER, 0),
    ]
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'THE SAME NUMBER, FOUR DIFFERENT MEANINGS</text>']
    y = 62
    for text, note, colour, direction in rows:
        parts.append(
            f'<text x="24" y="{y + 6}" fill="{colour}" font-size="19" font-weight="700" '
            f'font-family="JetBrains Mono, monospace">{text}</text>'
            f'<text x="250" y="{y + 5}" fill="#c6d6ea" font-size="14" '
            f'font-family="Sora, sans-serif">{note}</text>'
        )
        if direction is not None:
            cx, cy = 570, y - 4
            parts.append(_arrow(cx, cy, cx + 74, cy, MUTED, 1.4, 9, opacity=0.55))
            parts.append(_arrow(cx, cy,
                                cx + 74 * math.cos(math.radians(direction)),
                                cy - 74 * math.sin(math.radians(direction)),
                                colour, 2.6))
        y += 48
    parts.append(
        f'<text x="24" y="{h - 12}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">Two arrows of the same length pointing different '
        f'ways are different vectors, not the same vector twice.</text>'
    )
    return wrap("".join(parts), w, h, "The same number with and without a direction")


@cached
def vector_arrow(ax: float, ay: float, bx: float, by: float,
                 label_a: str = "A", label_b: str = "B",
                 show_components: bool = True, resultant: bool = True) -> str:
    """Two head-to-tail vectors with their components and the resultant."""
    w, h = 660, 420
    cx, cy, scale = 300, 330, 46.0
    ax *= scale
    ay *= -scale
    bx *= scale
    by *= -scale

    parts = [_axes(cx, cy, 280)]
    # Component rectangles, drawn as dashed guides.
    if show_components:
        parts.append(f'<rect x="{cx}" y="{cy + by:.1f}" width="{ax:.1f}" height="{ay:.1f}" '
                     f'fill="{CYAN}" opacity="0.10"/>')
        parts.append(f'<rect x="{cx + ax:.1f}" y="{cy}" width="{bx:.1f}" height="{by:.1f}" '
                     f'fill="{AMBER}" opacity="0.12"/>')
        parts.append(_arrow(cx, cy, cx + ax, cy, CYAN, 1.5, 9, dash="4 3", opacity=0.85))
        parts.append(_arrow(cx + ax, cy, cx + ax, cy + ay, CYAN, 1.5, 9, dash="4 3", opacity=0.85))
        parts.append(_arrow(cx, cy, cx, cy + by, AMBER, 1.5, 9, dash="4 3", opacity=0.85))
        parts.append(_arrow(cx, cy + by, cx + ax + bx, cy + by, AMBER, 1.5, 9, dash="4 3", opacity=0.85))

    parts.append(_arrow(cx, cy, cx + ax, cy + ay, CYAN, 3.2))
    parts.append(_arrow(cx + ax, cy + ay, cx + ax + bx, cy + by, AMBER, 3.2))
    if resultant:
        parts.append(_arrow(cx, cy, cx + ax + bx, cy + by, GREEN, 3.6))

    parts.append(
        f'<text x="{cx + ax + 10:.0f}" y="{cy + ay - 10:.0f}" fill="{CYAN}" font-size="17" '
        f'font-weight="700">{label_a}</text>'
        f'<text x="{cx + ax + bx - 12:.0f}" y="{cy + by - 12:.0f}" fill="{AMBER}" '
        f'font-size="17" font-weight="700">{label_b}</text>'
    )
    if resultant:
        parts.append(
            f'<text x="{cx + ax + bx + 12:.0f}" y="{cy + by + 20:.0f}" fill="{GREEN}" '
            f'font-size="17" font-weight="700">R = A + B</text>'
        )
    parts.append(
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'RESULTANT BY RECTANGULAR COMPONENTS</text>'
    )
    parts.append(
        f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">The two dashed rectangles have areas Ax·By and '
        f'Ay·Bx. These are equal and opposite, so they cancel, leaving the component '
        f'rectangle of the resultant.</text>'
    )
    return wrap("".join(parts), w, h, "Two vectors added by the rectangular component method")


@cached
def component_rectangle(magnitude: float, angle_deg: float) -> str:
    """One vector broken into its x and y components, with the right triangle."""
    w, h = 640, 380
    cx, cy, scale = 250, 300, 150.0
    ax = magnitude * scale * math.cos(math.radians(angle_deg))
    ay = magnitude * scale * math.sin(math.radians(angle_deg))

    parts = [_axes(cx, cy, 320)]
    parts.append(f'<polygon points="{cx},{cy} {cx + ax:.1f},{cy} {cx + ax:.1f},{cy - ay:.1f}" '
                 f'fill="{CYAN}" opacity="0.14"/>')
    parts.append(_arrow(cx, cy, cx + ax, cy, CYAN, 2, 11, dash="5 4"))
    parts.append(_arrow(cx, cy, cx, cy - ay, TEAL, 2, 11, dash="5 4"))
    parts.append(_arrow(cx, cy, cx + ax, cy - ay, AMBER, 3.4))
    parts.append(angle_arc(cx, cy, min(70, 12 + magnitude * 4), angle_deg, VIOLET))

    parts.append(
        f'<text x="{cx + ax / 2:.0f}" y="{cy + 18}" fill="{CYAN}" font-size="14" '
        f'font-family="JetBrains Mono, monospace">Ax = A cos θ</text>'
        f'<text x="{cx + 12}" y="{cy - ay / 2:.0f}" fill="{TEAL}" font-size="14" '
        f'font-family="JetBrains Mono, monospace">Ay</text>'
        f'<text x="{cx + ax + 12:.0f}" y="{cy - ay - 12:.0f}" fill="{AMBER}" font-size="16" '
        f'font-weight="700">A = {magnitude:g}</text>'
    )
    parts.append(
        f'<text x="{cx + ax / 2 + 10:.0f}" y="{cy - ay / 2:.0f}" fill="{VIOLET}" font-size="13" '
        f'font-family="JetBrains Mono, monospace">θ = {angle_deg:g}°</text>'
    )
    # The squared-length check.
    parts.append(
        f'<text x="20" y="{h - 34}" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace">'
        f'Ax² + Ay² = A² = {magnitude:g}² = {magnitude * magnitude:g}</text>'
        f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">Squaring and adding the components always gives '
        f'back the square of the magnitude — a free check on your arithmetic.</text>'
    )
    return wrap("".join(parts), w, h, "A vector resolved into rectangular components")


@cached
def angle_arc(cx: float, cy: float, radius: float, angle_deg: float,
              colour: str = VIOLET) -> str:
    """An arc showing an angle measured anticlockwise from the +x axis."""
    if angle_deg <= 0:
        return ""
    end = math.radians(angle_deg)
    x, y = cx + radius * math.cos(end), cy - radius * math.sin(end)
    large = 1 if angle_deg > 180 else 0
    return (
        f'<path d="M {cx + radius:.1f} {cy:.1f} A {radius:.1f} {radius:.1f} 0 {large} 0 '
        f'{x:.1f} {y:.1f}" fill="none" stroke="{colour}" stroke-width="2" opacity="0.8"/>'
    )


@cached
def resultant_parallelogram(magnitude_a: float, angle_a: float,
                            magnitude_b: float, angle_b: float) -> str:
    """The parallelogram construction behind the component method."""
    w, h = 620, 420
    cx, cy, scale = 190, 330, 40.0
    ax = magnitude_a * scale * math.cos(math.radians(angle_a))
    ay = -magnitude_a * scale * math.sin(math.radians(angle_a))
    bx = magnitude_b * scale * math.cos(math.radians(angle_b))
    by = -magnitude_b * scale * math.sin(math.radians(angle_b))

    parts = [_axes(cx, cy, 260)]
    parts.append(
        f'<polygon points="{cx:.1f},{cy:.1f} {cx + ax:.1f},{cy + ay:.1f} '
        f'{cx + ax + bx:.1f},{cy + ay + by:.1f} {cx + bx:.1f},{cy + by:.1f}" '
        f'fill="{VIOLET}" opacity="0.12"/>'
    )
    parts.append(_arrow(cx, cy, cx + ax, cy + ay, CYAN, 3))
    parts.append(_arrow(cx + ax, cy + ay, cx + ax + bx, cy + ay + by, CYAN, 2.4, 10, opacity=0.7))
    parts.append(_arrow(cx, cy, cx + bx, cy + by, AMBER, 3))
    parts.append(_arrow(cx + bx, cy + by, cx + ax + bx, cy + ay + by, AMBER, 2.4, 10, opacity=0.7))
    parts.append(_arrow(cx, cy, cx + ax + bx, cy + ay + by, GREEN, 3.6))
    parts.append(
        f'<text x="{cx + ax / 2:.0f}" y="{cy + ay / 2 - 10:.0f}" fill="{CYAN}" font-size="16" '
        f'font-weight="700">A = {magnitude_a:g}</text>'
        f'<text x="{cx + bx / 2:.0f}" y="{cy + by / 2 + 26:.0f}" fill="{AMBER}" font-size="16" '
        f'font-weight="700">B = {magnitude_b:g}</text>'
        f'<text x="{cx + ax + bx + 12:.0f}" y="{cy + ay + by + 6:.0f}" fill="{GREEN}" '
        f'font-size="16" font-weight="700">R</text>'
    )
    parts.append(
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'PARALLELOGRAM RULE</text>'
        f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">The diagonal is the resultant. Moving B is the '
        f'component method drawn on paper — the answer does not depend on the order.</text>'
    )
    return wrap("".join(parts), w, h, "Parallelogram rule for the resultant of two vectors")


@cached
def shadow_dial(angle_deg: float, magnitude_a: float = 5.0,
                magnitude_b: float = 4.0) -> str:
    """The scalar product as the shadow one vector casts on another."""
    w, h = 660, 340
    cx, cy, scale = 170, 250, 34.0
    ax = magnitude_a * scale
    bx = magnitude_b * scale * math.cos(math.radians(angle_deg))
    by = -magnitude_b * scale * math.sin(math.radians(angle_deg))
    scalar = magnitude_a * magnitude_b * math.cos(math.radians(angle_deg))

    parts = [_axes(cx, cy, 330)]
    # A is horizontal and fixed; B turns.
    parts.append(_arrow(cx, cy, cx + ax, cy, CYAN, 3.4))
    parts.append(_arrow(cx, cy, cx + bx, cy + by, AMBER, 3.4))
    # The shadow of B on A.
    shadow = abs(bx)
    parts.append(_arrow(cx, cy, cx + shadow, cy, TEAL, 2.6, 11, dash="6 4"))
    parts.append(angle_arc(cx, cy, 74, angle_deg, VIOLET))
    parts.append(
        f'<text x="{cx + 10}" y="{cy - 12}" fill="{CYAN}" font-size="16" font-weight="700">'
        f'A = {magnitude_a:g}</text>'
        f'<text x="{cx + bx - 14:.0f}" y="{cy + by - 14:.0f}" fill="{AMBER}" font-size="16" '
        f'font-weight="700">B = {magnitude_b:g}</text>'
        f'<text x="{cx + shadow + 8:.0f}" y="{cy + 22}" fill="{TEAL}" font-size="14" '
        f'font-family="JetBrains Mono, monospace">B cos θ</text>'
        f'<text x="{cx + 84}" y="{cy - 84}" fill="{VIOLET}" font-size="14" '
        f'font-family="JetBrains Mono, monospace">θ = {angle_deg:g}°</text>'
    )

    verdict = ("negative" if scalar < 0 else "zero" if abs(scalar) < 1e-9 else "positive")
    parts.append(
        f'<rect x="470" y="90" width="164" height="150" rx="12" fill="#0d1c30" '
        f'stroke="{VIOLET}" stroke-opacity="0.5"/>'
        f'<text x="552" y="120" text-anchor="middle" fill="{MUTED}" font-size="11" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="1.5">A · B</text>'
        f'<text x="552" y="164" text-anchor="middle" fill="{VIOLET}" font-size="27" '
        f'font-weight="800" font-family="JetBrains Mono, monospace">{scalar:.2f}</text>'
        f'<text x="552" y="192" text-anchor="middle" fill="#c6d6ea" font-size="12" '
        f'font-family="Sora, sans-serif">AB cos θ = {verdict}</text>'
        f'<text x="552" y="218" text-anchor="middle" fill="{MUTED}" font-size="11" '
        f'font-family="Sora, sans-serif">the length of the shadow</text>'
    )
    parts.append(
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'SCALAR PRODUCT AS A SHADOW</text>'
        f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">A · B is the length of B\'s shadow on A, taken with '
        f'a sign: positive when the angle is acute, negative when it is obtuse.</text>'
    )
    return wrap("".join(parts), w, h, "The scalar product shown as a projection")


@cached
def project_shadow(angle_deg: float, magnitude_a: float = 5.0,
                   magnitude_b: float = 4.0) -> str:
    """The part of B that lies along A, and the part that does not."""
    w, h = 620, 340
    cx, cy, scale = 160, 250, 32.0
    ax = magnitude_a * scale
    bx = magnitude_b * scale * math.cos(math.radians(angle_deg))
    by = -magnitude_b * scale * math.sin(math.radians(angle_deg))

    parts = [_axes(cx, cy, 300)]
    parts.append(_arrow(cx, cy, cx + ax, cy, CYAN, 3.2))
    parts.append(_arrow(cx, cy, cx + bx, cy + by, AMBER, 3.2))
    parts.append(_arrow(cx, cy, cx + bx, cy, GREEN, 2.4, 10, dash="6 4"))
    parts.append(_arrow(cx + bx, cy, cx + bx, cy + by, ROSE, 2.4, 10, dash="6 4"))
    parts.append(
        f'<text x="{cx + max(bx, 20) / 2:.0f}" y="{cy + 24}" fill="{GREEN}" font-size="13" '
        f'font-family="JetBrains Mono, monospace">along A: B cos θ</text>'
        f'<text x="{cx + bx + 12:.0f}" y="{cy + by / 2:.0f}" fill="{ROSE}" font-size="13" '
        f'font-family="JetBrains Mono, monospace">across</text>'
    )
    parts.append(
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'RESOLVING B RELATIVE TO A</text>'
        f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">Only the green part does work when B is applied to a '
        f'body moving along A. That is exactly what the scalar product measures.</text>'
    )
    return wrap("".join(parts), w, h, "A vector resolved along and across another vector")


@cached
def cross_plane(angle_deg: float, magnitude_a: float = 5.0,
                magnitude_b: float = 4.0) -> str:
    """The vector product: the turn between two vectors, and where it points."""
    w, h = 680, 380
    cx, cy, scale = 210, 290, 40.0
    ax = magnitude_a * scale
    bx = magnitude_b * scale * math.cos(math.radians(angle_deg))
    by = -magnitude_b * scale * math.sin(math.radians(angle_deg))
    cross = magnitude_a * magnitude_b * math.sin(math.radians(angle_deg))

    parts = [_axes(cx, cy, 300)]
    parts.append(f'<rect x="{cx - 290}" y="{cy - 190}" width="580" height="380" fill="{MUTED}" '
                 f'opacity="0.05"/>')
    parts.append(_arrow(cx, cy, cx + ax, cy, CYAN, 3.4))
    parts.append(_arrow(cx, cy, cx + bx, cy + by, AMBER, 3.4))
    parts.append(angle_arc(cx, cy, 92, angle_deg, VIOLET))

    # The parallelogram whose area is the magnitude of the cross product.
    parts.append(
        f'<polygon points="{cx:.1f},{cy:.1f} {cx + ax:.1f},{cy:.1f} '
        f'{cx + ax + bx:.1f},{cy + by:.1f} {cx + bx:.1f},{cy + by:.1f}" '
        f'fill="{TEAL}" opacity="0.10" stroke="{TEAL}" stroke-opacity="0.4" '
        f'stroke-dasharray="4 3"/>'
    )
    out_of_page = cross >= 0
    tip = "OUT OF THE PAGE (towards you)" if out_of_page else "INTO THE PAGE (away from you)"
    tip_colour = GREEN if out_of_page else ROSE
    parts.append(
        f'<circle cx="560" cy="150" r="44" fill="{tip_colour}" opacity="0.16"/>'
        f'<text x="560" y="143" text-anchor="middle" fill="{tip_colour}" font-size="34">'
        f'{"⊙" if out_of_page else "⊗"}</text>'
        f'<text x="560" y="172" text-anchor="middle" fill="{tip_colour}" font-size="11" '
        f'font-family="JetBrains Mono, monospace">A × B</text>'
        f'<text x="560" y="212" text-anchor="middle" fill="#c6d6ea" font-size="12" '
        f'font-family="Sora, sans-serif">{tip}</text>'
        f'<text x="560" y="232" text-anchor="middle" fill="{VIOLET}" font-size="14" '
        f'font-family="JetBrains Mono, monospace">|A × B| = {cross:.2f}</text>'
    )
    parts.append(
        f'<text x="{cx + ax / 2:.0f}" y="{cy - 12}" fill="{CYAN}" font-size="16" '
        f'font-weight="700">A</text>'
        f'<text x="{cx + bx - 16:.0f}" y="{cy + by - 14:.0f}" fill="{AMBER}" font-size="16" '
        f'font-weight="700">B</text>'
        f'<text x="{cx + 100}" y="{cy - 106}" fill="{VIOLET}" font-size="13" '
        f'font-family="JetBrains Mono, monospace">θ = {angle_deg:g}°</text>'
    )
    parts.append(
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'VECTOR PRODUCT</text>'
        f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">The dotted parallelogram has area AB sin θ. Its normal '
        f'gives the direction — anticlockwise gives ⊙, clockwise gives ⊗.</text>'
    )
    return wrap("".join(parts), w, h, "The vector product and its direction")


@cached
def torque_arc(r: float, force_deg: float, f: float, F: float,
               handle_deg: float = 0.0) -> str:
    """A lever, a force at an angle, and the torque it produces."""
    w, h = 640, 380
    cx, cy, scale = 200, 300, 60.0
    handle = r * scale
    fx = cx + handle * math.cos(math.radians(handle_deg))
    fy = cy - handle * math.sin(math.radians(handle_deg))
    ax = fx + F * scale * 0.55 * math.cos(math.radians(force_deg))
    ay = fy - F * scale * 0.55 * math.sin(math.radians(force_deg))
    # The perpendicular component of the force is the one that turns the lever.
    perp = F * math.cos(math.radians(force_deg - handle_deg))
    tau = r * F * math.sin(math.radians(force_deg - handle_deg))
    turning = (force_deg - handle_deg) * F * r

    parts = [_axes(cx, cy, 300)]
    parts.append(f'<rect x="{cx - 12}" y="{cy}" width="24" height="60" rx="5" '
                 f'fill="{MUTED}" opacity="0.4"/>')
    parts.append(_arrow(cx, cy, fx, fy, CYAN, 3.4))
    parts.append(_arrow(fx, fy, ax, ay, AMBER, 3.4))
    parts.append(angle_arc(fx, fy, 44, force_deg, VIOLET))
    # Circular arrow showing the sense of the turn.
    arrow_colour = GREEN if turning > 0 else ROSE
    parts.append(
        f'<path d="M {cx + 78:.0f} {cy:.0f} A 78 78 0 0 1 {cx + 55:.0f} {cy + 56:.0f}" '
        f'fill="none" stroke="{arrow_colour}" stroke-width="3"/>'
        f'<polygon points="{cx + 55:.0f},{cy + 62:.0f} {cx + 44:.0f},{cy + 54:.0f} '
        f'{cx + 56:.0f},{cy + 48:.0f}" fill="{arrow_colour}"/>'
    )
    parts.append(
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">TORQUE</text>'
        f'<text x="{cx + 92:.0f}" y="{cy + 26:.0f}" fill="{arrow_colour}" font-size="12" '
        f'font-family="JetBrains Mono, monospace">'
        f'{"anticlockwise" if turning > 0 else "clockwise"}</text>'
        f'<text x="{fx + 16:.0f}" y="{ay - 8:.0f}" fill="{AMBER}" font-size="15" '
        f'font-weight="700">F = {F:g}</text>'
        f'<text x="{cx + handle / 2:.0f}" y="{cy + 26}" fill="{CYAN}" font-size="14" '
        f'font-family="JetBrains Mono, monospace">r = {r:g}</text>'
        f'<text x="{fx + 52:.0f}" y="{fy - 52:.0f}" fill="{VIOLET}" font-size="13" '
        f'font-family="JetBrains Mono, monospace">φ = {force_deg - handle_deg:g}°</text>'
        f'<text x="430" y="140" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace">F_perp = F cos φ</text>'
        f'<text x="430" y="162" fill="{TEAL}" font-size="17" '
        f'font-family="JetBrains Mono, monospace">{perp:.2f} N</text>'
        f'<text x="430" y="200" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace">τ = r F sin φ</text>'
        f'<text x="430" y="228" fill="{VIOLET}" font-size="24" font-weight="800" '
        f'font-family="JetBrains Mono, monospace">{tau:.2f} N m</text>'
    )
    parts.append(
        f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="12" '
        f'font-family="Sora, sans-serif">Only the component perpendicular to the lever turns '
        f'it. Push along the lever and the torque is exactly zero.</text>'
    )
    return wrap("".join(parts), w, h, "Torque produced by a force at an angle to a lever")


@cached
def component_resultant(amag, aang, bmag, bang):
    """Two vectors resolved into components, and their resultant drawn to scale."""
    w, h = 660, 400
    left, right, base, top = 70, 620, 340, 60
    ax = amag * math.cos(math.radians(aang))
    ay = amag * math.sin(math.radians(aang))
    bx = bmag * math.cos(math.radians(bang))
    by = bmag * math.sin(math.radians(bang))
    rx, ry = ax + bx, ay + by
    reach = max(amag, bmag, math.hypot(rx, ry), 1e-6) * 1.25

    def X(v):
        return left + 270 + v / reach * 200

    def Y(v):
        return base - v / reach * 180

    parts = [_label(20, 24, "ADDING BY RECTANGULAR COMPONENTS", MUTED, 12),
             _label(20, 42, "Both vectors are resolved first. The parallelogram shows that "
                            "the resultant is the diagonal.", MUTED, 10, family=_SANS)]
    parts.append(_axes(X(0), Y(0), reach * 200 / 1.25 * 1.35))
    # dashed component rectangles
    parts.append(f'<line x1="{X(0):.1f}" y1="{Y(ay):.1f}" x2="{X(ax):.1f}" y2="{Y(ay):.1f}" '
                 f'stroke="{CYAN}" stroke-width="1" stroke-dasharray="3 3" opacity="0.7"/>')
    parts.append(f'<line x1="{X(ax):.1f}" y1="{Y(0):.1f}" x2="{X(ax):.1f}" y2="{Y(ay):.1f}" '
                 f'stroke="{CYAN}" stroke-width="1" stroke-dasharray="3 3" opacity="0.7"/>')
    parts.append(f'<line x1="{X(rx):.1f}" y1="{Y(ay):.1f}" x2="{X(rx):.1f}" y2="{Y(by):.1f}" '
                 f'stroke="{TEAL}" stroke-width="1" stroke-dasharray="3 3" opacity="0.7"/>')
    parts.append(f'<line x1="{X(0):.1f}" y1="{Y(ry):.1f}" x2="{X(rx):.1f}" y2="{Y(ry):.1f}" '
                 f'stroke="{TEAL}" stroke-width="1" stroke-dasharray="3 3" opacity="0.7"/>')
    # parallelogram
    parts.append(f'<polygon points="{X(0):.1f},{Y(0):.1f} {X(ax):.1f},{Y(ay):.1f} '
                 f'{X(rx):.1f},{Y(ry):.1f} {X(bx):.1f},{Y(by):.1f}" fill="{VIOLET}" '
                 f'opacity="0.10" stroke="{VIOLET}" stroke-width="1.2" stroke-dasharray="5 3"/>')
    parts.append(_arrow(X(0), Y(0), X(ax), Y(ay), CYAN, 3))
    parts.append(_arrow(X(ax), Y(ay), X(rx), Y(ry), TEAL, 3))
    parts.append(_arrow(X(bx), Y(by), X(rx), Y(ry), AMBER, 3))
    parts.append(_arrow(X(0), Y(0), X(rx), Y(ry), GREEN, 4))
    parts.append(_label(X(ax) + 6, Y(ay) - 8, "A", CYAN, 13))
    parts.append(_label(X(rx) + 6, Y(ry) - 8, "B", AMBER, 13))
    parts.append(_label(X(rx) + 10, Y(ry) + 16, f"R = {math.hypot(rx, ry):.4g} at "
                        f"{math.degrees(math.atan2(ry, rx)) % 360:.3g}°", GREEN, 12))
    rows = [("Ax", ax, CYAN), ("Ay", ay, CYAN), ("Bx", bx, AMBER), ("By", by, AMBER),
            ("Rx", rx, GREEN), ("Ry", ry, GREEN)]
    y = 96
    for name, value, colour in rows:
        parts.append(_label(432, y, f"{name} = {value:+.4g}", colour, 11, family=_MONO))
        y += 17
    parts.append(_label(20, h - 14, "dashed lines are the projections onto each axis",
                        MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Adding two vectors by components")


@cached
def dot_projection(amag, bmag, angle_deg):
    """The shadow B casts on A, which is the dot product."""
    w, h = 660, 320
    ox, oy = 140, 180
    scale = 170 / max(amag, bmag, 1e-6)
    parts = [_label(20, 24, "THE DOT PRODUCT AS A SHADOW", MUTED, 12),
             _label(20, 42, "B's component along A, signed. The bar under the figure is the "
                            "result itself.", MUTED, 10, family=_SANS)]
    parts.append(_arrow(ox, oy, ox + amag * scale, oy, CYAN, 3.4))
    parts.append(_label(ox + amag * scale / 2, oy - 12, "A", CYAN, 13, "middle"))
    ang = math.radians(angle_deg)
    tip = (ox + bmag * scale * math.cos(ang), oy - bmag * scale * math.sin(ang))
    parts.append(_arrow(ox, oy, tip[0], tip[1], AMBER, 3.4))
    parts.append(_label((ox + tip[0]) / 2 - 10, (oy + tip[1]) / 2, "B", AMBER, 13))
    proj = bmag * math.cos(ang)
    parts.append(_label(432, 96, f"|A||B|cosθ = {proj:+.4g}", GREEN, 14, family=_MONO))
    parts.append(_label(432, 118, f"cos {angle_deg:g}° = {math.cos(ang):+.4g}", MUTED, 11,
                        family=_MONO))
    parts.append(_label(432, 138, f"A.B = {amag * proj:+.4g}", GREEN, 12, family=_MONO))
    # signed bar
    parts.append(f'<rect x="432" y="170" width="190" height="18" rx="5" fill="{MUTED}" '
                 f'opacity="0.18"/>')
    frac = max(-1.0, min(1.0, math.cos(ang)))
    if frac >= 0:
        parts.append(f'<rect x="432" y="170" width="{95 * frac:.1f}" height="18" rx="5" '
                     f'fill="{GREEN}"/>')
    else:
        parts.append(f'<rect x="{432 + 95 * frac:.1f}" y="170" width="{95 * -frac:.1f}" '
                     f'height="18" rx="5" fill="{ROSE}"/>')
    parts.append(_label(432, 204, "0", MUTED, 9))
    parts.append(_label(622, 204, "+|B|", MUTED, 9, "end"))
    parts.append(_label(432, 236, "sign follows the direction of the projection", MUTED, 10,
                        family=_SANS))
    # projection foot
    foot = ox + bmag * scale * math.cos(ang)
    parts.append(f'<line x1="{foot:.1f}" y1="{oy:.1f}" x2="{foot:.1f}" y2="{oy - 12:.1f}" '
                 f'stroke="{GREEN}" stroke-width="1.4"/>')
    parts.append(_label(foot, oy - 20, "foot of the projection", GREEN, 9, "middle", _SANS))
    return wrap("".join(parts), w, h, "Dot product as a projection")


@cached
def cross_parallelogram(amag, bmag, angle_deg):
    """The parallelogram whose area is the cross product."""
    w, h = 660, 320
    ox, oy = 150, 210
    scale = 150 / max(amag, bmag, 1e-6)
    ang = math.radians(angle_deg)
    ax, ay = amag * scale, 0.0
    bx, by = bmag * scale * math.cos(ang), -bmag * scale * math.sin(ang)
    parts = [_label(20, 24, "THE CROSS PRODUCT AS AN AREA", MUTED, 12),
             _label(20, 42, "The magnitude is the area of the parallelogram the two vectors "
                            "span.", MUTED, 10, family=_SANS)]
    parts.append(f'<polygon points="{ox:.1f},{oy:.1f} {ox + ax:.1f},{oy + ay:.1f} '
                 f'{ox + ax + bx:.1f},{oy + ay + by:.1f} {ox + bx:.1f},{oy + by:.1f}" '
                 f'fill="{VIOLET}" opacity="0.14" stroke="{VIOLET}" stroke-width="1.3" '
                 f'stroke-dasharray="5 3"/>')
    parts.append(_arrow(ox, oy, ox + ax, oy + ay, CYAN, 3.2))
    parts.append(_arrow(ox, oy, ox + bx, oy + by, AMBER, 3.2))
    parts.append(_arrow(ox + bx, oy + by, ox + ax + bx, oy + ay + by, CYAN, 3.2))
    parts.append(_arrow(ox + ax, oy + ay, ox + ax + bx, oy + ay + by, AMBER, 3.2))
    parts.append(_label(ox + ax / 2, oy + 16, "A", CYAN, 13, "middle"))
    parts.append(_label(ox + bx / 2 - 12, oy + by / 2, "B", AMBER, 13, "middle"))
    mag = amag * bmag * math.sin(ang)
    parts.append(_label(452, 96, f"|A||B|sinθ = {mag:.4g}", GREEN, 14, family=_MONO))
    parts.append(_label(452, 118, f"sin {angle_deg:g}° = {math.sin(ang):+.4g}", MUTED, 11,
                        family=_MONO))
    parts.append(_label(452, 138, f"parallelogram area = {mag:.4g}", GREEN, 12, family=_MONO))
    parts.append(_label(452, 168, f"|A| = {amag:g}, |B| = {bmag:g}, θ = {angle_deg:g}°",
                        MUTED, 10, family=_MONO))
    parts.append(_label(20, h - 14, "at 0° or 180° the parallelogram collapses and the area "
                                    "is zero", MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Cross product as a parallelogram area")


@cached
def right_hand_rule(angle_deg):
    """The right-hand rule that fixes the direction of a cross product."""
    w, h = 660, 220
    cx, cy = 150, 120
    ang = math.radians(angle_deg)
    parts = [_label(20, 24, "THE RIGHT-HAND RULE", MUTED, 12),
             _label(20, 42, "Curl your fingers from A to B; your thumb points along A × B.",
                    MUTED, 10, family=_SANS)]
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="70" fill="none" stroke="{MUTED}" '
                 f'stroke-width="1" opacity="0.4"/>')
    for k in range(4):
        t = ang + k * math.pi / 2
        parts.append(f'<circle cx="{cx + 52 * math.cos(t):.1f}" '
                     f'cy="{cy - 52 * math.sin(t):.1f}" r="5" fill="{CYAN if k == 0 else MUTED}" '
                     f'opacity="{1.0 if k == 0 else 0.45}"/>')
    parts.append(_arrow(cx, cy, cx + 88, cy, CYAN, 3.2))
    parts.append(_label(cx + 96, cy + 4, "A", CYAN, 12))
    tipx = cx + 88 * math.cos(ang)
    tipy = cy - 88 * math.sin(ang)
    parts.append(_arrow(cx, cy, tipx, tipy, AMBER, 3.2))
    parts.append(_label(tipx + 8, tipy - 6, "B", AMBER, 12))
    parts.append(_arrow(cx, cy, cx, cy - 74, GREEN, 3.6))
    parts.append(f'<circle cx="{cx}" cy="{cy - 82}" r="4.5" fill="{GREEN}"/>')
    parts.append(_label(cx + 12, cy - 86, "A × B", GREEN, 13))
    parts.append(_label(430, 96, f"out of the page  :  A × B is +z", GREEN, 11, family=_MONO))
    parts.append(_label(430, 116, f"into the page   :  A × B is −z", ROSE, 11, family=_MONO))
    parts.append(_label(430, 146, "swap the order of A and B and the", MUTED, 10, family=_SANS))
    parts.append(_label(430, 162, "direction flips — A × B = −(B × A)", MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Right-hand rule for the cross product")
