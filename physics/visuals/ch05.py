"""Chapter 5 diagrams: deformation in solids."""

from __future__ import annotations

import math

from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, wrap

__all__ = ["load_extension_curve", "solid_types", "deformation_kinds", "stress_strain_curve",
           "load_unload_trace", "energy_triangle", "wire_comparison"]


def _axis(x0, y0, x1, y1, colour=MUTED, label="", dx=0, dy=0):
    return (
        f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{colour}" '
        f'stroke-width="2" stroke-linecap="round"/>'
        f'<polygon points="{x1},{y1} {x1 - 7},{y1 - 4} {x1 - 7},{y1 + 4}" fill="{colour}"/>'
        + (f'<text x="{x1 + dx}" y="{y1 + dy}" fill="{MUTED}" font-size="13" '
           f'font-family="JetBrains Mono, monospace">{label}</text>' if label else "")
    )


@cached
def solid_types() -> str:
    """Three solids side by side: lattice, no lattice, and chains."""
    w, h = 700, 300
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'THREE ARRANGEMENTS OF THE SAME ATOMS</text>']
    panels = [
        ("Crystalline", CYAN, "regular, repeating lattice"),
        ("Amorphous", AMBER, "no long-range order"),
        ("Polymeric", VIOLET, "very long chains"),
    ]
    for index, (name, colour, note) in enumerate(panels):
        x0 = 30 + index * 225
        parts.append(f'<rect x="{x0}" y="46" width="200" height="180" rx="12" fill="#0d1c30" '
                     f'stroke="{colour}" stroke-opacity="0.45"/>')
        for row in range(5):
            for column in range(5):
                cx, cy = x0 + 26 + column * 36, 74 + row * 34
                if index == 0:
                    # A perfect lattice.
                    if (row + column) % 2 == 0:
                        parts.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{colour}"/>')
                    else:
                        parts.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{colour}" '
                                     f'opacity="0.65"/>')
                elif index == 1:
                    # Random positions, fixed by a fixed pattern so the picture is stable.
                    offsets = [(4, 0), (-6, 7), (9, -5), (-3, -8), (0, 2), (7, 6),
                               (-9, 3), (2, -4), (-5, -2), (6, -7), (0, 9), (-7, -6),
                               (11, 1), (-11, -3), (3, 5), (-4, 10), (8, -9), (-8, 8),
                               (12, -4), (-12, 4), (5, 11), (-5, -11), (10, 5), (-10, -5),
                               (1, 13)]
                    dx, dy = offsets[(row * 5 + column) % len(offsets)]
                    parts.append(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="8" '
                                 f'fill="{colour}" opacity="0.85"/>')
                else:
                    # Long wandering chains.
                    if row % 2 == 0:
                        for column in range(4):
                            cx, cy = x0 + 26 + column * 48, 74 + row * 34 + 12
                            parts.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{colour}"/>')
                            if column < 3:
                                parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 48}" '
                                             f'y2="{cy}" stroke="{colour}" stroke-width="3"/>')
                    else:
                        for column in range(4):
                            cx, cy = x0 + 50 + column * 48, 74 + row * 34
                            parts.append(f'<circle cx="{cx}" cy="{cy}" r="9" '
                                         f'fill="{colour}" opacity="0.75"/>')
                            if column < 3:
                                parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 48}" '
                                             f'y2="{cy}" stroke="{colour}" stroke-width="3" '
                                             f'opacity="0.75"/>')
        parts.append(f'<text x="{x0 + 100}" y="250" text-anchor="middle" fill="{colour}" '
                     f'font-size="15" font-weight="700">{name}</text>'
                     f'<text x="{x0 + 100}" y="270" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="11" font-family="Sora, sans-serif">{note}</text>')
    parts.append(f'<text x="20" y="{h - 8}" fill="{MUTED}" font-size="12" '
                 f'font-family="Sora, sans-serif">Crystalline solids melt sharply; amorphous '
                 f'ones soften gradually. That single difference is the clearest experimental '
                 f'signature of long-range order.</text>')
    return wrap("".join(parts), w, h, "Crystalline, amorphous and polymeric solids")


@cached
def deformation_kinds() -> str:
    """The four kinds of deformation a body can undergo."""
    w, h = 680, 420
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'FOUR KINDS OF DEFORMATION</text>']
    panels = [
        ("Tensile", CYAN, "← ← ←   [██████]   → → →", "pulled apart — it stretches"),
        ("Compressive", AMBER, "→ → →   [██████]   ← ← ←", "pushed together — it squashes"),
        ("Shear", TEAL, "⇉⇉⇉⇉⇉⇉ over ⇉⇉⇉⇉⇉⇉", "pushed sideways — layers slide"),
        ("Torsional", VIOLET, "↻═══════╚", "twisted about an axis"),
    ]
    for index, (name, colour, glyph, note) in enumerate(panels):
        y = 66 + index * 78
        parts.append(f'<rect x="24" y="{y}" width="630" height="62" rx="10" fill="#0d1c30" '
                     f'stroke="{colour}" stroke-opacity="0.35"/>')
        parts.append(f'<text x="42" y="{y + 26}" fill="{colour}" font-size="15" '
                     f'font-weight="700">{name}</text>')
        parts.append(f'<text x="42" y="{y + 48}" fill="{MUTED}" font-size="12" '
                     f'font-family="Sora, sans-serif">{note}</text>')
        parts.append(f'<text x="250" y="{y + 38}" fill="{colour}" font-size="20" '
                     f'font-family="JetBrains Mono, monospace">{glyph}</text>')
    parts.append(f'<text x="20" y="{h - 10}" fill="{MUTED}" font-size="12" '
                 f'font-family="Sora, sans-serif">This chapter works mainly with tensile '
                 f'deformation, because that is the one with a simple one-dimensional formula.</text>')
    return wrap("".join(parts), w, h, "Tensile, compressive, shear and torsional deformation")


@cached
def stress_strain_curve(curve, width=680, height=460) -> str:
    """A material's stress–strain curve, drawn from a computed curve."""
    strains = curve["strain"]
    stresses = curve["stress"]
    if not strains:
        return wrap('<text x="20" y="40" fill="muted">No curve.</text>', width, height)

    x_max = max(strains) * 1.04 or 1.0
    y_max = max(stresses) * 1.12 or 1.0
    left, bottom, right, top = 74, height - 62, width - 28, 52

    def sx(value):
        return left + (value / x_max) * (right - left)

    def sy(value):
        return bottom - (value / y_max) * (bottom - top)

    colours = {"Elastic": CYAN, "Plastic": AMBER, "Fracture": ROSE}
    parts = [
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'STRESS – STRAIN CURVE · {curve["material"].upper()}</text>'
    ]
    # Grid.
    for fraction in (0.25, 0.5, 0.75, 1.0):
        parts.append(f'<line x1="{left}" y1="{sy(y_max * fraction):.1f}" '
                     f'x2="{right}" y2="{sy(y_max * fraction):.1f}" stroke="#1b3350" '
                     f'stroke-width="1"/>')
        parts.append(f'<text x="{left - 8}" y="{sy(y_max * fraction) + 4:.1f}" '
                     f'text-anchor="end" fill="{MUTED}" font-size="10" '
                     f'font-family="JetBrains Mono, monospace">{y_max * fraction:.3g}</text>')
        parts.append(f'<line x1="{sx(x_max * fraction):.1f}" y1="{top}" '
                     f'x2="{sx(x_max * fraction):.1f}" y2="{bottom}" stroke="#1b3350" '
                     f'stroke-width="1"/>')
        parts.append(f'<text x="{sx(x_max * fraction):.1f}" y="{bottom + 20}" '
                     f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                     f'font-family="JetBrains Mono, monospace">{x_max * fraction:.3g}</text>')
    parts.append(_axis(left, bottom, right + 6, bottom, MUTED, "strain ε", dx=18, dy=16))
    parts.append(f'<text x="20" y="{top - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">stress σ (Pa)</text>')

    # The curve, coloured by region.
    current = None
    run = []
    for index, (strain, stress, region) in enumerate(
            zip(strains, stresses, curve["regions"])):
        if region != current and run:
            parts.append(_polyline(run, colours[current]))
            run = []
        current = region
        run.append((sx(strain), sy(stress)))
    if run:
        parts.append(_polyline(run, colours[current]))

    # Landmarks.
    marks = [
        (curve["elastic_strain"], curve["youngs_modulus"] * curve["elastic_strain"],
         "elastic limit", CYAN),
        (curve["ultimate_strain"], curve["ultimate_stress"], "ultimate", AMBER),
        (curve["fracture_strain"], stresses[-1], "fracture", ROSE),
    ]
    for strain, stress, name, colour in marks:
        if strain > x_max:
            continue
        parts.append(f'<circle cx="{sx(strain):.1f}" cy="{sy(stress):.1f}" r="5" '
                     f'fill="{colour}"/>')
        parts.append(f'<text x="{sx(strain) + 9:.1f}" y="{sy(stress) - 8:.1f}" '
                     f'fill="{colour}" font-size="11" font-family="JetBrains Mono, monospace">'
                     f'{name}</text>')

    # The slope triangle, which is Young's modulus.
    el = curve["elastic_strain"]
    if el > 0:
        parts.append(f'<line x1="{sx(el):.1f}" y1="{sy(0):.1f}" x2="{sx(el):.1f}" '
                     f'y2="{sy(curve["youngs_modulus"] * el):.1f}" stroke="{GREEN}" '
                     f'stroke-width="2" stroke-dasharray="4 3"/>')
        parts.append(f'<line x1="{sx(0):.1f}" y1="{sy(curve["youngs_modulus"] * el):.1f}" '
                     f'x2="{sx(el):.1f}" y2="{sy(curve["youngs_modulus"] * el):.1f}" '
                     f'stroke="{GREEN}" stroke-width="2" stroke-dasharray="4 3"/>')
        parts.append(f'<text x="{sx(el) + 8:.1f}" y="{sy(curve["youngs_modulus"] * el / 2):.1f}" '
                     f'fill="{GREEN}" font-size="12" font-family="JetBrains Mono, monospace">'
                     f'slope = Y = {curve["youngs_modulus"]:.2g} Pa</text>')

    parts.append(f'<text x="20" y="{height - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Model curve generated from the material\'s '
                 f'modulus and yield stress — shaped for teaching, not a test certificate.</text>')
    return wrap("".join(parts), width, height,
                f"Stress-strain curve for {curve['material']}")


def _polyline(points, colour):
    if len(points) < 2:
        return ""
    joined = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return (f'<polyline points="{joined}" fill="none" stroke="{colour}" stroke-width="3.2" '
            f'stroke-linejoin="round" stroke-linecap="round"/>')


@cached
def load_unload_trace(load_strain: float, elastic_limit: float, yield_point: float) -> str:
    """Loading a bar and then removing the load, showing the permanent set."""
    w, h = 660, 400
    left, bottom, right, top = 70, h - 56, w - 130, 46
    x_max, y_max = 1.15, 1.15

    def sx(value):
        return left + value * (right - left)

    def sy(value):
        return bottom - value * (bottom - top)

    def profile(strain):
        """The loading path, up to the strain reached."""
        if strain <= elastic_limit:
            return [(x, x * elastic_limit) for x in
                    [i * strain / 40 for i in range(41)]]
        points = [(x, x * elastic_limit) for x in
                  [i * elastic_limit / 20 for i in range(21)]]
        extra = strain - elastic_limit
        points += [(elastic_limit + extra * t / 20,
                    elastic_limit * 0.45 + elastic_limit * 0.4 * (t / 20))
                   for t in range(21)]
        return points

    reach = min(load_strain, x_max * 0.95)
    loading = profile(reach)
    permanent = max(0.0, reach - elastic_limit)
    unloading = [(x, y) for x, y in reversed(loading)]
    unloading = [(x, y - permanent * elastic_limit) for x, y in unloading]

    parts = [
        f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'LOAD, THEN RELEASE</text>'
    ]
    parts.append(_axis(left, bottom, right + 6, bottom, MUTED, "strain", dx=20, dy=16))
    parts.append(f'<text x="20" y="{top - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">stress (fraction of Y)</text>')
    parts.append(f'<line x1="{sx(elastic_limit):.1f}" y1="{top}" x2="{sx(elastic_limit):.1f}" '
                 f'y2="{bottom}" stroke="{CYAN}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{sx(elastic_limit) + 6:.1f}" y="{top + 14}" fill="{CYAN}" '
                 f'font-size="11" font-family="JetBrains Mono, monospace">elastic limit</text>')
    parts.append(_polyline(loading, AMBER))
    parts.append(_polyline(unloading, VIOLET))
    if permanent > 1e-6:
        parts.append(f'<line x1="{sx(0):.1f}" y1="{sy(0):.1f}" x2="{sx(reach):.1f}" '
                     f'y2="{sy(0):.1f}" stroke="{ROSE}" stroke-width="2"/>')
        parts.append(f'<text x="{sx(reach) + 8:.1f}" y="{sy(0) + 18:.1f}" fill="{ROSE}" '
                     f'font-size="12" font-weight="700">permanent set '
                     f'{permanent:.3g}</text>')
    parts.append(f'<text x="{left + 12}" y="{bottom - 18}" fill="{AMBER}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">↗ loading</text>')
    parts.append(f'<text x="{right - 70}" y="{bottom - 18}" fill="{VIOLET}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">↙ unloading</text>')
    verdict = ("returns completely — fully elastic" if permanent <= 1e-6
               else f"stays stretched by {permanent:.3g} — plastic deformation")
    parts.append(f'<rect x="{right + 16}" y="{top + 24}" width="150" height="86" rx="10" '
                 f'fill="#0d1c30" stroke="{ROSE if permanent > 1e-6 else GREEN}" '
                 f'stroke-opacity="0.5"/>'
                 f'<text x="{right + 30}" y="{top + 48}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">ON RELEASE</text>'
                 f'<text x="{right + 30}" y="{top + 76}" fill="#eef6ff" font-size="12" '
                 f'font-family="Sora, sans-serif">{verdict}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The unloading line is parallel to the loading '
                 f'line: the same small strain removes the same small stress.</text>')
    return wrap("".join(parts), w, h, "Loading and unloading a bar, showing permanent set")


@cached
def energy_triangle(f_max: float, extension: float) -> str:
    """The elastic energy as the area under the straight force–extension line."""
    w, h = 620, 360
    left, bottom, right, top = 84, h - 60, w - 40, 52
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'ENERGY AS AN AREA</text>']
    parts.append(_axis(left, bottom, right + 6, bottom, MUTED, "extension x (m)", dx=10, dy=20))
    parts.append(f'<text x="20" y="{top - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">force F (N)</text>')
    parts.append(f'<polygon points="{left},{bottom} {right},{bottom} {right},{top + 40}" '
                 f'fill="{TEAL}" opacity="0.20"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{top + 40}" '
                 f'stroke="{TEAL}" stroke-width="3.5"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{left}" y2="{top + 40}" '
                 f'stroke="{CYAN}" stroke-width="2" stroke-dasharray="5 4"/>')
    parts.append(f'<line x1="{left}" y1="{top + 40}" x2="{right}" y2="{top + 40}" '
                 f'stroke="{CYAN}" stroke-width="2" stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{right - 10}" y="{top + 34}" text-anchor="end" fill="{CYAN}" '
                 f'font-size="13" font-family="JetBrains Mono, monospace">'
                 f'F = {f_max:.4g} N</text>')
    parts.append(f'<text x="{right + 2}" y="{bottom - 8}" fill="{TEAL}" font-size="13" '
                 f'font-family="JetBrains Mono, monospace">x = {extension:.4g} m</text>')
    energy = 0.5 * f_max * extension
    parts.append(f'<rect x="{left}" y="{top + 66}" width="300" height="58" rx="10" '
                 f'fill="#0d1c30" stroke="{AMBER}" stroke-opacity="0.5"/>'
                 f'<text x="{left + 14}" y="{top + 88}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">E = ½ F x = ½ k x²</text>'
                 f'<text x="{left + 14}" y="{top + 112}" fill="{AMBER}" font-size="20" '
                 f'font-weight="800" font-family="JetBrains Mono, monospace">'
                 f'{energy:.4g} J</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Energy goes as x², so doubling the stretch '
                 f'quadruples the energy stored — and that is why a hard squash feels so '
                 f'different from a gentle one.</text>')
    return wrap("".join(parts), w, h, "Elastic potential energy as the area under the graph")


@cached
def wire_comparison(rows) -> str:
    """Bar chart comparing moduli, so the scale of the differences is visible."""
    w, h = 640, 340
    left, right = 190, w - 110
    top, row_h = 60, 42
    highest = max((r["modulus"] for r in rows), default=1.0)
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'YOUNG\'S MODULUS ON A LOGARITHMIC SCALE</text>']
    for index, row in enumerate(rows):
        y = top + index * row_h
        # Each bar is drawn logarithmically: 1e6 Pa at the left, 1e12 Pa at the right.
        fraction = (math.log10(row["modulus"]) - 6.0) / 6.0
        width = max(4.0, fraction * (right - left))
        colour = GREEN if row["modulus"] > 1e10 else AMBER if row["modulus"] > 1e8 else ROSE
        parts.append(f'<text x="24" y="{y + 20}" fill="#eef6ff" font-size="13" '
                     f'font-family="Sora, sans-serif">{row["name"]}</text>')
        parts.append(f'<rect x="{left}" y="{y + 6}" width="{width:.1f}" height="20" rx="5" '
                     f'fill="{colour}" opacity="0.75"/>')
        parts.append(f'<text x="{left + width + 8:.1f}" y="{y + 21}" fill="{colour}" '
                     f'font-size="12" font-family="JetBrains Mono, monospace">'
                     f'{row["modulus"]:.2g}</text>')
    for power in range(6, 13, 2):
        x = left + (power - 6.0) / 6.0 * (right - left)
        parts.append(f'<text x="{x:.0f}" y="{h - 56}" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="10" font-family="JetBrains Mono, monospace">'
                     f'10^{power} Pa</text>')
    parts.append(f'<line x1="{left}" y1="{top - 6}" x2="{left}" y2="{h - 70}" '
                 f'stroke="#1b3350" stroke-width="1"/>')
    parts.append(f'<text x="20" y="{h - 16}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Because each bar spans five orders of '
                 f'magnitude, the axis is logarithmic. A linear chart would show every '
                 f'non-metal as a flat line.</text>')
    return wrap("".join(parts), w, h, "Young's modulus of different materials, log scale")


@cached
def load_extension_curve(limit=180.0, yield_load=260.0, break_load=340.0):
    """A force-extension curve with every named region marked."""
    from .common import MONO as _MONO, SANS as _SANS
    from .common import label as _label
    w, h = 680, 400
    left, right, base, top = 80, 600, 320, 60
    x_max, y_max = 2.4, 400.0

    def X(x):
        return left + (x / x_max) * (right - left)

    def Y(y):
        return base - (y / y_max) * (base - top)

    def f(x):
        """Linear to the limit, then a progressively steeper plastic rise."""
        if x <= 0.65:
            return limit * x / 0.65
        if x <= 1.35:
            return limit + (yield_load - limit) * 0.18 * (x - 0.65) / 0.70
        t = (x - 1.35) / (x_max - 1.35)
        return yield_load + (break_load - yield_load) * (t ** 1.8)

    pts = [f"{X(x_max * i / 120):.1f},{Y(f(x_max * i / 120)):.1f}" for i in range(121)]
    parts = [_label(20, 24, "FORCE-EXTENSION CURVE", MUTED, 12),
             _label(20, 42, "A ductile metal. The straight part gives Young's modulus; the "
                            "rest is the plastic region.", MUTED, 10, family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{base}" x2="{left}" y2="{top}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="2.8"/>')
    # the unload line from the elastic limit, showing it returns to the origin
    parts.append(f'<line x1="{X(0.65)}" y1="{Y(limit)}" x2="{X(0)}" y2="{Y(0)}" '
                 f'stroke="{ROSE}" stroke-width="1.6" stroke-dasharray="6 4"/>')
    parts.append(_label(X(0.62), Y(limit) + 26, "unloading returns it here", ROSE, 9,
                        "end", _SANS))
    for x, text, colour in ((0.0, "origin", MUTED), (0.65, "limit of\nproportionality", AMBER),
                            (1.35, "elastic limit", AMBER), (1.95, "yield\npoint", VIOLET),
                            (2.35, "fracture", ROSE)):
        y = f(x)
        parts.append(f'<line x1="{X(x):.1f}" y1="{Y(y):.1f}" x2="{X(x):.1f}" y2="{base}" '
                     f'stroke="{colour}" stroke-width="1" stroke-dasharray="3 3" '
                     f'opacity="0.55"/>')
        for i, line in enumerate(text.split("\n")):
            parts.append(_label(X(x), Y(y) - 22 + i * 12, line, colour, 9, "middle", _SANS))
    # gradient wedge on the straight section
    parts.append(f'<line x1="{X(0.0)}" y1="{Y(0)}" x2="{X(0.65)}" y2="{Y(limit)}" '
                 f'stroke="{GREEN}" stroke-width="5" opacity="0.18"/>')
    parts.append(_label(left + 8, top + 6, "gradient of this line = Young's modulus", GREEN,
                        11, "start", _SANS))
    for frac in (0.25, 0.5, 0.75, 1.0):
        parts.append(f'<line x1="{X(x_max * frac):.1f}" y1="{base}" x2="{X(x_max * frac):.1f}" '
                     f'y2="{base + 4}" stroke="{MUTED}"/>')
        parts.append(_label(X(x_max * frac), base + 16, f"{x_max * frac:.2f}", MUTED, 9))
        parts.append(f'<line x1="{left}" y1="{Y(y_max * frac):.1f}" x2="{left + 4}" '
                     f'y2="{Y(y_max * frac):.1f}" stroke="{MUTED}"/>')
        parts.append(_label(left - 6, Y(y_max * frac) + 3, f"{y_max * frac:.0f}", MUTED, 9,
                            "end"))
    parts.append(_label(right, base + 32, "extension / m", MUTED, 10, "end"))
    parts.append(f'<text transform="translate(26 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">load / N</text>')
    parts.append(_label(left, base + 32, "0", MUTED, 9, "start"))
    return wrap("".join(parts), w, h, "Force-extension curve")
