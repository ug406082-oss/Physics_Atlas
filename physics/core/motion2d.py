"""Chapter 4 - Motion in Two Dimensions.

Projectile motion, angular quantities and their link to the linear ones,
centripetal acceleration and force, moments of inertia and the conservation of
angular momentum.

Pure Python: no Streamlit, pandas, NumPy or Plotly.
"""

from __future__ import annotations

import math

__all__ = [
    "STANDARD_G", "projectile", "trajectory", "max_range", "optimal_angle",
    "horizontal_range", "maximum_height", "time_of_flight", "air_resistance_effect",
    "angular_displacement", "angular_velocity", "angular_acceleration",
    "linear_from_angular", "angular_from_linear", "rotation_series",
    "centripetal_acceleration", "centripetal_force", "apparent_weight",
    "artificial_gravity", "centrifuge_outward_shift", "MOI_SHAPES",
    "moment_of_inertia", "rotational_acceleration", "torque",
    "angular_momentum", "conserve_angular_momentum", "flywheel_note",
]

STANDARD_G = 9.8


# --------------------------------------------------------------------------
# 4.1  Projectile motion
# --------------------------------------------------------------------------

def projectile(u: float, theta_deg: float, g: float = STANDARD_G) -> dict:
    """The four standard relations for a projectile launched at speed ``u``.

    ``T = 2 u sin(theta) / g``          time of flight
    ``H = u^2 sin^2(theta) / 2 g``      maximum height above the launch point
    ``R = u^2 sin(2 theta) / g``        horizontal range
    ``R_max = u^2 / g`` at ``theta = 45 degrees``
    """
    theta = math.radians(theta_deg)
    t_peak = u * math.sin(theta) / g
    return {
        "time_of_flight": 2.0 * t_peak,
        "time_to_peak": t_peak,
        "max_height": u * u * math.sin(theta) ** 2 / (2.0 * g),
        "range": u * u * math.sin(2.0 * theta) / g,
        "max_range": u * u / g,
        "optimal_angle_deg": 45.0,
        "components": components_of(u, theta_deg),
        "angle_deg": theta_deg,
        "speed": u,
        "g": g,
    }


def components_of(u: float, theta_deg: float) -> tuple:
    """Horizontal and vertical launch components."""
    theta = math.radians(theta_deg)
    return u * math.cos(theta), u * math.sin(theta)


def time_of_flight(u: float, theta_deg: float, g: float = STANDARD_G) -> float:
    """``T = 2 u sin(theta) / g``."""
    return projectile(u, theta_deg, g)["time_of_flight"]


def maximum_height(u: float, theta_deg: float, g: float = STANDARD_G) -> float:
    """``H = u^2 sin^2(theta) / 2 g``."""
    return projectile(u, theta_deg, g)["max_height"]


def horizontal_range(u: float, theta_deg: float, g: float = STANDARD_G) -> float:
    """``R = u^2 sin(2 theta) / g``."""
    return projectile(u, theta_deg, g)["range"]


def max_range(u: float, g: float = STANDARD_G) -> float:
    """The greatest range possible, reached at ``theta = 45 degrees``: ``u^2 / g``."""
    return u * u / g


def optimal_angle(u: float, g: float = STANDARD_G) -> dict:
    """The launch angle giving the longest range, with the height and flight time."""
    best = projectile(u, 45.0, g)
    return {"angle_deg": 45.0, "max_range": best["max_range"],
            "max_height": best["max_height"],
            "time_of_flight": best["time_of_flight"]}


def trajectory(u: float, theta_deg: float, g: float = STANDARD_G, samples: int = 240) -> dict:
    """Sample the whole flight, for the trajectory plot.

    The horizontal and vertical coordinates are sampled at equal time steps
    from launch until the projectile returns to the launch height.
    """
    n = max(3, int(samples))
    vx, vy = components_of(u, theta_deg)
    total = time_of_flight(u, theta_deg, g)
    step = total / (n - 1)
    times = [i * step for i in range(n)]
    xs = [vx * t for t in times]
    ys = [vy * t - 0.5 * g * t * t for t in times]
    return {"t": times, "x": xs, "y": ys,
            "vx": vx, "vy": vy, "total_time": total,
            "range": xs[-1], "peak": max(ys)}


def air_resistance_effect(u: float, theta_deg: float, g: float = STANDARD_G) -> list:
    """Qualitative comparison of vacuum motion and motion through air.

    Air resistance always opposes the velocity, so it reduces both the
    horizontal range and the maximum height, lengthens the descent, and makes
    the descending limb of the path steeper than the ascending limb.
    """
    return [
        {"effect": "Horizontal range", "without_air": "u² sin(2θ) / g",
         "with_air": "less than u² sin(2θ) / g",
         "why": "Drag acts against the horizontal velocity, so the projectile "
                "travels less far in the same time."},
        {"effect": "Maximum height", "without_air": "u² sin²θ / 2g",
         "with_air": "less than u² sin²θ / 2g",
         "why": "Some of the upward kinetic energy is used against drag before "
                "the apex is reached."},
        {"effect": "Time of flight", "without_air": "2u sinθ / g",
         "with_air": "longer on the way down",
         "why": "The fall is slowed by drag, so the projectile stays in the air "
                "longer after the apex."},
        {"effect": "Shape of the path", "without_air": "symmetrical parabola",
         "with_air": "asymmetric, steeper on the way down",
         "why": "Drag removes horizontal speed throughout, but vertical speed is "
                "much smaller near the apex, so the braking is relatively stronger there."},
        {"effect": "Optimal angle for range", "without_air": "45°",
         "with_air": "less than 45°",
         "why": "A flatter launch suits the extra time that drag adds to the descent."},
    ]


# --------------------------------------------------------------------------
# 4.2  Angular motion
# --------------------------------------------------------------------------

def angular_displacement(degrees: float) -> float:
    """Radians from degrees: ``theta = theta_deg * pi / 180``."""
    return math.radians(degrees)


def angular_velocity(theta: float, t: float) -> float:
    """``omega = dtheta / dt``. Here ``theta`` is in radians."""
    return theta / t if t else float("nan")


def angular_acceleration(omega: float, t: float) -> float:
    """``alpha = domega / dt``."""
    return omega / t if t else float("nan")


def linear_from_angular(r: float, theta: float, omega: float, alpha: float = 0.0) -> dict:
    """``s = r theta``, ``v = r omega``, ``a_t = r alpha``.

    ``theta`` is in radians. This holds exactly for rigid rotation about a fixed
    axis, for every point on the body.
    """
    return {"s": r * theta, "v": r * omega, "a_t": r * alpha,
            "theta_rad": theta, "r": r, "omega": omega, "alpha": alpha}


def angular_from_linear(r: float, s: float, v: float, a_t: float = 0.0) -> dict:
    """The inverse relations: ``theta = s/r``, ``omega = v/r``, ``alpha = a/r``."""
    if r == 0:
        return {"theta_rad": float("nan"), "omega": float("nan"), "alpha": float("nan")}
    return {"theta_rad": s / r, "omega": v / r, "alpha": a_t / r}


def rotation_series(omega0: float, alpha: float, t_max: float, samples: int = 200) -> dict:
    """Angle, angular velocity and angular speed sampled in time."""
    n = max(2, int(samples))
    step = t_max / (n - 1)
    times = [i * step for i in range(n)]
    angles = [omega0 * t + 0.5 * alpha * t * t for t in times]
    omegas = [omega0 + alpha * t for t in times]
    return {"t": times, "theta": angles, "omega": omegas,
            "angular_speed": [abs(w) for w in omegas],
            "revolutions": [math.degrees(a) / 360.0 for a in angles]}


# --------------------------------------------------------------------------
# 4.3  Centripetal force and acceleration
# --------------------------------------------------------------------------

def centripetal_acceleration(speed: float, radius: float) -> float:
    """``a_c = v^2 / r`` for motion at a constant speed around a circle."""
    return speed * speed / radius if radius else float("inf")


def centripetal_force(mass: float, speed: float, radius: float) -> float:
    """``F_c = m v^2 / r``, directed along the radius towards the centre."""
    return mass * centripetal_acceleration(speed, radius)


def apparent_weight(mass: float, height: float, g_surface: float = STANDARD_G,
                    G: float = STANDARD_G ** 2 / 6.371e6, R: float = 6.371e6) -> dict:
    """Weight and orbital speed at a height above the Earth's surface.

    ``g_h = g (R/(R+h))^2`` falls off slowly, which is why astronauts in the
    International Space Station (about 400 km up) still feel about 90 % of
    their Earth weight - yet they appear weightless, because they and the
    station are both falling together.
    """
    g_h = g_surface * (R / (R + height)) ** 2
    radius = R + height
    return {"g": g_h, "radius": radius, "weight": mass * g_h,
            "orbital_speed": math.sqrt(G / radius) if radius else float("nan"),
            "fraction_of_surface_weight": (R / (R + height)) ** 2}


def artificial_gravity(radius: float, omega: float) -> float:
    """The apparent gravity produced by rotating a spacecraft: ``a = omega^2 r``.

    This is a centripetal acceleration that the floor presses against the
    soles of the crew's boots.
    """
    return omega * omega * radius


def centrifuge_outward_shift(radius: float, omega: float, samples: int = 60) -> dict:
    """How far a denser particle travels outward when a sample is spun.

    Every particle needs the same centripetal acceleration ``omega^2 r`` to stay
    in the rotating frame, so a dense particle must move further out, where the
    larger radius supplies the acceleration it needs.
    """
    n = max(3, int(samples))
    radii = [radius * (1.0 + 0.6 * i / (n - 1)) for i in range(n)]
    return {"r": radii, "a_required": [omega ** 2 * r for r in radii],
            "omega": omega, "base_radius": radius}


# --------------------------------------------------------------------------
# 4.4  Moment of inertia
# --------------------------------------------------------------------------

#: Moments of inertia about the stated axes. ``shape`` values are ``(I / m R^2)``
#: expressed as a list ``[numerator, denominator]`` so no float error creeps in.
MOI_SHAPES = [
    {"shape": "Thin ring (hoop)", "axis": "through the centre, perpendicular to the ring",
     "coefficient": (1, 1), "body": "ring", "spread": "all the mass at radius R",
     "note": "The largest of the set for a given m and R, because every particle "
             "sits at the full radius."},
    {"shape": "Thin uniform rod", "axis": "through the centre, perpendicular to the rod",
     "coefficient": (1, 12), "body": "rod", "spread": "mass spread along the length",
     "note": "Twelve times harder to start than a point mass at the same distance."},
    {"shape": "Thin uniform rod", "axis": "through one end, perpendicular to the rod",
     "coefficient": (1, 3), "body": "rod", "spread": "mass spread along the length",
     "note": "Four times the value about the centre - the pivot matters."},
    {"shape": "Uniform solid disc", "axis": "through the centre, perpendicular to the disc",
     "coefficient": (1, 2), "body": "disc", "spread": "mass filling the area",
     "note": "Half of the ring of the same mass and radius."},
    {"shape": "Uniform solid sphere", "axis": "through the centre (a diameter)",
     "coefficient": (2, 5), "body": "sphere", "spread": "mass filling the volume",
     "note": "Less than the flat disc because much of the mass sits closer to the axis."},
    {"shape": "Uniform hollow sphere", "axis": "through the centre (a diameter)",
     "coefficient": (2, 3), "body": "shell", "spread": "mass on the surface only",
     "note": "Four fifths of a solid sphere of the same mass and radius."},
    {"shape": "Uniform semi-disc", "axis": "through the centre of the flat side",
     "coefficient": (1, 8), "body": "semi", "spread": "mass filling half the area",
     "note": "The smallest here, because the removed half was carrying much of "
             "the moment."},
]


def moment_of_inertia(body: str, mass: float, radius: float,
                      length: float = 0.0, axis: str = "centre") -> float:
    """Moment of inertia ``I`` for one of :data:`MOI_SHAPES`.

    ``body`` is one of ``ring``, ``rod``, ``disc``, ``sphere``, ``shell`` or
    ``semi``. ``axis`` is ``centre`` or ``end`` and only applies to a rod.
    Units are ``kg m^2`` and the dimension is ``[M L^2]``.
    """
    table = {
        ("ring", "centre"): (1, 1), ("rod", "centre"): (1, 12), ("rod", "end"): (1, 3),
        ("disc", "centre"): (1, 2), ("sphere", "centre"): (2, 5),
        ("shell", "centre"): (2, 3), ("semi", "centre"): (1, 8),
    }
    key = (body, axis if body == "rod" else "centre")
    if key not in table:
        raise ValueError(f"no moment of inertia for body={body!r} axis={axis!r}")
    num, den = table[key]
    span = length if body == "rod" else radius
    return mass * span ** 2 * num / den


def rotational_acceleration(torque_value: float, inertia: float) -> float:
    """The rotational form of ``F = ma``: ``alpha = tau / I``."""
    return torque_value / inertia if inertia else float("nan")


def torque(r: float, force: float, theta_deg: float) -> float:
    """Torque ``tau = r F sin(theta)``.

    Only the component of the force perpendicular to the moment arm turns the
    body, so the force acts at its largest when it is at right angles to ``r``.
    """
    return r * force * math.sin(math.radians(theta_deg))


# --------------------------------------------------------------------------
# 4.5  Angular momentum
# --------------------------------------------------------------------------

def angular_momentum(inertia: float, omega: float) -> float:
    """``L = I omega``. SI unit ``kg m^2 s^-1``, dimension ``[M L^2 T^-1]``."""
    return inertia * omega


def conserve_angular_momentum(inertia_before: float, omega_before: float,
                              inertia_after: float) -> dict:
    """What happens when ``I`` changes with no external torque.

    ``L = I omega`` is unchanged, so the body speeds up when the inertia falls.
    This is why a spinning skater who pulls in her arms turns faster.
    """
    l_before = inertia_before * omega_before
    omega_after = l_before / inertia_after if inertia_after else float("nan")
    return {
        "angular_momentum_before": l_before,
        "angular_momentum_after": inertia_after * omega_after,
        "omega_before": omega_before, "omega_after": omega_after,
        "speed_factor": omega_after / omega_before if omega_before else float("nan"),
        "energy_before": 0.5 * inertia_before * omega_before ** 2,
        "energy_after": 0.5 * inertia_after * omega_after ** 2,
    }


def flywheel_note() -> list:
    """Why flywheels, gyroscopes and skaters all conserve angular momentum."""
    return [
        {"application": "Flywheel",
         "idea": "A heavy wheel set spinning stores angular momentum, so it keeps "
                 "its speed and smooths out the changes in speed of the shaft it "
                 "is attached to."},
        {"application": "Gyroscope",
         "idea": "With no external torque the spin axis stays fixed in direction. "
                 "That is what keeps a spacecraft pointing the same way, and what "
                 "makes a bicycle stable."},
        {"application": "Ice skater",
         "idea": "Pulling the arms in lowers I. Because L is unchanged, omega "
                 "rises; spinning faster to finish turns."},
        {"application": "Diver",
         "idea": "The same trick in water: a tucked somersault spins faster than "
                 "an extended one, purely because I is smaller."},
        {"application": "Whirling midges and helicopter tail rotor",
         "idea": "A tall thin tail rotor has a long moment arm, so for a small "
                 "tail force it produces a large torque."},
    ]
