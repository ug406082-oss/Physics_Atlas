"""Chapter 2 tutor: what the vector sandpit and the product dials can tell you.

The tutor answers from this chapter's own content and from the same
:mod:`physics.core.vectors` functions the interactive stations use, so a spoken
answer and a plotted answer can never disagree.
"""

from __future__ import annotations

import math

from ..core import vectors as V

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["scalar vs vector", "difference between scalar and vector",
              "what is a scalar", "what is a vector", "scalar or vector",
              "scalar and vector"],
     "title": "Scalar or vector?",
     "answer": (
         "A **scalar** has size only. Mass, time, temperature, speed, energy and "
         "density are scalars: 5 kg of rice is 5 kg of rice wherever it is.\n\n"
         "A **vector** has size *and* direction. Displacement, velocity, "
         "acceleration, force, momentum, weight and torque are vectors: 60 km/h "
         "north and 60 km/h east are genuinely different situations.\n\n"
         "The test is simple — if the direction changes what is being described, it "
         "is a vector."),
     "slo": "2.1.1"},
    {"keys": ["speed and velocity difference", "is speed a vector",
              "velocity vs speed"],
     "title": "Speed and velocity",
     "answer": (
         "**Speed** is a scalar — how fast, with no direction. **Velocity** is a "
         "vector — how fast *and which way*.\n\n"
         "This matters when something turns. A car going round a circular track at a "
         "steady 20 m/s has a constant *speed* but a constantly changing "
         "*velocity*, because the direction is turning. That change of direction is "
         "an acceleration, even though the speedometer needle is steady — which is "
         "exactly why Chapter 4 has a special name for it: centripetal acceleration."),
     "slo": "2.1.1"},
    {"keys": ["rectangular component", "resolve a vector", "components of a vector",
              "how do i add two vectors", "component method", "vector addition"],
     "title": "Rectangular components",
     "answer": (
         "Break each vector into x and y parts, add like with like, then rebuild.\n\n"
         "* Ax = A cos θ (along x)\n"
         "* Ay = A sin θ (along y)\n"
         "* R = √(Rx² + Ry²) where Rx = Ax + Bx and Ry = Ay + By\n\n"
         "You cannot add two vectors by adding their sizes — but you *can* add their "
         "components, because components are signed numbers."),
     "slo": "2.2.1"},
    {"keys": ["add two vectors", "resultant", "parallelogram rule",
              "head to tail"],
     "title": "Adding two vectors",
     "answer": (
         "**Head-to-tail** (triangle rule): draw A, then draw B starting where A "
         "finished. The straight line from the start to the end is the resultant.\n\n"
         "**Parallelogram rule**: draw A and B from the same origin, complete the "
         "parallelogram. The diagonal from the origin is the same resultant.\n\n"
         "The order never matters — A + B and B + A give the same answer. What does "
         "matter is the angle between them: at 0° the resultant is A + B, at 180° it "
         "is |A − B|, and at 90° it is √(A² + B²)."),
     "slo": "2.2.1"},
    {"keys": ["scalar product", "dot product", "a dot b", "vector dot product"],
     "title": "The scalar (dot) product",
     "answer": (
         "**A · B = A B cos θ**\n\n"
         "The answer is a plain number, not a vector. It is the length of the shadow "
         "that B casts on the direction of A, taken with a sign.\n\n"
         "* positive — the angle is acute, the two point broadly the same way\n"
         "* zero — θ = 90°, they are perpendicular\n"
         "* negative — the angle is obtuse, they oppose\n\n"
         "It is **commutative**: A · B = B · A. The physics use is work, "
         "W = F · d."),
     "slo": "2.3.1"},
    {"keys": ["vector product", "cross product", "a cross b", "vector cross product"],
     "title": "The vector (cross) product",
     "answer": (
         "**|A × B| = A B sin θ**, directed perpendicular to both A and B.\n\n"
         "The magnitude is the **area of the parallelogram** the two vectors enclose. "
         "The direction comes from the right-hand rule: curl your fingers from A to B "
         "and your thumb points along A × B.\n\n"
         "* zero — the vectors are parallel (θ = 0° or 180°)\n"
         "* largest — the vectors are perpendicular\n\n"
         "It is **anti-commutative**: A × B = −(B × A). The physics use is torque, "
         "τ = r × F."),
     "slo": "2.4.1"},
    {"keys": ["right hand rule", "which way does the cross product point"],
     "title": "The right-hand rule",
     "answer": (
         "1. Point the fingers of your **right** hand along the first vector.\n"
         "2. Curl them round towards the second vector, through the smaller angle.\n"
         "3. Your thumb points along the cross product.\n\n"
         "On a flat page: if the turn from A to B is anticlockwise the result comes "
         "**out** of the page (⊙); if it is clockwise the result goes **into** the "
         "page (⊗)."),
     "slo": "2.4.1"},
    {"keys": ["difference between dot and cross", "scalar vs vector product",
              "which product do i use"],
     "title": "Dot or cross?",
     "answer": (
         "Decide from the **answer you expect**, not from the inputs.\n\n"
         "* Answer is a **scalar** (a plain number) → use the **dot product**, "
         "which has cos θ. Work, and any projection.\n"
         "* Answer is a **vector** with a direction → use the **cross product**, "
         "which has sin θ. Torque and magnetic force.\n\n"
         "A useful check afterwards: if the unit comes out as N m for a quantity you "
         "expected to be a force, you picked the wrong one."),
     "slo": "2.4.1"},
    {"keys": ["work is a scalar", "work from force and displacement", "wdcos"],
     "title": "Work as a dot product",
     "answer": (
         "**W = F · d = F d cos θ**\n\n"
         "Only the component of the force *along* the displacement does work; the rest "
         "pushes sideways and changes nothing about the energy.\n\n"
         "* cos 0° = +1 — the force drives the motion, maximum positive work\n"
         "* cos 90° = 0 — perpendicular, no work at all\n"
         "* cos 180° = −1 — the force brakes the motion, negative work\n\n"
         "The units are newton-metres, and 1 N m = 1 J."),
     "slo": "2.3.1"},
    {"keys": ["torque formula", "moment of force", "turning effect"],
     "title": "Torque",
     "answer": (
         "**τ = r × F**, so **τ = r F sin θ**, measured in N m.\n\n"
         "θ is the angle between the position vector r and the force F. Only the "
         "component of the force perpendicular to r does the turning.\n\n"
         "Push perpendicular to the lever (θ = 90°) and you get the largest possible "
         "torque. Push *along* the lever (θ = 0°) and the torque is exactly zero — "
         "which is why door hinges belong on the side, and never in the middle."),
     "slo": "2.4.1"},
    {"keys": ["why can't i add vector magnitudes", "why add vectors like that"],
     "title": "Why vectors need components",
     "answer": (
         "Because a magnitude throws away the direction, and the direction is exactly "
         "the information you need to add.\n\n"
         "10 N east + 10 N east = 20 N east, because the two are parallel.\n"
         "10 N east + 10 N north = 14.1 N at 45°, not 20 N.\n\n"
         "The result of adding two vectors of magnitude 5 and 3 can be anything "
         "between 2 and 8, depending only on the angle between them. If you had "
         "kept only the magnitudes, you would have thrown away the one thing that "
         "decided the answer."),
     "slo": "2.2.1"},
]


# --------------------------------------------------------------------------
# Calculators
# --------------------------------------------------------------------------

def _components(value, angle):
    size, degrees = float(value), float(angle)
    x, y = V.components_from_polar(size, degrees)
    return (f"**A = ({x:.4g}, {y:.4g})**\n\n"
            f"|A| = {size:g}, θ = {degrees:g}°\n\n"
            f"* Ax = A cos θ = {x:.4g}\n"
            f"* Ay = A sin θ = {y:.4g}\n"
            f"* check: Ax² + Ay² = {x * x + y * y:.4g} = |A|² ✓")


def _resultant(ma, aa, mb, ab):
    a = V.components_from_polar(float(ma), float(aa))
    b = V.components_from_polar(float(mb), float(ab))
    total = V.add(a, b)
    return (f"**A = {float(ma):g} at {float(aa):g}°, B = {float(mb):g} at {float(ab):g}°**\n\n"
            f"* Ax = {a[0]:.4g}, Ay = {a[1]:.4g}\n"
            f"* Bx = {b[0]:.4g}, By = {b[1]:.4g}\n"
            f"* Rx = {total[0]:.4g}, Ry = {total[1]:.4g}\n"
            f"* **R = {V.magnitude(total):.4g} at {V.angle_of(total):.2f}°**\n\n"
            f"Note that {V.magnitude(total):.4g} is smaller than "
            f"{float(ma) + float(mb):g}, because the two are not in the same direction.")


def _dot(ma, aa, mb, ab):
    a = V.components_from_polar(float(ma), float(aa))
    b = V.components_from_polar(float(mb), float(ab))
    value = V.dot_product(a, b)
    sign = ("positive — the two pull the same way along A" if value > 1e-9
            else "negative — they oppose" if value < -1e-9 else "zero — perpendicular")
    return (f"**A · B = {value:.4g}** ({sign})\n\n"
            f"θ between them = {V.angle_between(a, b):.2f}°\n"
            f"A B cos θ = {float(ma):g} × {float(mb):g} × "
            f"cos {V.angle_between(a, b):.2f}° = {value:.4g}\n\n"
            f"It is a scalar, so it has no direction, and A · B = B · A.")


def _cross(ma, aa, mb, ab):
    a = V.components_from_polar(float(ma), float(aa))
    b = V.components_from_polar(float(mb), float(ab))
    value = V.cross_product(a, b)
    return (f"**|A × B| = {abs(value):.4g}**\n\n"
            f"θ between them = {V.angle_between(a, b):.2f}°\n"
            f"A B sin θ = {float(ma):g} × {float(mb):g} × "
            f"sin {V.angle_between(a, b):.2f}° = {abs(value):.4g}\n\n"
            f"Direction: {V.cross_direction(value)}.\n"
            f"Remember that reversing the order reverses the sign: "
            f"B × A = {V.cross_product(b, a):.4g}.")


def _work(force, distance, angle):
    f, d, degrees = float(force), float(distance), float(angle)
    value = f * d * math.cos(math.radians(degrees))
    verdict = ("energy is being added to the system" if value > 1e-9
               else "energy is being removed" if value < -1e-9
               else "the force is perpendicular, so nothing changes")
    return (f"**W = {value:.4g} J** — {verdict}.\n\n"
            f"W = F d cos θ = {f:g} × {d:g} × cos {degrees:g}° = {value:.4g} J\n\n"
            f"1 N m = 1 J, so the units are joules. Work is a scalar: no direction.")


CALCULATORS = [
    {"pattern": r"resolve\s+([\d.]+)\s*(?:at|@)\s*([\d.]+)\s*(?:deg|degrees|°)?" +
                r".*(?:vector|component)", "reply": _components},
    {"pattern": r"components\s+of\s+(?:a\s+)?vector\s+(?:of\s+)?([\d.]+)\s*(?:at|@)\s*([\d.]+)",
     "reply": _components},
    {"pattern": r"(?:resultant|sum)\s+of\s+([\d.]+)\s*(?:at|@)\s*([\d.]+)\s*(?:deg|degrees|°)?\s*"
                r"(?:and|,)\s*([\d.]+)\s*(?:at|@)\s*([\d.]+)", "reply": _resultant},
    {"pattern": r"(?:add|sum of)\s+(?:vectors\s+)?([\d.]+)\s*(?:at|@)\s*([\d.]+)\s*"
                r"(?:deg|degrees|°)?\s*(?:and|,)\s*([\d.]+)\s*(?:at|@)\s*([\d.]+)",
     "reply": _resultant},
    {"pattern": r"dot\s+product\s+of\s+([\d.]+)\s*(?:at|@)\s*([\d.]+)\s*"
                r"(?:deg|degrees|°)?\s*(?:and|,)\s*([\d.]+)\s*(?:at|@)\s*([\d.]+)",
     "reply": _dot},
    {"pattern": r"cross\s+product\s+of\s+([\d.]+)\s*(?:at|@)\s*([\d.]+)\s*"
                r"(?:deg|degrees|°)?\s*(?:and|,)\s*([\d.]+)\s*(?:at|@)\s*([\d.]+)",
     "reply": _cross},
    {"pattern": r"work\s+done.*?([\d.]+)\s*N.*?([\d.]+)\s*m.*?([\d.]+)\s*(?:deg|degrees|°)?" +
                r".*", "reply": _work},
    {"pattern": r"work\s*=\s*([\d.]+)\s*\*\s*([\d.]+)\s*\*\s*cos\s*([\d.]+)",
     "reply": _work},
]
