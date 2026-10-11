"""Chapter 6 diagrams: fluids dynamics."""

from __future__ import annotations

import math

from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, wrap

__all__ = ["archimedes_bench", "hull_diagram", "flow_regime_strip",
           "pipe_continuity", "bernoulli_profile", "atomizer_diagram",
           "viscosity_ladder", "superfluidity_panel"]


def _axis(x0, y0, x1, y1, colour=MUTED, label="", size=13):
    return (
        f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{colour}" '
        f'stroke-width="2" stroke-linecap="round"/>'
        f'<polygon points="{x1},{y1} {x1 - 7},{y1 - 4} {x1 - 7},{y1 + 4}" fill="{colour}"/>'
        + (f'<text x="{x1 + 8}" y="{y1 + 4}" fill="{MUTED}" font-size="{size}" '
           f'font-family="JetBrains Mono, monospace">{label}</text>' if label else "")
    )


@cached
def archimedes_bench(object_density: float, fluid_density: float, volume: float,
                     g: float = 9.8) -> str:
    """A body in a fluid with the force balance drawn on it."""
    w, h = 640, 400
    weight = object_density * volume * g
    maximum_up = fluid_density * volume * g
    if fluid_density and object_density <= fluid_density:
        submerged = min(1.0, object_density / fluid_density)
        verdict = "FLOATS"
        colour = GREEN
    else:
        submerged = 1.0
        verdict = "SINKS"
        colour = ROSE
    displaced = volume * submerged
    upthrust = fluid_density * displaced * g

    waterline = 150
    parts = [
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'THE ARCHIMEDES BENCH</text>'
    ]
    parts.append(f'<rect x="0" y="{waterline}" width="400" height="{h - waterline}" '
                 f'fill="{CYAN}" opacity="0.10"/>')
    for y in range(waterline + 22, h, 22):
        parts.append(f'<line x1="0" y1="{y}" x2="400" y2="{y}" stroke="{CYAN}" '
                     f'stroke-width="1" opacity="0.22"/>')
    parts.append(f'<line x1="0" y1="{waterline}" x2="400" y2="{waterline}" '
                 f'stroke="{CYAN}" stroke-width="2.5"/>')
    parts.append(f'<text x="14" y="{waterline - 8}" fill="{CYAN}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">waterline</text>')

    # The body: 40 % submerged if floating.
    body_w, body_h = 150, 130
    top = waterline - body_h * submerged
    parts.append(f'<rect x="200" y="{top:.1f}" width="{body_w}" height="{body_h}" '
                 f'rx="8" fill="{AMBER}" fill-opacity="0.35" stroke="{AMBER}" '
                 f'stroke-width="2.5"/>')
    if submerged < 1.0:
        cut = waterline - top
        parts.append(f'<rect x="200" y="{top:.1f}" width="{body_w}" height="{cut:.1f}" '
                     f'rx="8" fill="{CYAN}" opacity="0.30"/>')

    # Forces.
    cx = 275
    parts.append(f'<line x1="{cx}" y1="{top + body_h * 0.55:.1f}" x2="{cx}" '
                 f'y2="{top + body_h * 0.55 + 44:.1f}" stroke="{ROSE}" stroke-width="4"/>'
                 f'<polygon points="{cx},{top + body_h * 0.55 + 52:.1f} '
                 f'{cx - 7},{top + body_h * 0.55 + 38:.1f} {cx + 7},'
                 f'{top + body_h * 0.55 + 38:.1f}" fill="{ROSE}"/>'
                 f'<text x="{cx + 12}" y="{top + body_h * 0.55 + 34:.1f}" fill="{ROSE}" '
                 f'font-size="12" font-family="JetBrains Mono, monospace">'
                 f'weight {weight:.3g} N</text>')
    parts.append(f'<line x1="{cx}" y1="{top + body_h * 0.45:.1f}" x2="{cx}" '
                 f'y2="{top + body_h * 0.45 - 40:.1f}" stroke="{GREEN}" stroke-width="4"/>'
                 f'<polygon points="{cx},{top + body_h * 0.45 - 48:.1f} '
                 f'{cx - 7},{top + body_h * 0.45 - 34:.1f} {cx + 7},'
                 f'{top + body_h * 0.45 - 34:.1f}" fill="{GREEN}"/>'
                 f'<text x="{cx + 12}" y="{top + body_h * 0.45 - 38:.1f}" fill="{GREEN}" '
                 f'font-size="12" font-family="JetBrains Mono, monospace">'
                 f'upthrust {upthrust:.3g} N</text>')

    # Panel.
    parts.append(f'<rect x="410" y="52" width="216" height="252" rx="12" fill="#0d1c30" '
                 f'stroke="{colour}" stroke-opacity="0.5"/>'
                 f'<text x="426" y="80" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace" letter-spacing="1.5">FORCE BALANCE</text>'
                 f'<text x="426" y="108" fill="{colour}" font-size="21" font-weight="800">'
                 f'{verdict}</text>'
                 f'<text x="426" y="134" fill="#c6d6ea" font-size="12" '
                 f'font-family="Sora, sans-serif">ρ body {object_density:.4g}</text>'
                 f'<text x="426" y="152" fill="#c6d6ea" font-size="12" '
                 f'font-family="Sora, sans-serif">ρ fluid {fluid_density:.4g}</text>'
                 f'<text x="426" y="178" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">MAX UPTHRUST</text>'
                 f'<text x="426" y="198" fill="{TEAL}" font-size="15" '
                 f'font-family="JetBrains Mono, monospace">{maximum_up:.4g} N</text>'
                 f'<text x="426" y="222" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">SUBMERGED FRACTION</text>'
                 f'<text x="426" y="242" fill="{VIOLET}" font-size="15" '
                 f'font-family="JetBrains Mono, monospace">{submerged * 100:.1f} %</text>'
                 f'<text x="426" y="266" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">DISPLACED VOLUME</text>'
                 f'<text x="426" y="286" fill="{AMBER}" font-size="15" '
                 f'font-family="JetBrains Mono, monospace">{displaced:.4g} m³</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Upthrust equals the weight of the fluid '
                 f'displaced — {fluid_density:.4g} × 9.8 × {displaced:.4g} = {upthrust:.4g} N. '
                 f'Note that g cancels from the submerged fraction.</text>')
    return wrap("".join(parts), w, h, "Upthrust and floatation in a fluid")


@cached
def hull_diagram(displaced_volume: float, ship_mass: float, g: float = 9.8) -> str:
    """A ship's hull displacing water, with the waterline and the cargo."""
    w, h = 620, 360
    waterline = 190
    parts = [
        f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'WHY A SHIP FLOATS</text>',
        f'<rect x="0" y="{waterline}" width="620" height="{h - waterline}" fill="{CYAN}" '
        f'opacity="0.10"/>',
    ]
    for y in range(waterline + 20, h, 20):
        parts.append(f'<line x1="0" y1="{y}" x2="620" y2="{y}" stroke="{CYAN}" '
                     f'stroke-width="1" opacity="0.22"/>')
    parts.append(f'<line x1="0" y1="{waterline}" x2="620" y2="{waterline}" '
                 f'stroke="{CYAN}" stroke-width="2.5"/>')

    # Hull outline: hollow, not solid.
    parts.append(f'<path d="M 130 {waterline - 6} L 150 116 L 440 116 L 470 {waterline - 6} Z" '
                 f'fill="none" stroke="{AMBER}" stroke-width="3.5"/>')
    parts.append(f'<rect x="180" y="132" width="230" height="{waterline - 138}" rx="6" '
                 f'fill="{AMBER}" opacity="0.12"/>')
    # Cargo.
    for i in range(4):
        parts.append(f'<rect x="{196 + i * 56}" y="{waterline - 62}" width="44" '
                     f'height="48" rx="5" fill="{VIOLET}" opacity="0.55"/>')
    # Displaced water: the part of the hull below the waterline.
    parts.append(f'<clipPath id="hullClip"><path d="M 130 {waterline} L 150 116 L 440 116 '
                 f'L 470 {waterline} Z"/></clipPath>')
    parts.append(f'<g clip-path="url(#hullClip)">'
                 f'<rect x="120" y="{waterline}" width="360" height="60" fill="{CYAN}" '
                 f'opacity="0.55"/></g>')
    parts.append(f'<text x="300" y="{waterline + 32}" text-anchor="middle" fill="{CYAN}" '
                 f'font-size="13" font-family="JetBrains Mono, monospace">'
                 f'displaced {displaced_volume:.4g} m³</text>')
    parts.append(f'<text x="300" y="{waterline + 52}" text-anchor="middle" fill="{CYAN}" '
                 f'font-size="11" font-family="Sora, sans-serif">excluded from the water by '
                 f'the hull</text>')
    parts.append(f'<text x="300" y="106" text-anchor="middle" fill="{VIOLET}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">cargo + steel shell = '
                 f'{ship_mass:.4g} kg</text>')
    parts.append(f'<rect x="430" y="52" width="176" height="104" rx="10" fill="#0d1c30" '
                 f'stroke="{GREEN}" stroke-opacity="0.5"/>'
                 f'<text x="446" y="76" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">UPTHRUST</text>'
                 f'<text x="446" y="102" fill="{GREEN}" font-size="21" font-weight="800" '
                 f'font-family="JetBrains Mono, monospace">{ship_mass * g:.4g} N</text>'
                 f'<text x="446" y="126" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">= weight of the ship</text>'
                 f'<text x="446" y="144" fill="{MUTED}" font-size="10" '
                 f'font-family="Sora, sans-serif">so it floats</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">A solid block of steel this size would sink. '
                 f'Hollowing it out changes the displaced volume without changing the mass much '
                 f'— and that is the whole engineering.</text>')
    return wrap("".join(parts), w, h, "A ship's hull displacing seawater")


@cached
def flow_regime_strip(re_number: float, regime: str) -> str:
    """Three panels: the same flow as laminar, transitional and turbulent."""
    w, h = 660, 300
    panels = [("Laminar (Re < 2000)", "lines stay parallel", CYAN),
              ("Transitional", "layers begin to mix", AMBER),
              ("Turbulent (Re > 4000)", "chaotic eddies", ROSE)]
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'REYNOLDS NUMBER {re_number:.3g}</text>']
    for index, (title, note, colour) in enumerate(panels):
        x0 = 24 + index * 212
        active = title.split("(")[0].strip().lower() in regime.lower()
        parts.append(f'<rect x="{x0}" y="46" width="196" height="170" rx="12" '
                     f'fill="#0d1c30" stroke="{colour}" '
                     f'stroke-opacity="{0.75 if active else 0.28}" '
                     f'stroke-width="{2.5 if active else 1.5}"/>')
        cx, cy = x0 + 98, 128
        for row in range(7):
            y = cy - 52 + row * 17
            if index == 0:
                points = [(x0 + 22, y), (x0 + 174, y)]
            elif index == 1:
                points = []
                for step in range(0, 153, 6):
                    wobble = 7 * math.sin((step / x0 if x0 else 1) * 1.3 + row * 0.9) * (row / 6)
                    points.append((x0 + 22 + step, y + wobble * (row - 3) / 3))
            else:
                points = []
                for step in range(0, 153, 6):
                    wobble = 15 * math.sin(step * 0.22 + row * 1.7) * (1 - abs(row - 3) / 4)
                    points.append((x0 + 22 + step, y + wobble))
            if index == 2:
                for (ax, ay), (bx, by) in zip(points, points[1:]):
                    parts.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" '
                                 f'y2="{by:.1f}" stroke="{colour}" stroke-width="1.6" '
                                 f'opacity="0.9"/>')
            else:
                joined = " ".join(f"{px:.1f},{py:.1f}" for px, py in points)
                parts.append(f'<polyline points="{joined}" fill="none" stroke="{colour}" '
                             f'stroke-width="1.8" opacity="0.9"/>')
        parts.append(f'<text x="{x0 + 98}" y="196" text-anchor="middle" fill="{colour}" '
                     f'font-size="12" font-weight="700">{title}</text>')
        parts.append(f'<text x="{x0 + 98}" y="212" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="10" font-family="Sora, sans-serif">{note}</text>')
    parts.append(f'<text x="20" y="{h - 34}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'Re = ρ v L / η  —  higher speed, larger diameter and lower viscosity all '
                 f'make turbulence more likely.</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">'
                 f'This flow is {regime.lower()}.</text>')
    return wrap("".join(parts), w, h, "Laminar, transitional and turbulent flow")


@cached
def pipe_continuity(series, width=680, height=420) -> str:
    """A tapering pipe with area and velocity tracked along it."""
    w, h = width, height
    positions = series["position"]
    areas = series["area"]
    velocities = series["velocity"]
    left, right = 70, w - 190
    top, bottom = 60, h - 66
    span = max(areas) or 1.0
    v_max = max(velocities) or 1.0

    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'EQUATION OF CONTINUITY · A₁v₁ = A₂v₂</text>']
    upper, lower = [], []
    for index, (position, area, velocity) in enumerate(zip(positions, areas, velocities)):
        x = left + position * (right - left)
        half = (area / span) * (bottom - top) * 0.42
        upper.append((x, (top + bottom) / 2 - half))
        lower.append((x, (top + bottom) / 2 + half))
    joined_u = " ".join(f"{x:.1f},{y:.1f}" for x, y in upper)
    joined_l = " ".join(f"{x:.1f},{y:.1f}" for x, y in lower)
    parts.append(f'<polygon points="{joined_u} {" ".join(f"{x:.1f},{y:.1f}" for x, y in reversed(lower))}" '
                 f'fill="{CYAN}" opacity="0.12" stroke="{CYAN}" stroke-width="2.5"/>')

    # Velocity curve above the pipe.
    points = [(left + p * (right - left), bottom - (v / v_max) * (bottom - top) * 0.42)
              for p, v in zip(positions, velocities)]
    joined_v = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    parts.append(f'<polyline points="{joined_v}" fill="none" stroke="{AMBER}" stroke-width="3"/>')
    for x, y in points[::12]:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{AMBER}"/>')
    parts.append(f'<text x="{left}" y="{bottom - (bottom - top) * 0.42 - 8}" fill="{AMBER}" '
                 f'font-size="12" font-family="JetBrains Mono, monospace">v</text>')
    parts.append(f'<text x="{right + 8}" y="{top + 20}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">narrow →</text>')
    parts.append(f'<text x="{left + 4}" y="{bottom + 24}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">wide</text>')
    parts.append(f'<rect x="{right + 24}" y="{top}" width="150" height="150" rx="10" '
                 f'fill="#0d1c30" stroke="{GREEN}" stroke-opacity="0.5"/>'
                 f'<text x="{right + 38}" y="{top + 24}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">VOLUME FLOW</text>'
                 f'<text x="{right + 38}" y="{top + 50}" fill="{GREEN}" font-size="17" '
                 f'font-weight="800" font-family="JetBrains Mono, monospace">'
                 f'{series["flow_rate"]:.3g}</text>'
                 f'<text x="{right + 38}" y="{top + 68}" fill="{MUTED}" font-size="10" '
                 f'font-family="Sora, sans-serif">m³ s⁻¹</text>'
                 f'<text x="{right + 38}" y="{top + 94}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">SAME EVERYWHERE</text>'
                 f'<text x="{right + 38}" y="{top + 116}" fill="{GREEN}" font-size="11" '
                 f'font-family="Sora, sans-serif">'
                 f'{"✓" if series["constant"] else "✗"} at every point</text>'
                 f'<text x="{right + 38}" y="{top + 138}" fill="{MUTED}" font-size="10" '
                 f'font-family="Sora, sans-serif">area × speed = constant</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">As the pipe narrows the fluid speeds up, '
                 f'because the same volume must pass every second through a smaller area.</text>')
    return wrap("".join(parts), w, h, "A tapering pipe showing continuity")


@cached
def bernoulli_profile(p1: float, v1: float, p2: float, v2: float,
                      rho: float = 1000.0) -> str:
    """The three terms of Bernoulli as a stacked energy budget at two points."""
    w, h = 660, 300
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'BERNOULLI · THE ENERGY BUDGET IS THE SAME AT BOTH POINTS</text>']
    terms = [("P", CYAN, "pressure"), ("½ρv²", AMBER, "motion"), ("ρgh", VIOLET, "height")]
    heights = [[p1, 0.5 * rho * v1 ** 2, 0.0], [p2, 0.5 * rho * v2 ** 2, 0.0]]
    total = sum(heights[0]) or 1.0
    bar_h = 190
    for column, (x0, label) in enumerate([(150, "point 1"), (400, "point 2")]):
        y = 240
        for (name, colour, note), value in zip(terms, heights[column]):
            segment = (value / total) * bar_h
            parts.append(f'<rect x="{x0}" y="{y - segment:.1f}" width="110" '
                         f'height="{max(segment, 1):.1f}" fill="{colour}" opacity="0.75"/>')
            if segment > 18:
                parts.append(f'<text x="{x0 + 55}" y="{y - segment / 2 + 4:.1f}" '
                             f'text-anchor="middle" fill="#081426" font-size="12" '
                             f'font-weight="700" font-family="JetBrains Mono, monospace">'
                             f'{name}</text>')
            y -= segment
        parts.append(f'<line x1="{x0 - 14}" y1="{240 - bar_h}" x2="{x0 + 124}" '
                     f'y2="{240 - bar_h}" stroke="{GREEN}" stroke-width="2.5"/>')
        parts.append(f'<text x="{x0 + 55}" y="{240 - bar_h - 10}" text-anchor="middle" '
                     f'fill="{GREEN}" font-size="12" font-weight="700" '
                     f'font-family="JetBrains Mono, monospace">constant</text>')
        parts.append(f'<text x="{x0 + 55}" y="262" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="12" font-family="Sora, sans-serif">{label}</text>')
    parts.append(f'<text x="540" y="140" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Where the fluid speeds</text>'
                 f'<text x="540" y="158" fill="{AMBER}" font-size="11" '
                 f'font-family="Sora, sans-serif">up, the pressure</text>'
                 f'<text x="540" y="176" fill="{AMBER}" font-size="11" '
                 f'font-family="Sora, sans-serif">must fall.</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">At equal heights the ρgh bar is zero in both '
                 f'columns, leaving pressure to trade directly against motion.</text>')
    return wrap("".join(parts), w, h, "The three terms of Bernoulli's equation")


@cached
def atomizer_diagram(pressure_difference: float, density: float = 1.0e3) -> str:
    """An atomizer: the fast jet, the low pressure, and the liquid that follows."""
    w, h = 620, 340
    speed = math.sqrt(2.0 * pressure_difference / density) if pressure_difference > 0 else 0.0
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'ATOMIZER · BERNOULLI AT WORK</text>']
    parts.append(f'<path d="M 60 200 L 60 240 L 300 240 L 300 200 Z" fill="{MUTED}" '
                 f'opacity="0.28"/>')
    parts.append(f'<path d="M 60 200 L 60 240" stroke="{MUTED}" stroke-width="2"/>'
                 f'<path d="M 300 200 L 300 240" stroke="{MUTED}" stroke-width="2"/>')
    parts.append(f'<text x="170" y="262" text-anchor="middle" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">the liquid in the bottle</text>')
    parts.append(f'<path d="M 190 240 L 190 200 L 270 200 L 300 214" fill="none" '
                 f'stroke="{VIOLET}" stroke-width="3"/>')
    parts.append(f'<text x="176" y="288" text-anchor="middle" fill="{VIOLET}" '
                 f'font-size="11" font-family="JetBrains Mono, monospace">narrow tube</text>')
    parts.append(f'<path d="M 300 232 L 560 232 L 520 204 L 540 232 L 500 254 Z" '
                 f'fill="{AMBER}" opacity="0.75"/>')
    parts.append(f'<text x="430" y="182" text-anchor="middle" fill="{AMBER}" '
                 f'font-size="12" font-weight="700" font-family="JetBrains Mono, monospace">'
                 f'fast jet, v = {speed:.4g} m s⁻¹</text>')
    parts.append(f'<text x="300" y="192" text-anchor="middle" fill="{GREEN}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">P below atmospheric</text>')
    parts.append(f'<path d="M 190 214 C 150 208 120 202 92 196" fill="none" stroke="{VIOLET}" '
                 f'stroke-width="4" stroke-dasharray="6 4"/>')
    for index in range(6):
        parts.append(f'<circle cx="{318 + index * 34}" cy="{278 + (index % 3) * 16}" r="3.5" '
                     f'fill="{VIOLET}" opacity="{0.85 - index * 0.1}"/>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Squeeze the bulb: air is forced through a '
                 f'narrow jet, its speed rises, its pressure falls below atmospheric, and the '
                 f'outside air pushes the liquid up into that low-pressure region.</text>')
    return wrap("".join(parts), w, h, "How an atomizer works")


@cached
def viscosity_ladder(rows) -> str:
    """Viscosities on a logarithmic ladder from air to superfluid helium."""
    w, h = 640, 330
    left, right = 210, w - 130
    top, row_h = 56, 44
    floor = 1e-6
    ceiling = 1e2
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'VISCOSITY ACROSS FOUR ORDERS OF MAGNITUDE</text>']
    for index, row in enumerate(rows):
        y = top + index * row_h
        eta = row["eta_pa_s"]
        if eta <= floor:
            fraction = 0.0
            colour = VIOLET
            label = "0"
        else:
            fraction = (math.log10(eta) - math.log10(floor)) / (math.log10(ceiling) - math.log10(floor))
            colour = ROSE if eta > 1 else AMBER if eta > 1e-3 else GREEN
            label = f"{eta:.3g}"
        width = max(3.0, min(1.0, fraction) * (right - left))
        parts.append(f'<text x="24" y="{y + 20}" fill="#eef6ff" font-size="13" '
                     f'font-family="Sora, sans-serif">{row["liquid"]}</text>')
        parts.append(f'<rect x="{left}" y="{y + 6}" width="{width:.1f}" height="20" rx="5" '
                     f'fill="{colour}" opacity="0.78"/>')
        parts.append(f'<text x="{left + width + 8:.1f}" y="{y + 21}" fill="{colour}" '
                     f'font-size="12" font-family="JetBrains Mono, monospace">{label}</text>')
    parts.append(f'<text x="{left}" y="{h - 44}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">0 Pa·s</text>')
    parts.append(f'<text x="{right}" y="{h - 44}" text-anchor="end" fill="{MUTED}" '
                 f'font-size="10" font-family="JetBrains Mono, monospace">100 Pa·s</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The bar for superfluid helium is zero: not '
                 f'small, but exactly zero. That is the limit case, and it behaves nothing like '
                 f'an ordinary liquid.</text>')
    return wrap("".join(parts), w, h, "Viscosity of everyday liquids")


@cached
def superfluidity_panel() -> str:
    """Four consequences of zero viscosity, drawn as a simple panel."""
    w, h = 660, 250
    panels = [("No energy loss", "a stirred bath\nnever slows", CYAN),
              ("Creeps up walls", "climbs out and\ncoats the glass", AMBER),
              ("Fountain effect", "heating a point\njets upward", GREEN),
              ("Quantised swirl", "a spun bucket\nspins forever", VIOLET)]
    parts = [f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'SUPERFLUID HELIUM BELOW 2.2 K</text>']
    for index, (title, note, colour) in enumerate(panels):
        x0 = 24 + index * 160
        parts.append(f'<rect x="{x0}" y="46" width="144" height="150" rx="12" fill="#0d1c30" '
                     f'stroke="{colour}" stroke-opacity="0.5"/>')
        parts.append(f'<circle cx="{x0 + 72}" cy="100" r="26" fill="{colour}" opacity="0.18"/>')
        parts.append(f'<text x="{x0 + 72}" y="108" text-anchor="middle" fill="{colour}" '
                     f'font-size="22">{["◎", "↥", "⇡", "↻"][index]}</text>')
        parts.append(f'<text x="{x0 + 72}" y="152" text-anchor="middle" fill="{colour}" '
                     f'font-size="12" font-weight="700">{title}</text>')
        for line_index, line in enumerate(note.split("\n")):
            parts.append(f'<text x="{x0 + 72}" y="{172 + line_index * 15}" '
                         f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                         f'font-family="Sora, sans-serif">{line}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Helium is the only liquid on Earth that '
                 f'shows these. Its viscosity falls smoothly at first and then, below 2.2 K, '
                 f'drops to exactly zero.</text>')
    return wrap("".join(parts), w, h, "Four consequences of superfluidity")
