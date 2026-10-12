"""Chapter 4 diagrams: projectiles, circular motion and rotation."""

from __future__ import annotations

import math

from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET
from .common import cached, wrap

__all__ = ["trajectory_family", "component_split", "rotation_disc",
           "centripetal_circle", "centrifuge_tube", "weightless_orbit",
           "inertia_shapes", "skater_spin", "angular_dials"]


@cached
def trajectory_family(speeds, angles, g: float = 9.8) -> str:
    """A family of trajectories, so the 45-degree maximum is visible not tabulated."""
    w, h = 700, 420
    left, bottom, right, top = 60, h - 50, w - 200, 50
    span = max(speeds) ** 2 / g * 1.05
    parts = [
        f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
        f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
        f'EVERY TRAJECTORY FROM ONE POINT</text>',
        f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" '
        f'stroke="{MUTED}" stroke-width="2"/>',
    ]
    peak_y = 0
    for index, angle in enumerate(angles):
        colour = [CYAN, GREEN, AMBER, VIOLET, ROSE, TEAL][index % 6]
        peak_x, peak_h, end_x = 0, 0, 0
        points = []
        for step in range(0, 121):
            fraction = step / 120.0
            theta = math.radians(angle)
            t = 2.0 * max(speeds) * math.sin(theta) / g * fraction
            x = max(speeds) * math.cos(theta) * t
            y = max(speeds) * math.sin(theta) * t - 0.5 * g * t * t
            px = left + (x / span) * (right - left)
            py = bottom - (y / (span / 2)) * (bottom - top)
            points.append(f"{px:.1f},{py:.1f}")
            peak_y = max(peak_y, py)
            if step == 60:
                peak_x, peak_h = px, py
                parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3" fill="{colour}"/>')
            end_x = px
        parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{colour}" '
                     f'stroke-width="2.2" opacity="0.9"/>')
        parts.append(f'<text x="{end_x + 6:.1f}" y="{bottom - 4}" fill="{colour}" '
                     f'font-size="11" font-family="JetBrains Mono, monospace">{angle}°</text>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{left}" y2="{bottom - 24}" '
                 f'stroke="{MUTED}" stroke-width="2"/>')
    parts.append(f'<text x="{right + 12}" y="{top + 24}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">range →</text>')
    parts.append(f'<rect x="{right + 14}" y="{top}" width="170" height="150" rx="10" '
                 f'fill="#0d1c30" stroke="{GREEN}" stroke-opacity="0.45"/>'
                 f'<text x="{right + 28}" y="{top + 24}" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">LONGEST RANGE</text>'
                 f'<text x="{right + 28}" y="{top + 54}" fill="{GREEN}" font-size="24" '
                 f'font-weight="800">45°</text>'
                 f'<text x="{right + 28}" y="{top + 78}" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">sin 2θ cannot exceed 1,</text>'
                 f'<text x="{right + 28}" y="{top + 94}" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">and it reaches 1 at 2θ = 90°</text>'
                 f'<text x="{right + 28}" y="{top + 122}" fill="{MUTED}" font-size="10" '
                 f'font-family="Sora, sans-serif">Note: 30° and 60° reach the</text>'
                 f'<text x="{right + 28}" y="{top + 138}" fill="{MUTED}" font-size="10" '
                 f'font-family="Sora, sans-serif">same distance, since sin 60° = sin 120°</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Each curve is a parabola with its apex marked. '
                 f'The steepest reaches highest; the 45° one reaches furthest.</text>')
    return wrap("".join(parts), w, h, "A family of projectile trajectories")


@cached
def component_split(u: float, theta_deg: float, g: float = 9.8) -> str:
    """The same throw drawn as two independent motions, side by side."""
    w, h = 700, 340
    theta = math.radians(theta_deg)
    vx, vy = u * math.cos(theta), u * math.sin(theta)
    t_top = vy / g
    t_flight = 2 * t_top
    peak_h = vy ** 2 / (2 * g)
    range_x = vx * t_flight

    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'TWO MOTIONS, ONE THROW</text>']
    # Left: the horizontal motion, a straight line.
    parts.append(f'<rect x="40" y="46" width="280" height="240" rx="10" fill="#0b1a2c" '
                 f'stroke="#1b3350"/>')
    parts.append(f'<line x1="60" y1="250" x2="300" y2="250" stroke="{MUTED}" stroke-width="2"/>')
    parts.append(f'<text x="180" y="276" text-anchor="middle" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">horizontal: constant {vx:.3g} m s⁻¹</text>')
    for step in range(6):
        parts.append(f'<circle cx="{60 + step * 48}" cy="250" r="7" fill="{CYAN}" '
                     f'opacity="{0.4 + step * 0.12:.2f}"/>')
    parts.append(f'<text x="180" y="76" text-anchor="middle" fill="{CYAN}" font-size="14" '
                 f'font-weight="700">a = 0, so v is constant</text>')

    # Right: the vertical motion, up then down.
    parts.append(f'<rect x="360" y="46" width="300" height="240" rx="10" fill="#0b1a2c" '
                 f'stroke="#1b3350"/>')
    parts.append(f'<line x1="380" y1="250" x2="640" y2="250" stroke="{MUTED}" stroke-width="2"/>')
    points = []
    for step in range(0, 41):
        frac = step / 40.0
        t = t_flight * frac
        y = vy * t - 0.5 * g * t * t
        px = 380 + frac * 260
        py = 250 - (y / max(peak_h, 1e-9)) * 150
        points.append(f"{px:.1f},{py:.1f}")
        if step % 5 == 0:
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="{AMBER}" '
                         f'opacity="{0.5 + frac * 0.5:.2f}"/>')
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{AMBER}" '
                 f'stroke-width="3"/>')
    parts.append(f'<text x="510" y="76" text-anchor="middle" fill="{AMBER}" font-size="14" '
                 f'font-weight="700">a = g downwards</text>')
    parts.append(f'<text x="510" y="276" text-anchor="middle" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">vertical: starts at {vy:.3g}, ends at '
                 f'{-vy:.3g} m s⁻¹</text>')
    parts.append(f'<text x="20" y="{h - 30}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'T = {t_flight:.3g} s · H = {peak_h:.3g} m · R = {range_x:.3g} m · '
                 f'time to apex {t_top:.3g} s</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Nothing about the horizontal motion is '
                 f'affected by the vertical motion. That independence is the whole chapter.</text>')
    return wrap("".join(parts), w, h, "Horizontal and vertical motion drawn separately")


@cached
def rotation_disc(radius: float, omega: float, alpha: float = 0.0) -> str:
    """A rigid disc with marked radii, showing that every point shares ω and α."""
    w, h = 620, 400
    cx, cy = 310, 200
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'EVERY POINT SHARES THE SAME ω AND α</text>']
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{CYAN}" opacity="0.06" '
                 f'stroke="{CYAN}" stroke-width="2.5"/>')
    for index in range(5):
        angle = math.radians(omega * 0.02 + index * 72)
        ex = cx + radius * math.cos(angle)
        ey = cy - radius * math.sin(angle)
        vx = radius * omega
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" '
                     f'stroke="{MUTED}" stroke-width="1.2" stroke-dasharray="3 3"/>')
        parts.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="6" fill="{AMBER}"/>')
        parts.append(f'<text x="{ex + 10:.1f}" y="{ey - 8:.1f}" fill="{AMBER}" font-size="11" '
                     f'font-family="JetBrains Mono, monospace">v={vx:.3g}</text>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{MUTED}"/>')
    # Arrow showing the sense of rotation.
    arc_r = radius * 0.55
    parts.append(f'<path d="M {cx:.0f} {cy - arc_r:.0f} A {arc_r:.0f} {arc_r:.0f} 0 1 1 '
                 f'{cx - arc_r:.0f} {cy:.0f}" fill="none" stroke="{GREEN}" stroke-width="3"/>')
    parts.append(f'<polygon points="{cx - arc_r:.0f},{cy:.0f} {cx - arc_r + 10:.0f},'
                 f'{cy - 7:.0f} {cx - arc_r + 10:.0f},{cy + 7:.0f}" fill="{GREEN}"/>')
    # Anchored to the right of the disc this ran into the quantity column at
    # x=450 once the radius grew - at r=150 the text started at x=406 and ran
    # past 500. Above the arc there is nothing to collide with.
    parts.append(f'<text x="{cx:.0f}" y="{cy - arc_r - 12:.0f}" fill="{GREEN}" '
                 f'text-anchor="middle" font-size="13" font-weight="700" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'ω = {omega:.3g} rad s⁻¹</text>')
    rows = [
        ("r", f"{radius:g} m", CYAN),
        ("v = rω", f"{radius * omega:.3g} m s⁻¹", AMBER),
        ("a_t = rα", f"{radius * alpha:.3g} m s⁻²", VIOLET),
        ("a_c = ω²r", f"{omega ** 2 * radius:.3g} m s⁻²", ROSE),
    ]
    for index, (label, value, colour) in enumerate(rows):
        y = 54 + index * 34
        parts.append(f'<text x="450" y="{y}" fill="{MUTED}" font-size="11" '
                     f'font-family="JetBrains Mono, monospace">{label}</text>'
                     f'<text x="530" y="{y}" fill="{colour}" font-size="13" '
                     f'font-family="JetBrains Mono, monospace">{value}</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The tangential and centripetal '
                 f'accelerations are at right angles, so the total is '
                 f'√((rα)² + (ω²r)²).</text>')
    return wrap("".join(parts), w, h, "A rotating disc with marked radii")


@cached
def centripetal_circle(speed: float, radius: float, mass: float = 1.0) -> str:
    """A body on a circle with its velocity and centripetal acceleration drawn."""
    w, h = 600, 420
    cx, cy, r = 300, 200, 150
    a_c = speed * speed / radius if radius else float("inf")
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'CONSTANT SPEED, TURNING DIRECTION</text>',
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1b3350" '
             f'stroke-width="2"/>',
             f'<line x1="{cx - r - 20}" y1="{cy}" x2="{cx + r + 20}" y2="{cy}" '
             f'stroke="#18304b" stroke-width="1"/>',
             f'<line x1="{cx}" y1="{cy - r - 20}" x2="{cx}" y2="{cy + r + 20}" '
             f'stroke="#18304b" stroke-width="1"/>']
    body = (cx + r, cy)
    parts.append(f'<circle cx="{body[0]}" cy="{body[1]}" r="10" fill="{AMBER}"/>')
    parts.append(f'<text x="{body[0] + 16}" y="{body[1] - 8}" fill="{AMBER}" font-size="13" '
                 f'font-weight="700">m = {mass:g} kg</text>')
    # Velocity is tangential.
    parts.append(f'<line x1="{body[0]}" y1="{body[1]}" x2="{body[0]}" y2="{body[1] - 80}" '
                 f'stroke="{CYAN}" stroke-width="3.5"/>')
    parts.append(f'<polygon points="{body[0]},{body[1] - 88} {body[0] - 6},'
                 f'{body[1] - 76} {body[0] + 6},{body[1] - 76}" fill="{CYAN}"/>')
    parts.append(f'<text x="{body[0] + 12}" y="{body[1] - 92}" fill="{CYAN}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">v = {speed:g} m s⁻¹</text>')
    # Acceleration is radial.
    parts.append(f'<line x1="{body[0]}" y1="{body[1]}" x2="{cx}" y2="{cy}" '
                 f'stroke="{ROSE}" stroke-width="3.5"/>')
    parts.append(f'<polygon points="{cx + 12},{cy} {cx + 24},{cy - 7} {cx + 24},{cy + 7}" '
                 f'fill="{ROSE}"/>')
    parts.append(f'<text x="{body[0] - 70}" y="{body[1] + 30}" fill="{ROSE}" font-size="12" '
                 f'font-family="JetBrains Mono, monospace">a = {a_c:.3g} m s⁻²</text>')
    parts.append(f'<text x="{cx - 26}" y="{cy - 10}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">r = {radius:g}</text>')
    parts.append(f'<text x="460" y="60" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">v ⊥ a, always</text>'
                 f'<text x="460" y="82" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">so W = Fd cos 90° = 0</text>')
    parts.append(f'<text x="460" y="116" fill="{VIOLET}" font-size="13" '
                 f'font-family="JetBrains Mono, monospace">F = {mass * a_c:.3g} N</text>')
    parts.append(f'<text x="20" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">The speed never changes, but the direction of '
                 f'the velocity does — and that alone is an acceleration, directed to the centre.</text>')
    return wrap("".join(parts), w, h, "Centripetal acceleration on a circular path")


@cached
def centrifuge_tube(omega: float, radius: float, samples) -> str:
    """A centrifuge tube with particles sorting outwards by density."""
    w, h = 620, 330
    cx, cy = 300, 150
    span = 180.0
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'ω = {omega:g} rad s⁻¹ — heavier particles travel further out</text>']
    for index in range(3):
        y = cy - 60 + index * 60
        parts.append(f'<rect x="{cx - span}" y="{y - 16}" width="{2 * span}" height="32" rx="16" '
                     f'fill="#0b1a2c" stroke="#1b3350"/>')
    colours = {"light": CYAN, "medium": AMBER, "dense": ROSE}
    for name, target in samples:
        colour = colours[target["kind"]]
        fraction = min(1.0, target["ratio"])
        for slot in range(int(round(fraction * 8))):
            slot_from = 8 - 1 - slot
            row = {"light": 0, "medium": 1, "dense": 2}[target["kind"]]
            y = cy - 60 + row * 60
            x = cx + span - 14 - slot_from * 22
            parts.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{colour}" '
                         f'opacity="{0.45 + 0.55 * fraction:.2f}"/>')
    parts.append(f'<text x="{cx - span}" y="{cy - 90}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">axis</text>')
    parts.append(f'<text x="{cx + span - 50}" y="{cy - 90}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">outer wall</text>')
    for index, (label, target) in enumerate(samples):
        colour = colours[target["kind"]]
        parts.append(f'<circle cx="{60 + index * 150}" cy="{cy + 120}" r="9" fill="{colour}"/>')
        parts.append(f'<text x="{78 + index * 150}" y="{cy + 124}" fill="#c6d6ea" font-size="11" '
                     f'font-family="Sora, sans-serif">{label}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Every particle needs the same a = ω²r, and '
                 f'heavier particles need more force — so only a larger r will do.</text>')
    return wrap("".join(parts), w, h, "Particles separating in a centrifuge")


@cached
def weightless_orbit(altitude_km: float) -> str:
    """The Earth, an orbit, and the fraction of surface gravity still present."""
    w, h = 660, 380
    cx, cy, r_earth = 250, 190, 90.0
    radius = r_earth * (1.0 + altitude_km / 6371.0)
    fraction = (1.0 / (1.0 + altitude_km / 6371.0)) ** 2
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'ALTITUDE {altitude_km:.4g} km</text>',
             f'<circle cx="{cx}" cy="{cy}" r="{r_earth}" fill="{CYAN}" opacity="0.35"/>',
             f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{AMBER}" '
             f'stroke-width="2" stroke-dasharray="6 4"/>']
    sat = (cx + radius, cy)
    parts.append(f'<rect x="{sat[0] - 10}" y="{sat[1] - 6}" width="20" height="12" rx="2" '
                 f'fill="{GREEN}"/>')
    parts.append(f'<text x="{sat[0] + 16}" y="{sat[1] + 4}" fill="{GREEN}" font-size="12" '
                 f'font-weight="700">satellite + astronaut</text>')
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{sat[0]}" y2="{sat[1]}" stroke="{ROSE}" '
                 f'stroke-width="2" stroke-dasharray="4 3"/>')
    parts.append(f'<text x="{cx + 30}" y="{cy + 40}" fill="{ROSE}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">gravity, {fraction * 100:.1f}% '
                 f'of surface</text>')
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r_earth - 6}" y2="{cy}" '
                 f'stroke="{VIOLET}" stroke-width="2.5"/>')
    parts.append(f'<text x="{cx + r_earth + 10}" y="{cy + 4}" fill="{VIOLET}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">g = 9.8</text>')
    parts.append(f'<rect x="470" y="56" width="176" height="180" rx="10" fill="#0d1c30" '
                 f'stroke="{AMBER}" stroke-opacity="0.45"/>'
                 f'<text x="486" y="82" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">WHAT THE ASTRONAUT FEELS</text>'
                 f'<text x="486" y="112" fill="{AMBER}" font-size="15" font-weight="700">'
                 f'weightlessness</text>'
                 f'<text x="486" y="136" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">because both are falling</text>'
                 f'<text x="486" y="152" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">together at the same rate,</text>'
                 f'<text x="486" y="168" fill="#c6d6ea" font-size="11" '
                 f'font-family="Sora, sans-serif">so the floor never pushes up</text>'
                 f'<text x="486" y="198" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">g = {fraction * 9.8:.3g} m s⁻² '
                 f'here</text>'
                 f'<text x="486" y="220" fill="{MUTED}" font-size="10" '
                 f'font-family="Sora, sans-serif">not zero — just unsupported</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Weightlessness is free fall, not an absence of '
                 f'gravity. At the space station&apos;s height gravity is still about 90 % of '
                 f'surface value.</text>')
    return wrap("".join(parts), w, h, "Orbit and apparent weightlessness")


@cached
def inertia_shapes(rows) -> str:
    """Every shape in the syllabus, drawn with its mass where it really sits."""
    w, h = 700, 330
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'SAME MASS, SAME RADIUS — VERY DIFFERENT INERTIA</text>']
    highest = max(r["coefficient"][0] / r["coefficient"][1] for r in rows)
    panel_w, panel_h = 108, 180
    top = 46
    for index, row in enumerate(rows):
        x0 = 26 + index * (panel_w + 8)
        fraction = (row["coefficient"][0] / row["coefficient"][1]) / highest
        colour = [CYAN, AMBER, GREEN, VIOLET, ROSE, TEAL][index % 6]
        cx, cy = x0 + panel_w / 2, top + panel_h / 2
        r = panel_w / 2 - 14
        body = row["body"]
        if body == "ring":
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{colour}" '
                         f'stroke-width="9"/>')
            for step in range(12):
                a = step * 30
                parts.append(f'<circle cx="{cx + r * math.cos(math.radians(a)):.1f}" '
                             f'cy="{cy + r * math.sin(math.radians(a)):.1f}" r="4" '
                             f'fill="{colour}"/>')
        elif body == "shell":
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colour}" '
                         f'opacity="0.08" stroke="{colour}" stroke-width="2"/>')
            for step in range(10):
                a = step * 36
                parts.append(f'<circle cx="{cx + r * math.cos(math.radians(a)):.1f}" '
                             f'cy="{cy + r * math.sin(math.radians(a)):.1f}" r="4" '
                             f'fill="{colour}"/>')
        elif body == "disc":
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colour}" opacity="0.25" '
                         f'stroke="{colour}" stroke-width="1.5"/>')
            for ring_r, count in ((r * 0.33, 5), (r * 0.66, 8), (r * 0.97, 11)):
                for step in range(count):
                    a = step * (360 / count)
                    parts.append(f'<circle cx="{cx + ring_r * math.cos(math.radians(a)):.1f}" '
                                 f'cy="{cy + ring_r * math.sin(math.radians(a)):.1f}" r="3.4" '
                                 f'fill="{colour}" opacity="0.8"/>')
        elif body == "sphere":
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{colour}" opacity="0.16" '
                         f'stroke="{colour}" stroke-width="1.5"/>')
            for ring_r, count in ((r * 0.3, 4), (r * 0.6, 7), (r * 0.92, 10)):
                for step in range(count):
                    a = step * (360 / count)
                    parts.append(f'<circle cx="{cx + ring_r * math.cos(math.radians(a)):.1f}" '
                                 f'cy="{cy + ring_r * math.sin(math.radians(a)):.1f}" r="3.2" '
                                 f'fill="{colour}" opacity="0.7"/>')
        elif body == "semi":
            parts.append(f'<path d="M {cx - r} {cy} A {r} {r} 0 0 1 {cx + r} {cy} Z" '
                         f'fill="{colour}" opacity="0.25" stroke="{colour}" stroke-width="1.5"/>')
            for ring_r, count in ((r * 0.35, 3), (r * 0.7, 5), (r * 0.95, 7)):
                for step in range(count):
                    a = math.radians(step * (150 / max(count - 1, 1)))
                    parts.append(f'<circle cx="{cx + ring_r * math.cos(a):.1f}" '
                                 f'cy="{cy - ring_r * math.sin(a):.1f}" r="3.2" '
                                 f'fill="{colour}" opacity="0.8"/>')
        elif body == "rod":
            parts.append(f'<rect x="{cx - r}" y="{cy - 5}" width="{2 * r}" height="10" rx="5" '
                         f'fill="{colour}" opacity="0.5"/>')
            for step in range(7):
                parts.append(f'<circle cx="{cx - r + step * (2 * r / 6):.1f}" cy="{cy}" r="4" '
                             f'fill="{colour}"/>')
        parts.append(f'<rect x="{x0}" y="{top}" width="{panel_w}" height="{panel_h}" rx="8" '
                     f'fill="none" stroke="#1b3350"/>')
        parts.append(f'<text x="{cx}" y="{top + panel_h + 18}" text-anchor="middle" '
                     f'fill="{colour}" font-size="11" font-family="JetBrains Mono, monospace">'
                     f'{row["coefficient"][0]}/{row["coefficient"][1]} = {fraction:.3g}</text>')
        parts.append(f'<text x="{cx}" y="{top + panel_h + 34}" text-anchor="middle" '
                     f'fill="{MUTED}" font-size="9" font-family="Sora, sans-serif">'
                     f'I / (MR²)</text>')
    parts.append(f'<text x="20" y="{h - 26}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Dots show where the mass actually is. The '
                 f'bigger the share of dots at large r, the harder the body is to spin up.</text>')
    parts.append(f'<text x="20" y="{h - 10}" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'ring 1 &gt; hollow sphere 0.667 &gt; disc 0.5 &gt; sphere 0.4 &gt; '
                 f'semi-disc 0.125</text>')
    return wrap("".join(parts), w, h, "Moments of inertia of standard shapes")


@cached
def skater_spin(i_before: float, omega_before: float, i_after: float) -> str:
    """A skater pulling in her arms, with the two spin rates and energies shown."""
    w, h = 640, 340
    cx, cy = 250, 170
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'PULLING IN THE ARMS</text>']
    for index, (radius, colour, label, omega) in enumerate([
            (i_before / omega_before, CYAN, "before", omega_before),
            (i_after, GREEN, "after", i_before * omega_before / i_after)]):
        rr = min(110.0, 20.0 + i_before / omega_before * 6.0 if index == 0 else 62.0)
        x0 = cx - 140 + index * 300
        parts.append(f'<circle cx="{x0}" cy="{cy}" r="{rr:.1f}" fill="none" stroke="{colour}" '
                     f'stroke-width="2" stroke-dasharray="4 4"/>')
        points = []
        for step in range(9):
            a = math.radians(step * 40 + omega * 4)
            points.append((x0 + rr * math.cos(a), cy + rr * math.sin(a)))
        for (ax, ay) in points:
            parts.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="6" fill="{colour}"/>')
        parts.append(f'<circle cx="{x0}" cy="{cy}" r="9" fill="{AMBER}"/>')
        for side in (1, -1):
            parts.append(f'<line x1="{x0 + 22 * side}" y1="{cy}" x2="{x0 + 46 * side}" '
                         f'y2="{cy}" stroke="{colour}" stroke-width="3"/>')
        parts.append(f'<text x="{x0}" y="{cy + rr + 40:.0f}" text-anchor="middle" '
                     f'fill="{colour}" font-size="13" font-weight="700">{label}</text>')
        parts.append(f'<text x="{x0}" y="{cy + rr + 58:.0f}" text-anchor="middle" '
                     f'fill="{MUTED}" font-size="11" font-family="JetBrains Mono, monospace">'
                     f'ω = {omega:.4g} rad s⁻¹</text>')
    k_before = 0.5 * i_before * omega_before ** 2
    k_after = 0.5 * i_after * (i_before * omega_before / i_after) ** 2
    parts.append(f'<rect x="470" y="60" width="156" height="140" rx="10" fill="#0d1c30" '
                 f'stroke="{VIOLET}" stroke-opacity="0.45"/>'
                 f'<text x="486" y="84" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">CONSERVED</text>'
                 f'<text x="486" y="106" fill="{VIOLET}" font-size="14" font-weight="700">'
                 f'I ω = {i_before * omega_before:.4g}</text>'
                 f'<text x="486" y="136" fill="{MUTED}" font-size="10" '
                 f'font-family="JetBrains Mono, monospace">ENERGY (NOT CONSERVED)</text>'
                 f'<text x="486" y="158" fill="{AMBER}" font-size="14" font-weight="700">'
                 f'{k_before:.3g} → {k_after:.3g} J</text>'
                 f'<text x="486" y="180" fill="{GREEN}" font-size="11" '
                 f'font-family="Sora, sans-serif">×{k_after / k_before:.3g}</text>')
    parts.append(f'<text x="20" y="{h - 12}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">Angular momentum is conserved; the extra '
                 f'kinetic energy came from the skater&apos;s own muscles.</text>')
    return wrap("".join(parts), w, h, "A skater pulling in her arms")


@cached
def angular_dials(theta: float, omega: float, alpha: float) -> str:
    """Angle, angular velocity and angular acceleration, shown together."""
    w, h = 680, 250
    parts = [f'<text x="20" y="24" fill="{MUTED}" font-size="12" '
             f'font-family="JetBrains Mono, monospace" letter-spacing="2">'
             f'THE THREE ANGULAR QUANTITIES</text>']
    rows = [("θ", math.degrees(theta), "rad", f"{theta:.4g} rad", CYAN),
            ("ω", omega, "rad s⁻¹", f"{omega:.4g} rad s⁻¹", AMBER),
            ("α", alpha, "rad s⁻²", f"{alpha:.4g} rad s⁻²", GREEN)]
    for index, (symbol, value, unit, text, colour) in enumerate(rows):
        y = 60 + index * 50
        parts.append(f'<rect x="30" y="{y - 26}" width="300" height="40" rx="8" '
                     f'fill="#0d1c30" stroke="{colour}" stroke-opacity="0.4"/>'
                     f'<text x="48" y="{y}" fill="{colour}" font-size="20" '
                     f'font-weight="700" font-family="JetBrains Mono, monospace">{symbol}</text>'
                     f'<text x="86" y="{y}" fill="#eef6ff" font-size="14" '
                     f'font-family="JetBrains Mono, monospace">{text}</text>'
                     f'<text x="346" y="{y}" fill="{MUTED}" font-size="12" '
                     f'font-family="Sora, sans-serif">{symbol} = d{symbol}/dt</text>')
    parts.append(f'<text x="30" y="80" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">θ in radians:</text>')
    parts.append(f'<text x="30" y="98" fill="{MUTED}" font-size="11" '
                 f'font-family="JetBrains Mono, monospace">'
                 f'θ(deg) × π/180 = {math.degrees(theta):.4g}° = {theta:.4g} rad</text>')
    parts.append(f'<text x="30" y="{h - 14}" fill="{MUTED}" font-size="11" '
                 f'font-family="Sora, sans-serif">One radian is the angle subtended by an arc '
                 f'whose length equals the radius, which is why 2π rad is one full turn.</text>')
    return wrap("".join(parts), w, h, "Angular displacement, velocity and acceleration")