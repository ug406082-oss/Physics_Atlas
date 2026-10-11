"""Hand-drawn SVG illustrations for Physics Atlas.

Every diagram is plain SVG embedded as HTML, so it needs no internet
connection, no image files and no JavaScript. Scientific content here is
limited to geometry and labelling; all physics lives in ``physics_core``.
"""

from __future__ import annotations

import math

from .common import cached
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET

GOLDEN_ANGLE = 137.50776405


def _svg(body: str, width: int, height: int, label: str = "") -> str:
    role = f'role="img" aria-label="{label}"' if label else ""
    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" '
        f'style="max-width:{width}px;display:block;margin:0 auto" {role}>'
        f"{body}</svg>"
    )


@cached
def ambiguity_bars() -> str:
    """Show what the bare number "5" could mean in four different units."""
    rows = [
        ("5 mm", 0.005, "a tiny screw", CYAN),
        ("5 cm", 0.05, "a short pen", TEAL),
        ("5 m", 5.0, "a classroom", AMBER),
        ("5 km", 5000.0, "a short drive", VIOLET),
    ]
    width, height = 720, 236
    parts = []
    max_log = math.log10(5000.0)
    min_log = math.log10(0.001)
    bar_x, bar_max = 96, 470
    for index, (label, metres, note, colour) in enumerate(rows):
        y = 34 + index * 50
        span = (math.log10(metres) - min_log) / (max_log - min_log)
        length = max(10, span * bar_max)
        parts.append(
            f'<text x="0" y="{y + 15}" fill="#e6eefb" font-size="15" '
            f'font-family="JetBrains Mono, monospace">{label}</text>'
        )
        parts.append(
            f'<rect x="{bar_x}" y="{y}" width="{length:.1f}" height="24" rx="7" '
            f'fill="{colour}" opacity="0.85"/>'
        )
        parts.append(
            f'<text x="{bar_x + length + 10:.1f}" y="{y + 17}" fill="#9fb4cc" '
            f'font-size="13">≈ {note}</text>'
        )
    parts.append(
        f'<text x="0" y="{height - 12}" fill="{MUTED}" font-size="12">'
        f"Bars use a logarithmic length scale so all four fit on one picture.</text>"
    )
    return _svg("".join(parts), width, height,
                "The number 5 drawn as 5 millimetres, 5 centimetres, 5 metres and 5 kilometres")


@cached
def si_wheel() -> str:
    """A wheel of the seven SI base units."""
    size, cx, cy, radius = 560, 280, 218, 150
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="66" fill="rgba(45,212,191,.14)" '
        f'stroke="{TEAL}" stroke-width="2"/>',
        f'<text x="{cx}" y="{cy - 8}" text-anchor="middle" fill="#f1f7ff" '
        f'font-size="20" font-weight="700">7 base</text>',
        f'<text x="{cx}" y="{cy + 16}" text-anchor="middle" fill="{TEAL}" '
        f'font-size="18" font-weight="700">units</text>',
    ]
    labels = [
        ("m", "length"), ("kg", "mass"), ("s", "time"), ("A", "current"),
        ("K", "temperature"), ("mol", "amount"), ("cd", "luminous"),
    ]
    palette = [CYAN, TEAL, AMBER, VIOLET, ROSE, GREEN, "#7dd3fc"]
    for index, ((symbol, name), colour) in enumerate(zip(labels, palette)):
        angle = -math.pi / 2 + index * (2 * math.pi / len(labels))
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        lx = cx + (radius + 54) * math.cos(angle)
        ly = cy + (radius + 54) * math.sin(angle)
        parts.append(
            f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#24486e" '
            f'stroke-width="1.5"/>'
        )
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="34" fill="rgba(9,22,40,.95)" '
            f'stroke="{colour}" stroke-width="2.5"/>'
        )
        parts.append(
            f'<text x="{x:.1f}" y="{y + 6:.1f}" text-anchor="middle" fill="{colour}" '
            f'font-size="20" font-weight="700" font-family="JetBrains Mono, monospace">'
            f"{symbol}</text>"
        )
        parts.append(
            f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="middle" fill="#9fb4cc" '
            f'font-size="13">{name}</text>'
        )
    return _svg("".join(parts), size, 440, "Wheel of the seven SI base units")


@cached
def balance(left: str, right: str, balanced: bool, left_dims: str = "",
            right_dims: str = "") -> str:
    """A weighing-beam picture for a dimensional homogeneity test."""
    width, height = 640, 260
    pivot_x, beam_y = 320, 150
    tilt = 0 if balanced else 13
    colour = GREEN if balanced else ROSE
    left_y = beam_y - math.sin(math.radians(tilt)) * 200
    right_y = beam_y + math.sin(math.radians(tilt)) * 200
    parts = [
        f'<polygon points="{pivot_x},{beam_y - 4} {pivot_x - 34},215 {pivot_x + 34},215" '
        f'fill="#12304f" stroke="#2b5a86" stroke-width="2"/>',
        f'<rect x="{pivot_x - 96}" y="215" width="192" height="12" rx="6" fill="#16345a"/>',
        f'<g transform="rotate({tilt} {pivot_x} {beam_y})">',
        f'<rect x="{pivot_x - 210}" y="{beam_y - 7}" width="420" height="14" rx="7" '
        f'fill="{colour}" opacity="0.9"/>',
        f'<circle cx="{pivot_x}" cy="{beam_y}" r="11" fill="#0b1a2d" stroke="{colour}" '
        f'stroke-width="3"/>',
        f'<line x1="{pivot_x - 190}" y1="{beam_y}" x2="{pivot_x - 190}" y2="{beam_y + 34}" '
        f'stroke="{MUTED}" stroke-width="2"/>',
        f'<line x1="{pivot_x + 190}" y1="{beam_y}" x2="{pivot_x + 190}" y2="{beam_y + 34}" '
        f'stroke="{MUTED}" stroke-width="2"/>',
        f'<rect x="{pivot_x - 250}" y="{beam_y + 34}" width="120" height="52" rx="10" '
        f'fill="rgba(9,22,40,.96)" stroke="{CYAN}" stroke-width="2"/>',
        f'<text x="{pivot_x - 190}" y="{beam_y + 58}" text-anchor="middle" fill="#f1f7ff" '
        f'font-size="17" font-weight="700">{left}</text>',
        f'<text x="{pivot_x - 190}" y="{beam_y + 76}" text-anchor="middle" fill="{CYAN}" '
        f'font-size="12" font-family="JetBrains Mono, monospace">{left_dims}</text>',
        f'<rect x="{pivot_x + 130}" y="{beam_y + 34}" width="120" height="52" rx="10" '
        f'fill="rgba(9,22,40,.96)" stroke="{AMBER}" stroke-width="2"/>',
        f'<text x="{pivot_x + 190}" y="{beam_y + 58}" text-anchor="middle" fill="#f1f7ff" '
        f'font-size="17" font-weight="700">{right}</text>',
        f'<text x="{pivot_x + 190}" y="{beam_y + 76}" text-anchor="middle" fill="{AMBER}" '
        f'font-size="12" font-family="JetBrains Mono, monospace">{right_dims}</text>',
        "</g>",
        f'<text x="{pivot_x}" y="34" text-anchor="middle" fill="{colour}" font-size="20" '
        f'font-weight="800">'
        + ("BALANCED · both sides match" if balanced else "TILTED · the sides disagree")
        + "</text>",
        f'<text x="{pivot_x}" y="58" text-anchor="middle" fill="#9fb4cc" font-size="13">'
        + ("Homogeneous: every term has the same dimensions."
           if balanced else "Not homogeneous: the two sides have different dimensions.")
        + "</text>",
    ]
    _ = left_y, right_y
    return _svg("".join(parts), width, height,
                "Balance beam comparing the two sides of an equation")


@cached
def error_target(readings, reference: float, mean: float, spread: float) -> str:
    """A bullseye where the distance from the centre equals the size of the error."""
    size = 460
    cx = cy = size / 2
    scale = max(spread * 3.0, abs(mean - reference) * 2.0, 1e-9)
    parts = []
    for ring in (1.0, 0.66, 0.33):
        r = 160 * ring
        parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="#22406a" '
            f'stroke-width="1.5"/>'
        )
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{GREEN}"/>')
    for index, value in enumerate(readings):
        error = (value - reference) / scale
        radius = min(abs(error) * 160.0, 178.0)
        angle = math.radians(index * GOLDEN_ANGLE)
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{CYAN}" '
            f'stroke="#04101f" stroke-width="1.2" opacity="0.92"/>'
        )
    bias = mean - reference
    bx = cx + min(abs(bias) / scale * 160.0, 178.0) * (1 if bias >= 0 else -1)
    parts.append(
        f'<line x1="{cx}" y1="{cy}" x2="{bx:.1f}" y2="{cy}" stroke="{AMBER}" '
        f'stroke-width="3" stroke-dasharray="6 5"/>'
    )
    parts.append(
        f'<text x="{cx}" y="{size - 16}" text-anchor="middle" fill="{MUTED}" font-size="13">'
        f"Distance from the green centre = size of the error</text>"
    )
    return _svg("".join(parts), size, size,
                "Bullseye of simulated readings; distance from centre is the measurement error")


@cached
def uncertainty_number_line(value: float, uncertainty: float) -> str:
    """Draw the reported interval ``value ± uncertainty`` on a number line."""
    width, height = 640, 150
    low, high = value - uncertainty, value + uncertainty
    pad = max(abs(uncertainty) * 2.5, abs(value) * 0.15, 1e-9)
    axis_low, axis_high = low - pad, high + pad
    if axis_high == axis_low:
        axis_high = axis_low + 1.0

    def place(x: float) -> float:
        return 40 + (x - axis_low) / (axis_high - axis_low) * (width - 80)

    x_low, x_high, x_val = place(low), place(high), place(value)
    parts = [
        f'<line x1="30" y1="70" x2="{width - 30}" y2="70" stroke="#2b4a72" stroke-width="2"/>',
        f'<rect x="{x_low:.1f}" y="52" width="{x_high - x_low:.1f}" height="36" rx="6" '
        f'fill="{CYAN}" opacity="0.28" stroke="{CYAN}" stroke-width="1.5"/>',
        f'<line x1="{x_val:.1f}" y1="44" x2="{x_val:.1f}" y2="96" stroke="{AMBER}" '
        f'stroke-width="3"/>',
        f'<text x="{x_val:.1f}" y="36" text-anchor="middle" fill="{AMBER}" font-size="15" '
        f'font-weight="700">{value:g} ± {uncertainty:g}</text>',
        f'<text x="{x_low:.1f}" y="116" text-anchor="middle" fill="#9fb4cc" font-size="13">'
        f"{low:g}</text>",
        f'<text x="{x_high:.1f}" y="116" text-anchor="middle" fill="#9fb4cc" font-size="13">'
        f"{high:g}</text>",
        f'<text x="{width / 2}" y="140" text-anchor="middle" fill="{MUTED}" font-size="12">'
        f"The shaded band is the range the true value is expected to lie in.</text>",
    ]
    return _svg("".join(parts), width, height, "Number line showing a value plus or minus an uncertainty")


@cached
def sigfig_highlight(text: str) -> str:
    """Colour the significant digits of a written value and grey out the rest.

    Green = significant, grey = not significant, amber = ambiguous (a trailing
    zero in a whole number with no decimal point).
    """
    body = str(text).strip().replace(" ", "")
    digits: list[str] = []
    suffix = ""
    for index, char in enumerate(body):
        if char in "eE" and index + 1 < len(body):
            suffix = body[index:]
            break
        digits.append(char)

    flags: list[str] = []
    seen_nonzero = point_seen = False
    for position, char in enumerate(digits):
        if char == ".":
            point_seen = True
            flags.append("plain")
            continue
        if not char.isdigit():
            flags.append("plain")
            continue
        if char != "0":
            seen_nonzero = True
            flags.append("yes")
            continue
        if not seen_nonzero:
            flags.append("no")
        elif point_seen:
            flags.append("yes")
        elif any(c not in "0" and c.isdigit() for c in digits[position + 1:]):
            flags.append("yes")
        else:
            flags.append("maybe")

    palette = {"yes": GREEN, "no": "#5b7391", "maybe": AMBER, "plain": "#c6d6ea"}
    spans = [
        f'<tspan fill="{palette[flag]}" font-weight="{"700" if flag == "yes" else "400"}">'
        f"{char}</tspan>"
        for char, flag in zip(digits, flags)
    ]
    if suffix:
        spans.append(f'<tspan fill="#9fb4cc">{suffix}</tspan>')
    return (
        '<div class="atlas-card" style="text-align:center">'
        f'<div class="kicker"><span style="color:{GREEN}">SIGNIFICANT</span> · '
        f'<span style="color:#5b7391">NOT SIGNIFICANT</span> · '
        f'<span style="color:{AMBER}">AMBIGUOUS</span></div>'
        '<div style="font-family:JetBrains Mono,monospace;font-size:2.4rem;letter-spacing:.08em">'
        + "".join(spans) +
        "</div></div>"
    )


@cached
def progress_ring(fraction: float, caption: str = "", size: int = 190) -> str:
    """A circular mastery meter."""
    radius = 74
    circumference = 2 * math.pi * radius
    filled = max(0.0, min(1.0, fraction)) * circumference
    percent = round(fraction * 100)
    parts = [
        f'<circle cx="100" cy="100" r="{radius}" fill="none" stroke="#16324f" stroke-width="18"/>',
        f'<circle cx="100" cy="100" r="{radius}" fill="none" stroke="{TEAL}" stroke-width="18" '
        f'stroke-linecap="round" stroke-dasharray="{filled:.1f} {circumference - filled:.1f}" '
        f'transform="rotate(-90 100 100)"/>',
        f'<text x="100" y="96" text-anchor="middle" fill="#f1f7ff" font-size="38" '
        f'font-weight="800">{percent}%</text>',
        f'<text x="100" y="124" text-anchor="middle" fill="{TEAL}" font-size="14" '
        f'font-weight="700">MASTERED</text>',
    ]
    if caption:
        parts.append(
            f'<text x="100" y="176" text-anchor="middle" fill="#9fb4cc" font-size="13">'
            f"{caption}</text>"
        )
    return _svg("".join(parts), 200, 190 if caption else 170, "Mastery progress ring")


@cached
def unit_blocks(symbol: str, parts: list[tuple[str, str]]) -> str:
    """Draw a derived unit as stacked building blocks of base units."""
    width = 640
    block_w, gap = 132, 16
    total = len(parts) * block_w + (len(parts) - 1) * gap
    start = max(10, (width - total) / 2)
    shapes = [
        f'<text x="{width / 2}" y="34" text-anchor="middle" fill="#f1f7ff" font-size="22" '
        f'font-weight="800">{symbol}</text>',
        f'<text x="{width / 2}" y="58" text-anchor="middle" fill="{MUTED}" font-size="13">'
        f"built from the base units</text>",
    ]
    for index, (unit, role) in enumerate(parts):
        x = start + index * (block_w + gap)
        colour = [CYAN, AMBER, VIOLET, GREEN][index % 4]
        shapes.append(
            f'<rect x="{x:.0f}" y="80" width="{block_w}" height="86" rx="14" '
            f'fill="rgba(9,22,40,.96)" stroke="{colour}" stroke-width="2.5"/>'
        )
        shapes.append(
            f'<text x="{x + block_w / 2:.0f}" y="126" text-anchor="middle" fill="{colour}" '
            f'font-size="26" font-weight="700" font-family="JetBrains Mono, monospace">'
            f"{unit}</text>"
        )
        shapes.append(
            f'<text x="{x + block_w / 2:.0f}" y="150" text-anchor="middle" fill="#9fb4cc" '
            f'font-size="12">{role}</text>'
        )
        if index < len(parts) - 1:
            shapes.append(
                f'<text x="{x + block_w + gap / 2:.0f}" y="132" text-anchor="middle" '
                f'fill="#5b7391" font-size="22">×</text>'
            )
    return _svg("".join(shapes), width, 190, f"How the unit {symbol} is built from base units")


@cached
def reading_ruler(reading: float, resolution: float, reference: float) -> str:
    """A zoomed-in scale showing one reading against its smallest division."""
    width, height = 640, 150
    divisions = 10
    span = resolution * divisions
    left_value = reading - span * 0.45

    def place(x: float) -> float:
        return 40 + (x - left_value) / span * (width - 80)

    parts = [
        f'<line x1="40" y1="86" x2="{width - 40}" y2="86" stroke="#2b4a72" stroke-width="3"/>'
    ]
    for i in range(divisions + 1):
        value = left_value + i * resolution
        x = place(value)
        tall = i % 5 == 0
        parts.append(
            f'<line x1="{x:.1f}" y1="86" x2="{x:.1f}" y2="{70 if tall else 78}" '
            f'stroke="#7f9ab8" stroke-width="{2 if tall else 1.2}"/>'
        )
        if tall:
            parts.append(
                f'<text x="{x:.1f}" y="108" text-anchor="middle" fill="#9fb4cc" font-size="11">'
                f"{value:.3g}</text>"
            )
    xr = place(reading)
    xf = place(reference)
    parts.append(
        f'<polygon points="{xr:.1f},86 {xr - 9:.1f},58 {xr + 9:.1f},58" fill="{AMBER}"/>'
    )
    parts.append(
        f'<text x="{xr:.1f}" y="46" text-anchor="middle" fill="{AMBER}" font-size="14" '
        f'font-weight="700">reading {reading:.4g}</text>'
    )
    parts.append(
        f'<line x1="{xf:.1f}" y1="94" x2="{xf:.1f}" y2="126" stroke="{GREEN}" '
        f'stroke-width="3" stroke-dasharray="5 4"/>'
    )
    parts.append(
        f'<text x="{xf:.1f}" y="142" text-anchor="middle" fill="{GREEN}" font-size="13">'
        f"reference {reference:.4g}</text>"
    )
    parts.append(
        f'<text x="{width / 2}" y="20" text-anchor="middle" fill="{MUTED}" font-size="12">'
        f"One small division = {resolution:g} · the amber triangle is your reading.</text>"
    )
    return _svg("".join(parts), width, height, "Scale showing a reading and its smallest division")
