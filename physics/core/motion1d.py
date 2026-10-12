"""Chapter 3 - Motion in One Dimension.

Covers the uniform-acceleration equations, conservation of linear momentum,
elastic and inelastic collisions, work from a force-displacement graph,
conservative and non-conservative fields, and the work-energy theorem.

All motion is taken along the x axis. ``u`` is initial velocity, ``a`` is
constant acceleration, ``s`` is displacement and ``t`` is time.
"""

from __future__ import annotations

import math

__all__ = [
    "STANDARD_G", "velocity", "displacement", "displacement_from_velocity",
    "time_from_displacement", "time_from_velocity", "solve_from_u_at",
    "solve_from_u_as", "solve_from_uas", "kinematic_series", "free_fall",
    "total_momentum", "momentum_series", "elastic_collision_1d",
    "inelastic_collision_1d", "collision_report", "two_dimensional_collision",
    "work_from_steps", "area_under_fd", "spring_force", "net_work",
    "work_energy_check", "potential_energy", "kinetic_energy",
    "is_conservative_force", "path_independence_error", "conservative_examples",
    "spring_energy", "escape_and_orbit",
]

STANDARD_G = 9.8


# --------------------------------------------------------------------------
# 3.1  Equations of motion for uniform acceleration
# --------------------------------------------------------------------------

def velocity(u: float, a: float, t: float) -> float:
    """First equation of motion: ``v = u + a t``."""
    return u + a * t


def displacement(u: float, a: float, t: float) -> float:
    """Second equation of motion: ``s = u t + (1/2) a t^2``."""
    return u * t + 0.5 * a * t * t


def displacement_from_velocity(u: float, v: float, a: float) -> float:
    """Third equation of motion: ``s = (u + v) t / 2`` solved for displacement,
    using ``t = (v - u)/a``. Returns ``float('inf')`` when ``a`` is zero,
    because then the third equation cannot determine ``s``."""
    if a == 0:
        return math.inf
    return (v * v - u * u) / (2.0 * a)


def time_from_displacement(u: float, a: float, s: float) -> float:
    """Time from ``s = u t + (1/2) a t^2``.

    Two roots can exist; the physically sensible one is returned (the later
    root when ``a`` is negative, so the time is never negative). Returns
    ``float('nan')`` when the motion never reaches ``s``.
    """
    disc = u * u + 2.0 * a * s
    if disc < 0:
        return float("nan")
    root = math.sqrt(disc)
    first = (-u + root) / (2.0 * a) if a else (s / u if u else float("nan"))
    second = (-u - root) / (2.0 * a) if a else first
    candidates = [t for t in (first, second) if t == t]
    if not candidates:
        return float("nan")
    return max(candidates)


def time_from_velocity(u: float, v: float, a: float) -> float:
    """Time from ``v = u + a t``. Returns ``inf`` when ``a`` is zero."""
    if a == 0:
        return math.inf
    return (v - u) / a


def solve_from_u_at(u: float, a: float, t: float) -> dict:
    """Given ``u``, ``a`` and ``t`` find ``v`` and ``s``."""
    return {"v": velocity(u, a, t), "s": displacement(u, a, t),
            "u": u, "a": a, "t": t}


def solve_from_u_as(u: float, a: float, s: float) -> dict:
    """Given ``u``, ``a`` and ``s`` find ``t`` and ``v``."""
    t = time_from_displacement(u, a, s)
    return {"t": t, "v": velocity(u, a, t) if t == t else float("nan"),
            "u": u, "a": a, "s": s}


def solve_from_uas(u: float, a: float, s: float) -> dict:
    """Given ``u``, ``a`` and ``s`` find ``v`` using the third equation."""
    v2 = u * u + 2.0 * a * s
    if v2 < 0:
        return {"v": float("nan"), "v_squared": v2, "u": u, "a": a, "s": s}
    v = math.sqrt(v2) if v2 > 0 else 0.0
    return {"v": v if u >= 0 else -v, "v_squared": v2, "u": u, "a": a, "s": s}


def kinematic_series(u: float, a: float, t_max: float, samples: int = 200) -> dict:
    """Position, velocity and acceleration sampled in time, for the motion lab."""
    n = max(2, int(samples))
    step = t_max / (n - 1)
    times = [i * step for i in range(n)]
    return {
        "t": times,
        "s": [displacement(u, a, t) for t in times],
        "v": [velocity(u, a, t) for t in times],
        "a": [a] * n,
    }


def free_fall(height: float, u: float = 0.0, g: float = STANDARD_G) -> dict:
    """A body dropped (or thrown) from rest through a height under gravity."""
    t = time_from_displacement(u, g, height)
    return {"t": t, "v": velocity(u, g, t) if t == t else float("nan"),
            "height": height, "g": g,
            "impact_speed": math.sqrt(u * u + 2.0 * g * height)}


def escape_and_orbit(radius: float, speed: float, g: float = STANDARD_G) -> dict:
    """Classify a throw from the surface of a planet.

    Uses ``g = GM / R^2``, so the escape speed is ``sqrt(2 g R)`` and the
    circular-orbit speed is ``sqrt(g R)``.
    """
    escape = math.sqrt(2.0 * g * radius)
    circular = math.sqrt(g * radius)
    if speed >= escape:
        state = "Escapes - the speed reaches or exceeds escape velocity"
    elif speed >= circular:
        state = "Orbits in an ellipse that touches the surface"
    else:
        state = "Falls back to the surface"
    return {"escape_speed": escape, "orbital_speed": circular, "state": state,
            "surface_g": g, "radius": radius}


# --------------------------------------------------------------------------
# 3.2  Conservation of linear momentum and collisions
# --------------------------------------------------------------------------

def total_momentum(masses, velocities) -> float:
    """Total momentum of a system along the line of motion."""
    return sum(m * v for m, v in zip(masses, velocities))


def momentum_series(bodies, steps: int = 60) -> dict:
    """Track the total momentum of a set of bodies across a collision.

    ``bodies`` is a list of ``{"m": float, "u": float, "v": float}`` records.
    Before the collision each body moves at ``u``; afterwards at ``v``. The
    same total is plotted on both sides, which is the whole point.
    """
    before = total_momentum([b["m"] for b in bodies], [b["u"] for b in bodies])
    after = total_momentum([b["m"] for b in bodies], [b["v"] for b in bodies])
    n = max(2, int(steps))
    rising = [before] * (n // 2)
    falling = [after] * (n - n // 2)
    return {"time": list(range(n)), "momentum": rising + falling,
            "before": before, "after": after, "conserved": math.isclose(before, after, rel_tol=1e-9)}


def elastic_collision_1d(m1: float, u1: float, m2: float, u2: float) -> dict:
    """Final velocities after a one-dimensional elastic collision.

    Both momentum and kinetic energy are conserved, so

    ``v1 = (m1 - m2) u1 / (m1 + m2) + 2 m2 u2 / (m1 + m2)``
    ``v2 = 2 m1 u1 / (m1 + m2) + (m2 - m1) u2 / (m1 + m2)``
    """
    total = m1 + m2
    v1 = ((m1 - m2) * u1 + 2.0 * m2 * u2) / total
    v2 = (2.0 * m1 * u1 + (m2 - m1) * u2) / total
    return collision_report(m1, u1, m2, u2, v1, v2, kind="elastic")


def inelastic_collision_1d(m1: float, u1: float, m2: float, u2: float) -> dict:
    """Final common velocity after a perfectly inelastic collision.

    Momentum is conserved but kinetic energy is not; the surplus becomes heat,
    sound and deformation.
    """
    shared = total_momentum([m1, m2], [u1, u2]) / (m1 + m2)
    return collision_report(m1, u1, m2, u2, shared, shared, kind="perfectly inelastic")


def collision_report(m1: float, u1: float, m2: float, u2: float,
                     v1: float, v2: float, kind: str = "elastic") -> dict:
    """Momentum and kinetic energy on both sides of a collision, plus the losses."""
    p_before = m1 * u1 + m2 * u2
    p_after = m1 * v1 + m2 * v2
    ke_before = 0.5 * m1 * u1 ** 2 + 0.5 * m2 * u2 ** 2
    ke_after = 0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2
    return {
        "v1": v1, "v2": v2, "kind": kind,
        "momentum_before": p_before, "momentum_after": p_after,
        "kinetic_before": ke_before, "kinetic_after": ke_after,
        "kinetic_lost": ke_before - ke_after,
        "momentum_conserved": math.isclose(p_before, p_after, rel_tol=1e-9, abs_tol=1e-9),
        "kinetic_conserved": math.isclose(ke_before, ke_after, rel_tol=1e-9, abs_tol=1e-9),
    }


def two_dimensional_collision(m1: float, p1, m2: float, p2,
                              restitution: float = 1.0) -> dict:
    """Oblique collision of two smooth spheres, one at rest.

    ``p1`` and ``p2`` are ``(x, y)`` component tuples. ``restitution`` ``e``
    runs from 1 (perfectly elastic) down to 0 (perfectly inelastic). For smooth
    spheres the impulse acts along the line of centres, so momentum is
    conserved in both directions while kinetic energy is conserved only when
    ``e = 1``.
    """
    from . import vectors as V

    nx, ny = V.subtract(p2, p1)
    size = V.magnitude((nx, ny))
    if size == 0:
        return {"error": "The two balls occupy the same point; the line of centres is undefined."}
    nhat = (nx / size, ny / size)
    approaching = V.dot_product(p1, nhat)
    if approaching <= 0:
        return {"error": "The first ball is not moving towards the second, so they do not collide."}

    v1n = (1.0 - restitution / 2.0) * approaching
    v2n = (restitution / 2.0) * approaching
    v1 = V.subtract(p1, V.scale(nhat, approaching - v1n))
    v2 = V.subtract(p2, V.scale(nhat, -v2n))

    return {
        "v1": v1, "v2": v2, "restitution": restitution,
        "unit_normal": nhat, "centre_angle_deg": V.angle_between(p1, p2),
        **collision_report(m1, 0.0, m2, 0.0, 0.0, 0.0, kind="oblique"),
        "momentum_before_vec": V.add(V.scale(p1, m1), V.scale(p2, m2)),
        "momentum_after_vec": V.add(V.scale(v1, m1), V.scale(v2, m2)),
        "momentum_conserved": math.isclose(
            V.magnitude(V.subtract(V.add(V.scale(p1, m1), V.scale(p2, m2)),
                                   V.add(V.scale(v1, m1), V.scale(v2, m2)))),
            0.0, abs_tol=1e-9),
    }


# --------------------------------------------------------------------------
# 3.3  Work
# --------------------------------------------------------------------------

def spring_force(k: float, extension: float) -> float:
    """Hooke's law: ``F = k x``. The force opposes the extension."""
    return -k * extension


def work_from_steps(force, distance) -> float:
    """Constant force along a straight displacement: ``W = F d``.

    The cosine is carried explicitly so the interface can show why the force
    must point along the displacement.
    """
    from . import vectors as V

    direction = V.angle_of(distance)
    return V.work(force, V.scale(V.unit_vector(distance), 1.0)) * V.magnitude(distance)


def area_under_fd(forces, distances) -> float:
    """Work done from a force-displacement graph, by the trapezium rule.

    ``forces`` and ``distances`` are equal-length sequences sampled along the
    path. The area under the curve is the work; a curve below the axis gives a
    negative result, meaning energy is taken out of the body.
    """
    if len(forces) != len(distances):
        raise ValueError("forces and distances must have the same number of points")
    if len(forces) < 2:
        return 0.0
    total = 0.0
    for i in range(len(forces) - 1):
        width = distances[i + 1] - distances[i]
        total += 0.5 * (forces[i] + forces[i + 1]) * width
    return total


def net_work(steps) -> float:
    """Total work from a list of ``{"F": float, "d": float, "cos": float}`` steps.

    A negative step (a resistive force opposing the motion) subtracts energy.
    """
    return sum(step["F"] * step["d"] * step.get("cos", 1.0) for step in steps)


# --------------------------------------------------------------------------
# 3.4  Conservative and non-conservative fields
# --------------------------------------------------------------------------

def is_conservative_force(force, displacement) -> bool:
    """A field is conservative when the work it does does not depend on the path.

    The test used here is the gradient of a position-dependent potential: a
    force is conservative exactly when the work around any closed loop is zero.
    """
    from . import vectors as V

    # Closing the loop A -> B -> -B -> -A -> A must give zero net work.
    loop = [displacement, V.negate(displacement)]
    work = 0.0
    for leg in loop:
        work += V.work(force, leg)
    return math.isclose(work, 0.0, abs_tol=1e-9)


def path_independence_error(force, path) -> float:
    """Difference between the work along two different routes to the same point.

    ``path`` is a list of displacement vectors. For a conservative field the
    two sums agree to within rounding.
    """
    from . import vectors as V

    direct = V.work(force, V.as_tuple(path[0]))
    detour = sum(V.work(force, V.as_tuple(leg)) for leg in path[1:])
    return abs(direct - detour)


def conservative_examples() -> list:
    """A small catalogue of forces and whether the field they create is conservative."""
    from . import vectors as V

    g = V.magnitude((0.0, -STANDARD_G))
    entries = [
        ("Gravitational force near the Earth's surface", (0.0, -STANDARD_G),
         True, "The work depends only on the height lost, not on the route taken."),
        ("Electrostatic force between two point charges", (-4.0, 0.0),
         True, "Electrostatic force is conservative, so a charge can be returned "
               "to its starting point with no net work."),
        ("Elastic force of a stretched spring", (-1.0, 0.0),
         True, "A spring stores potential energy, so its force is conservative."),
        ("Kinetic friction between sliding surfaces", (3.0, 0.0),
         False, "Friction always opposes the motion, so it dissipates energy and "
                "the work depends on the path."),
        ("Air resistance (drag)", (-2.5, 0.0),
         False, "Drag removes mechanical energy from the system."),
    ]
    return [{"field": name, "force": force, "g_magnitude": g,
             "conservative": flag, "reason": reason} for name, force, flag, reason in entries]


# --------------------------------------------------------------------------
# 3.5  Work-energy theorem
# --------------------------------------------------------------------------

def kinetic_energy(mass: float, velocity_value: float) -> float:
    """``K = (1/2) m v^2``."""
    return 0.5 * mass * velocity_value ** 2


def potential_energy(mass: float, height: float, g: float = STANDARD_G) -> float:
    """``U = m g h``, measured from an arbitrary zero level."""
    return mass * g * height


def spring_energy(k: float, extension: float) -> float:
    """Elastic potential energy ``E = (1/2) k x^2``."""
    return 0.5 * k * extension ** 2


def work_energy_check(mass: float, u: float, v: float,
                      distance: float = 0.0,
                      g: float = STANDARD_G, height: float = 0.0,
                      friction: float = 0.0) -> dict:
    """Work-energy theorem in a resistive medium.

    The net work done on the body equals the change in kinetic energy. The net
    work is the sum of the work done against each force, one of which may be
    the retarding force of friction.

    Work is force times distance, so the friction term is ``-F x d``. It was
    once written as ``-friction`` alone, which reported the retarding *force*
    under a heading that said work: 10 N over 10 m came out as -10 J instead of
    -100 J, a factor of ten out.

    The remaining forces are not separately known here, so ``work_other`` is
    whatever balances the books. That makes ``net_work == delta_k`` an
    identity rather than a test of anything; it is reported because the
    balancing term is pedagogically the interesting one - it is the work the
    driving force must supply.
    """
    delta_k = kinetic_energy(mass, v) - kinetic_energy(mass, u)
    # "+ 0.0" normalises -0.0 to 0.0, so an unused friction input reads "0 J"
    # rather than "-0 J".
    work_friction = -abs(friction) * distance + 0.0
    work_other = delta_k - work_friction
    return {
        "delta_kinetic": delta_k,
        "work_friction": work_friction,
        "work_other_forces": work_other,
        "net_work": work_other + work_friction,
        "consistent": math.isclose(work_other + work_friction, delta_k, rel_tol=1e-9),
        "mean_driving_force": (work_other / distance) if distance else 0.0,
        "distance": distance, "friction": friction,
        "height": height, "g": g,
    }
