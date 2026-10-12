"""Chapter 8 diagrams: waves, interference, stationary waves and Doppler."""

from __future__ import annotations

import math

from ..core import waves as W
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, wave_scale as _wave_scale, wrap

__all__ = ["progressive_trace", "two_wave_bench", "wave_graph_annotated",
           "particle_motion", "interference_map", "beat_panel",
           "stationary_bench", "pipe_bench", "doppler_explorer",
           "spectrum_shift", "round_trip"]


@cached
def progressive_trace(amplitude: float, wavelength: float, snapshots: int = 4) -> str:
    """Four moments of one progressive wave, to show the shape travelling."""
    w, h = 700, 300
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'THE SHAPE MOVES; THE POINTS DO NOT</text>']
    panel_w = (w - 40) / snapshots
    top, bottom = 50, 250
    # metres -> pixels, so a 0.5 m wave is a visible wave and not a flat line
    scale = _wave_scale(amplitude, room=(bottom - top) / 2 - 14)
    for index in range(snapshots):
        x0 = 20 + index * panel_w
        # mid is a *y* value. It was computed as x0 + panel_w/2, which mixes the
        # panel's horizontal offset into its vertical centre: panel 0 landed on
        # 102 by luck and drew correctly, while panels 1-3 drew at y=267, 432
        # and 597 on a 300px canvas - all off the bottom, which is why the
        # screenshots showed only t=0 with a wave in it.
        mid = (top + bottom) / 2
        parts.append(f'<rect x="{x0}" y="46" width="{panel_w - 8}" height="212" rx="8" '
                     f'fill="#0b1a2c" stroke="#1b3350"/>')
        parts.append(f'<line x1="{x0 + 10}" y1="{mid}" x2="{x0 + panel_w - 18}" y2="{mid}" '
                     f'stroke="#18304b" stroke-width="1"/>')
        points = []
        steps = 90
        shift = index * 0.22
        amp_px = amplitude * scale
        for step in range(steps + 1):
            frac = step / steps
            xx = x0 + 10 + frac * (panel_w - 28)
            y = mid - amp_px * math.sin(2 * math.pi * (frac * 3 + shift))
            points.append(f"{xx:.1f},{y:.1f}")
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
                     f'stroke-width="2.6"/>')
        # One marked particle: it oscillates but never travels.
        px = x0 + 10 + 0.22 * (panel_w - 28)
        py = mid - amp_px * math.sin(2 * math.pi * (0.22 * 3 + shift))
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="{AMBER}"/>')
        parts.append(f'<line x1="{px:.1f}" y1="{mid}" x2="{px:.1f}" y2="{mid + 150}" '
                     f'stroke="{AMBER}" stroke-width="0.8" stroke-dasharray="3 3" '
                     f'opacity="0.5"/>')
        parts.append(f'<text x="{x0 + panel_w / 2:.0f}" y="{bottom - 2}" text-anchor="middle" '
                     f'fill="{MUTED}" font-size="10" font-family="JetBrains Mono, monospace">'
                     f't = {index}</text>')
    parts.append(f'<text x="20" y="{h - 30}" fill="{AMBER}" font-size="11" '
                 f'font-family="Sora, sans-serif">The amber dot is always at the same position '
                 f'on the medium — it only moves up and down.</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Meanwhile the whole pattern travels to the '
                 f'right. Energy is leaving the source; the medium is not.</text>')
    return wrap("".join(parts), w, h, "A progressive wave carrying energy, not matter")


@cached
def two_wave_bench(a1, f1, a2, f2, extent=1.0, samples=400) -> str:
    """Two waves and their sum, drawn together on one axis."""
    w, h = 700, 430
    left, right = 60, w - 150
    n = samples
    xs = [i * extent / (n - 1) for i in range(n)]
    y1 = [a1 * math.sin(2 * math.pi * f1 * x) for x in xs]
    y2 = [a2 * math.sin(2 * math.pi * f2 * x) for x in xs]
    total = [p + q for p, q in zip(y1, y2)]
    peak = max(max(abs(v) for v in total), 1e-9)

    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'SUPERPOSITION: THE RESULT IS THE SUM</text>']
    rows = [("wave A", y1, CYAN), ("wave B", y2, AMBER), ("A + B", total, GREEN)]
    for index, (label, values, colour) in enumerate(rows):
        top = 50 + index * 122
        bottom = top + 104
        mid = (top + bottom) / 2
        parts.append(f'<line x1="{left}" y1="{mid:.1f}" x2="{right}" y2="{mid:.1f}" '
                     f'stroke="#18304b" stroke-width="1"/>')
        points = []
        for step, value in enumerate(values):
            px = left + (step / (n - 1)) * (right - left)
            py = mid - (value / peak) * (104 / 2 - 6)
            points.append(f"{px:.1f},{py:.1f}")
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{colour}" '
                     f'stroke-width="2.6"/>')
        parts.append(f'<text x="20" y="{mid + 4:.1f}" fill="{colour}" font-size="13" '
                     f'font-weight="700">{label}</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Set both frequencies equal and the sum '
                 f'flattens to twice the amplitude; set them far apart and it simply ripples '
                 f'up and down.</text>')
    return wrap("".join(parts), w, h, "Two waves and their superposition")


@cached
def wave_graph_annotated(amplitude: float, wavelength: float) -> str:
    """A transverse wave with every feature labelled."""
    w, h = 700, 300
    left, right = 70, w - 40
    mid = 170
    n = 400
    points = []
    amp_px = amplitude * _wave_scale(amplitude, room=128.0)
    for step in range(n + 1):
        frac = step / n
        x = left + frac * (right - left)
        y = mid - amp_px * math.sin(2 * math.pi * frac * 2)
        points.append(f"{x:.1f},{y:.1f}")
    parts = [f'<line x1="{left}" y1="{mid}" x2="{right}" y2="{mid}" stroke="{MUTED}" '
             f'stroke-width="1.5" stroke-dasharray="5 4"/>',
             f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
             f'stroke-width="3"/>']
    crest_x = left + (right - left) * 0.25
    trough_x = left + (right - left) * 0.75
    parts.append(f'<circle cx="{crest_x:.0f}" cy="{mid - amplitude:.0f}" r="5" fill="{GREEN}"/>')
    parts.append(f'<circle cx="{trough_x:.0f}" cy="{mid + amplitude:.0f}" r="5" fill="{ROSE}"/>')
    parts.append(f'<line x1="{crest_x:.0f}" y1="{mid}" x2="{crest_x:.0f}" '
                 f'y2="{mid - amplitude:.0f}" stroke="{GREEN}" stroke-width="2"/>')
    parts.append(f'<text x="{crest_x + 10:.0f}" y="{mid - amplitude - 12:.0f}" fill="{GREEN}" '
                 f'font-size="13" font-weight="700">crest</text>')
    parts.append(f'<text x="{trough_x + 10:.0f}" y="{mid + amplitude + 20:.0f}" fill="{ROSE}" '
                 f'font-size="13" font-weight="700">trough</text>')
    parts.append(f'<text x="{crest_x - 40:.0f}" y="{mid - amplitude / 2:.0f}" fill="{AMBER}" '
                 f'font-size="12" font-family="JetBrains Mono, monospace">'
                 f'A = {amplitude:g}</text>')
    parts.append(f'<line x1="{crest_x:.0f}" y1="{mid + amplitude + 30:.0f}" '
                 f'x2="{crest_x + (right - left) / 2:.0f}" y2="{mid + amplitude + 30:.0f}" '
                 f'stroke="{VIOLET}" stroke-width="2"/>')
    parts.append(f'<text x="{crest_x + (right - left) / 4:.0f}" y="{mid + amplitude + 50:.0f}" '
                 f'text-anchor="middle" fill="{VIOLET}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">lambda</text>')
    parts.append(f'<line x1="{left - 10}" y1="{mid - amplitude:.0f}" x2="{left - 10}" '
                 f'y2="{mid + amplitude:.0f}" stroke="{AMBER}" stroke-width="1.5" '
                 f'stroke-dasharray="3 3"/>')
    parts.append(f'<text x="20" y="26" fill="{MUTED}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
                 f'FULLY LABELLED TRANSVERSE WAVE</text>')
    parts.append(f'<text x="20" y="{h - 26}" fill="{AMBER}" font-size="11" '
                 f'font-family="Sora, sans-serif">Amplitude is measured from the equilibrium '
                 f'line, not from crest to trough: the peak-to-peak height here is '
                 f'{2 * amplitude:g}.</text>')
    parts.append(f'<text x="20" y="{h - 10}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Wavelength is measured crest to crest, or '
                 f'trough to trough — never crest to trough.</text>')
    return wrap("".join(parts), w, h, "An annotated transverse wave")


@cached
def particle_motion() -> str:
    """Transverse and longitudinal side by side, with the particle motion shown."""
    w, h = 700, 320
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'THE TEST IS HOW THE PARTICLES MOVE</text>']
    for index, (name, colour, note) in enumerate(
            [("Transverse", CYAN, "particles ⊥ the direction of travel"),
             ("Longitudinal", AMBER, "particles ‖ the direction of travel")]):
        x0 = 30 + index * 350
        top, mid = 70, 170
        parts.append(f'<rect x="{x0}" y="{top}" width="320" height="200" rx="10" '
                     f'fill="#0b1a2c" stroke="#1b3350"/>')
        parts.append(f'<text x="{x0 + 12}" y="{top + 22}" fill="{colour}" font-size="14" '
                     f'font-weight="700">{name}</text>')
        parts.append(f'<text x="{x0 + 12}" y="{top + 40}" fill="{MUTED}" font-size="11" '
                     f'font-family="Sora, sans-serif">{note}</text>')
        if index == 0:
            points = []
            for step in range(161):
                frac = step / 160
                x = x0 + 16 + frac * 288
                y = mid - 46 * math.sin(2 * math.pi * frac * 2)
                points.append(f"{x:.1f},{y:.1f}")
            parts.append(f'<polyline points="{" ".join(points)}" fill="none" '
                         f'stroke="{colour}" stroke-width="2.6"/>')
            for step in range(9):
                frac = step / 8
                x = x0 + 16 + frac * 288
                y = mid - 46 * math.sin(2 * math.pi * frac * 2)
                parts.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" '
                             f'y2="{y - 18:.1f}" stroke="{colour}" stroke-width="2"/>')
                parts.append(f'<polygon points="{x:.1f},{y - 24:.1f} {x - 4:.1f},'
                             f'{y - 14:.1f} {x + 4:.1f},{y - 14:.1f}" fill="{colour}"/>')
        else:
            for step in range(13):
                x = x0 + 30 + step * 24
                y = mid
                offset = 26 * math.sin(2 * math.pi * step / 6)
                parts.append(f'<circle cx="{x}" cy="{y - offset:.1f}" r="5" '
                             f'fill="{colour}"/>')
                parts.append(f'<line x1="{x}" y1="{y - offset:.1f}" x2="{x}" '
                             f'y2="{y - offset - 16:.1f}" stroke="{colour}" '
                             f'stroke-width="1.6"/>')
            for step in range(0, 289, 24):
                parts.append(f'<line x1="{x0 + 16 + step}" y1="{mid + 42}" '
                             f'x2="{x0 + 16 + step}" y2="{mid + 62}" stroke="#1b3350" '
                             f'stroke-width="1"/>')
        parts.append(f'<line x1="{x0 + 16}" y1="{mid + 72}" x2="{x0 + 304}" y2="{mid + 72}" '
                     f'stroke="{MUTED}" stroke-width="2"/>')
        parts.append(f'<polygon points="{x0 + 304},{mid + 72} {x0 + 294},{mid + 67} '
                     f'{x0 + 294},{mid + 77}" fill="{MUTED}"/>')
        parts.append(f'<text x="{x0 + 150}" y="{mid + 92}" text-anchor="middle" '
                     f'fill="{MUTED}" font-size="11" font-family="Sora, sans-serif">'
                     f'wave travels this way</text>')
        parts.append(f'<text x="{x0 + 12}" y="{top + 66}" fill="{MUTED}" font-size="11" '
                     f'font-family="JetBrains Mono, monospace">'
                     f'{"crests and troughs" if index == 0 else "compressions and rarefactions"}</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Only transverse waves can be polarised, '
                 f'because polarisation is about the plane of vibration — and a '
                 f'longitudinal wave has none.</text>')
    return wrap("".join(parts), w, h, "Transverse and longitudinal waves compared")


@cached
def interference_map(path_difference: float, wavelength: float) -> str:
    """Intensity against path difference, with the bright and quiet points marked."""
    w, h = 700, 330
    left, right, top, bottom = 70, w - 150, 60, 260
    n = 400
    span = max(wavelength * 2.5, path_difference * 1.3, 1e-9)
    points = []
    for step in range(n + 1):
        frac = step / n
        d = frac * span
        value = 2.0 * math.cos(math.pi * d / wavelength) ** 2
        px = left + frac * (right - left)
        py = bottom - value * (bottom - top)
        points.append(f"{px:.1f},{py:.1f}")
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'INTERFERENCE AGAINST PATH DIFFERENCE</text>',
             f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
             f'stroke-width="3"/>',
             f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="{MUTED}" '
             f'stroke-width="2"/>',
             f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{MUTED}" '
             f'stroke-width="2"/>']
    for index in range(6):
        d = index * wavelength
        if d > span:
            break
        px = left + (d / span) * (right - left)
        loud = "louder"
        py = top if index % 2 == 0 else bottom - 2 * (bottom - top)
        parts.append(f'<line x1="{px:.1f}" y1="{bottom}" x2="{px:.1f}" y2="{bottom - 8:.0f}" '
                     f'stroke="{GREEN if index % 2 == 0 else ROSE}" stroke-width="2"/>')
        parts.append(f'<text x="{px:.1f}" y="{bottom + 18:.0f}" text-anchor="middle" '
                     f'fill="{GREEN if index % 2 == 0 else ROSE}" font-size="10" '
                     f'font-family="JetBrains Mono, monospace">{d:.3g}</text>')
    here = left + (min(path_difference, span) / span) * (right - left)
    parts.append(f'<line x1="{here:.1f}" y1="{top - 8}" x2="{here:.1f}" y2="{bottom + 6}" '
                 f'stroke="{AMBER}" stroke-width="2.5" stroke-dasharray="5 4"/>')
    frac = (path_difference % wavelength) / wavelength if wavelength else 0
    if abs(frac) < 1e-9:
        kind, colour = "CONSTRUCTIVE", GREEN
    elif abs(frac - 0.5) < 1e-9:
        kind, colour = "DESTRUCTIVE", ROSE
    else:
        kind, colour = "PARTLY CONSTRUCTIVE", AMBER
    parts.append(f'<rect x="{right + 16}" y="80" width="164" height="120" rx="10" '
                 f'fill="#0d1c30" stroke="{colour}" stroke-opacity="0.5"/>'
                 f'<text x="{right + 30}" y="106" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">PATH DIFFERENCE</text>'
                 f'<text x="{right + 30}" y="134" fill="#eef6ff" font-size="17" '
                 f'font-family="JetBrains Mono, monospace">{path_difference:.4g} m</text>'
                 f'<text x="{right + 30}" y="160" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">= {frac:.3g} lambda</text>'
                 f'<text x="{right + 30}" y="184" fill="{colour}" font-size="12" '
                 f'font-weight="700">{kind}</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Bright at whole wavelengths, dark at half '
                 f'ones — and the phase difference is 2 pi times that fraction.</text>')
    return wrap("".join(parts), w, h, "Interference intensity against path difference")


@cached
def beat_panel(f1: float, f2: float, duration: float = 0.6) -> str:
    """The summed wave inside its drifting envelope."""
    w, h = 700, 320
    left, right = 60, w - 40
    mid, amplitude = 170, 46.0
    n = 600
    fb = abs(f1 - f2)
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'f1 = {f1:g} Hz, f2 = {f2:g} Hz → {fb:g} beats per second</text>']
    points, env = [], []
    for step in range(n + 1):
        frac = step / n
        t = frac * duration
        x = left + frac * (right - left)
        value = math.sin(2 * math.pi * f1 * t) + math.sin(2 * math.pi * f2 * t)
        points.append(f"{x:.1f},{mid - value * amplitude:.1f}")
        env.append(abs(2.0 * math.cos(math.pi * (f1 - f2) * t)))
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="1.6"/>')
    for sign, dash in ((1, ""), (-1, "")):
        pts = []
        for step in range(0, n + 1, 12):
            frac = step / n
            x = left + frac * (right - left)
            y = mid - sign * env[step] * amplitude
            pts.append(f"{x:.1f},{y:.1f}")
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{AMBER}" '
                     f'stroke-width="2.2" stroke-dasharray="7 4" opacity="0.9"/>')
    parts.append(f'<line x1="{left}" y1="{mid}" x2="{right}" y2="{mid}" stroke="#18304b" '
                 f'stroke-width="1"/>')
    if fb:
        beats = fb * duration
        parts.append(f'<text x="20" y="{h - 30}" fill="{AMBER}" font-size="11" '
                     f'font-family="JetBrains Mono, monospace">'
                     f'envelope breathes {beats:.3g} times in {duration:g} s '
                     f'→ beat period = {1 / fb:.4g} s</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The rapid oscillation is the sound itself; '
                 f'the slow swelling of the dashed envelope is the beat you hear.</text>')
    return wrap("".join(parts), w, h, "Beats formed by two close frequencies")


@cached
def stationary_bench(length: float, mode: int, amplitude: float = 1.0) -> str:
    """A string carrying a stationary wave, nodes and antinodes labelled."""
    w, h = 700, 340
    left, right = 70, w - 40
    top, bottom = 90, 250
    n = max(3, int(mode))
    total = length * n
    points = []
    for step in range(n * 120 + 1):
        frac = step / (n * 120)
        x = left + frac * (right - left)
        y = (top + bottom) / 2 - amplitude * 40 * math.sin(n * math.pi * frac)
        points.append(f"{x:.1f},{y:.1f}")
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'STATIONARY WAVE, MODE {mode}</text>',
             f'<line x1="{left}" y1="60" x2="{left}" y2="{bottom + 30}" stroke="{MUTED}" '
             f'stroke-width="5"/>',
             f'<line x1="{right}" y1="60" x2="{right}" y2="{bottom + 30}" stroke="{MUTED}" '
             f'stroke-width="5"/>',
             f'<line x1="{left}" y1="60" x2="{right}" y2="60" stroke="{MUTED}" '
             f'stroke-width="3"/>',
             f'<polyline points="{" ".join(points)}" fill="none" stroke="{CYAN}" '
             f'stroke-width="3"/>']
    for index in range(n + 1):
        frac = index / n
        x = left + frac * (right - left)
        parts.append(f'<circle cx="{x:.1f}" cy="{(top + bottom) / 2:.0f}" r="8" '
                     f'fill="{ROSE}"/>')
        parts.append(f'<text x="{x:.1f}" y="{(top + bottom) / 2 + 28:.0f}" text-anchor="middle" '
                     f'fill="{ROSE}" font-size="11" font-family="JetBrains Mono, monospace">'
                     f'N{index + 1}</text>')
    for index in range(n):
        frac = (index + 0.5) / n
        x = left + frac * (right - left)
        y = (top + bottom) / 2 - amplitude * 40
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{GREEN}"/>')
        parts.append(f'<text x="{x:.1f}" y="{y - 14:.1f}" text-anchor="middle" fill="{GREEN}" '
                     f'font-size="11" font-family="JetBrains Mono, monospace">A{index + 1}</text>')
    parts.append(f'<text x="{right - 6}" y="{bottom + 56}" text-anchor="end" fill="{MUTED}" '
                 f'font-size="11" font-family="JetBrains Mono, monospace">L = {length:g}</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">{n + 1} nodes and {n} antinodes, alternating '
                 f'lambda/2 apart. The pattern does not travel, and no energy leaves the '
                 f'string.</text>')
    return wrap("".join(parts), w, h, "A stationary wave on a string")


@cached
def pipe_bench() -> str:
    """String, open pipe and closed pipe side by side."""
    w, h = 700, 300
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'THE END CONDITION DECIDES WHICH HARMONICS EXIST</text>']
    panels = [("String, fixed ends", CYAN, "node at both ends", "n v / 2L", "n = 1,2,3, ..."),
              ("Pipe, both open", TEAL, "antinode at both ends", "n v / 2L", "n = 1,2,3, ..."),
              ("Pipe, one closed", AMBER, "node closed, antinode open",
               "(2n-1) v / 4L", "n = 1,3,5, ...")]
    for index, (title, colour, cond, formula, allowed) in enumerate(panels):
        x0 = 20 + index * 228
        top, bottom = 70, 170
        parts.append(f'<rect x="{x0}" y="{top}" width="212" height="190" rx="10" '
                     f'fill="#0b1a2c" stroke="{colour}" stroke-opacity="0.4"/>')
        for edge in (0, 1):
            x = x0 + 12 + edge * 188
            if "node" in cond.split(" at ")[0] or (edge == 0 and "closed" in cond):
                parts.append(f'<line x1="{x}" y1="{top + 20}" x2="{x}" y2="{bottom}" '
                             f'stroke="{ROSE}" stroke-width="5"/>')
            elif "antinode" in cond and edge in (0, 1) and "closed" not in cond:
                parts.append(f'<line x1="{x}" y1="{top + 20}" x2="{x}" y2="{bottom}" '
                             f'stroke="{MUTED}" stroke-width="3"/>')
                parts.append(f'<circle cx="{x}" cy="{(top + bottom) / 2:.0f}" r="8" '
                             f'fill="{GREEN}"/>')
        if index == 2:
            parts.append(f'<line x1="{x0 + 12}" y1="{top + 20}" x2="{x0 + 12}" '
                         f'y2="{bottom}" stroke="{ROSE}" stroke-width="5"/>')
            parts.append(f'<line x1="{x0 + 200}" y1="{top + 20}" x2="{x0 + 200}" '
                         f'y2="{bottom}" stroke="{MUTED}" stroke-width="3"/>')
            parts.append(f'<circle cx="{x0 + 200}" cy="{(top + bottom) / 2:.0f}" r="8" '
                         f'fill="{GREEN}"/>')
        pts = []
        for step in range(101):
            frac = step / 100
            x = x0 + 12 + frac * 188
            shape = (math.sin(2 * math.pi * frac) if index < 2
                     else math.sin(1.5 * math.pi * frac))
            pts.append(f"{x:.1f},{((top + bottom) / 2 - 26 * shape):.1f}")
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{colour}" '
                     f'stroke-width="2.6"/>')
        parts.append(f'<text x="{x0 + 10}" y="{top + 16}" fill="{colour}" font-size="11" '
                     f'font-weight="700">{title}</text>')
        parts.append(f'<text x="{x0 + 10}" y="{bottom + 26}" fill="{MUTED}" font-size="10" '
                     f'font-family="Sora, sans-serif">{cond}</text>')
        parts.append(f'<text x="{x0 + 10}" y="{bottom + 46}" fill="{colour}" font-size="13" '
                     f'font-family="JetBrains Mono, monospace">f = {formula}</text>')
        parts.append(f'<text x="{x0 + 10}" y="{bottom + 64}" fill="{MUTED}" font-size="10" '
                     f'font-family="JetBrains Mono, monospace">{allowed}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">A stopped pipe fits a whole number of half '
                 f'wavelengths, so it sounds an octave below and has no even harmonics — '
                 f'which is why it sounds hollow.</text>')
    return wrap("".join(parts), w, h, "Strings and air columns compared")


@cached
def doppler_explorer(f: float, speed: float, source_speed: float,
                      observer_speed: float, case: str) -> str:
    """Wavefronts from a moving source, and the wavefronts the observer meets."""
    w, h = 700, 340
    mid = 170
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'CASE ({case}) — SOURCE SPEED {source_speed:g} m s⁻¹</text>']
    for index in range(7):
        age = index * 0.22
        x = 340 + source_speed * age
        radius = speed * age * 0.75
        parts.append(f'<circle cx="{x:.1f}" cy="{mid}" r="{radius:.1f}" fill="none" '
                     f'stroke="{CYAN}" stroke-width="1.4" opacity="{0.85 - index * 0.08:.2f}"/>')
    sx = 340 + source_speed * 6 * 0.22
    parts.append(f'<circle cx="{sx:.1f}" cy="{mid}" r="9" fill="{AMBER}"/>')
    parts.append(f'<text x="{sx - 4:.1f}" y="{mid - 16:.1f}" fill="{AMBER}" font-size="11" '
                 f'font-weight="700">source</text>')
    ox = 560 + observer_speed * 6 * 0.22
    parts.append(f'<polygon points="{ox:.1f},{mid - 10} {ox + 8:.1f},{mid} '
                 f'{ox:.1f},{mid + 10}" fill="{GREEN}"/>')
    parts.append(f'<text x="{ox - 14:.1f}" y="{mid + 28}" fill="{GREEN}" font-size="11" '
                 f'font-weight="700">observer</text>')
    apparent = W_doppler(f, speed, observer_speed, source_speed, case)
    higher = apparent > f
    parts.append(f'<line x1="{sx:.1f}" y1="{mid}" x2="{ox:.1f}" y2="{mid}" '
                 f'stroke="{MUTED}" stroke-width="1" stroke-dasharray="3 3"/>')
    parts.append(f'<rect x="20" y="240" width="660" height="64" rx="10" fill="#0d1c30" '
                 f'stroke="{GREEN if higher else ROSE}" stroke-opacity="0.45"/>'
                 f'<text x="36" y="264" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">APPARENT FREQUENCY</text>'
                 f'<text x="36" y="290" fill="{GREEN if higher else ROSE}" font-size="19" '
                 f'font-weight="800" font-family="JetBrains Mono, monospace">'
                 f'{apparent:.4g} Hz</text>'
                 f'<text x="200" y="264" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">EMITTED</text>'
                 f'<text x="200" y="288" fill="#c6d6ea" font-size="15" '
                 f'font-family="JetBrains Mono, monospace">{f:g} Hz</text>'
                 f'<text x="330" y="264" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">SHIFT</text>'
                 f'<text x="330" y="288" fill="#c6d6ea" font-size="15" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'{100 * (apparent / f - 1):+.2g} %</text>'
                 f'<text x="470" y="276" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">'
                 f'{"rising" if higher else "falling"} pitch</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The wavefronts bunch up in front of a '
                 f'moving source and spread out behind it. The speed of sound itself never '
                 f'changes.</text>')
    return wrap("".join(parts), w, h, "Doppler shift with a moving source")


def W_doppler(f, v, v_o, v_s, case):
    """Apparent frequency for one of the four classical Doppler cases.

    Delegates to :mod:`physics.core.waves` so the formula lives in one place.
    """
    return W.doppler(f, v, v_o, v_s, case)


@cached
def spectrum_shift(rest_wavelength: float) -> str:
    """A spectrum bar with the shift drawn as a visible offset."""
    w, h = 660, 280
    left, right = 60, w - 60
    top = 90
    bar_h = 46
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'RED SHIFT: A REST LINE AND ITS OBSERVED POSITION</text>']
    bands = [("violet", 0.75), ("blue", 0.65), ("green", 0.55), ("yellow", 0.47),
             ("orange", 0.42), ("red", 0.38)]
    for name, pos in bands:
        x = left + pos * (right - left)
        parts.append(f'<rect x="{x - 18:.1f}" y="{top}" width="36" height="{bar_h}" '
                     f'fill="{name}" opacity="0.75"/>')
    parts.append(f'<text x="{left}" y="{top - 10}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">shorter lambda</text>')
    parts.append(f'<text x="{right}" y="{top - 10}" text-anchor="end" fill="{MUTED}" '
                 f'font-size="10" font-family="JetBrains Mono, monospace">longer lambda</text>')
    rest = left + 0.47 * (right - left)
    # Map the wavelength onto the same band positions used for the spectrum.
    ratio = (rest_wavelength / 570e-9) if rest_wavelength else 1.0
    observed = left + (0.47 * (2.0 - 1.0 / ratio)) * (right - left) if ratio else rest
    observed = max(left + 6.0, min(right - 6.0, observed))
    parts.append(f'<line x1="{rest:.1f}" y1="{top - 6}" x2="{rest:.1f}" '
                 f'y2="{top + bar_h + 22}" stroke="{MUTED}" stroke-width="2" '
                 f'stroke-dasharray="5 4"/>')
    parts.append(f'<line x1="{observed:.1f}" y1="{top - 6}" x2="{observed:.1f}" '
                 f'y2="{top + bar_h + 22}" stroke="{ROSE}" stroke-width="3"/>')
    parts.append(f'<text x="{rest:.1f}" y="{top + bar_h + 40}" text-anchor="middle" '
                 f'fill="{MUTED}" font-size="11" font-family="JetBrains Mono, monospace">'
                 f'rest 570 nm</text>')
    parts.append(f'<text x="{observed:.1f}" y="{top + bar_h + 40}" text-anchor="middle" '
                 f'fill="{ROSE}" font-size="11" font-family="JetBrains Mono, monospace">'
                 f'observed {rest_wavelength * 1e9:.4g} nm</text>')
    direction = ("further into the red — the source is receding"
                 if rest_wavelength > 570e-9 else
                 "towards the blue — the source is approaching")
    parts.append(f'<text x="20" y="{h - 40}" fill="{ROSE}" font-size="12" '
                 f'font-family="Sora, sans-serif">{direction}</text>')
    parts.append(f'<text x="20" y="{h - 18}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Every distant galaxy is red-shifted in '
                 f'proportion to its distance — the direct evidence that the universe is '
                 f'expanding.</text>')
    return wrap("".join(parts), w, h, "A spectrum line and its Doppler shift")


@cached
def round_trip(target_speed: float, wave_speed: float = 3.0e8,
               carrier: float = 1.0e10) -> str:
    """Radar: the pulse is Doppler shifted twice, once out and once back."""
    w, h = 680, 300
    shift = 2.0 * carrier * target_speed / wave_speed
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'TWO DOPPLER SHIFTS, SO THE MEASURED BEAT IS ROUGHLY 2fv/c</text>',
             f'<circle cx="80" cy="160" r="26" fill="none" stroke="{MUTED}" stroke-width="2"/>'
             f'<text x="80" y="165" text-anchor="middle" fill="{MUTED}" font-size="11">RADAR</text>',
             f'<rect x="540" y="146" width="64" height="28" rx="5" fill="{AMBER}"/>'
             f'<text x="600" y="165" text-anchor="middle" fill="{AMBER}" font-size="11">target</text>',
             f'<polygon points="612,152 636,160 612,168" fill="{AMBER}"/>',
             f'<line x1="112" y1="150" x2="536" y2="150" stroke="{CYAN}" stroke-width="2"/>'
             f'<text x="324" y="140" text-anchor="middle" fill="{CYAN}" font-size="11" '
             f'font-family="JetBrains Mono, monospace">outbound: +f v/c</text>',
             f'<line x1="536" y1="180" x2="112" y2="180" stroke="{ROSE}" stroke-width="2"/>'
             f'<text x="324" y="196" text-anchor="middle" fill="{ROSE}" font-size="11" '
             f'font-family="JetBrains Mono, monospace">return: +f v/c again</text>']
    parts.append(f'<rect x="200" y="226" width="440" height="62" rx="10" fill="#0d1c30" '
                 f'stroke="{GREEN}" stroke-opacity="0.45"/>')
    for index, (label, value, colour) in enumerate([
            ("f", f"{carrier:.3g} Hz", MUTED),
            ("at the target", f"{carrier * (1 + target_speed / wave_speed):.4g} Hz", CYAN),
            ("echo", f"{carrier * (1 + 2 * target_speed / wave_speed):.4g} Hz", ROSE),
            ("beat = 2 f v / c", f"{shift:.3g} Hz", GREEN)]):
        parts.append(f'<text x="{214 + index * 110}" y="250" fill="{MUTED}" font-size="9" '
                     f'font-family="JetBrains Mono, monospace">{label}</text>'
                     f'<text x="{214 + index * 110}" y="272" fill="{colour}" font-size="13" '
                     f'font-family="JetBrains Mono, monospace">{value}</text>')
    parts.append(
        f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
        f'font-family="Sora, sans-serif">That factor of two is what turns an impossibly '
        f'small single shift into something a radar set can measure reliably.</text>')
    return wrap("".join(parts), w, h, "Radar and the doubled Doppler shift")