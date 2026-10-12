"""Chapter 9 diagrams: interference, diffraction, diffraction gratings, X-rays
and polarisation.

One mathematical idea runs through the whole chapter - bright when the path
difference is m lambda, dark at (m + 1/2) lambda - so the ``interference_explorer``
below is reused for Young's slits, a single slit, a grating and Michelson alike.
"""

from __future__ import annotations

import math

from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, wrap

__all__ = ["wavefront_growth", "huygens_construction", "coherence_panel",
           "interference_explorer", "youngs_arrangement", "fringe_pattern",
           "michelson_layout", "spacetime_ring", "sensitivity_scale",
           "diffraction_pattern", "grating_panel", "bragg_layers",
           "bragg_derivation", "polarisation_types", "polaroid_chain",
           "malus_curve", "brewster_diagram"]


def _axes(left, bottom, right, top, label_x, label_y):
    return (f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" '
            f'stroke="{MUTED}" stroke-width="1.5"/>'
            f'<line x1="{left}" y1="{bottom}" x2="{left}" y2="{top}" '
            f'stroke="{MUTED}" stroke-width="1.5"/>'
            f'<text x="{right}" y="{bottom + 18}" text-anchor="end" fill="{MUTED}" '
            f'font-size="10" font-family="JetBrains Mono, monospace">{label_x}</text>'
            f'<text x="{left - 6}" y="{top - 4}" text-anchor="end" fill="{MUTED}" '
            f'font-size="10" font-family="JetBrains Mono, monospace">{label_y}</text>')


@cached
def wavefront_growth(snapshots: int = 4, radius: float = 90.0) -> str:
    """Circular wavefronts growing from a point, and the line joining them."""
    w, h = 700, 260
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'WAVEFRONTS FROM A POINT SOURCE</text>']
    panel = (w - 40) / snapshots
    for index in range(snapshots):
        x0 = 20 + index * panel
        cx, cy = x0 + panel / 2, 150
        r = radius * (index + 1) * 0.85
        parts.append(f'<rect x="{x0}" y="46" width="{panel - 8}" height="190" rx="8" '
                     f'fill="#0b1a2c" stroke="#1b3350"/>')
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="{r:.1f}" fill="none" '
                     f'stroke="{CYAN}" stroke-width="2.5"/>')
        for sub in range(1, 4):
            parts.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="{r * sub / 3:.1f}" '
                         f'fill="none" stroke="#1b3350" stroke-width="1"/>')
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="4" fill="{AMBER}"/>')
        parts.append(f'<text x="{cx:.1f}" y="224" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="10" font-family="JetBrains Mono, monospace">t = {index}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">A wavefront is every point reached at the same '
                 f'instant. It always travels normal to itself, so a circle spreads radially.</text>')
    return wrap("".join(parts), w, h, "Circular wavefronts growing from a point source")


@cached
def huygens_construction() -> str:
    """Secondary wavelets from a wavefront and their envelope."""
    w, h = 700, 340
    cx, cy = 180, 110
    front = 130.0
    span = 330.0
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'HUYGENS: EVERY POINT SENDS A WAVELET</text>',
             f'<line x1="{cx}" y1="{cy}" x2="{cx + front}" y2="{cy}" stroke="{CYAN}" '
             f'stroke-width="4"/>',
             f'<text x="{cx + front + 8:.0f}" y="{cy - 10}" fill="{CYAN}" font-size="12" '
             f'font-weight="700">old wavefront</text>']
    n = 7
    for index in range(n):
        frac = index / (n - 1)
        y = cy - front / 2 + front * frac
        parts.append(f'<circle cx="{cx + front:.1f}" cy="{y:.1f}" r="{span * 0.42:.1f}" '
                     f'fill="none" stroke="{AMBER}" stroke-width="1.2" opacity="0.65"/>')
        parts.append(f'<circle cx="{cx + front:.1f}" cy="{y:.1f}" r="3.5" fill="{GREEN}"/>')
    # The envelope: the tangent line across the wavelets.
    parts.append(f'<line x1="{cx + front + span * 0.42:.1f}" y1="{cy - front / 2:.1f}" '
                 f'x2="{cx + front + span * 0.42:.1f}" y2="{cy + front / 2:.1f}" '
                 f'stroke="{GREEN}" stroke-width="3.5"/>')
    parts.append(f'<text x="{cx + front + span * 0.42 + 10:.0f}" y="{cy:.0f}" fill="{GREEN}" '
                 f'font-size="12" font-weight="700">new wavefront (the envelope)</text>')
    parts.append(f'<text x="{cx + 10}" y="{cy + 30}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Each amber circle is a secondary wavelet; the '
                 f'green line just touches all of them.</text>')
    parts.append(f'<text x="20" y="{h - 40}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'1. every point on the wavefront is a wavelet source</text>')
    parts.append(f'<text x="20" y="{h - 24}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'2. each spreads at the wave speed in all directions</text>')
    parts.append(f'<text x="20" y="{h - 8}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'3. the envelope touching them all is the new wavefront</text>')
    return wrap("".join(parts), w, h, "Huygens' construction of a new wavefront")


@cached
def coherence_panel() -> str:
    """Two cases that look identical on paper and behave completely differently."""
    w, h = 700, 300
    panels = [("Two lamps, same frequency", ROSE, "phase difference drifts",
               "fringes average out to a uniform glow"),
              ("One source, two slits", GREEN, "phase difference constant",
               "fringes stay put and are visible")]
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'SAME FREQUENCY IS NOT THE SAME AS COHERENT</text>']
    for index, (title, colour, detail, outcome) in enumerate(panels):
        x0 = 24 + index * 340
        top = 56
        parts.append(f'<rect x="{x0}" y="{top}" width="312" height="220" rx="10" '
                     f'fill="#0b1a2c" stroke="{colour}" stroke-opacity="0.45"/>')
        parts.append(f'<text x="{x0 + 16}" y="{top + 26}" fill="{colour}" font-size="14" '
                     f'font-weight="700">{title}</text>')
        for k in range(2):
            bx = x0 + 60 + k * 110
            parts.append(f'<circle cx="{bx}" cy="{top + 80}" r="12" fill="{colour}" '
                         f'opacity="0.8"/>')
            parts.append(f'<text x="{bx}" y="{top + 84}" text-anchor="middle" '
                         f'fill="#081426" font-size="11" font-weight="700">{k + 1}</text>')
        if index == 0:
            for k in range(3):
                phase = k * 2.1
                parts.append(f'<path d="M {bx + 26 + k * 8} {top + 80} '
                             f'l {14 * math.cos(phase):.1f} {14 * math.sin(phase):.1f}" '
                             f'stroke="{ROSE}" stroke-width="2"/>')
        else:
            for k in range(3):
                parts.append(f'<line x1="{bx + 26 + k * 8}" y1="{top + 80}" '
                             f'x2="{bx + 40 + k * 8}" y2="{top + 80}" '
                             f'stroke="{GREEN}" stroke-width="2"/>')
        parts.append(f'<text x="{x0 + 16}" y="{top + 132}" fill="#c6d6ea" font-size="12" '
                     f'font-family="Sora, sans-serif">{detail}</text>')
        parts.append(f'<text x="{x0 + 16}" y="{top + 154}" fill="#c6d6ea" font-size="12" '
                     f'font-family="Sora, sans-serif">{outcome}</text>')
        parts.append(f'<text x="{x0 + 16}" y="{top + 186}" fill="{colour}" font-size="11" '
                     f'font-family="JetBrains Mono, monospace">'
                     f'{"phase(t) = random" if index == 0 else "phase fixed"}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Coherence is about the relationship between two '
                 f'beams, not about either beam on its own.</text>')
    return wrap("".join(parts), w, h, "Coherent and incoherent sources compared")


@cached
def interference_explorer(wavelength: float, path_difference: float,
                           geometry: str = "double") -> str:
    """The common heart of the chapter: intensity against path difference.

    ``geometry`` selects the weighting - cos squared for two slits, the
    single-slit sinc envelope, or the sharp grating orders - but the bright and
    dark positions are the same rule throughout.
    """
    w, h = 700, 340
    left, right = 80, w - 200
    top, bottom = 70, 250
    span = max(wavelength * 3.0, path_difference * 1.25, 1e-12)
    n = 500

    def intensity(d):
        x = d / wavelength
        if geometry == "double":
            return math.cos(math.pi * x) ** 2
        if geometry == "single":
            return (math.sin(math.pi * x) / (math.pi * x) if x else 1.0) ** 2
        # Grating: sharp principal maxima with faint subsidiary fringes.
        return math.cos(math.pi * x) ** 8 if abs(x) < 40 else 0.0

    points = []
    for step in range(n + 1):
        frac = step / n
        d = frac * span
        px = left + frac * (right - left)
        py = bottom - intensity(d) * (bottom - top)
        points.append(f"{px:.1f},{py:.1f}")
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'{geometry.upper()} · ONE RULE FOR EVERY OPTICAL EXPERIMENT</text>',
             f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
             f'stroke-width="3"/>',
             _axes(left, bottom, right, top, "path difference", "I")]
    for order in range(-3, 4):
        d = order * wavelength
        if -span <= d <= span:
            px = left + (d + span) / (2 * span) * (right - left)
            colour = GREEN if order % 2 == 0 else ROSE
            parts.append(f'<line x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{bottom}" '
                         f'stroke="{colour}" stroke-width="1.4" stroke-dasharray="4 4" '
                         f'opacity="0.7"/>')
            parts.append(f'<text x="{px:.1f}" y="{top - 8}" text-anchor="middle" '
                         f'fill="{colour}" font-size="10" '
                         f'font-family="JetBrains Mono, monospace">{order}λ</text>')
    here = left + (min(path_difference, span) + span) / (2 * span) * (right - left)
    frac = (path_difference % wavelength) / wavelength if wavelength else 0
    if abs(frac) < 1e-9:
        kind, colour = "BRIGHT (constructive)", GREEN
    elif abs(frac - 0.5) < 1e-9:
        kind, colour = "DARK (destructive)", ROSE
    else:
        kind, colour = "PARTLY CONSTRUCTIVE", AMBER
    parts.append(f'<line x1="{here:.1f}" y1="{top - 4}" x2="{here:.1f}" y2="{bottom + 6}" '
                 f'stroke="{AMBER}" stroke-width="3"/>')
    parts.append(f'<rect x="{right + 20}" y="90" width="176" height="132" rx="10" '
                 f'fill="#0d1c30" stroke="{colour}" stroke-opacity="0.5"/>'
                 f'<text x="{right + 34}" y="114" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">PATH DIFFERENCE</text>'
                 f'<text x="{right + 34}" y="140" fill="#eef6ff" font-size="16" '
                 f'font-family="JetBrains Mono, monospace">{path_difference:.4g} m</text>'
                 f'<text x="{right + 34}" y="160" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">= {frac:.3g} λ</text>'
                 f'<text x="{right + 34}" y="186" fill="{colour}" font-size="12" '
                 f'font-weight="700">{kind}</text>'
                 f'<text x="{right + 34}" y="208" fill="{MUTED}" font-size="9" '
                 f'font-family="Sora, sans-serif">φ = 2π × '
                 f'{frac:.3g} = {2 * math.pi * frac:.4g} rad</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Bright at whole wavelengths, dark at half '
                 f'ones — true of Young’s slits, a single slit, a grating and '
                 f'Michelson alike.</text>')
    return wrap("".join(parts), w, h, f"Interference pattern: {geometry}")


@cached
def youngs_arrangement(wavelength: float, distance: float, separation: float,
                       slit_sep_label: float = 0.0) -> str:
    """The optical arrangement, drawn, with the path difference marked."""
    w, h = 700, 400
    src_x, scr_x = 60, 620
    mid = 180
    slity = mid - 26
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'YOUNG’S DOUBLE SLIT</text>',
             f'<circle cx="{src_x}" cy="{mid}" r="7" fill="{AMBER}"/>',
             f'<text x="{src_x - 4}" y="{mid - 14}" fill="{AMBER}" font-size="11" '
             f'font-weight="700">S</text>',
             f'<line x1="{src_x}" y1="{mid}" x2="{scr_x}" y2="{mid}" stroke="#1b3350" '
             f'stroke-width="2"/>',
             f'<rect x="{scr_x - 8}" y="{mid - 90}" width="14" height="180" rx="3" '
             f'fill="#0b1a2c" stroke="{MUTED}" stroke-width="2"/>']
    for offset in (-26, 26):
        parts.append(f'<line x1="{scr_x}" y1="{mid + offset - 9}" '
                     f'x2="{scr_x}" y2="{mid + offset + 9}" stroke="{MUTED}" '
                     f'stroke-width="7"/>')
    parts.append(f'<text x="{scr_x + 14}" y="{slity + 4}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">screen</text>')
    parts.append(f'<line x1="{scr_x - 30}" y1="{mid - 26}" x2="{scr_x - 30}" '
                 f'y2="{mid + 26}" stroke="{VIOLET}" stroke-width="2"/>')
    parts.append(f'<text x="{scr_x - 40}" y="{mid - 34}" text-anchor="end" fill="{VIOLET}" '
                 f'font-size="10" font-family="JetBrains Mono, monospace">d</text>')
    for offset in (-26, 26):
        colour = CYAN if offset < 0 else AMBER
        parts.append(f'<line x1="{src_x}" y1="{mid}" x2="{scr_x}" y2="{mid + offset}" '
                     f'stroke="{colour}" stroke-width="2" stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{scr_x + 22}" y="{mid - 32}" fill="{CYAN}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">path 1</text>')
    parts.append(f'<text x="{scr_x + 22}" y="{mid + 40}" fill="{AMBER}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">path 2</text>')
    parts.append(f'<text x="20" y="{h - 52}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'dy = λ L / d = ({wavelength:.3g} × {distance:.3g}) / '
                 f'{separation:.3g}</text>')
    parts.append(f'<text x="20" y="{h - 34}" fill="{GREEN}" font-size="14" '
                 f'font-weight="700" font-family="JetBrains Mono, monospace">'
                 f'fringe spacing = {wavelength * distance / separation:.4g} m</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Both beams leave the same source, so they stay '
                 f'coherent. Nothing is projecting through two separate lamps.</text>')
    return wrap("".join(parts), w, h, "Young's double slit arrangement")


@cached
def fringe_pattern(wavelength: float, distance: float, separation: float,
                   extent: float = 0.0) -> str:
    """A computed double-slit fringe pattern with the envelope marked."""
    w, h = 700, 300
    if extent <= 0:
        extent = 12.0 * wavelength * distance / separation
    left, right, top, bottom = 70, w - 40, 60, 240
    n = 600
    width = wavelength * distance / separation
    points = []
    for step in range(n + 1):
        frac = step / n
        y = -extent + frac * 2 * extent
        px = left + frac * (right - left)
        py = bottom - math.cos(math.pi * y / width) ** 2 * (bottom - top)
        points.append(f"{px:.1f},{py:.1f}")
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'FRINGE PATTERN, DRAWN FROM THE FORMULA</text>',
             f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
             f'stroke-width="2.4"/>',
             f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="{MUTED}" '
             f'stroke-width="1.5"/>']
    peak_x = left + (extent / (2 * extent)) * (right - left)
    parts.append(f'<line x1="{peak_x:.1f}" y1="{top - 6}" x2="{peak_x:.1f}" y2="{bottom}" '
                 f'stroke="{GREEN}" stroke-width="2" stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{peak_x:.1f}" y="{top - 12}" text-anchor="middle" fill="{GREEN}" '
                 f'font-size="11" font-family="JetBrains Mono, monospace">'
                 f'central maximum</text>')
    order = 1
    while True:
        y = order * width
        if y > extent:
            break
        for sign in (1, -1):
            px = left + ((y * sign + extent) / (2 * extent)) * (right - left)
            parts.append(f'<circle cx="{px:.1f}" cy="{top:.0f}" r="4" fill="{GREEN}"/>')
        order += 1
    parts.append(f'<text x="20" y="{h - 30}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'fringe spacing dy = {width:.4g} m; the envelope is a single-slit sinc '
                 f'squared, so fringes fade towards the edges</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">In a real experiment you would also see dust '
                 f'scattering and the single-slit diffraction envelope over the top.</text>')
    return wrap("".join(parts), w, h, "Double-slit fringe pattern")


@cached
def michelson_layout(arm_length: float = 4.0, path_change: float = 0.0) -> str:
    """The two arms, the beam splitter and where the fringes are counted."""
    w, h = 700, 340
    cx, cy = 210, 170
    right_x, up_y = cx + 230, cy - 130
    fringe = abs(path_change) / 5.0e-7
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'MICHELSON INTERFEROMETER · ARMS {arm_length:g} km</text>',
             f'<line x1="{cx}" y1="{cy}" x2="{right_x}" y2="{cy}" stroke="{CYAN}" '
             f'stroke-width="2.5"/>',
             f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{up_y}" stroke="{AMBER}" '
             f'stroke-width="2.5"/>',
             f'<line x1="{right_x}" y1="{cy}" x2="{right_x}" y2="{cy - 40}" '
             f'stroke="{CYAN}" stroke-width="6"/>',
             f'<line x1="{cx}" y1="{up_y}" x2="{cx + 40}" y2="{up_y}" '
             f'stroke="{AMBER}" stroke-width="6"/>',
             f'<rect x="{cx - 22}" y="{cy - 22}" width="44" height="44" rx="5" '
             f'fill="{VIOLET}" opacity="0.4" stroke="{VIOLET}" stroke-width="2"/>',
             f'<text x="{cx}" y="{cy + 58}" text-anchor="middle" fill="{VIOLET}" '
             f'font-size="12" font-weight="700">beam splitter</text>',
             f'<line x1="{cx - 90}" y1="{cy}" x2="{cx - 26}" y2="{cy}" stroke="{GREEN}" '
             f'stroke-width="2"/>',
             f'<text x="{cx - 96}" y="{cy - 12}" text-anchor="end" fill="{GREEN}" '
             f'font-size="11">source</text>',
             f'<circle cx="{cx + 30}" cy="{cy - 30}" r="34" fill="#081524" stroke="{GREEN}" '
             f'stroke-width="1.5"/>',
             f'<text x="{cx + 30}" y="{cy - 70}" text-anchor="middle" fill="{GREEN}" '
             f'font-size="11" font-family="JetBrains Mono, monospace">fringes</text>']
    # Fringes, not just a circle labelled "fringes". The whole point of moving
    # the mirror is that the pattern slides past the detector, so the bars are
    # offset by the fractional order: one full lambda/2 of path change shifts
    # them by one spacing and looks identical, which is exactly what happens.
    fx, fy, fr = cx + 30, cy - 30, 34
    spacing = 6.0
    offset = (fringe % 1.0) * spacing
    bar = 0
    x = fx - fr + offset - spacing
    while x < fx + fr and bar < 16:
        parts.append(f'<rect x="{x:.1f}" y="{fy - fr}" width="{spacing / 2:.1f}" '
                     f'height="{2 * fr}" fill="{GREEN}" opacity="0.55"/>')
        x += spacing
        bar += 1
    parts.append(f'<circle cx="{fx}" cy="{fy}" r="{fr}" fill="none" stroke="{GREEN}" '
                 f'stroke-width="1.5"/>')

    for index, (label, value, colour) in enumerate([
            ("arm length", f"{arm_length:g} km", CYAN),
            ("path change", f"{path_change:.4g} m", AMBER),
            ("fringes crossed", f"{fringe:.4g}", GREEN)]):
        parts.append(f'<text x="{right_x + 24}" y="{70 + index * 34}" fill="{MUTED}" '
                     f'font-size="10" font-family="JetBrains Mono, monospace">{label}</text>'
                     f'<text x="{right_x + 24}" y="{88 + index * 34}" fill="{colour}" '
                     f'font-size="14" font-family="JetBrains Mono, monospace">{value}</text>')
    parts.append(f'<text x="20" y="{h - 34}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'one fringe per λ/2 of mirror movement, because the light makes the '
                 f'round trip</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Michelson and Morley found no shift from an '
                 f'‘ether wind’ — and that null result became one of the two '
                 f'pillars of special relativity.</text>')
    return wrap("".join(parts), w, h, "Michelson interferometer layout")


@cached
def spacetime_ring(strain: float = 1.0e-21) -> str:
    """A ring of test masses before, during and after a wave passes."""
    w, h = 700, 320
    cx = 350
    panels = [("before", 0.0, MUTED), ("during - stretched", strain, ROSE),
              ("during - squeezed", -strain, CYAN), ("after", 0.0, MUTED)]
    for index, (label, value, colour) in enumerate(panels):
        x0 = 30 + index * 168
        top = 70
        cxr = x0 + 60
        parts = None
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'A GRAVITATIONAL WAVE DISTORTING SPACETIME</text>']
    for index, (label, value, colour) in enumerate(panels):
        x0 = 30 + index * 168
        cxr, cyr = x0 + 62, 165
        parts.append(f'<circle cx="{cxr}" cy="{cyr}" r="42" fill="none" stroke="#1b3350" '
                     f'stroke-width="1.5"/>')
        for k in range(8):
            angle = k * math.pi / 4
            # The wave squeezes one axis and stretches the perpendicular one.
            rx = 42 * (1.0 + value / 1e-21 * 60.0 * math.cos(2 * angle))
            ry = 42 * (1.0 - value / 1e-21 * 60.0 * math.cos(2 * angle))
            px = cxr + rx * math.cos(angle)
            py = cyr + ry * math.sin(angle)
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{colour}"/>')
        parts.append(f'<circle cx="{cxr}" cy="{cyr}" r="3" fill="{AMBER}"/>')
        parts.append(f'<text x="{cxr}" y="236" text-anchor="middle" fill="{colour}" '
                     f'font-size="10" font-family="Sora, sans-serif">{label}</text>')
    parts.append(f'<text x="20" y="{h - 34}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'LIGO arms: 4 km, strain ~ 1e-21 → an arm change of about 1e-18 m</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">That is a part in a million billion. The wave '
                 f'stretches one direction while squeezing the perpendicular one.</text>')
    return wrap("".join(parts), w, h, "A gravitational wave distorting a ring of masses")


@cached
def sensitivity_scale() -> str:
    """Lengths from a crystal lattice down to a gravitational wave."""
    w, h = 690, 300
    rows = [("crystal spacing", 1e-10, VIOLET),
            ("visible light", 5e-7, CYAN),
            ("human hair", 7e-5, GREEN),
            ("LIGO arm change", 1e-18, ROSE)]
    left, right = 220, w - 90
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'FOUR LENGTHS, TWENTY ORDERS OF MAGNITUDE</text>']
    lo, hi = -19.0, -3.0
    for index, (name, value, colour) in enumerate(rows):
        y = 70 + index * 52
        exponent = math.log10(value)
        frac = (exponent - lo) / (hi - lo)
        parts.append(f'<text x="24" y="{y + 18}" fill="#eef6ff" font-size="13" '
                     f'font-family="Sora, sans-serif">{name}</text>')
        parts.append(f'<rect x="{left}" y="{y + 4}" width="{(right - left) * frac:.1f}" '
                     f'height="18" rx="4" fill="{colour}" opacity="0.8"/>')
        parts.append(f'<text x="{left + (right - left) * frac + 8:.1f}" y="{y + 18}" '
                     f'fill="{colour}" font-size="12" font-family="JetBrains Mono, monospace">'
                     f'{value:.0e} m</text>')
    for power in range(-18, -2, 3):
        frac = (power - lo) / (hi - lo)
        x = left + frac * (right - left)
        parts.append(f'<text x="{x:.0f}" y="{h - 76}" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="9" font-family="JetBrains Mono, monospace">'
                     f'10^{power}</text>')
    parts.append(f'<text x="20" y="{h - 16}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Because the last figure is 10^8 smaller than a '
                 f'hair, LIGO uses 4 km arms and mirrors free of any material.</text>')
    return wrap("".join(parts), w, h, "Length scales compared on a logarithmic axis")


@cached
def diffraction_pattern(slit_width: float, wavelength: float) -> str:
    """Single-slit diffraction with the minima labelled."""
    w, h = 700, 320
    left, right, top, bottom = 70, w - 190, 60, 245
    first = wavelength / slit_width if slit_width else 0
    extent = first * 4.2 if first else 1.0
    n = 700

    def intensity(theta):
        x = slit_width * math.sin(theta) / wavelength if wavelength else 0.0
        return (math.sin(math.pi * x) / (math.pi * x) if abs(x) > 1e-12 else 1.0) ** 2

    points = []
    for step in range(n + 1):
        frac = step / n
        theta = -extent + frac * 2 * extent
        px = left + frac * (right - left)
        py = bottom - intensity(theta) * (bottom - top)
        points.append(f"{px:.1f},{py:.1f}")
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'SINGLE-SLIT DIFFRACTION · a sin θ = mλ</text>',
             f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
             f'stroke-width="3"/>',
             _axes(left, bottom, right, top, "θ", "I")]
    for order in range(0, 6):
        theta = order * first
        if theta > extent:
            break
        px = left + (theta + extent) / (2 * extent) * (right - left)
        py = bottom - intensity(theta) * (bottom - top)
        if order:
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{ROSE}"/>')
            parts.append(f'<text x="{px:.1f}" y="{bottom + 20}" text-anchor="middle" '
                         f'fill="{ROSE}" font-size="9" '
                         f'font-family="JetBrains Mono, monospace">m={order}</text>')
    peak_x = left + extent / (2 * extent) * (right - left)
    parts.append(f'<line x1="{peak_x:.1f}" y1="{top - 6}" x2="{peak_x:.1f}" y2="{bottom}" '
                 f'stroke="{GREEN}" stroke-width="2" stroke-dasharray="5 4"/>')
    parts.append(f'<line x1="{left}" y1="{top - 6}" x2="{peak_x:.1f}" y2="{top - 6}" '
                 f'stroke="{GREEN}" stroke-width="2"/>')
    parts.append(f'<line x1="{peak_x:.1f}" y1="{top - 6}" x2="{right}" y2="{top - 6}" '
                 f'stroke="{GREEN}" stroke-width="2"/>')
    parts.append(f'<text x="{peak_x:.1f}" y="{top - 14}" text-anchor="middle" fill="{GREEN}" '
                 f'font-size="11" font-family="JetBrains Mono, monospace">'
                 f'central max = 2λ/a</text>')
    parts.append(f'<rect x="{right + 16}" y="80" width="156" height="132" rx="10" '
                 f'fill="#0d1c30" stroke="{VIOLET}" stroke-opacity="0.5"/>'
                 f'<text x="{right + 30}" y="104" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">FIRST MINIMUM</text>'
                 f'<text x="{right + 30}" y="128" fill="{VIOLET}" font-size="15" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'θ = {math.degrees(first):.4g}°</text>'
                 f'<text x="{right + 30}" y="152" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">central maximum is</text>'
                 f'<text x="{right + 30}" y="170" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">twice as wide</text>'
                 f'<text x="{right + 30}" y="196" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">λ/a = '
                 f'{first:.4g}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">There is **no** minimum at m = 0 — the '
                 f'centre is the brightest point.</text>')
    return wrap("".join(parts), w, h, "Single-slit diffraction pattern")


@cached
def grating_panel(spacing: float, wavelength: float, max_order: int = 5) -> str:
    """Principal maxima of a grating, and the orders that cannot exist."""
    w, h = 700, 320
    left, right = 70, w - 180
    mid, half = 160, 60
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'GRATING ORDERS · d sin θ = mλ</text>',
             f'<line x1="{left}" y1="{mid}" x2="{right}" y2="{mid}" stroke="{MUTED}" '
             f'stroke-width="2"/>']
    limit = min(1.0, wavelength / spacing) if spacing else 1.0
    order = 0
    while order * limit <= max_order and order * wavelength / spacing <= 1.0:
        ratio = order * wavelength / spacing
        if ratio <= 1.0:
            px = left + (ratio) * (right - left)
            theta = math.degrees(math.asin(ratio))
            height = (1.0 / (1.0 + order * order)) * half
            parts.append(f'<line x1="{px:.1f}" y1="{mid}" x2="{px:.1f}" '
                         f'y2="{mid - height:.1f}" stroke="{GREEN}" stroke-width="4"/>')
            parts.append(f'<text x="{px:.1f}" y="{mid - height - 8:.1f}" text-anchor="middle" '
                         f'fill="{GREEN}" font-size="10" '
                         f'font-family="JetBrains Mono, monospace">m={order}, '
                         f'{theta:.1f}°</text>')
            parts.append(f'<line x1="{px:.1f}" y1="{mid}" x2="{px:.1f}" y2="{mid + 18}" '
                         f'stroke="{GREEN}" stroke-width="2"/>')
        order += 1
    blocked = order
    parts.append(f'<rect x="{right + 14}" y="70" width="166" height="150" rx="10" '
                 f'fill="#0d1c30" stroke="{MUTED}" stroke-opacity="0.5"/>'
                 f'<text x="{right + 28}" y="94" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">ORDER LIMITS</text>'
                 f'<text x="{right + 28}" y="120" fill="#eef6ff" font-size="13" '
                 f'font-family="JetBrains Mono, monospace">d = {spacing:.3g} m</text>'
                 f'<text x="{right + 28}" y="142" fill="#eef6ff" font-size="13" '
                 f'font-family="JetBrains Mono, monospace">λ = {wavelength:.3g} m</text>'
                 f'<text x="{right + 28}" y="172" fill="{GREEN}" font-size="12" '
                 f'font-weight="700">highest order: {blocked - 1}</text>'
                 f'<text x="{right + 28}" y="194" fill="{ROSE}" font-size="11" '
                 f'font-family="Sora, sans-serif">m = {blocked} would need</text>'
                 f'<text x="{right + 28}" y="210" fill="{ROSE}" font-size="11" '
                 f'font-family="Sora, sans-serif">sin θ &gt; 1</text>')
    parts.append(f'<text x="20" y="{h - 34}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'R = λ/Δλ = mN, with N = number of ruled lines</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The maxima come from thousands of wavelets in '
                 f'step; a slight angle destroys that, which is why they are so narrow.</text>')
    return wrap("".join(parts), w, h, "Diffraction grating orders")


@cached
def bragg_layers(plane_spacing: float, wavelength: float, order: int = 1,
                 theta_deg: float = 0.0) -> str:
    """Parallel crystal planes with the extra path drawn."""
    w, h = 700, 340
    theta = math.radians(theta_deg) if theta_deg else 0.35
    gap = 78.0
    top_y = 70
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'BRAGG: 2 d sin θ = mλ</text>']
    for index in range(4):
        y = top_y + index * gap
        parts.append(f'<line x1="60" y1="{y}" x2="460" y2="{y}" stroke="{CYAN}" '
                     f'stroke-width="5"/>')
        for atom in range(6):
            parts.append(f'<circle cx="{70 + atom * 76}" cy="{y}" r="6" fill="{CYAN}" '
                         f'opacity="0.8"/>')
    origin_x, origin_y = 70, top_y
    dx = math.cos(theta) * 330
    dy = math.sin(theta) * 330
    parts.append(f'<line x1="{origin_x}" y1="{origin_y}" x2="{origin_x + dx:.1f}" '
                 f'y2="{origin_y + dy:.1f}" stroke="{AMBER}" stroke-width="3"/>')
    parts.append(f'<line x1="{origin_x}" y1="{origin_y + gap}" x2="{origin_x + dx:.1f}" '
                 f'y2="{origin_y + gap + dy:.1f}" stroke="{VIOLET}" stroke-width="3"/>')
    parts.append(f'<line x1="{origin_x}" y1="{origin_y}" x2="{origin_x}" '
                 f'y2="{origin_y + gap}" stroke="{ROSE}" stroke-width="2" '
                 f'stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{origin_x - 10}" y="{origin_y + gap / 2 + 4}" '
                 f'text-anchor="end" fill="{ROSE}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">d</text>')
    parts.append(f'<text x="{origin_x + dx + 8:.1f}" y="{origin_y + dy + 16:.1f}" '
                 f'fill="{AMBER}" font-size="11" font-family="JetBrains Mono, monospace">'
                 f'ray 1 (grazing)</text>')
    parts.append(f'<text x="{origin_x + dx + 8:.1f}" y="{origin_y + gap + dy + 32:.1f}" '
                 f'fill="{VIOLET}" font-size="11" font-family="JetBrains Mono, monospace">'
                 f'ray 2 (down and back)</text>')
    extra = 2 * plane_spacing * math.sin(theta)
    ratio = extra / wavelength if wavelength else 0.0
    parts.append(f'<rect x="470" y="80" width="210" height="150" rx="10" fill="#0d1c30" '
                 f'stroke="{GREEN}" stroke-opacity="0.45"/>'
                 f'<text x="486" y="104" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">EXTRA PATH</text>'
                 f'<text x="486" y="130" fill="#eef6ff" font-size="14" '
                 f'font-family="JetBrains Mono, monospace">2 d sin θ</text>'
                 f'<text x="486" y="152" fill="{GREEN}" font-size="13" '
                 f'font-family="JetBrains Mono, monospace">= {extra:.4g} m</text>'
                 f'<text x="486" y="180" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">= {ratio:.4g} λ</text>'
                 f'<text x="486" y="204" fill="{GREEN}" font-size="12" font-weight="700">'
                 f'order {order}</text>')
    parts.append(f'<text x="20" y="{h - 36}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'sin θ = mλ/(2d); θ = '
                 f'{math.degrees(theta):.3g}° here</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">θ is the glancing angle to the plane, '
                 f'which is why detectors are quoted at 2θ.</text>')
    return wrap("".join(parts), w, h, "Bragg reflection from parallel crystal planes")


@cached
def polarisation_types() -> str:
    """Unpolarised, plane, circular and partial, drawn as vibrations."""
    w, h = 700, 300
    panels = [("Unpolarised", MUTED, "every plane at once"),
              ("Plane-polarised", CYAN, "one plane"),
              ("Circularly polarised", GREEN, "rotating steadily"),
              ("Partially polarised", AMBER, "mostly one plane")]
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'FOUR KINDS OF LIGHT, DRAWN ALONG THE BEAM</text>']
    for index, (title, colour, note) in enumerate(panels):
        x0 = 26 + index * 166
        cx, cy = x0 + 68, 150
        parts.append(f'<rect x="{x0}" y="52" width="150" height="190" rx="10" '
                     f'fill="#0b1a2c" stroke="{colour}" stroke-opacity="0.35"/>')
        if index == 0:
            for k in range(7):
                angle = k * 0.45
                parts.append(f'<line x1="{cx - 42}" y1="{cy}" x2="{cx + 42:.1f}" '
                             f'y2="{cy + 42 * math.sin(angle):.1f}" stroke="{colour}" '
                             f'stroke-width="1.4" opacity="0.75" '
                             f'transform="rotate(0 {cx} {cy})"/>')
        elif index == 1:
            parts.append(f'<line x1="{cx - 44}" y1="{cy}" x2="{cx + 44}" y2="{cy}" '
                         f'stroke="{colour}" stroke-width="3"/>')
        elif index == 2:
            for k in range(60):
                t = k / 59 * 2 * math.pi
                px = cx - 44 + t / (2 * math.pi) * 88
                py = cy + 34 * math.sin(t)
                parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.4" fill="{colour}"/>')
        else:
            parts.append(f'<line x1="{cx - 44}" y1="{cy}" x2="{cx + 44}" y2="{cy}" '
                         f'stroke="{colour}" stroke-width="3"/>')
            for k in range(3):
                parts.append(f'<line x1="{cx - 44}" y1="{cy + (k - 1) * 22}" '
                             f'x2="{cx + 44}" y2="{cy + (k - 1) * 22}" stroke="{colour}" '
                             f'stroke-width="1.2" opacity="0.55"/>')
        parts.append(f'<text x="{cx}" y="212" text-anchor="middle" fill="{colour}" '
                     f'font-size="12" font-weight="700">{title}</text>')
        parts.append(f'<text x="{cx}" y="230" text-anchor="middle" fill="{MUTED}" '
                     f'font-size="9" font-family="Sora, sans-serif">{note}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only transverse waves have a plane of '
                 f'vibration, which is why only they can be polarised.</text>')
    return wrap("".join(parts), w, h, "Four kinds of polarisation")


@cached
def polaroid_chain(angle: float, second: bool = False) -> str:
    """Unpolarised light through one, two or three polarisers."""
    w, h = 700, 320
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'LIGHT THROUGH A CHAIN OF POLAROIDS</text>']
    steps = [("unpolarised", 1.0, MUTED)]
    steps.append(("after 1st", 0.5, CYAN))
    if second:
        middle = 0.5 * math.cos(math.radians(angle)) ** 2
        steps.append((f"after 2nd ({angle:g}°)", middle, AMBER))
        steps.append(("after 3rd (45°)",
                      0.5 * math.cos(math.radians(angle)) ** 2 * 0.5, GREEN))
    else:
        steps.append((f"after 2nd ({angle:g}°)",
                      0.5 * math.cos(math.radians(angle)) ** 2, GREEN))
    panel = (w - 40) / len(steps)
    for index, (label, value, colour) in enumerate(steps):
        x0 = 20 + index * panel
        top, bottom = 60, 210
        parts.append(f'<rect x="{x0}" y="{top}" width="{panel - 10}" height="{bottom - top}" '
                     f'rx="10" fill="#0b1a2c" stroke="#1b3350"/>')
        bar_h = max(4.0, value * (bottom - top - 20))
        parts.append(f'<rect x="{x0 + 16}" y="{bottom - bar_h:.1f}" width="{panel - 42}" '
                     f'height="{bar_h:.1f}" rx="4" fill="{colour}" opacity="0.8"/>')
        parts.append(f'<text x="{x0 + (panel - 10) / 2:.0f}" y="{top + 24}" text-anchor="middle" '
                     f'fill="{colour}" font-size="11" font-weight="700">{value * 100:.3g}%</text>')
        parts.append(f'<text x="{x0 + (panel - 10) / 2:.0f}" y="{bottom + 22:.0f}" '
                     f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                     f'font-family="Sora, sans-serif">{label}</text>')
    if second:
        parts.append(f'<text x="20" y="{h - 30}" fill="{GREEN}" font-size="11" '
                     f'font-family="Sora, sans-serif">Three polarisers let light through that two '
                     f'crossed ones would block entirely.</text>')
        parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                     f'font-family="Sora, sans-serif">The middle one re-orients the vibrations, so '
                     f'the final filter has something to pass. Proof that this is interference, '
                     f'not simple filtering.</text>')
    else:
        parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                     f'font-family="Sora, sans-serif">The first polaroid halves unpolarised light; '
                     f'every one after that obeys Malus’s law, I = I₀ cos²θ.</text>')
    return wrap("".join(parts), w, h, "Light passing through polarisers")


@cached
def malus_curve() -> str:
    """The cos-squared curve with the transmission axes drawn."""
    w, h = 660, 320
    left, right, top, bottom = 70, w - 50, 60, 250
    n = 400
    points = []
    for step in range(n + 1):
        frac = step / n
        angle = frac * 180.0
        value = math.cos(math.radians(angle)) ** 2
        px = left + frac * (right - left)
        py = bottom - value * (bottom - top)
        points.append(f"{px:.1f},{py:.1f}")
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'MALUS’S LAW · I = I₀ cos²θ</text>',
             f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
             f'stroke-width="3.5"/>',
             _axes(left, bottom, right, top, "θ (degrees)", "I / I₀")]
    for angle, label in [(0, "100%"), (30, "75%"), (45, "50%"), (60, "25%"), (90, "0%")]:
        frac = angle / 180.0
        px = left + frac * (right - left)
        py = bottom - math.cos(math.radians(angle)) ** 2 * (bottom - top)
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{AMBER}"/>')
        parts.append(f'<text x="{px:.1f}" y="{bottom + 18}" text-anchor="middle" '
                     f'fill="{MUTED}" font-size="9" font-family="JetBrains Mono, monospace">'
                     f'{angle}°</text>')
        parts.append(f'<text x="{px + 10:.1f}" y="{py - 10:.1f}" fill="{AMBER}" font-size="11" '
                     f'font-family="JetBrains Mono, monospace">{label}</text>')
    parts.append(f'<text x="20" y="{h - 26}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The transmitted intensity can never exceed the '
                 f'input: a polariser only ever removes light.</text>')
    parts.append(f'<text x="20" y="{h - 10}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Note the squaring — halving the angle does '
                 f'not halve the intensity.</text>')
    return wrap("".join(parts), w, h, "Malus's law curve")


@cached
def brewster_diagram(n1: float = 1.0, n2: float = 1.5) -> str:
    """The Brewster angle, with the reflected and refracted rays at right angles."""
    import math as _m
    theta = _m.degrees(_m.atan(n2 / n1))
    w, h = 680, 330
    cx, cy = 200, 60
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'POLARISATION BY REFLECTION · θB = {theta:.2f}°</text>',
             f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{h - 70}" stroke="{MUTED}" '
             f'stroke-width="2.5"/>',
             f'<line x1="50" y1="{cy}" x2="{cx + 300}" y2="{cy}" stroke="{MUTED}" '
             f'stroke-width="2"/>',
             f'<rect x="{cx}" y="{cy}" width="440" height="{h - 70 - cy}" '
             f'fill="{CYAN}" opacity="0.07"/>']
    rad = _m.radians(theta)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 330 * _m.cos(rad):.1f}" '
                 f'y2="{cy + 330 * _m.sin(rad):.1f}" stroke="{AMBER}" stroke-width="3"/>')
    parts.append(f'<text x="{cx + 210}" y="{cy - 10}" fill="{AMBER}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">incident</text>')
    refl = _m.pi - _m.pi / 2 - rad
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx - 300 * _m.cos(refl):.1f}" '
                 f'y2="{cy + 300 * _m.sin(refl):.1f}" stroke="{ROSE}" stroke-width="3"/>')
    parts.append(f'<text x="{cx - 150}" y="{cy + 60}" fill="{ROSE}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">reflected (polarised)</text>')
    refr = _m.pi / 2 - rad
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 330 * _m.sin(refr):.1f}" '
                 f'y2="{cy + 330 * _m.cos(refr):.1f}" stroke="{GREEN}" stroke-width="3"/>')
    parts.append(f'<text x="{cx + 246}" y="{cy + 128}" fill="{GREEN}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">refracted</text>')
    parts.append(f'<rect x="{cx + 24}" y="{cy + 150}" width="180" height="66" rx="10" '
                 f'fill="#0d1c30" stroke="{GREEN}" stroke-opacity="0.45"/>'
                 f'<text x="{cx + 38}" y="{cy + 174}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">THE TWO RAYS</text>'
                 f'<text x="{cx + 38}" y="{cy + 202}" fill="{GREEN}" font-size="12" '
                 f'font-weight="700">are at 90° to each other</text>')
    parts.append(f'<text x="20" y="{h - 18}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'tan θB = n₂/n₁ = {n2}/{n1} = {n2 / n1:.4g}</text>')
    return wrap("".join(parts), w, h, "Brewster's angle and polarisation by reflection")