"""Chapter 3 tutor: equations of motion, momentum, work and energy."""

from __future__ import annotations

import math

from ..core import motion1d as M

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["equations of motion", "what are the three equations", "kinematic equations",
              "v = u + at", "s = ut", "uniform acceleration"],
     "title": "The three equations of motion",
     "answer": (
         "For a body with **constant** acceleration along a straight line:\n\n"
         "1. **v = u + at** — velocity after time t\n"
         "2. **s = ut + ½at²** — displacement after time t\n"
         "3. **v² = u² + 2as** — velocity after displacement s\n\n"
         "Pick the one that does **not** contain the quantity you do not know. No v? "
         "Use the second. No t? Use the third."),
     "slo": "3.1.1"},
    {"keys": ["free fall", "falling object", "dropped from", "thrown upward",
              "why does a ball come back down"],
     "title": "Free fall",
     "answer": (
         "Near the Earth's surface, a body in free fall has **a = g = 9.8 m s⁻² "
         "downward**, whatever its mass.\n\n"
         "Upwards positive, that is a = −9.8. A ball at the top of its flight has "
         "**v = 0 but a = −9.8** — zero velocity is not the same as 'not falling'.\n\n"
         "Useful shortcuts, from rest: t = √(2L/g) and v = √(2gL)."),
     "slo": "3.1.2"},
    {"keys": ["conservation of momentum", "law of conservation of momentum",
              "what is momentum", "p equals m v"],
     "title": "Conservation of linear momentum",
     "answer": (
         "**p = m v**, a vector, measured in kg m s⁻¹.\n\n"
         "**The law:** if no resultant external force acts on a system, the total momentum "
         "of that system is constant. Not approximately — exactly.\n\n"
         "The law does **not** say kinetic energy is conserved. That is a separate question "
         "and the answer is usually no."),
     "slo": "3.2.1"},
    {"keys": ["elastic collision", "inelastic collision", "difference between elastic",
              "perfectly inelastic"],
     "title": "Elastic and inelastic collisions",
     "answer": (
         "**Elastic:** momentum *and* kinetic energy are both conserved. It rings, and "
         "springs back.\n"
         "* **Inelastic:** only momentum. Kinetic energy falls and becomes heat, sound and "
         "permanent deformation.\n"
         "* **Perfectly inelastic:** the bodies stick together and move off at one shared "
         "velocity.\n\n"
         "Momentum is conserved in **all three**. That is the constant."),
     "slo": "3.2.3"},
    {"keys": ["elastic collision formula", "final velocity after collision",
              "swap velocities", "equal masses collide"],
     "title": "Elastic collision formulas",
     "answer": (
         "* **v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁ + m₂)**\n"
         "* **v₂ = (2m₁u₁ + (m₂−m₁)u₂) / (m₁ + m₂)**\n\n"
         "The special case everyone should know: **if the masses are equal, they simply "
         "swap velocities**. That is why identical pool balls look as though they pass "
         "through one another."),
     "slo": "3.2.4"},
    {"keys": ["oblique collision", "two dimensional collision", "line of centres",
              "collision at an angle"],
     "title": "Collisions in two dimensions",
     "answer": (
         "For smooth spheres the contact force acts **only along the line joining the "
         "centres at the moment of impact**.\n\n"
         "* **Along** that line: apply the one-dimensional elastic or inelastic result.\n"
         "* **Across** it: nothing happens — those components are completely unchanged.\n\n"
         "So split both velocities along and across the line first, do the 1-D problem, then "
         "put the pieces back together. Splitting later is the classic wrong answer."),
     "slo": "3.2.5"},
    {"keys": ["work done", "what is work", "work is the dot product", "f d cos"],
     "title": "Work",
     "answer": (
         "**W = F · d = F d cos θ**, measured in joules (newton-metres).\n\n"
         "* θ = 0° → maximum **positive** work; the force drives the motion\n"
         "* θ = 90° → **zero**; the force only turns the path (this is why a satellite does "
         "no work)\n"
         "* θ = 180° → maximum **negative** work; the force brakes the motion\n\n"
         "Work is a **scalar** even though F and d are vectors."),
     "slo": "3.3.1"},
    {"keys": ["area under graph", "force displacement graph", "f d graph",
              "work from a graph"],
     "title": "Work from a force–displacement graph",
     "answer": (
         "**The work done is the area under the F–d curve**, found by the trapezium rule: "
         "W = ½(F₁ + F₂)d.\n\n"
         "* constant force → rectangle, Fd\n"
         "* Hooke's-law spring → triangle, ½kx²\n"
         "* curve below the axis → **negative** area; energy is being removed\n"
         "* curve crossing the axis → take the signed sum, so parts cancel"),
     "slo": "3.3.2"},
    {"keys": ["conservative force", "non conservative", "conservative field",
              "path independent"],
     "title": "Conservative and non-conservative fields",
     "answer": (
         "**Conservative:** the work between two points does **not** depend on the route, "
         "and the net work round any closed loop is zero. The energy is stored in a "
         "potential and can be recovered. Gravity, electrostatics, springs.\n\n"
         "**Non-conservative:** the work **does** depend on the path, because energy is "
         "dissipated along the way. Friction, air resistance, drag.\n\n"
         "Test it: slide a box across a table the long way round and the short way. Friction "
         "charges you more for the longer route; gravity does not."),
     "slo": "3.4.1"},
    {"keys": ["work energy theorem", "w equals delta k", "work energy relationship",
              "net work"],
     "title": "The work-energy theorem",
     "answer": (
         "**W = ΔK = ½mv² − ½mu²**\n\n"
         "The **net** work done on a body equals its change in kinetic energy. It holds "
         "whether or not friction is present — friction simply contributes a negative term, "
         "which is why a sliding body ends up with less kinetic energy than it started with.\n\n"
         "Note that the mass often cancels out, which is a useful hint that this is the "
         "quickest route."),
     "slo": "3.5.1"},
    {"keys": ["karate chop", "car crash", "bat and ball", "rocket", "momentum examples",
              "real life momentum"],
     "title": "Momentum in the real world",
     "answer": (
         "**Karate chop:** a slow heavy hand and a fast light hand can carry the same "
         "momentum. What breaks the board is the *rate of change* — the force — over a very "
         "short time.\n"
         "**Car crash:** the combined wreck moves more slowly than either car did; the "
         "missing kinetic energy is heat, noise and bent metal.\n"
         "**Bat and ball:** the bat does not create energy, it transfers momentum. A heavy "
         "bat losing a little speed gives the light ball a large speed gain.\n"
         "**Rocket:** include the exhaust in the system. The gases go backwards, the rocket "
         "goes forwards, and the total stays zero."),
     "slo": "3.2.2"},
]


def _kinematics(u, a, t):
    return (f"**u = {float(u):g} m s⁻¹, a = {float(a):g} m s⁻², t = {float(t):g} s**\n\n"
            f"* v = u + at = {float(u) + float(a) * float(t):.4g} m s⁻¹\n"
            f"* s = ut + ½at² = {M.displacement(float(u), float(a), float(t)):.4g} m\n\n"
            f"The same result from the third equation: v² = {float(u) ** 2 + 2 * float(a) * M.displacement(float(u), float(a), float(t)):.4g}")


def _freecall(height, u):
    result = M.free_fall(float(height), float(u))
    return (f"**Dropped from {float(height):g} m at {float(u):g} m s⁻¹ (g = 9.8)**\n\n"
            f"* time of fall = {result['t']:.4g} s\n"
            f"* speed at the bottom = {abs(result['impact_speed']):.4g} m s⁻¹\n\n"
            f"From v² = u² + 2gs: v² = {float(u) ** 2:.4g} + 2(9.8)({float(height):g}) = "
            f"{float(u) ** 2 + 2 * 9.8 * float(height):.4g}")


def _momentum(masses, velocities):
    parts = [f"* {m:g} × {v:g} = {m * v:.4g}" for m, v in zip(
        [float(x) for x in masses.split(",")], [float(x) for x in velocities.split(",")])]
    total = M.total_momentum([float(x) for x in masses.split(",")],
                             [float(x) for x in velocities.split(",")])
    return ("**Total momentum**\n\n" + "\n".join(parts) +
            f"\n\nTotal = **{total:.4g} kg m s⁻¹**. In an isolated system this is the same "
            f"before and after, whatever happens in between.")


def _elastic(m1, u1, m2, u2):
    result = M.elastic_collision_1d(float(m1), float(u1), float(m2), float(u2))
    return (f"**Elastic collision: {float(m1):g} kg at {float(u1):g} m s⁻¹ hits "
            f"{float(m2):g} kg at {float(u2):g} m s⁻¹**\n\n"
            f"* v₁ = **{result['v1']:.4g} m s⁻¹**\n"
            f"* v₂ = **{result['v2']:.4g} m s⁻¹**\n\n"
            f"Momentum: {result['momentum_before']:.4g} → {result['momentum_after']:.4g} "
            f"({'conserved' if result['momentum_conserved'] else 'NOT conserved'})\n"
            f"Kinetic energy: {result['kinetic_before']:.4g} J → "
            f"{result['kinetic_after']:.4g} J "
            f"({'conserved' if result['kinetic_conserved'] else 'NOT conserved'})")


def _inelastic(m1, u1, m2, u2):
    result = M.inelastic_collision_1d(float(m1), float(u1), float(m2), float(u2))
    return (f"**Perfectly inelastic collision**\n\n"
            f"* shared velocity = **{result['v1']:.4g} m s⁻¹**\n"
            f"* momentum {result['momentum_before']:.4g} → {result['momentum_after']:.4g} "
            f"({'conserved' if result['momentum_conserved'] else 'NOT conserved'})\n"
            f"* kinetic energy {result['kinetic_before']:.4g} J → "
            f"{result['kinetic_after']:.4g} J, so **{result['kinetic_lost']:.4g} J lost**\n\n"
            f"That missing energy has become heat, sound and deformation. It has not been "
            f"destroyed — it has simply become unrecoverable.")


def _work(force, distance, angle):
    value = float(force) * float(distance) * math.cos(math.radians(float(angle)))
    return (f"**W = {value:.4g} J**\n\n"
            f"W = F d cos θ = {float(force):g} × {float(distance):g} × "
            f"cos {float(angle):g}° = {value:.4g} J\n\n"
            f"{'Positive — the force has a component along the motion.' if value > 0 else ('Negative — the force opposes the motion.' if value < 0 else 'Zero — the force is perpendicular to the motion.')}")


CALCULATORS = [
    {"pattern": r"u\s*=\s*([\d.]+)[,\s]+a\s*=\s*([\d.]+)[,\s]+t\s*=\s*([\d.]+)", "reply": _kinematics},
    {"pattern": r"u\s*([\d.]+)\s*a\s*([\d.]+)\s*t\s*([\d.]+)", "reply": _kinematics},
    {"pattern": r"(?:drop|dropped|fall|falls|falls from|throw)\D*?([\d.]+)\s*m\D*?"
                r"(?:at|from|with)?\s*([\d.]+)?", "reply": _freecall},
    {"pattern": r"momentum\s+of\s+([\d.,\s]+)\s+(?:kg\s+)?(?:at|moving at)\s+([\d.,\s-]+)",
     "reply": _momentum},
    {"pattern": r"elastic\s+collision\D*?([\d.]+)\s*(?:kg)?\s*(?:at|moving at)\s*([\d.]+)\s*"
                r"\D*?([\d.]+)\s*(?:kg)?\s*(?:at|moving at)\s*([\d.]+)", "reply": _elastic},
    {"pattern": r"(?:inelastic|sticky)\s+collision\D*?([\d.]+)\s*(?:kg)?\s*(?:at|moving at)\s*"
                r"([\d.]+)\s*\D*?([\d.]+)\s*(?:kg)?\s*(?:at|moving at)\s*([\d.]+)",
     "reply": _inelastic},
    {"pattern": r"work\s*=\s*([\d.]+)\s*\*\s*([\d.]+)\s*\*\s*cos\s*([\d.]+)", "reply": _work},
    {"pattern": r"work\s+done.*?([\d.]+)\s*N.*?([\d.]+)\s*m.*?([\d.]+)\s*(?:deg|degrees|°)?"
                r".*", "reply": _work},
]
