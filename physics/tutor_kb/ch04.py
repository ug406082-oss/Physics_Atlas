"""Chapter 4 tutor: projectiles, circular motion and rotation."""

from __future__ import annotations

import math

from ..core import motion2d as M

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["projectile motion", "what is a projectile", "horizontal motion",
              "why does the horizontal speed stay the same"],
     "title": "Projectile motion",
     "answer": (
         "A **projectile** is a body given a velocity and then left alone under gravity "
         "alone.\n\n"
         "* **Horizontally**: no force acts, so the velocity never changes. Not slowed, "
         "not sped — unchanged for the whole flight.\n"
         "* **Vertically**: gravity gives a constant −9.8 m s⁻², so the velocity changes "
         "steadily.\n\n"
         "The two motions are completely independent. Adding them gives the resultant "
         "velocity, but neither part affects the rules of the other."),
     "slo": "4.1.1"},
    {"keys": ["time of flight", "maximum height", "horizontal range", "range formula",
              "projectile formula", "45 degrees"],
     "title": "The four projectile relations",
     "answer": (
         "* **T = 2u sin θ / g** — time of flight (the rise takes half of it)\n"
         "* **H = u² sin²θ / 2g** — maximum height\n"
         "* **R = u² sin 2θ / g** — range. Note **sin 2θ**, not sin θ\n"
         "* **R_max = u² / g at θ = 45°** — sin 2θ cannot exceed 1\n\n"
         "Any two angles adding to 90° give the same range, because sin 60° = sin 120°."),
     "slo": "4.1.2"},
    {"keys": ["air resistance", "effect of drag on projectiles", "drag range",
              "air resistance projectile"],
     "title": "Air resistance and projectiles",
     "answer": (
         "Drag always opposes the velocity, so it can only remove speed:\n\n"
         "* **range is shorter**\n"
         "* **peak height is lower**\n"
         "* **the descent takes longer**, so the flight time increases\n"
         "* **the path is asymmetric** — steeper going down\n"
         "* **the best angle is below 45°**\n\n"
         "The asymmetry arises because near the apex the vertical speed is tiny, so drag "
         "is relatively stronger there and shortens the rise more than the fall."),
     "slo": "4.1.4"},
    {"keys": ["radians", "why radians", "convert degrees to radians", "angular displacement",
              "angular velocity", "angular acceleration"],
     "title": "Angular quantities",
     "answer": (
         "**θ** angular displacement in **radians**, **ω = dθ/dt** angular velocity, "
         "**α = dω/dt** angular acceleration.\n\n"
         "One radian is the angle subtended by an arc whose length equals the radius, which "
         "is why **2π rad is one full turn**.\n\n"
         "Convert with θ(rad) = θ(deg) × π/180. Skipping that conversion is the commonest "
         "error in this chapter."),
     "slo": "4.2.1"},
    {"keys": ["s equals r theta", "linear and angular", "r omega", "relation between linear",
              "v equals r omega"],
     "title": "Linear and angular relations",
     "answer": (
         "* **s = rθ** (θ in radians)\n"
         "* **v = rω**\n"
         "* **a_t = rα**\n\n"
         "These hold exactly for a **rigid** body rotating about a fixed axis — which is why "
         "every point on the rim has the same ω and α but different v."),
     "slo": "4.2.2"},
    {"keys": ["centripetal", "what is centripetal force", "centripetal acceleration",
              "v squared over r"],
     "title": "Centripetal force",
     "answer": (
         "**a_c = v²/r**, directed **towards the centre**.\n"
         "**F_c = mv²/r**, the inward force that supplies it.\n\n"
         "It is needed because a speed alone does not describe uniform circular motion — "
         "the *direction* of the velocity is turning every instant, and a changing velocity "
         "means an acceleration.\n\n"
         "It does **no work**, because the force is perpendicular to the velocity."),
     "slo": "4.3.1"},
    {"keys": ["centrifuge", "how does a centrifuge work", "separating mixture"],
     "title": "The centrifuge",
     "answer": (
         "Every particle in a spinning sample needs the same centripetal acceleration "
         "**a = ω²r**.\n\n"
         "The dense particles have more mass and so need more inward force, but the "
         "available force is the same for everybody. The only way a heavy particle can get "
         "more is by sitting at a **larger radius**, where ω²r is bigger.\n\n"
         "So the dense material ends up packed against the outside wall. That is also why "
         "you must never open a spinning centrifuge."),
     "slo": "4.3.3"},
    {"keys": ["weightless", "why are astronauts weightless", "zero gravity",
              "weightlessness in orbit", "free fall"],
     "title": "Weightlessness",
     "answer": (
         "An astronaut in orbit is **weightless because everything is falling together**, "
         "not because gravity is absent.\n\n"
         "The spacecraft and the astronaut both accelerate at the same rate, so the floor "
         "never has to push up on the astronaut — and 'weight' means exactly that push.\n\n"
         "At the space station's altitude gravity is still about **90 %** of its surface "
         "value. What is missing is the supporting force, not the pull."),
     "slo": "4.3.4"},
    {"keys": ["artificial gravity", "rotating spacecraft", "centrifugation weightlessness",
              "counter weightlessness"],
     "title": "Artificial gravity",
     "answer": (
         "Spin the spacecraft. The floor then pushes the crew up with a **centripetal "
         "acceleration**:\n\n"
         "**a = ω²R**, so **ω = √(a/R)** and the period is **T = 2π/ω**.\n\n"
         "A 60 m diameter habitat needs about **11 s** per turn (5.5 rpm) to give Earth "
         "gravity at the rim. Faster spins would give stronger gravity but the Coriolis "
         "force makes that unbearable — which is why real designs use a **large radius and a "
         "slow spin**."),
     "slo": "4.3.5"},
    {"keys": ["moment of inertia", "what is moment of inertia", "unit of moment of inertia",
              "i equals mr squared"],
     "title": "Moment of inertia",
     "answer": (
         "**I = Σmr²** — the rotational measure of how much stuff there is.\n\n"
         "Unit: **kg m²**. Dimension: **[ML²]**.\n\n"
         "Unlike mass it depends on **where the mass is relative to the axis**. Moving mass "
         "outwards always increases I, and shifting the axis outwards does too."),
     "slo": "4.4.1"},
    {"keys": ["compare ring disc sphere", "which has larger moment of inertia",
              "order of moment of inertia", "rod ring disc"],
     "title": "Comparing moments of inertia",
     "answer": (
         "For the same mass and radius, the order is:\n\n"
         "**ring (MR²) > hollow sphere (2/3 MR²) > disc (½MR²) > solid sphere (2/5 MR²) > "
         "semi-disc (1/8 MR²)**\n\n"
         "For a rod: **1/12 ML²** about its centre, **1/3 ML²** about one end — four times "
         "larger, purely because of the pivot."),
     "slo": "4.4.2"},
    {"keys": ["torque", "tau equals i alpha", "rotational newton", "torque formula"],
     "title": "Torque and angular acceleration",
     "answer": (
         "**τ = rF sin θ** — only the component of the force *perpendicular* to the lever "
         "turns the body. τ = rF only at θ = 90°.\n\n"
         "**τ = Iα** — the rotational form of F = ma.\n\n"
         "The whole of rotational dynamics follows from that second line, just as Newton's "
         "second law governs linear dynamics."),
     "slo": "4.4.3"},
    {"keys": ["angular momentum", "what is angular momentum", "l equals i omega",
              "unit of angular momentum"],
     "title": "Angular momentum",
     "answer": (
         "**L = Iω**\n\n"
         "Unit: **kg m² s⁻¹**. Dimension: **[ML²T⁻¹]**.\n\n"
         "It is a vector pointing **along the axis of rotation**, with a sense fixed by the "
         "right-hand rule."),
     "slo": "4.5.1"},
    {"keys": ["conservation of angular momentum", "skater pulling arms",
              "why does the skater speed up", "flywheel", "gyroscope"],
     "title": "Conservation of angular momentum",
     "answer": (
         "With **no external torque**, total L is constant.\n\n"
         "So if I falls, ω must rise: ω₂ = I₁ω₁/I₂.\n\n"
         "That is why a skater pulling in her arms spins faster, why a diver tucks to "
         "somersault, and why a gyroscope's axis holds its direction — all three are the "
         "same conservation law.\n\n"
         "**Careful:** energy is *not* conserved through the skater's change of I. She "
         "supplies it with her muscles."),
     "slo": "4.5.3"},
]


def _projectile(u, theta):
    result = M.projectile(float(u), float(theta))
    return (f"**u = {float(u):g} m s⁻¹ at {float(theta):g}°** (g = 9.8)\n\n"
            f"* time of flight T = **{result['time_of_flight']:.4g} s**\n"
            f"* maximum height H = **{result['max_height']:.4g} m**\n"
            f"* range R = **{result['range']:.4g} m**\n"
            f"* longest possible range = {result['max_range']:.4g} m, at 45°\n\n"
            f"Check: uₓ × T = {result['components'][0]:.4g} × "
            f"{result['time_of_flight']:.4g} = "
            f"{result['components'][0] * result['time_of_flight']:.4g} m, which should equal R.")


def _maxrange(u):
    best = M.optimal_angle(float(u))
    return (f"**u = {float(u):g} m s⁻¹**\n\n"
            f"* best angle: **{best['angle_deg']:.0f}°**\n"
            f"* longest range: **{best['max_range']:.4g} m**\n"
            f"* height at that angle: {best['max_height']:.4g} m\n\n"
            f"R_max = u²/g, reached at 45°, because sin 2θ cannot exceed 1. The height there "
            f"is only half the greatest height the ball could reach.")


def _centripetal(v, r, m):
    return (f"**v = {float(v):g} m s⁻¹, r = {float(r):g} m, m = {float(m):g} kg**\n\n"
            f"* a_c = v²/r = **{M.centripetal_acceleration(float(v), float(r)):.4g} m s⁻²**\n"
            f"* F_c = mv²/r = **{M.centripetal_force(float(m), float(v), float(r)):.4g} N**\n"
            f"* period = **{2 * math.pi * float(r) / float(v):.4g} s**\n\n"
            f"The acceleration points to the centre and does no work, because the force is "
            f"perpendicular to the velocity.")


def _moment(body, m, radius):
    value = M.moment_of_inertia(body, float(m), float(radius))
    return (f"**I = {value:.4g} kg m²**\n\n"
            f"I = Σmr², and for standard shapes the factor I/(mR²) is:\n"
            f"ring 1, hollow sphere 2/3, disc 1/2, solid sphere 2/5, semi-disc 1/8.\n\n"
            f"Unit kg m², dimension [ML²].")


def _torque(r, f, phi):
    tau = M.torque(float(r), float(f), float(phi))
    return (f"**τ = {tau:.4g} N m**\n\n"
            f"τ = rF sin φ = {float(r):g} × {float(f):g} × sin {float(phi):g}° = {tau:.4g} N m\n\n"
            f"At 90° the force is perpendicular and you get the largest torque this moment "
            f"arm allows. Along the lever (0° or 180°) the torque is exactly zero.")


def _angular_momentum(i, omega):
    return (f"**L = {M.angular_momentum(float(i), float(omega)):.4g} kg m² s⁻¹**\n\n"
            f"L = Iω = {float(i):g} × {float(omega):g}\n\n"
            f"Unit kg m² s⁻¹, dimension [ML²T⁻¹]. It points along the axis of rotation.")


def _skater(i1, i2, w1):
    result = M.conserve_angular_momentum(float(i1), float(w1), float(i2))
    return (f"**I falls from {float(i1):g} to {float(i2):g} kg m²**\n\n"
            f"* L is conserved at **{result['angular_momentum_before']:.4g} kg m² s⁻¹**\n"
            f"* ω rises from {float(w1):g} to **{result['omega_after']:.4g} rad s⁻¹**\n"
            f"* that is ×{result['speed_factor']:.4g}\n\n"
            f"Rotational energy goes {result['energy_before']:.4g} J → "
            f"{result['energy_after']:.4g} J, because her muscles supplied it. L is conserved; "
            f"energy is not.")


CALCULATORS = [
    {"pattern": r"projectile\D*?([\d.]+)\s*m\s*s?-?\s*\w*\s*at\s*([\d.]+)\s*(?:deg|degrees|°)?",
     "reply": _projectile},
    {"pattern": r"range\D*?([\d.]+)\s*m\s*s?-\s*1\D*?([\d.]+)\s*(?:deg|degrees|°)?", "reply": _projectile},
    {"pattern": r"max(?:imum)?\s*range\D*?([\d.]+)", "reply": _maxrange},
    {"pattern": r"longest\s*range\D*?([\d.]+)", "reply": _maxrange},
    {"pattern": r"centripetal\D*?([\d.]+)\s*[,/]?\s*([\d.]+)\s*[,/]?\s*([\d.]+)", "reply": _centripetal},
    {"pattern": r"moment\s+of\s+inertia\D*?([a-z]+)\D*?([\d.]+)\D*?([\d.]+)", "reply": _moment},
    {"pattern": r"torque\D*?([\d.]+)\s*[,/]?\s*([\d.]+)\s*[,/]?\s*([\d.]+)", "reply": _torque},
    {"pattern": r"angular\s+momentum\D*?([\d.]+)\s*[,/]?\s*([\d.]+)", "reply": _angular_momentum},
    {"pattern": r"skater\D*?([\d.]+)\s*(?:to|→|and)\s*([\d.]+)\s*(?:at|with|ω)\s*([\d.]+)",
     "reply": _skater},
]
