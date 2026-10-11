"""Chapter 10 diagrams: heat, the molecular model, gas laws, molecular speeds,
the first law, entropy and the Carnot cycle.

Nothing in this chapter is drawn from a photograph. Every curve here is computed
from the same formulas the core module uses, so the picture and the number can
never drift apart: the P-V axes rescale to the path you choose, the speed
distribution is the Maxwell-Boltzmann function evaluated from R and T, and the
Carnot cycle's enclosed area really is the trapezium sum of its own four legs.
"""

from __future__ import annotations

import math

from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, wrap

__all__ = ["temperature_scales", "thermometer_cutaway", "equilibrium_contact",
           "molecular_box", "pressure_collisions", "derivation_ladder",
           "speed_distribution", "energy_lines", "gas_law_grid",
           "pv_area", "process_quadrant", "heat_capacity_bars",
           "reversible_split", "entropy_room", "engine_blocks",
           "carnot_cycle_plot", "refrigerator_blocks", "work_by_vs_on",
           "degradation_scale", "design_energy_flow"]

_MONO = "JetBrains Mono, monospace"
_SANS = "Inter, system-ui, sans-serif"


def _label(x, y, text, fill=MUTED, size=10, anchor="start", family=_MONO):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{fill}" '
            f'font-size="{size}" font-family="{family}">{text}</text>')


def _tick(x, y, text, fill=MUTED, size=9, anchor="middle"):
    return (f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y + 4:.1f}" '
            f'stroke="{fill}" stroke-width="1"/>' + _label(x, y + 14, text, fill, size, anchor))


# --------------------------------------------------------------------------
# 10.1  Heat and temperature
# --------------------------------------------------------------------------

@cached
def temperature_scales(absolute_zero: float = -273.15, reading: float = 25.0) -> str:
    """One thermometer marked on all three scales, with absolute zero at the bottom."""
    w, h = 720, 330
    bulb_x, top, bottom = 150, 44, 270
    span = 120.0 - absolute_zero                      # kelvin across the scale
    zero_y = bottom - (0 - absolute_zero) / span * (bottom - top)

    def y_of(kelvin):
        return bottom - (kelvin - absolute_zero) / span * (bottom - top)

    parts = [_label(24, 26, "ONE THERMOMETER, THREE SCALES", MUTED, 12),
             _label(24, 44, "A temperature difference is the same size in C and K; only the "
                            "zero points differ.", MUTED, 10, family=_SANS)]

    # bulb and stem
    parts.append(f'<circle cx="{bulb_x}" cy="{bottom + 22}" r="20" fill="{ROSE}" '
                 f'opacity="0.25" stroke="{ROSE}" stroke-width="1.5"/>')
    parts.append(f'<rect x="{bulb_x - 6}" y="{top}" width="12" height="{bottom - top}" rx="6" '
                 f'fill="{ROSE}" opacity="0.12" stroke="{ROSE}" stroke-width="1.2"/>')
    # mercury up to the current reading
    mark_y = y_of(reading + 273.15)
    parts.append(f'<rect x="{bulb_x - 4}" y="{mark_y:.1f}" width="8" '
                 f'height="{bottom - mark_y:.1f}" rx="4" fill="{ROSE}" opacity="0.75"/>')

    for celsius in (-273.15, -100, 0, 37, 100, 120):
        k = celsius - absolute_zero
        y = y_of(k)
        if not top - 4 <= y <= bottom + 4:
            continue
        parts.append(f'<line x1="{bulb_x - 14}" y1="{y:.1f}" x2="{bulb_x + 14}" y2="{y:.1f}" '
                     f'stroke="{MUTED}" stroke-width="1.4"/>')
        if abs(celsius + 273.15) < 1e-9 or abs(celsius - 100) < 1e-9 or abs(celsius) < 1e-9:
            kelvin = celsius + 273.15
            parts.append(_label(bulb_x + 26, y + 4, f"{celsius:g} °C", CYAN, 11))
            parts.append(_label(bulb_x + 122, y + 4, f"{kelvin:.2f} K", TEAL, 11))
            parts.append(_label(bulb_x + 210, y + 4,
                                f"{celsius * 9 / 5 + 32:g} °F", AMBER, 11))
    # the three scale headings
    parts.append(_label(bulb_x + 26, top - 14, "CELSIUS", CYAN, 10))
    parts.append(_label(bulb_x + 122, top - 14, "KELVIN", TEAL, 10))
    parts.append(_label(bulb_x + 210, top - 14, "FAHRENHEIT", AMBER, 10))

    # absolute zero is the important one - mark it hard
    parts.append(f'<line x1="{bulb_x - 30}" y1="{zero_y:.1f}" x2="{bulb_x + 250}" '
                 f'y2="{zero_y:.1f}" stroke="{VIOLET}" stroke-width="1.6" '
                 f'stroke-dasharray="5 4"/>')
    parts.append(_label(bulb_x - 34, zero_y + 4, "ABSOLUTE ZERO", VIOLET, 11, "end"))
    parts.append(_label(bulb_x - 34, zero_y + 20, "0 K = −273.15 °C", VIOLET, 10, "end"))

    # a note panel on the right
    panel = [("Why the kelvin scale exists",
              "The volume of a gas is proportional to T on a kelvin axis and on nothing else."),
             ("Why that is not circular",
              "It is measured: the isotherm lines of real gases all extrapolate to the same "
              "intercept."),
             ("What is fixed, now",
              "Since 2019 the kelvin is defined by fixing the Boltzmann constant, so k = "
              "1.380649e-23 J K⁻¹ exactly.")]
    y = 120
    for title, body in panel:
        parts.append(_label(420, y, title, CYAN, 12, family=_SANS))
        for i, line in enumerate(_wrap_text(body, 42)):
            parts.append(_label(420, y + 18 + i * 15, line, MUTED, 10, family=_SANS))
        y += 40 + 15 * len(_wrap_text(body, 42))
    parts.append(f'<line x1="{bulb_x - 34}" y1="{mark_y:.1f}" x2="{bulb_x + 250}" '
                 f'y2="{mark_y:.1f}" stroke="{ROSE}" stroke-width="1" '
                 f'stroke-dasharray="2 3" opacity="0.7"/>')
    parts.append(_label(bulb_x + 258, mark_y + 4, f"your reading: {reading:g} °C", ROSE, 10))
    return wrap("".join(parts), w, h, "Temperature scales and absolute zero")


def _wrap_text(text: str, width: int) -> list:
    words, lines, current = text.split(), [], ""
    for word in words:
        if len(current) + len(word) + 1 > width and current:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    return lines


@cached
def thermometer_cutaway(expansion_ratio: float = 100.0) -> str:
    """A liquid-in-glass thermometer cut open, showing both expansion volumes."""
    w, h = 700, 280
    parts = [_label(24, 26, "LIQUID-IN-GLASS, CUT OPEN", MUTED, 12),
             _label(24, 44, "The liquid expands about a hundred times faster than the glass "
                            "around it, so the column climbs.", MUTED, 10, family=_SANS)]

    glass_x, bulb_cx, bulb_cy = 210, 210, 216
    parts.append(f'<path d="M {glass_x - 7} 52 L {glass_x + 7} 52 L {glass_x + 7} 186 '
                 f'C {glass_x + 10} 196, {glass_x + 10} 204 C {bulb_cx + 58} 218, '
                 f'{bulb_cx + 58} 268, {bulb_cx} 268 C {bulb_cx - 58} 268, '
                 f'{bulb_cx - 58} 218, {glass_x - 10} 204 C {glass_x - 10} 196, '
                 f'{glass_x - 7} 186, {glass_x - 7} 52 Z" fill="{CYAN}" opacity="0.12" '
                 f'stroke="{MUTED}" stroke-width="2"/>')
    parts.append(f'<circle cx="{bulb_cx}" cy="{bulb_cy}" r="40" fill="{ROSE}" opacity="0.35"/>')
    parts.append(f'<rect x="{glass_x - 5}" y="140" width="10" height="90" fill="{ROSE}" '
                 f'opacity="0.7"/>')

    # the two expansions, side by side
    panels = [("LIQUID", "1.00", ROSE, 470, 86),
              ("GLASS", "1.01", MUTED, 470, 176)]
    for title, base, colour, x, y in panels:
        parts.append(f'<rect x="{x}" y="{y}" width="120" height="56" rx="8" '
                     f'fill="{colour}" opacity="0.10" stroke="{colour}" stroke-width="1.2"/>')
        parts.append(_label(x + 12, y + 22, f"{title}  V = {base}", colour, 11))
        parts.append(_label(x + 12, y + 42, "expanded by 1 degree", MUTED, 9))

    parts.append(f'<rect x="620" y="86" width="34" height="56" rx="6" fill="{ROSE}" '
                 f'opacity="0.35" stroke="{ROSE}"/>')
    parts.append(_label(637, 158, "1.00", ROSE, 10, "middle"))
    parts.append(f'<rect x="620" y="176" width="36" height="56" rx="6" fill="{MUTED}" '
                 f'opacity="0.30" stroke="{MUTED}"/>')
    parts.append(_label(638, 248, "1.01", MUTED, 10, "middle"))
    parts.append(_label(470, 264, f"ratio ≈ {expansion_ratio:.0f} : 1 over 0 °C to 100 °C",
                        AMBER, 11))
    parts.append(_label(24, 264, "A constriction above the bulb (clinical thermometer) traps "
                                 "the column so the reading can be taken.", MUTED, 10,
                        family=_SANS))
    return wrap("".join(parts), w, h, "Liquid-in-glass thermometer")


@cached
def equilibrium_contact(count: int = 4) -> str:
    """A row of bodies in thermal contact, with the heat direction shown."""
    w, h = 700, 240
    parts = [_label(24, 26, "THERMAL CONTACT", MUTED, 12),
             _label(24, 44, "Heat flows from the hotter body to the colder one until they "
                            "all share one temperature.", MUTED, 10, family=_SANS)]
    temps = [90.0, 60.0, 45.0, 30.0]
    x0, gap, bw, bh = 60, 60, 80, 120
    for i, t in enumerate(temps):
        x = x0 + i * (bw + gap)
        height = 20 + t * 0.9
        colour = ROSE if t >= 60 else (AMBER if t >= 40 else CYAN)
        parts.append(f'<rect x="{x}" y="{180 - height:.1f}" width="{bw}" height="{height:.1f}" '
                     f'rx="6" fill="{colour}" opacity="0.28" stroke="{colour}" '
                     f'stroke-width="1.5"/>')
        parts.append(_label(x + bw / 2, 200, f"body {i + 1}", MUTED, 10, "middle"))
        parts.append(_label(x + bw / 2, 218, f"{t:g} °C", colour, 12, "middle"))
        if i < len(temps) - 1:
            mid = x + bw + gap / 2
            parts.append(f'<line x1="{mid:.1f}" y1="130" x2="{mid:.1f}" y2="112" '
                         f'stroke="{AMBER}" stroke-width="2.2"/>')
            parts.append(f'<path d="M {mid - 5:.1f} 118 L {mid + 5:.1f} 118 L {mid:.1f} 108 Z" '
                         f'fill="{AMBER}"/>')
            parts.append(_label(mid, 102, "Q", AMBER, 11, "middle"))
    parts.append(f'<rect x="{x0 - 20}" y="234" width="520" height="2" fill="{MUTED}" '
                 f'opacity="0.4"/>')
    parts.append(_label(x0 - 20, 12, "not in equilibrium", ROSE, 11))
    parts.append(_label(430, 26, "THE ZEROTH LAW", CYAN, 12))
    for i, line in enumerate(["If A = B and B = C in temperature,",
                              "then A = C. That is what makes a",
                              "thermometer worth owning."]):
        parts.append(_label(430, 50 + i * 16, line, MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Thermal contact and heat flow")


# --------------------------------------------------------------------------
# 10.2  The molecular model
# --------------------------------------------------------------------------

@cached
def molecular_box(count: int = 40, seed: int = 7) -> str:
    """A box of molecules, positions drawn from a fixed seed so the picture is stable."""
    w, h = 700, 360
    left, right, top, bottom = 60, 660, 70, 330
    parts = [_label(24, 26, "A GAS, AS KINETIC MOLECULAR THEORY SEES IT", MUTED, 12),
             _label(24, 44, "The molecule size drawn here is hugely exaggerated. In a real gas "
                            "their own total volume is negligible.", MUTED, 10, family=_SANS)]
    parts.append(f'<rect x="{left}" y="{top}" width="{right - left}" height="{bottom - top}" '
                 f'rx="10" fill="{CYAN}" opacity="0.05" stroke="{CYAN}" stroke-width="2"/>')

    state = seed
    for i in range(count):
        state = (1103515245 * state + 12345) % (1 << 31)
        px = left + 18 + (state % (right - left - 36))
        state = (1103515245 * state + 12345) % (1 << 31)
        py = top + 18 + (state % (bottom - top - 36))
        state = (1103515245 * state + 12345) % (1 << 31)
        angle = (state % 360)
        state = (1103515245 * state + 12345) % (1 << 31)
        speed = 6 + state % 14
        dx = math.cos(math.radians(angle)) * speed
        dy = math.sin(math.radians(angle)) * speed
        colour = [CYAN, TEAL, AMBER, VIOLET][i % 4]
        parts.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{px + dx:.1f}" y2="{py + dy:.1f}" '
                     f'stroke="{colour}" stroke-width="1.6" opacity="0.8"/>')
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{colour}"/>')

    parts.append(_label(left, bottom + 24, "random motion, constant elastic collisions",
                        CYAN, 11))
    parts.append(_label(left, bottom + 42, "no attractions between molecules, so they reach "
                                           "every corner", MUTED, 10, family=_SANS))
    parts.append(_label(left, bottom + 58, "total volume of molecules ≪ volume of container",
                        MUTED, 10, family=_SANS))
    parts.append(f'<text x="{(left + right) / 2:.0f}" y="{top - 14}" text-anchor="middle" '
                 f'fill="{MUTED}" font-size="11" font-family="{_SANS}">'
                 f'pressure = rate of momentum transfer to these walls</text>')
    return wrap("".join(parts), w, h, "Molecules in a box")


@cached
def pressure_collisions(speed: float = 300.0) -> str:
    """One molecule rebounding from a wall, with its momentum change marked."""
    w, h = 700, 260
    wall_x, cy = 560, 150
    parts = [_label(24, 26, "WHERE PRESSURE COMES FROM", MUTED, 12),
             _label(24, 44, "One molecule, one wall, one momentum change. Add up a "
                            "quadrillion of these and you have a pressure.", MUTED, 10,
                    family=_SANS)]
    parts.append(f'<line x1="{wall_x}" y1="70" x2="{wall_x}" y2="230" stroke="{CYAN}" '
                 f'stroke-width="5" stroke-linecap="round"/>')
    parts.append(_label(wall_x + 14, 84, "WALL", CYAN, 11))

    arrow = [("before", 180, wall_x - 40, TEAL, "+mv"),
             ("after", wall_x - 40, 180, AMBER, "−mv")]
    for label, x1, x2, colour, tag in arrow:
        parts.append(f'<line x1="{x1}" y1="{cy}" x2="{x2}" y2="{cy}" stroke="{colour}" '
                     f'stroke-width="3"/>')
        direction = 1 if x2 > x1 else -1
        parts.append(f'<path d="M {x2 - direction * 12} {cy - 7} L {x2} {cy} '
                     f'L {x2 - direction * 12} {cy + 7} Z" fill="{colour}"/>')
        parts.append(_label((x1 + x2) / 2, cy - 14, tag, colour, 12, "middle"))
        parts.append(_label((x1 + x2) / 2, cy + 26, label, MUTED, 10, "middle"))

    parts.append(f'<circle cx="{wall_x - 8}" cy="{cy}" r="9" fill="{ROSE}" opacity="0.8"/>')
    parts.append(_label(wall_x - 8, cy + 30, "m", ROSE, 12, "middle"))

    for i, (title, body) in enumerate([
            ("Momentum change",
             "Δp = 2mv — the molecule rebounds with equal speed in the opposite direction."),
            ("Force is the rate of it",
             "Add every collision per second and divide by the wall area: that is the force."),
            ("Pressure is force per area",
             "P = F / A. Nothing mysterious is happening; it is all bookkeeping of impacts."),
            ("Hence the ideal gas law",
             "P V = (1/3) N m <v²>. The factor 3 is there because motion is in three "
             "dimensions.")]):
        y = 70 + i * 48
        parts.append(f'<circle cx="46" cy="{y}" r="13" fill="{VIOLET}" opacity="0.22"/>')
        parts.append(_label(46, y + 4, str(i + 1), VIOLET, 12, "middle"))
        parts.append(_label(70, y + 1, title, CYAN, 11))
        for j, line in enumerate(_wrap_text(body, 52)):
            parts.append(_label(70, y + 16 + j * 14, line, MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Molecular pressure at a wall")


@cached
def derivation_ladder() -> str:
    """The five steps from a collision to PV = nRT, drawn as a ladder."""
    w, h = 700, 330
    steps = [
        ("1", "molecule rebounds", "Δp = 2 m v"),
        ("2", "sum over all N", "F = N m v² / A"),
        ("3", "divide by the area", "P = N m <v²> / 3V"),
        ("4", "the kinetic relation", "P V = (1/3) N m <v²>"),
        ("5", "recognise n R T", "P V = n R T"),
    ]
    colours = [CYAN, TEAL, AMBER, VIOLET, GREEN]
    base_y, box_w, box_h, gap = 280, 118, 74, 16
    total = len(steps) * box_w + (len(steps) - 1) * gap
    x0 = (w - total) / 2
    parts = [_label(24, 26, "FROM ONE COLLISION TO THE IDEAL GAS LAW", MUTED, 12),
             _label(24, 44, "Five steps. Every gas law in the syllabus is a rearrangement of "
                            "the last box.", MUTED, 10, family=_SANS)]
    for i, ((num, title, formula), colour) in enumerate(zip(steps, colours)):
        x = x0 + i * (box_w + gap)
        y = base_y - box_h
        parts.append(f'<rect x="{x:.1f}" y="{y}" width="{box_w}" height="{box_h}" rx="10" '
                     f'fill="{colour}" opacity="0.12" stroke="{colour}" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{x + 18:.1f}" cy="{y + 20}" r="11" fill="{colour}" '
                     f'opacity="0.85"/>')
        parts.append(_label(x + 18, y + 24, num, "#0b1220", 12, "middle"))
        for j, line in enumerate(_wrap_text(title, 16)):
            parts.append(_label(x + 36, y + 24 + j * 14, line, MUTED, 10, family=_SANS))
        parts.append(_label(x + box_w / 2, y + box_h - 22, formula, colour, 11, "middle",
                            _MONO))
        if i < len(steps) - 1:
            mid = x + box_w + gap / 2
            parts.append(f'<line x1="{mid:.1f}" y1="{base_y - box_h / 2:.1f}" '
                         f'x2="{mid:.1f}" y2="{base_y - box_h / 2:.1f}" stroke="{MUTED}"/>')
            parts.append(f'<path d="M {mid - 5:.1f} {base_y - box_h / 2 - 5:.1f} '
                         f'L {mid + 5:.1f} {base_y - box_h / 2 - 5:.1f} '
                         f'L {mid:.1f} {base_y - box_h / 2 + 5:.1f} Z" fill="{MUTED}"/>')
    parts.append(_label(x0, base_y + 24, "the molecular model", MUTED, 10))
    parts.append(_label(x0 + total - 100, base_y + 24, "the ideal gas equation", GREEN, 11))
    return wrap("".join(parts), w, h, "Deriving the ideal gas law")


# --------------------------------------------------------------------------
# 10.4  Molecular speeds
# --------------------------------------------------------------------------

@cached
def speed_distribution(temperature: float = 300.0, molar_mass: float = 0.028014) -> str:
    """The Maxwell-Boltzmann curve with v_mp, v_mean and v_rms marked on it."""
    from ..core.thermo import GAS_CONSTANT, mean_speed, most_probable_speed, rms_speed

    w, h = 700, 360
    left, right, base, top = 70, 660, 300, 70
    v_mp, v_mean, v_rms = most_probable_speed(temperature, molar_mass), mean_speed(
        temperature, molar_mass), rms_speed(temperature, molar_mass)
    v_max = v_rms * 1.55

    def y_of(v):
        arg = molar_mass * v * v / (2.0 * GAS_CONSTANT * temperature)
        if arg > 700:
            return base
        pdf = math.sqrt(arg / math.pi) * math.exp(-arg)
        peak_arg = molar_mass * v_mp * v_mp / (2.0 * GAS_CONSTANT * temperature)
        peak = math.sqrt(peak_arg / math.pi) * math.exp(-peak_arg)
        return base - (pdf / peak) * (base - top)

    def x_of(v):
        return left + (v / v_max) * (right - left)

    parts = [_label(24, 26, "MAXWELL-BOLTZMANN DISTRIBUTION", MUTED, 12),
             _label(24, 44, f"T = {temperature:g} K,  M = {molar_mass:g} kg mol⁻¹", MUTED, 10,
                    family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{base}" x2="{left}" y2="{top - 10}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    points = []
    for i in range(161):
        v = v_max * i / 160
        points.append(f"{x_of(v):.1f},{y_of(v):.1f}")
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="2.6"/>')
    area = " ".join(points)
    parts.append(f'<polygon points="{left},{base} {area} {right},{base}" fill="{CYAN}" '
                 f'opacity="0.10"/>')

    marks = [(v_mp, "v_mp", "most probable", TEAL),
             (v_mean, "v_mean", "mean speed", AMBER),
             (v_rms, "v_rms", "root-mean-square", VIOLET)]
    for v, tag, name, colour in marks:
        x = x_of(v)
        parts.append(f'<line x1="{x:.1f}" y1="{top - 10}" x2="{x:.1f}" y2="{base}" '
                     f'stroke="{colour}" stroke-width="1.4" stroke-dasharray="4 4" '
                     f'opacity="0.8"/>')
        parts.append(_label(x, top - 18, f"{tag} = {v:.0f} m s⁻¹", colour, 11, "middle"))
        parts.append(_label(x, base + 34, name, colour, 9, "middle", _SANS))
    parts.append(_label((left + right) / 2, base + 52, "speed of the molecules  →",
                        MUTED, 10, "middle"))
    parts.append(f'<text transform="translate(26 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">number of molecules at that speed</text>')
    parts.append(_label(left, base + 20, "0", MUTED, 9, "start"))
    for frac in (0.25, 0.5, 0.75, 1.0):
        parts.append(_tick(left + frac * (right - left), base,
                           f"{v_max * frac:.0f}", MUTED, 9))
    return wrap("".join(parts), w, h, "Molecular speed distribution")


@cached
def energy_lines(temperature: float = 300.0) -> str:
    """Average molecular energy against temperature, identical for every gas."""
    from ..core.thermo import BOLTZMANN, GAS_CONSTANT

    w, h = 700, 300
    left, right, base, top = 80, 660, 240, 60
    t_max = 600.0
    e_max = 1.5 * BOLTZMANN * t_max

    def x_of(t):
        return left + (t / t_max) * (right - left)

    def y_of(e):
        return base - (e / e_max) * (base - top)

    parts = [_label(24, 26, "AVERAGE TRANSLATIONAL ENERGY", MUTED, 12),
             _label(24, 44, "The same straight line for every gas. That is the postulate, "
                            "drawn.", MUTED, 10, family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{base}" x2="{left}" y2="{top - 10}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    points = [f"{x_of(t_max * i / 100):.1f},{y_of(1.5 * BOLTZMANN * t_max * i / 100):.1f}"
              for i in range(101)]
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{ROSE}" '
                 f'stroke-width="2.8"/>')
    # three gases marked on the *same* line
    for name, mass, colour in [("hydrogen", 0.002016, TEAL), ("nitrogen", 0.028014, CYAN),
                               ("carbon dioxide", 0.044009, AMBER)]:
        y = y_of(1.5 * BOLTZMANN * temperature)
        parts.append(f'<circle cx="{x_of(temperature):.1f}" cy="{y:.1f}" r="6" fill="{colour}"/>')
    y = y_of(1.5 * BOLTZMANN * temperature)
    parts.append(_label(x_of(temperature) + 12, y - 12, "all three, here", MUTED, 10))
    parts.append(_label(left, base + 34, "absolute temperature / K", MUTED, 10))
    parts.append(f'<text transform="translate(28 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">energy per molecule / J</text>')
    for frac in (0.25, 0.5, 0.75, 1.0):
        parts.append(_tick(left + frac * (right - left), base, f"{t_max * frac:.0f}", MUTED, 9))
    parts.append(_label(left, base + 20, "0", MUTED, 9, "start"))
    now = y_of(1.5 * BOLTZMANN * temperature)
    parts.append(_label(left + 8, now - 10,
                        f"{temperature:g} K → {1.5 * BOLTZMANN * temperature:.3g} J", ROSE, 11))
    parts.append(_label(right - 8, top + 14, "per mole: 3/2 RT", TEAL, 11, "end"))
    return wrap("".join(parts), w, h, "Energy per molecule against temperature")


# --------------------------------------------------------------------------
# 10.3 and 10.5  Gas laws, work and the four processes
# --------------------------------------------------------------------------

@cached
def gas_law_grid(temperatures=(200.0, 300.0, 400.0), volume: float = 0.0020,
                 pressure: float = 1.0e5) -> str:
    """Isotherms and isochores on one P-V grid, with the Boyle and Charles families."""
    from ..core.thermo import GAS_CONSTANT

    w, h = 700, 340
    left, right, base, top = 70, 660, 290, 60
    v_max = volume * 4.0
    p_max = pressure * 3.2

    def x_of(v):
        return left + (v / v_max) * (right - left)

    def y_of(p):
        return base - (p / p_max) * (base - top)

    parts = [_label(24, 26, "THE GAS LAWS ON ONE DIAGRAM", MUTED, 12),
             _label(24, 44, "Curving lines are isotherms (Boyle). Straight lines through the "
                            "origin are isochores (Gay-Lussac).", MUTED, 10, family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{base}" x2="{left}" y2="{top - 10}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')

    for t, colour in zip(temperatures, (VIOLET, CYAN, TEAL)):
        points = []
        for i in range(1, 81):
            v = v_max * i / 80
            p = GAS_CONSTANT * t / v
            if p > p_max:
                continue
            points.append(f"{x_of(v):.1f},{y_of(p):.1f}")
        if points:
            parts.append(f'<polyline points="{" ".join(points)}" fill="none" '
                         f'stroke="{colour}" stroke-width="2.3"/>')
            parts.append(_label(x_of(v_max * 0.97), y_of(GAS_CONSTANT * t / (v_max * 0.97)) + 16,
                                f"{t:g} K", colour, 11, "end"))
    # isochore: P against T at fixed V, drawn as a straight line
    t_max = 800.0
    p2_max = pressure * 2.2
    parts.append(f'<line x1="{x_of(volume):.1f}" y1="{base}" x2="{x_of(volume):.1f}" '
                 f'y2="{y_of(min(pressure * 2.0, p2_max)):.1f}" stroke="{AMBER}" '
                 f'stroke-width="2" stroke-dasharray="6 4"/>')
    parts.append(_label(x_of(volume) + 8, base - 12, "fixed V", AMBER, 10))
    parts.append(_label((left + right) / 2, base + 34, "volume →", MUTED, 10, "middle"))
    parts.append(f'<text transform="translate(26 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">pressure →</text>')
    for frac in (0.25, 0.5, 0.75, 1.0):
        parts.append(_tick(left + frac * (right - left), base, f"{v_max * frac * 1000:.1f}",
                           MUTED, 9))
        parts.append(_tick(left, base - frac * (base - top), f"{p_max * frac / 1000:.0f}",
                           MUTED, 9, "end"))
    parts.append(_label(left - 6, base + 20, "cm³", MUTED, 9, "end"))
    parts.append(_label(left, top - 18, "kPa", MUTED, 9, "start"))
    parts.append(_label(left + 8, top + 4, "PV = constant on every curve above", MUTED, 10,
                        family=_SANS))
    return wrap("".join(parts), w, h, "Gas laws on a P-V diagram")


@cached
def pv_area(path=((1.0e5, 0.0010), (1.0e5, 0.0020), (4.0e4, 0.0040))) -> str:
    """A P-V path with the area under it shaded, and the work split into strips."""
    w, h = 700, 340
    left, right, base, top = 70, 660, 290, 60
    v_max = 0.0050
    p_max = 1.2e5

    def x_of(v):
        return left + (v / v_max) * (right - left)

    def y_of(p):
        return base - (p / p_max) * (base - top)

    parts = [_label(24, 26, "WORK = AREA UNDER THE PATH", MUTED, 12),
             _label(24, 44, "Heat at constant pressure, then an expansion. Every strip under "
                            "the line is work done by the gas.", MUTED, 10, family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{base}" x2="{left}" y2="{top - 10}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')

    dense = []
    for i in range(len(path) - 1):
        (p1, v1), (p2, v2) = path[i], path[i + 1]
        for k in range(24):
            t = k / 24
            pv, vv = p1 + (p2 - p1) * t, v1 + (v2 - v1) * t
            dense.append((vv, pv))
    poly = [f"{x_of(v):.1f},{y_of(p):.1f}" for v, p in dense]
    parts.append(f'<polygon points="{x_of(0.0006):.1f},{base} {" ".join(poly)} '
                 f'{x_of(dense[-1][0]):.1f},{base}" fill="{CYAN}" opacity="0.20"/>')
    parts.append(f'<polyline points="{" ".join(poly)}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="2.6"/>')
    for i, (p, v) in enumerate(path):
        parts.append(f'<circle cx="{x_of(v):.1f}" cy="{y_of(p):.1f}" r="5" fill="{AMBER}"/>')
        parts.append(_label(x_of(v), y_of(p) - 12, f"{i + 1}", AMBER, 12, "middle"))
    parts.append(_label(right - 10, base + 34, "volume →", MUTED, 10, "end"))
    parts.append(f'<text transform="translate(26 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">pressure →</text>')
    parts.append(_label(left + 16, top + 2, "shaded area = work done by the gas", CYAN, 12,
                        family=_SANS))
    parts.append(_label(left + 16, top + 20, "compression would push the path left and "
                                             "make the work negative", MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Work as area on a P-V diagram")


@cached
def process_quadrant() -> str:
    """All four processes drawn together on one P-V grid and labelled."""
    w, h = 700, 360
    left, right, base, top = 90, 500, 300, 60
    v_max, p_max = 4.0, 5.0

    def x_of(v):
        return left + (v / v_max) * (right - left)

    def y_of(p):
        return base - (p / p_max) * (base - top)

    parts = [_label(24, 26, "THE FOUR PROCESSES", MUTED, 12),
             _label(24, 44, "One is held constant in each case, and that single fact fixes "
                            "everything else.", MUTED, 10, family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{base}" x2="{left}" y2="{top - 10}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')

    # isobaric: horizontal
    parts.append(f'<line x1="{x_of(1.0):.1f}" y1="{y_of(3.0):.1f}" x2="{x_of(3.6):.1f}" '
                 f'y2="{y_of(3.0):.1f}" stroke="{TEAL}" stroke-width="3"/>')
    parts.append(_label(x_of(2.3), y_of(3.0) - 12, "isobaric  W = P dV", TEAL, 11, "middle"))
    # isochoric: vertical
    parts.append(f'<line x1="{x_of(1.0):.1f}" y1="{y_of(1.0):.1f}" x2="{x_of(1.0):.1f}" '
                 f'y2="{y_of(3.0):.1f}" stroke="{ROSE}" stroke-width="3"/>')
    parts.append(_label(x_of(1.0) + 10, (y_of(1.0) + y_of(3.0)) / 2, "isochoric  W = 0",
                        ROSE, 11))
    # isothermal and adiabatic through the same point
    for k, (label, colour, note) in enumerate([("isothermal  Q = W", CYAN, 1.0),
                                              ("adiabatic  Q = 0", AMBER, 1.4)]):
        points = []
        for i in range(41):
            v = 1.0 + 2.8 * i / 40
            p = 3.0 * (1.0 / v) ** (1.0 if k == 0 else 1.4)
            if p < 0.2 or p > p_max:
                continue
            points.append(f"{x_of(v):.1f},{y_of(p):.1f}")
        if points:
            parts.append(f'<polyline points="{" ".join(points)}" fill="none" '
                         f'stroke="{colour}" stroke-width="2.4"/>')
            parts.append(_label(x_of(3.4), y_of(3.0 * (1 / 3.4) ** (1.0 if k == 0 else 1.4)) - 10,
                                label, colour, 11, "end"))

    legend = [("isothermal", "T fixed → dU = 0, all heat becomes work", CYAN),
              ("adiabatic", "Q = 0 → the gas cools as it works", AMBER),
              ("isobaric", "P fixed → part of the heat leaves as work", TEAL),
              ("isochoric", "V fixed → no work at all, Q = dU", ROSE)]
    y = 78
    for name, note, colour in legend:
        parts.append(f'<rect x="530" y="{y - 10}" width="12" height="12" rx="3" '
                     f'fill="{colour}" opacity="0.75"/>')
        parts.append(_label(550, y, name, colour, 12))
        for j, line in enumerate(_wrap_text(note, 26)):
            parts.append(_label(550, y + 16 + j * 14, line, MUTED, 10, family=_SANS))
        y += 62
    parts.append(_label((left + right) / 2, base + 32, "volume →", MUTED, 10, "middle"))
    parts.append(f'<text transform="translate(44 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">pressure →</text>')
    return wrap("".join(parts), w, h, "Four thermodynamic processes")


# --------------------------------------------------------------------------
# 10.6  Heat capacities
# --------------------------------------------------------------------------

@cached
def heat_capacity_bars() -> str:
    """Cv, Cp and gamma side by side for the three common gases."""
    from ..core.thermo import GAS_CONSTANT, cp_cv

    w, h = 700, 300
    cases = [(3, "monatomic", "He, Ne, Ar", CYAN),
             (5, "diatomic", "N₂, O₂, CO", TEAL),
             (6, "polyatomic", "H₂O, CO₂", AMBER)]
    base, left, bar_w, gap = 240, 90, 56, 16
    cmax = 4.0 * GAS_CONSTANT
    parts = [_label(24, 26, "Cv, Cp AND GAMMA", MUTED, 12),
             _label(24, 44, "Cv comes from the degrees of freedom; Cp is always R more.",
                    MUTED, 10, family=_SANS)]

    for i, (f, name, examples, colour) in enumerate(cases):
        r = cp_cv(f)
        x = left + i * 210
        for j, (key, val, alpha) in enumerate([("Cv", r["cv"], 0.75), ("Cp", r["cp"], 0.45)]):
            height = (val / cmax) * (base - 70)
            bx = x + j * (bar_w + gap)
            parts.append(f'<rect x="{bx}" y="{base - height:.1f}" width="{bar_w}" '
                         f'height="{height:.1f}" rx="5" fill="{colour}" opacity="{alpha}" '
                         f'stroke="{colour}"/>')
            parts.append(_label(bx + bar_w / 2, base + 16, key, colour, 11, "middle"))
            parts.append(_label(bx + bar_w / 2, base - height - 8, f"{val:.1f}", colour, 10,
                                "middle"))
        parts.append(_label(x + bar_w, base + 36, name, colour, 12, "middle"))
        parts.append(_label(x + bar_w, base + 52, examples, MUTED, 10, "middle"))
        parts.append(_label(x + bar_w + gap + bar_w, base + 36, f"γ = {r['gamma']:.3f}",
                            VIOLET, 12, "middle"))
        parts.append(_label(x + bar_w + gap + bar_w, base + 52, f"f = {f}", MUTED, 10, "middle"))
    parts.append(f'<line x1="{left - 20}" y1="{base}" x2="{left + 3 * 210 - 40}" '
                 f'y2="{base}" stroke="{MUTED}" stroke-width="1.5"/>')
    parts.append(_label(left - 20, 62, "J mol⁻¹ K⁻¹", MUTED, 9))
    parts.append(_label(left - 20, base + 76, "Mayer's relation: Cp − Cv = R = "
                                             f"{GAS_CONSTANT:.3f}, for all three", GREEN, 11))
    return wrap("".join(parts), w, h, "Heat capacities of common gases")


# --------------------------------------------------------------------------
# 10.7 and 10.8  Reversibility, the second law and entropy
# --------------------------------------------------------------------------

@cached
def reversible_split() -> str:
    """Real processes sorted into the reversible pile and the irreversible pile."""
    w, h = 700, 300
    reversible = ["frictionless slow piston", "freezing water at 0 °C",
                  "a reversible isothermal expansion"]
    irreversible = ["gas into a vacuum", "a brake heating up", "tea cooling in a room",
                    "two gases mixing", "current through a resistor", "a candle flame"]
    parts = [_label(24, 26, "REVERSIBLE OR NOT?", MUTED, 12),
             _label(24, 44, "Reversible is a limit, not a thing you can actually achieve.",
                    MUTED, 10, family=_SANS)]
    for j, (title, items, colour, note) in enumerate([
            ("REVERSIBLE", reversible, TEAL,
             "no friction, no finite temperature or pressure difference"),
            ("IRREVERSIBLE", irreversible, ROSE,
             "something is dissipated and cannot be gathered back")]):
        x = 40 + j * 340
        parts.append(f'<rect x="{x}" y="70" width="300" height="200" rx="12" '
                     f'fill="{colour}" opacity="0.08" stroke="{colour}" stroke-width="1.5" '
                     f'stroke-dasharray="6 4"/>')
        parts.append(_label(x + 16, 94, title, colour, 13))
        parts.append(_label(x + 16, 112, note, MUTED, 9))
        for i, item in enumerate(items):
            parts.append(f'<circle cx="{x + 22}" cy="{138 + i * 22}" r="3.5" fill="{colour}"/>')
            parts.append(_label(x + 36, 142 + i * 22, item, MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Reversible and irreversible processes")


@cached
def entropy_room(fraction: float = 0.25) -> str:
    """A gas confined to part of a room, and the same gas filling all of it."""
    w, h = 700, 300
    left, right, top, bottom = 70, 630, 76, 250
    parts = [_label(24, 26, "ENTROPY COUNTS ARRANGEMENTS", MUTED, 12),
             _label(24, 44, "Same gas, same energy, same temperature. Only the number of "
                            "places it can be differs.", MUTED, 10, family=_SANS)]
    state, seed = 7, 11

    def draw(x, y, bw, bh, count, colour, caption, sub):
        nonlocal state
        box = [f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10" fill="{colour}" '
               f'opacity="0.06" stroke="{colour}" stroke-width="2"/>']
        for _ in range(count):
            state = (1103515245 * state + 12345) % (1 << 31)
            px = x + 12 + state % max(bw - 24, 1)
            state = (1103515245 * state + 12345) % (1 << 31)
            py = y + 12 + state % max(bh - 24, 1)
            box.append(f'<circle cx="{px}" cy="{py}" r="4" fill="{colour}" opacity="0.85"/>')
        box.append(_label(x + bw / 2, y + bh + 22, caption, colour, 12, "middle"))
        box.append(_label(x + bw / 2, y + bh + 40, sub, MUTED, 10, "middle"))
        return box

    small_w = (right - left) * fraction
    parts += draw(left, top, small_w, bottom - top, 14, ROSE, "confined",
                  f"only {fraction:.0%} of the room available")
    parts += draw(left, top, right - left, bottom - top, 42, TEAL, "fills the room",
                  "every corner available")
    parts.append(_label(left, 60, "SAME gas, SAME T, SAME U — and a very different entropy",
                        GREEN, 12))
    parts.append(_label(left, bottom + 70, "A reversible expansion into the empty half "
                                           "raises the entropy without raising the "
                                           "temperature.", MUTED, 10, family=_SANS))
    parts.append(_label(right, bottom + 70, "The universe's entropy never falls.", VIOLET, 11,
                        "end"))
    return wrap("".join(parts), w, h, "Entropy as accessible arrangements")


# --------------------------------------------------------------------------
# 10.9  Heat engines, Carnot and refrigerators
# --------------------------------------------------------------------------

@cached
def engine_blocks(efficiency: float = 0.40) -> str:
    """A heat engine as three blocks with the energy streams labelled."""
    w, h = 700, 250
    parts = [_label(24, 26, "A HEAT ENGINE", MUTED, 12),
             _label(24, 44, "Two reservoirs and a working substance. The balance Q_h = W + Q_c "
                            "always closes.", MUTED, 10, family=_SANS)]
    hot_x, eng_x, cold_x = 90, 300, 500
    box_w, box_h, y = 170, 90, 110
    for x, title, sub, colour in [(hot_x, "HOT RESERVOIR", "at T_h", ROSE),
                                  (eng_x, "ENGINE", "the working substance", CYAN),
                                  (cold_x, "COLD RESERVOIR", "at T_c", TEAL)]:
        parts.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="12" '
                     f'fill="{colour}" opacity="0.14" stroke="{colour}" stroke-width="1.8"/>')
        parts.append(_label(x + box_w / 2, y + 36, title, colour, 12, "middle"))
        parts.append(_label(x + box_w / 2, y + 58, sub, MUTED, 10, "middle"))

    def stream(x1, y1, x2, y2, text, colour, width=3):
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colour}" '
                     f'stroke-width="{width}"/>')
        direction = 1 if x2 > x1 else -1
        parts.append(f'<path d="M {x2 - direction * 11} {y2 - 6} L {x2} {y2} '
                     f'L {x2 - direction * 11} {y2 + 6} Z" fill="{colour}"/>')
        parts.append(_label((x1 + x2) / 2, min(y1, y2) - 10, text, colour, 11, "middle"))

    stream(hot_x + box_w, y + 28, eng_x, y + 28, "Q_h  heat in", ROSE)
    stream(eng_x + box_w, y + 28, cold_x, y + 28, "Q_c  heat rejected", TEAL)
    stream(eng_x + box_w / 2, y, eng_x + box_w / 2, y - 60, "W  work out", GREEN, 3.4)
    parts.append(f'<path d="M {eng_x + box_w / 2 - 14} {y - 60} l 14 -14 l 14 14 Z" '
                 f'fill="{GREEN}"/>')
    parts.append(_label(20, 60, f"η = W / Q_h = {efficiency:.2%} shown here", CYAN, 12))
    parts.append(_label(20, 80, "the other part is not optional — it goes to the cold reservoir",
                        MUTED, 10, family=_SANS))
    parts.append(f'<text x="{eng_x + box_w / 2:.0f}" y="{y - 70}" text-anchor="middle" '
                 f'fill="{GREEN}" font-size="12" font-family="{_MONO}">useful work</text>')
    return wrap("".join(parts), w, h, "Heat engine block diagram")


@cached
def carnot_cycle_plot(volume_ratio: float = 4.0, adiabatic_ratio: float = 1.8) -> str:
    """The Carnot cycle plotted from the corner calculation in the core module."""
    from ..core.thermo import carnot_cycle_series

    series = carnot_cycle_series(1.0e5, 1.0, volume_ratio, adiabatic_ratio, samples=60)
    corners = series["corners"]
    legs = [("hot_isothermal", TEAL, "1→2  isothermal expansion at T_h"),
            ("adiabatic_expansion", AMBER, "2→3  adiabatic expansion"),
            ("cold_isothermal", CYAN, "3→4  isothermal compression at T_c"),
            ("adiabatic_compression", VIOLET, "4→1  adiabatic compression")]

    w, h = 700, 380
    left, right, base, top = 70, 660, 320, 60
    v_max = max(corners[k]["V"] for k in "1234") * 1.08
    p_max = max(corners[k]["P"] for k in "1234") * 1.15

    def x_of(v):
        return left + (v / v_max) * (right - left)

    def y_of(p):
        return base - (p / p_max) * (base - top)

    parts = [_label(24, 26, "THE CARNOT CYCLE", MUTED, 12),
             _label(24, 44, "Two isotherms joined by two adiabats. The enclosed area is the "
                            "net work of one cycle.", MUTED, 10, family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{base}" x2="{left}" y2="{top - 10}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')

    # shade the enclosed area
    poly = []
    for key, _, _ in legs:
        trace = series[key]
        xs = trace["V"]
        ys = trace["P"]
        order = range(len(xs)) if key != "adiabatic_compression" else range(len(xs) - 1, -1, -1)
        for i in order:
            poly.append(f"{x_of(xs[i]):.1f},{y_of(ys[i]):.1f}")
    parts.append(f'<polygon points="{" ".join(poly)}" fill="{GREEN}" opacity="0.14"/>')
    for key, colour, _ in legs:
        trace = series[key]
        pts = [f"{x_of(v):.1f},{y_of(p):.1f}" for v, p in zip(trace["V"], trace["P"])]
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{colour}" '
                     f'stroke-width="2.8"/>')
    for key in "1234":
        c = corners[key]
        x, y = x_of(c["V"]), y_of(c["P"])
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{AMBER}"/>')
        parts.append(_label(x + 10, y - 8, key, AMBER, 13))
    parts.append(_label(left + 130, top + 4, f"enclosed area = {series['enclosed_area']:.4g} J",
                        GREEN, 12, family=_SANS))
    parts.append(_label((left + right) / 2, base + 34, "volume →", MUTED, 10, "middle"))
    parts.append(f'<text transform="translate(26 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">pressure →</text>')
    for i, (_, colour, label) in enumerate(legs):
        parts.append(f'<rect x="{left}" y="{base + 48 + i * 18}" width="14" height="4" '
                     f'rx="2" fill="{colour}"/>')
        parts.append(_label(left + 22, base + 53 + i * 18, label, colour, 10))
    return wrap("".join(parts), w, h, "Carnot cycle on a P-V diagram")


@cached
def refrigerator_blocks(temperature_gap: float = 50.0) -> str:
    """A refrigerator as a heat engine run backwards."""
    w, h = 700, 250
    parts = [_label(24, 26, "A REFRIGERATOR IS A HEAT ENGINE, BACKWARDS", MUTED, 12),
             _label(24, 44, f"The arrows that were heat out and work out are reversed. "
                            f"It still must not violate the second law.", MUTED, 10,
                    family=_SANS)]
    cold_x, eng_x, room_x = 80, 290, 500
    box_w, box_h, y = 170, 92, 112
    for x, title, sub, colour in [(cold_x, "COLD SPACE", "at T_c", CYAN),
                                  (eng_x, "REFRIGERATOR", "a reversed engine", AMBER),
                                  (room_x, "ROOM", "at T_h", ROSE)]:
        parts.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="12" '
                     f'fill="{colour}" opacity="0.14" stroke="{colour}" stroke-width="1.8"/>')
        parts.append(_label(x + box_w / 2, y + 36, title, colour, 12, "middle"))
        parts.append(_label(x + box_w / 2, y + 58, sub, MUTED, 10, "middle"))

    def stream(x1, y1, x2, y2, text, colour, dash=False):
        dash_attr = ' stroke-dasharray="7 4"' if dash else ''
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colour}" '
                     f'stroke-width="3"{dash_attr}/>')
        direction = 1 if x2 > x1 else -1
        parts.append(f'<path d="M {x2 - direction * 11} {y2 - 6} L {x2} {y2} '
                     f'L {x2 - direction * 11} {y2 + 6} Z" fill="{colour}"/>')
        parts.append(_label((x1 + x2) / 2, y1 - 10, text, colour, 11, "middle"))

    stream(cold_x + box_w, y + 28, eng_x, y + 28, "Q_c  heat taken in", CYAN)
    stream(eng_x + box_w, y + 28, room_x, y + 28, "Q_h  heat dumped out", ROSE)
    stream(eng_x + box_w / 2, y + box_h, eng_x + box_w / 2, y + box_h + 42,
           "W  electricity in", AMBER, dash=True)
    parts.append(f'<path d="M {eng_x + box_w / 2 - 8} {y + box_h + 32} '
                 f'l 8 -10 l 8 10 Z" fill="{AMBER}"/>')
    parts.append(_label(20, 62, f"COP = Q_c / W,  working against a {temperature_gap:g} K gap",
                        AMBER, 12))
    parts.append(_label(20, 82, "heat is moved, not created — so COP may exceed 1",
                        MUTED, 10, family=_SANS))
    return wrap("".join(parts), w, h, "Refrigerator block diagram")

@cached
def work_by_vs_on(pressure, delta_volume):
    """The same expansion or compression described in both conventions."""
    w = pressure * delta_volume
    expanding = delta_volume > 0
    parts = [_label(24, 26, "TWO CONVENTIONS, ONE PROCESS", MUTED, 12),
             _label(24, 44, "The physics does not change. Only the name attached to the sign "
                            "does.", MUTED, 10, family=_SANS)]
    for i, (title, value, note, colour) in enumerate([
            ("Work done BY the gas", w,
             "the gas pushes the surroundings outwards" if expanding
             else "the surroundings squeeze the gas inwards", TEAL),
            ("Work done ON the gas", -w,
             "the surroundings push back on the gas" if expanding
             else "the gas pushes the surroundings outwards", AMBER)]):
        x = 40 + i * 320
        parts.append(f'<rect x="{x}" y="70" width="290" height="120" rx="12" '
                     f'fill="{colour}" opacity="0.08" stroke="{colour}" stroke-width="1.4"/>')
        parts.append(_label(x + 16, 96, title, colour, 12))
        parts.append(_label(x + 16, 124, f"W = {value:+.4g} J", colour, 16))
        parts.append(_label(x + 16, 150, note, MUTED, 10, family=_SANS))
        sign = "+" if value > 0 else ("\u2212" if value < 0 else "")
        parts.append(_label(x + 16, 174, f"positive work {sign}" if value > 0
                            else (f"negative work {sign}" if value < 0 else "no work at all"),
                            colour, 11))
    parts.append(_label(24, 216, "This chapter uses  dU = Q \u2212 W  with W measured as work "
                                 "done BY the gas.", MUTED, 11, family=_SANS))
    parts.append(_label(24, 236, "So compression makes W negative, and compression therefore "
                                 "raises the internal energy for a given Q.", MUTED, 10,
                        family=_SANS))
    return wrap("".join(parts), 700, 250, "Work by and work on a gas")


@cached
def degradation_scale():
    """Energy quality falling from concentrated to fully dispersed."""
    w, h = 700, 250
    steps = [("concentrated", "stored chemical energy in fuel", 1.00, TEAL),
             ("useful work", "does the job we wanted", 0.72, GREEN),
             ("low-grade heat", "spread into the surroundings", 0.34, AMBER),
             ("random motion", "too spread out to recover", 0.06, ROSE)]
    parts = [_label(24, 26, "QUALITY FALLS. AMOUNT NEVER DOES.", MUTED, 12),
             _label(24, 44, "Each step spreads the energy out more. The total is conserved; the "
                            "usefulness is not.", MUTED, 10, family=_SANS)]
    left, width, top, height = 40, 140, 90, 90
    for i, (name, note, frac, colour) in enumerate(steps):
        x = left + i * (width + 14)
        bh = max(height * frac, 8)
        parts.append(f'<rect x="{x}" y="{top + height - bh:.1f}" width="{width}" '
                     f'height="{bh:.1f}" rx="8" fill="{colour}" opacity="0.55" '
                     f'stroke="{colour}"/>')
        parts.append(_label(x + width / 2, top + height + 20, name, colour, 11, "middle"))
        for j, line in enumerate(_wrap_text(note, 17)):
            parts.append(_label(x + width / 2, top + height + 36 + j * 12, line, MUTED, 9,
                                "middle", _SANS))
        if i:
            px = left + (i - 1) * (width + 14) + width
            parts.append(f'<path d="M {px + 3:.0f} {top + height / 2 - 6} '
                         f'l 9 6 l -9 6 Z" fill="{MUTED}"/>')
    parts.append(_label(24, 218, "recovering any of it would need work greater than the "
                                 "work it could then do", ROSE, 11))
    return wrap("".join(parts), w, h, "Degradation of energy")


@cached
def design_energy_flow():
    """The energy budget a student fills in for the design brief."""
    w, h = 700, 230
    parts = [_label(24, 26, "THE ENERGY BUDGET YOU MUST BALANCE", MUTED, 12),
             _label(24, 44, "Every branch has to be accounted for, and the total must close.",
                    MUTED, 10, family=_SANS)]
    rows = [("Heat leaking in from the room at 303 K", "Q_leak", ROSE, "?"),
            ("Heat removed from the milk", "Q_c", CYAN, "?"),
            ("Electrical energy you pay for", "W", AMBER, "?"),
            ("Heat rejected into the room", "Q_h", GREEN, "?")]
    y = 76
    for name, symbol, colour, value in rows:
        parts.append(f'<rect x="40" y="{y - 16}" width="460" height="26" rx="7" '
                     f'fill="{colour}" opacity="0.10" stroke="{colour}" stroke-width="1.1"/>')
        parts.append(_label(56, y + 2, name, MUTED, 11, family=_SANS))
        parts.append(_label(420, y + 2, symbol, colour, 13))
        parts.append(_label(520, y + 2, value, colour, 13))
        y += 36
    parts.append(f'<line x1="600" y1="76" x2="600" y2="{y - 20}" stroke="{MUTED}" '
                 f'stroke-width="1.4"/>')
    parts.append(_label(608, 110, "Q_c = T_c/(T_h \u2212 T_c) \u00d7 W", GREEN, 11))
    parts.append(_label(608, 130, "so Q_c/W is fixed", GREEN, 10))
    parts.append(_label(608, 152, "by the gap alone", GREEN, 10))
    parts.append(_label(608, 174, "\u2193", MUTED, 14))
    parts.append(_label(608, 196, "shrinking the gap", GREEN, 10))
    parts.append(_label(608, 210, "is the whole design", GREEN, 10))
    return wrap("".join(parts), w, h, "Design brief energy budget")
