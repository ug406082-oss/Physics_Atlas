"""Chapter 7 diagrams: oscillations."""

from __future__ import annotations

import math

from ..core import oscillations as O
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, wrap

__all__ = ["energy_exchange", "resonance_curve", "damping_comparison", "shm_scope", "circle_projection", "spring_rig", "pendulum_rig",
           "energy_bars", "phase_dial", "period_comparison"]


@cached
def shm_scope(amplitude: float, omega: float, periods: float = 1.5,
              phase: float = 0.0) -> str:
    """Displacement, velocity and acceleration on one shared time axis.

    Drawing all three on a single axis is the point: the quarter-period offsets
    are then visible as horizontal shifts rather than something to be memorised.
    """
    w, h = 700, 550
    left, right = 70, w - 150
    panel_h = 118
    n = 260
    period = 2 * math.pi / omega
    t_max = period * max(periods, 0.5)
    ts = [i * t_max / (n - 1) for i in range(n)]
    xs = [amplitude * math.sin(omega * t + phase) for t in ts]
    vs = [amplitude * omega * math.cos(omega * t + phase) for t in ts]
    accs = [-amplitude * omega ** 2 * math.sin(omega * t + phase) for t in ts]

    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'A = {amplitude:.4g} m · ω = {omega:.4g} rad s⁻¹ · T = {period:.4g} s</text>']
    quarter = period / 4.0
    for index, (label, values, colour) in enumerate([("x", xs, CYAN), ("v", vs, AMBER),
                                                     ("a", accs, ROSE)]):
        top = 58 + index * (panel_h + 40)
        bottom = top + panel_h
        peak = amplitude * (omega ** 2 if label == "a" else omega if label == "v" else 1.0)
        scale = peak or 1.0
        parts.append(f'<rect x="{left}" y="{top}" width="{right - left}" '
                     f'height="{panel_h}" rx="8" fill="#0b1a2c" stroke="#1b3350"/>')
        mid = top + panel_h / 2
        parts.append(f'<line x1="{left}" y1="{mid:.1f}" x2="{right}" y2="{mid:.1f}" '
                     f'stroke="#18304b" stroke-width="1" stroke-dasharray="3 3"/>')
        points = []
        for step, value in enumerate(values):
            px = left + (step / (n - 1)) * (right - left)
            py = mid - (value / scale) * (panel_h / 2 - 10)
            points.append(f"{px:.1f},{py:.1f}")
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{colour}" '
                     f'stroke-width="2.6"/>')
        parts.append(f'<text x="24" y="{top - 10}" fill="{colour}" font-size="17" '
                     f'font-weight="700">{label}</text>')
        parts.append(f'<text x="{left - 8}" y="{top + 22}" fill="{MUTED}" font-size="10" '
                     f'text-anchor="end" font-family="JetBrains Mono, monospace">'
                     f'{peak:.4g}</text>')
        parts.append(f'<text x="{right + 8}" y="{top + 22}" fill="{MUTED}" font-size="10" '
                     f'font-family="JetBrains Mono, monospace">−{peak:.4g}</text>')
        # Mark where this quantity peaks, and the T/4 shifts.
        peak_index = (index * n) // 4
        px = left + peak_index / (n - 1) * (right - left)
        parts.append(f'<line x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{bottom}" '
                     f'stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    parts.append(f'<text x="{left}" y="{h - 40}" fill="{GREEN}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'green lines: x peaks, then v a quarter later, then a a quarter after that</text>')
    parts.append(f'<text x="20" y="{h - 16}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">v leads x by T/4 = {quarter:.3g} s, and a lags v '
                 f'by T/4, so a is always half a cycle behind x — and opposite to it.</text>')
    return wrap("".join(parts), w, h, "Displacement, velocity and acceleration on one axis")


@cached
def circle_projection(radius: float, omega: float, t: float) -> str:
    """S.H.M. drawn as the shadow of a point moving round a circle."""
    w, h = 680, 340
    cx, cy, r = 230, 170, 120.0
    x = r * math.sin(omega * t)
    y = r * math.cos(omega * t)
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'ONE CIRCLE, ONE SINE WAVE</text>',
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1b3350" stroke-width="2"/>',
             f'<line x1="{cx - r - 24}" y1="{cy}" x2="{cx + r + 24}" y2="{cy}" '
             f'stroke="#18304b" stroke-width="1"/>',
             f'<line x1="{cx}" y1="{cy - r - 24}" x2="{cx}" y2="{cy + r + 24}" '
             f'stroke="#18304b" stroke-width="1"/>',
             f'<line x1="{cx}" y1="{cy - r}" x2="{cx}" y2="{cy + r}" stroke="{ROSE}" '
             f'stroke-width="1.5" stroke-dasharray="5 4"/>',
             f'<text x="{cx - 26}" y="{cy - r - 8}" fill="{ROSE}" font-size="11" '
             f'font-family="JetBrains Mono, monospace">equilibrium</text>',
             f'<circle cx="{cx + x:.1f}" cy="{cy - y:.1f}" r="9" fill="{AMBER}"/>',
             f'<line x1="{cx}" y1="{cy}" x2="{cx + x:.1f}" y2="{cy - y:.1f}" '
             f'stroke="{AMBER}" stroke-width="2" stroke-dasharray="4 3"/>',
             f'<line x1="{cx - r - 10}" y1="{cy}" x2="{cx + x:.1f}" y2="{cy}" '
             f'stroke="{CYAN}" stroke-width="3"/>',
             f'<text x="{cx + x + 12:.1f}" y="{cy + 4}" fill="{CYAN}" font-size="12" '
             f'font-weight="700">x = {x:.4g} m</text>',
             f'<text x="{cx + r + 28}" y="{cy - r + 4}" fill="{MUTED}" font-size="11" '
             f'font-family="JetBrains Mono, monospace">R = {radius:g} m</text>']
    # The projected wave.
    wave_left, wave_right = 430, w - 30
    mid = 250
    points = []
    for step in range(121):
        frac = step / 120.0
        tt = frac * 2 * math.pi / omega * 1.0
        value = radius * math.sin(tt)
        px = wave_left + frac * (wave_right - wave_left)
        py = mid - (value / radius) * 60
        points.append(f"{px:.1f},{py:.1f}")
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{TEAL}" '
                 f'stroke-width="2.6"/>')
    frac = (omega * t) % (2 * math.pi) / (2 * math.pi)
    px = wave_left + frac * (wave_right - wave_left)
    parts.append(f'<line x1="{px:.1f}" y1="{mid - 70}" x2="{px:.1f}" y2="{mid + 70}" '
                 f'stroke="{GREEN}" stroke-width="2" stroke-dasharray="4 3"/>')
    parts.append(f'<line x1="{wave_left}" y1="{mid}" x2="{wave_right}" y2="{mid}" '
                 f'stroke="#18304b" stroke-width="1"/>')
    parts.append(f'<text x="{wave_left}" y="{mid - 80}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">x against time</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The horizontal coordinate of the point is '
                 f'exactly a simple harmonic oscillation: amplitude = radius, '
                 f'ω = the circular speed.</text>')
    return wrap("".join(parts), w, h, "Simple harmonic motion as a circular projection")


@cached
def spring_rig(mass: float, k: float, amplitude: float, samples: int = 260) -> str:
    """A mass on a spring, with the force arrow and the acceleration traced."""
    w, h = 660, 380
    cx, cy = 200, 150
    omega = math.sqrt(k / mass)
    period = 2 * math.pi / omega
    width = 260.0
    scale = amplitude * scale_factor(amplitude)
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'm = {mass:g} kg · k = {k:g} N m⁻¹ · T = {period:.4g} s</text>']
    # Anchor.
    parts.append(f'<line x1="{cx - width - 40}" y1="60" x2="{cx + width + 40}" y2="60" '
                 f'stroke="{MUTED}" stroke-width="4"/>')
    for tick in range(-3, 4):
        parts.append(f'<path d="M {cx + tick * 40 - 6} 60 L {cx + tick * 40 + 6} 74" '
                     f'stroke="{MUTED}" stroke-width="1.5"/>')
    equilibrium_y = cy + 120
    parts.append(f'<line x1="{cx - width - 40}" y1="{equilibrium_y}" x2="{cx + width + 40}" '
                 f'y2="{equilibrium_y}" stroke="{GREEN}" stroke-width="1.5" '
                 f'stroke-dasharray="5 4"/>')
    parts.append(f'<text x="{cx + width + 44}" y="{equilibrium_y + 4}" fill="{GREEN}" '
                 f'font-size="10" font-family="JetBrains Mono, monospace">equilibrium</text>')
    # Coil.
    turns = 12
    top_y = cy - 60 - amplitude * scale
    coil = []
    for step in range(turns * 2 + 1):
        px = cx - width + step * (2 * width / (turns * 2))
        py = top_y + (12 if step % 2 else -12)
        coil.append(f"{px:.1f},{py:.1f}")
    parts.append(f'<polyline points="{" ".join(coil)}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="3"/>')
    for step in range(11):
        px = cx - amplitude * scale + step * (2 * amplitude * scale / 10)
        py = equilibrium_y
        parts.append(f'<circle cx="{px:.1f}" cy="{py}" r="7" fill="{CYAN}"/>')
    bob_x = cx + amplitude * scale * math.sin(math.pi / 2)
    bob_y = equilibrium_y
    parts.append(f'<rect x="{bob_x - 13:.1f}" y="{bob_y - 13}" width="26" height="26" rx="4" '
                 f'fill="{AMBER}"/>')
    parts.append(f'<text x="{bob_x + 18:.1f}" y="{bob_y + 4}" fill="{AMBER}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">m</text>')
    parts.append(f'<text x="20" y="{h - 60}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'A = {amplitude:g} m · ω = √(k/m) = {omega:.4g} rad s⁻¹</text>')
    parts.append(f'<text x="20" y="{h - 40}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'E = ½kA² = {0.5 * k * amplitude ** 2:.4g} J = ½mω²A²</text>')
    parts.append(f'<text x="20" y="{h - 20}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">F = −kx gives a = −(k/m)x = −ω²x, which is '
                 f'exactly the S.H.M. condition. The period never depends on the amplitude.</text>')
    return wrap("".join(parts), w, h, "A mass oscillating on a spring")


def scale_factor(amplitude: float) -> float:
    """Keep the drawing inside the box whatever the amplitude."""
    return min(1.0, 90.0 / max(amplitude, 1e-9))


@cached
def pendulum_rig(length: float, start_deg: float, g: float = 9.8) -> str:
    """A pendulum swinging, with the small-angle and large-angle periods compared."""
    w, h = 660, 400
    cx, cy = 330, 60
    pixels = 250.0
    theta = math.radians(start_deg)
    bob = (cx + pixels * math.sin(theta), cy + pixels * math.cos(theta))
    small = oscillations_period(length, g)
    error = pendulum_error(length, start_deg, g)
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'L = {length:g} m · swing {start_deg:g}°</text>',
             f'<circle cx="{cx}" cy="{cy}" r="5" fill="{MUTED}"/>',
             f'<line x1="{cx}" y1="{cy}" x2="{bob[0]:.1f}" y2="{bob[1]:.1f}" stroke="{CYAN}" '
             f'stroke-width="2.5"/>',
             f'<circle cx="{bob[0]:.1f}" cy="{bob[1]:.1f}" r="14" fill="{AMBER}"/>',
             f'<text x="{bob[0] + 20:.1f}" y="{bob[1] + 4}" fill="{AMBER}" font-size="11" '
             f'font-family="JetBrains Mono, monospace">m</text>',
             f'<path d="M {cx - 70} {cy + 8} L {cx} {cy} L {cx + 70} {cy + 8}" fill="none" '
             f'stroke="#1b3350" stroke-width="2"/>',
             f'<path d="M {cx} {cy + 8} L {cx} {cy + pixels + 30}" stroke="{GREEN}" '
             f'stroke-width="1.5" stroke-dasharray="5 4"/>']
    # Arc showing the amplitude.
    arc_r = 70
    parts.append(f'<path d="M {cx - arc_r} {cy + 8} A {arc_r} {arc_r} 0 0 0 '
                 f'{cx + arc_r * math.cos(math.radians(start_deg)):.1f} '
                 f'{cy + 8 + arc_r * math.sin(math.radians(start_deg)):.1f}" fill="none" '
                 f'stroke="{VIOLET}" stroke-width="2"/>')
    parts.append(f'<text x="{cx + 90}" y="{cy + 24}" fill="{VIOLET}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">θ₀ = {start_deg:g}°</text>')
    rows = [("small-angle formula", f"{small:.4g} s", CYAN),
            ("true period", f"{small * (1 + error / 100):.4g} s", AMBER),
            ("error", f"{error:.3g} %", ROSE if error > 1 else GREEN)]
    for index, (label, value, colour) in enumerate(rows):
        y = 110 + index * 40
        parts.append(f'<text x="20" y="{y}" fill="{MUTED}" font-size="12" '
                     f'font-family="Sora, sans-serif">{label}</text>'
                     f'<text x="210" y="{y}" fill="{colour}" font-size="14" '
                     f'font-family="JetBrains Mono, monospace">{value}</text>')
    parts.append(f'<text x="20" y="{h - 40}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'T = 2π√(L/g) = 2π√({length:g}/{g}) = {small:.4g} s</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The mass cancels out, and the amplitude does '
                 f'not appear at all — except through the small-angle approximation failing.</text>')
    return wrap("".join(parts), w, h, "A simple pendulum and the size of the small-angle error")


def oscillations_period(length: float, g: float) -> float:
    """T = 2π√(L/g), the small-angle pendulum period.

    Delegates to :mod:`physics.core.oscillations` so there is one implementation
    of the formula, not two that can drift apart.
    """
    return O.pendulum_period(length, g)


def pendulum_error(length: float, angle_deg: float, g: float) -> float:
    """Percentage by which the true period exceeds 2π√(L/g) at this amplitude."""
    return O.pendulum_accuracy(length, angle_deg, g)


@cached
def energy_bars(amplitude: float, omega: float, mass: float = 1.0) -> str:
    """Energy sloshing between the kinetic and potential stores over one cycle."""
    w, h = 660, 300
    left, right = 70, w - 40
    top, bottom = 60, 250
    k = mass * omega ** 2
    total = 0.5 * k * amplitude ** 2
    n = 120
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'E = ½kA² = ½mω²A² = {total:.4g} J, constant throughout</text>']
    for index, (label, kind) in enumerate([("potential ½kx²", "p"), ("kinetic ½mω²(A²−x²)", "k")]):
        colour = CYAN if kind == "p" else AMBER
        points = []
        for step in range(n + 1):
            frac = step / n
            theta = frac * 2 * math.pi
            value = 0.5 * k * amplitude ** 2 * math.cos(theta) ** 2
            px = left + frac * (right - left)
            py = bottom - (value / total if total else 0) * (bottom - top)
            points.append(f"{px:.1f},{py:.1f}")
        joined = " ".join(points)
        parts.append(f'<polygon points="{left},{bottom} {joined} {right},{bottom}" '
                     f'fill="{colour}" opacity="0.28"/>')
        parts.append(f'<polyline points="{joined}" fill="none" stroke="{colour}" '
                     f'stroke-width="2.8"/>')
        parts.append(f'<text x="{left + 10}" y="{top + 14 + index * 0}" fill="{colour}" '
                     f'font-size="12" font-weight="700">{label}</text>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" '
                 f'stroke="{MUTED}" stroke-width="2"/>')
    # The constant total.
    y_top = top
    parts.append(f'<line x1="{left}" y1="{y_top}" x2="{right}" y2="{y_top}" stroke="{GREEN}" '
                 f'stroke-width="2" stroke-dasharray="6 4"/>')
    parts.append(f'<text x="{right - 4}" y="{y_top - 6}" text-anchor="end" fill="{GREEN}" '
                 f'font-size="11" font-family="JetBrains Mono, monospace">'
                 f'potential + kinetic = {total:.4g} J</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">All potential at maximum extension, all '
                 f'kinetic as it crosses equilibrium, and back again. The two curves always '
                 f'sum to the same flat line.</text>')
    return wrap("".join(parts), w, h, "Energy exchanging between two stores")


@cached
def phase_dial(theta_deg: float) -> str:
    """A phasor: where in the cycle the oscillator currently is."""
    w, h = 620, 300
    cx, cy, r = 200, 160, 110
    theta = math.radians(theta_deg)
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'PHASE = {theta_deg:.4g}°</text>',
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0b1a2c" stroke="#1b3350"/>',
             f'<line x1="{cx - r - 18}" y1="{cy}" x2="{cx + r + 18}" y2="{cy}" '
             f'stroke="{MUTED}" stroke-width="1.5"/>',
             f'<line x1="{cx}" y1="{cy - r - 18}" x2="{cx}" y2="{cy + r + 18}" '
             f'stroke="{MUTED}" stroke-width="1.5"/>']
    for name, offset, colour in [("x", 0, CYAN), ("v", -90, AMBER), ("a", 180, ROSE)]:
        angle = theta + math.radians(offset)
        ex = cx + r * math.cos(angle)
        ey = cy - r * math.sin(angle)
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" '
                     f'stroke="{colour}" stroke-width="3"/>')
        parts.append(f'<text x="{cx + (r + 16) * math.cos(angle):.1f}" '
                     f'y="{cy - (r + 16) * math.sin(angle) + 4:.1f}" fill="{colour}" '
                     f'font-size="13" font-weight="700">{name}</text>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{MUTED}"/>')
    parts.append(f'<rect x="360" y="60" width="236" height="176" rx="10" fill="#0d1c30" '
                 f'stroke="{VIOLET}" stroke-opacity="0.45"/>'
                 f'<text x="376" y="86" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">QUARTER-CYCLE OFFSETS</text>'
                 f'<text x="376" y="114" fill="{CYAN}" font-size="11" '
                 f'font-family="Sora, sans-serif">x at full displacement → v = 0</text>'
                 f'<text x="376" y="136" fill="{AMBER}" font-size="11" '
                 f'font-family="Sora, sans-serif">v at full speed → x = 0</text>'
                 f'<text x="376" y="158" fill="{ROSE}" font-size="11" '
                 f'font-family="Sora, sans-serif">a full → x = 0, opposite</text>'
                 f'<text x="376" y="190" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Each leads the previous by T/4.</text>'
                 f'<text x="376" y="212" fill="{VIOLET}" font-size="11" '
                 f'font-family="Sora, sans-serif">Phase is measured in radians.</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Rotating this dial traces the whole cycle: '
                 f'the three arrows always keep their quarter-period spacing.</text>')
    return wrap("".join(parts), w, h, "A phase dial for the three S.H.M. quantities")


@cached
def period_comparison(rows) -> str:
    """Mass-spring next to pendulum: what each period depends on."""
    w, h = 680, 280
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'TWO OSCILLATORS, TWO PERIOD FORMULAS</text>']
    for index, row in enumerate(rows):
        y = 56 + index * 40
        colour = CYAN if index == 0 else AMBER
        parts.append(f'<text x="24" y="{y + 14}" fill="{MUTED}" font-size="12" '
                     f'font-family="Sora, sans-serif">{row["question"]}</text>'
                     f'<text x="300" y="{y + 14}" fill="{colour}" font-size="13" '
                     f'font-family="JetBrains Mono, monospace">{row["spring"]}</text>'
                     f'<text x="490" y="{y + 14}" fill="{AMBER}" font-size="13" '
                     f'font-family="JetBrains Mono, monospace">{row["pendulum"]}</text>')
    parts.append(f'<text x="300" y="48" fill="{CYAN}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">mass-spring</text>'
                 f'<text x="490" y="48" fill="{AMBER}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">pendulum</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Neither period contains the amplitude. Both '
                 f'contain a square root, which is why doubling one variable only changes the '
                 f'period by a factor of √2.</text>')
    return wrap("".join(parts), w, h, "Comparing the two period formulas")

@cached
def energy_exchange(amplitude=1.0, cycles=1.0):
    """Kinetic and potential energy across one cycle, crossing twice."""
    from .common import MONO as _MONO, SANS as _SANS
    from .common import label as _label
    w, h = 680, 360
    left, right, base, top = 80, 620, 290, 60
    emax = amplitude * amplitude
    n = 200

    def Y(v):
        return base - (v / emax) * (base - top)

    parts = [_label(20, 24, "KINETIC AND POTENTIAL ENERGY IN S.H.M.", MUTED, 12),
             _label(20, 42, "One curve rises exactly as the other falls. Their sum never "
                            "changes \u2014 that is the whole of 7.5.1.", MUTED, 10,
                    family=_SANS)]
    ke, pe = [], []
    for i in range(n + 1):
        t = cycles * i / n
        x = amplitude * math.cos(t)
        v = -amplitude * math.sin(t)
        px, vx = left + t / cycles * (right - left), Y(0.5 * x * x)
        pe.append(f"{px:.1f},{vx:.1f}")
        ke.append(f"{px:.1f},{Y(0.5 * v * v):.1f}")
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<polyline points="{" ".join(pe)}" fill="none" stroke="{AMBER}" '
                 f'stroke-width="2.8"/>')
    parts.append(f'<polyline points="{" ".join(ke)}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="2.8"/>')
    parts.append(f'<line x1="{left}" y1="{Y(0.5 * emax):.1f}" x2="{right}" '
                 f'y2="{Y(0.5 * emax):.1f}" stroke="{GREEN}" stroke-width="1.4" '
                 f'stroke-dasharray="6 4"/>')
    parts.append(_label(right - 4, Y(0.5 * emax) - 8, "total energy (1/2)kA\u00b2", GREEN,
                        11, "end"))
    for xpos, text in ((left, "x = A\nall potential"), (left + (right - left) / 2,
                                                        "x = 0\nall kinetic"),
                       (right, "x = A\nagain")):
        parts.append(f'<line x1="{xpos:.1f}" y1="{top - 6}" x2="{xpos:.1f}" y2="{base}" '
                     f'stroke="{MUTED}" stroke-width="1" stroke-dasharray="3 3" '
                     f'opacity="0.5"/>')
        for i, line in enumerate(text.split("\n")):
            parts.append(_label(xpos, top - 22 + i * 13, line, MUTED, 9, "middle", _SANS))
    parts.append(_label(left + 8, top + 4, "\u2014 potential energy  (1/2)k x\u00b2", AMBER, 11,
                        "start", _SANS))
    parts.append(_label(left + 8, top + 20, "\u2014 kinetic energy  (1/2)m v\u00b2", CYAN, 11,
                        "start", _SANS))
    parts.append(_label(right, base + 26, "time \u2192", MUTED, 10, "end"))
    return wrap("".join(parts), w, h, "Energy exchange in simple harmonic motion")


@cached
def resonance_curve(damping=0.25):
    """Amplitude against driving frequency, with the resonance peak marked."""
    from .common import SANS as _SANS
    from .common import label as _label
    w, h = 680, 360
    left, right, base, top = 80, 560, 300, 60
    f_lo, f_hi, amp_max = 0.5, 1.6, 3.2

    def X(f):
        return left + (f - f_lo) / (f_hi - f_lo) * (right - left)

    def Y(a):
        return base - a / amp_max * (base - top)

    parts = [_label(20, 24, "AMPLITUDE AGAINST DRIVING FREQUENCY", MUTED, 12),
             _label(20, 42, "The peak sits at the natural frequency. Narrow peak means low "
                            "damping.", MUTED, 10, family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    pts = []
    for i in range(161):
        f = f_lo + (f_hi - f_lo) * i / 160
        a = damping / math.sqrt((f / 1.0 - 1.0) ** 2 * 9.0 + damping ** 2)
        pts.append(f"{X(f):.1f},{Y(min(a, amp_max)):.1f}")
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="2.8"/>')
    parts.append(f'<line x1="{X(1.0):.1f}" y1="{top - 10}" x2="{X(1.0):.1f}" y2="{base}" '
                 f'stroke="{ROSE}" stroke-width="1.6" stroke-dasharray="5 3"/>')
    peak = damping / damping
    parts.append(_label(X(1.0), top + 22, "resonance", ROSE, 12, "middle"))
    parts.append(_label(X(1.0) + 8, top + 2, f"amplitude \u2248 {peak:.2g}", ROSE, 10))
    for f, text, colour in ((0.7, "off resonance", MUTED),
                             (1.25, "off resonance", MUTED)):
        x = X(f)
        a = damping / math.sqrt((f - 1.0) ** 2 * 9.0 + damping ** 2)
        parts.append(f'<circle cx="{x:.1f}" cy="{Y(min(a, amp_max)):.1f}" r="5" '
                     f'fill="{colour}"/>')
        parts.append(_label(x, Y(min(a, amp_max)) - 14, text, colour, 9, "middle"))
    parts.append(_label(X(0.5), base + 28, "0.5", MUTED, 10, "middle"))
    parts.append(_label(X(1.0), base + 28, "natural frequency", MUTED, 10, "middle"))
    parts.append(_label(X(1.6), base + 28, "1.6", MUTED, 10, "middle"))
    parts.append(_label(right, base + 44, "driving frequency \u2192", MUTED, 10, "end"))
    parts.append(f'<text transform="translate(28 {(top + base) / 2:.0f}) rotate(-90)" '
                 f'text-anchor="middle" fill="{MUTED}" font-size="10" '
                 f'font-family="{_SANS}">amplitude \u2192</text>')
    return wrap("".join(parts), w, h, "Resonance curve")


@cached
def damping_comparison(kind="light"):
    """Displacement-time traces for light, critical and heavy damping."""
    from .common import SANS as _SANS
    from .common import label as _label
    w, h = 680, 300
    left, right, base, top = 80, 620, 230, 50
    traces = {
        "light": ("light damping", VIOLET, 0.02, True),
        "critical": ("critical damping", GREEN, 1.2, False),
        "heavy": ("heavy damping", ROSE, 3.2, False),
    }
    parts = [_label(20, 24, "THREE DEGREES OF DAMPING", MUTED, 12),
             _label(20, 42, "Same spring, same mass. Only the damping differs.", MUTED, 10,
                    family=_SANS)]
    parts.append(f'<line x1="{left}" y1="{base}" x2="{right}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{base}" stroke="{MUTED}" '
                 f'stroke-width="1.5"/>')
    for key, (name, colour, gamma, oscillating) in traces.items():
        pts = []
        for i in range(161):
            t = 6.0 * i / 160
            if key == "critical":
                y = (1 + gamma * t) * math.exp(-gamma * t)
            elif key == "heavy":
                y = (1 + gamma * t) * math.exp(-gamma * t)
            else:
                y = math.exp(-gamma * t) * math.cos(3.0 * t)
            x = left + 6.0 * t / 6.0 * (right - left)
            pts.append(f"{x:.1f},{base - 0.82 * y * (base - top):.1f}")
        thick = 3.4 if key == kind else 1.6
        op = 1.0 if key == kind else 0.35
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{colour}" '
                     f'stroke-width="{thick}" opacity="{op}"/>')
        parts.append(_label(right + 2, base - 0.82 * 0.15 * (base - top) +
                             {"light": -18, "critical": 2, "heavy": 22}[key],
                             name, colour, 11 if key == kind else 9, "start"))
    parts.append(_label(left, base + 22, "time \u2192", MUTED, 10))
    parts.append(_label(left, base + 40, "the bold trace is the one selected", MUTED, 9,
                        family=_SANS))
    return wrap("".join(parts), w, h, "Light, critical and heavy damping")
