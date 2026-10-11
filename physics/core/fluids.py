"""Chapter 6 - Fluids Dynamics.

Upthrust and floatation, streamline and turbulent flow, the equation of
continuity, Bernoulli's equation, viscosity and fluid friction.

Pure Python: no Streamlit, pandas, NumPy or Plotly.
"""

from __future__ import annotations

import math

__all__ = [
    "STANDARD_G", "FLUIDS", "upthrust", "floatation_verdict", "sink_or_float",
    "ship_displacement", "displaced_volume", "REYNOLDS_LIMITS", "reynolds_number",
    "flow_regime", "pipe_series", "continuity_area", "continuity_velocity",
    "continuity_time", "bernoulli", "atomiser_speed", "magnus_lift",
    "venturi_pressure", "VISCOUS_FLUIDS", "drag_ratio", "drag_relation",
    "superfluidity", "stokes_drag", "reynolds_flow",
]

STANDARD_G = 9.8

#: Densities in kg m^-3 at room temperature.
FLUIDS = [
    {"name": "Water", "density": 1.0e3, "viscosity": 1.0e-3, "kind": "Non-viscous in school models",
     "note": "Its viscosity is small, so it is usually treated as an ideal fluid."},
    {"name": "Sea water", "density": 1.025e3, "viscosity": 1.8e-3, "kind": "Non-viscous in school models",
     "note": "Salt makes sea water denser, so a body floats higher in it than in fresh water."},
    {"name": "Mercury", "density": 1.36e4, "viscosity": 1.5e-3, "kind": "Non-viscous in school models",
     "note": "13.6 times denser than water, so an iron nail floats on it."},
    {"name": "Honey", "density": 1.42e3, "viscosity": 2.0e1, "kind": "Viscous",
     "note": "About 20 000 times more viscous than water; it pours slowly and resists shear."},
    {"name": "Engine oil", "density": 8.7e2, "viscosity": 0.1, "kind": "Viscous",
     "note": "The viscosity of oil falls as it warms, which is why engines need different grades."},
    {"name": "Air", "density": 1.2, "viscosity": 1.8e-5, "kind": "Non-viscous in school models",
     "note": "Very light, so upthrust in air is small - but it is enough for a balloon."},
]


# --------------------------------------------------------------------------
# 6.1  Upthrust and floatation
# --------------------------------------------------------------------------

def upthrust(fluid_density: float, displaced_volume: float,
             g: float = STANDARD_G) -> float:
    """Upthrust ``U = rho_f g V`` - the weight of the fluid displaced."""
    return fluid_density * g * displaced_volume


def displaced_volume(fluid_density: float, weight: float,
                     g: float = STANDARD_G) -> float:
    """The volume that must be displaced to support a given weight."""
    return weight / (fluid_density * g) if fluid_density * g else float("inf")


def floatation_verdict(object_density: float, object_volume: float,
                       fluid_density: float, g: float = STANDARD_G) -> dict:
    """Decide whether a body floats, sinks or is exactly suspended.

    The maximum upthrust is the weight of the whole volume of the body. A body
    floats when its own weight is no more than that; a floating body only
    displaces as much fluid as it needs to support its weight.
    """
    weight = object_density * object_volume * g
    maximum_upthrust = upthrust(fluid_density, object_volume, g)
    if object_density > fluid_density:
        verdict, why = "Sinks", ("Its density is greater than the fluid's, so even the "
                                 "full upthrust is smaller than its weight.")
    elif object_density == fluid_density:
        verdict, why = "Fully submerged and in equilibrium", (
            "It displaces its own volume of fluid, which is exactly its weight.")
    else:
        fraction = object_density / fluid_density
        verdict, why = "Floats", (
            f"It floats with about {fraction * 100:.0f} % of its volume below the surface, "
            "displacing only the fluid needed to balance its weight.")
    return {"weight": weight, "maximum_upthrust": maximum_upthrust,
            "verdict": verdict, "reason": why,
            "submerged_fraction": min(1.0, object_density / fluid_density) if fluid_density else 1.0}


def sink_or_float(object_density: float, fluid_density: float) -> str:
    """One-word verdict, for the quick classifier."""
    if object_density > fluid_density:
        return "Sinks"
    if object_density == fluid_density:
        return "Suspended"
    return "Floats"


def ship_displacement(ship_mass: float, g: float = STANDARD_G,
                      sea_density: float = 1.025e3) -> dict:
    """How much sea water a ship must displace to float, and the hull shape that does it.

    A ship floats because its hull is hollow: a small mass spread over a very
    large waterplane area displaces a huge volume of water.
    """
    volume = ship_mass / (sea_density * g)
    return {"displaced_volume": volume, "displaced_mass": ship_mass,
            "upthrust": ship_mass * g, "sea_density": sea_density,
            "why": "The hull is shaped so that it pushes aside enough water for the "
                   "upthrust to equal the weight of the whole ship, cargo included."}


# --------------------------------------------------------------------------
# 6.2  Streamline and turbulent flow
# --------------------------------------------------------------------------

#: Below Re ~ 2000 the flow in a pipe is laminar; above ~4000 it is turbulent.
REYNOLDS_LIMITS = {"laminar": 2000.0, "turbulent": 4000.0}


def reynolds_number(density: float, speed: float, length: float,
                    viscosity: float) -> float:
    """Reynolds number ``Re = rho v L / eta``.

    It compares the inertia of the fluid with its viscosity. When inertia wins
    the fluid keeps going straight past an obstacle and layers slide over one
    another; when viscosity wins, swirls are smoothed out and the layers stay
    parallel. ``Re`` is dimensionless, which is itself a useful check.
    """
    return density * speed * length / viscosity if viscosity else float("inf")


def flow_regime(re_number: float) -> dict:
    """Classify a flow from its Reynolds number."""
    if re_number <= REYNOLDS_LIMITS["laminar"]:
        return {"regime": "Laminar (streamline)",
                "note": "The fluid moves in smooth parallel layers that never mix. "
                        "Streamline drawings are accurate here."}
    if re_number < REYNOLDS_LIMITS["turbulent"]:
        return {"regime": "Transitional",
                "note": "Some layers begin to mix; the flow has no fixed pattern."}
    return {"regime": "Turbulent",
            "note": "The fluid mixes in irregular swirls and eddies. Streamline "
                    "drawings become misleading."}


def reynolds_flow(density: float, speed: float, length: float,
                  viscosity: float) -> dict:
    """Reynolds number together with its regime, and what changes the regime."""
    re_number = reynolds_number(density, speed, length, viscosity)
    return {"re": re_number, **flow_regime(re_number),
            "driven_by": "A larger speed, a larger diameter or a smaller viscosity "
                         "all make the flow more likely to become turbulent."}


# --------------------------------------------------------------------------
# 6.3  Equation of continuity
# --------------------------------------------------------------------------

def continuity_area(area_a: float, velocity_a: float) -> float:
    """``A_1 v_1`` - the volume flow rate, in m^3 s^-1."""
    return area_a * velocity_a


def continuity_velocity(area_a: float, velocity_a: float, area_b: float) -> float:
    """``v_2 = A_1 v_1 / A_2`` from ``A_1 v_1 = A_2 v_2``.

    Halving the cross-section doubles the speed. The mass flow rate
    ``rho A v`` is also conserved, but for an incompressible fluid the density
    cancels and only ``A v`` needs to be held constant.
    """
    return continuity_area(area_a, velocity_a) / area_b if area_b else float("inf")


def continuity_time(volume: float, area: float, velocity_a: float) -> dict:
    """How long a given volume of fluid takes to pass through a pipe."""
    flow = continuity_area(area, velocity_a)
    return {"flow_rate": flow, "time": volume / flow if flow else float("inf")}


def pipe_series(area_a: float, area_b: float, velocity_a: float, samples: int = 120) -> dict:
    """A tapering pipe sampled along its length, for the continuity visual.

    The cross-section shrinks smoothly from ``A_1`` at the wide end to ``A_2``
    at the narrow end, and the speed follows from continuity.
    """
    n = max(3, int(samples))
    positions = [i / (n - 1) for i in range(n)]
    areas = [area_a + (area_b - area_a) * p for p in positions]
    velocities = [continuity_velocity(area_a, velocity_a, a) for a in areas]
    return {"position": positions, "area": areas, "velocity": velocities,
            "flow_rate": continuity_area(area_a, velocity_a),
            "constant": all(math.isclose(continuity_area(a, v),
                                         continuity_area(area_a, velocity_a), rel_tol=1e-9)
                            for a, v in zip(areas, velocities))}


# --------------------------------------------------------------------------
# 6.4  Bernoulli's equation
# --------------------------------------------------------------------------

def bernoulli(p1: float = 101325.0, v1: float = 0.0, h1: float = 0.0,
              density: float = 1.0e3, *, p2: float | None = None,
              v2: float | None = None, h2: float | None = None) -> dict:
    """Bernoulli's equation ``P + (1/2) rho v^2 + rho g h = constant``.

    Exactly one of ``p2``, ``v2`` or ``h2`` may be left as ``None``, and that
    is the quantity solved for. The equation is the statement that energy is
    conserved along a streamline of steady, incompressible, non-viscous flow.
    """
    if sum(x is None for x in (p2, v2, h2)) != 1:
        raise ValueError("leave exactly one of p2, v2 or h2 unset to solve for it")
    head1 = p1 + 0.5 * density * v1 ** 2 + density * STANDARD_G * h1

    if v2 is None:
        # P + rho g h2 = constant - half rho v2^2, with p2 given.
        value2 = head1 - p2 - density * STANDARD_G * (h2 or 0.0)
        if value2 < 0:
            return {"error": "These conditions cannot be joined by a streamline: the "
                             "energy per unit volume would be negative."}
        return {"p2": p2, "v2": math.sqrt(2.0 * value2 / density), "h2": h2 or 0.0,
                "constant": head1}
    if p2 is None:
        value2 = head1 - density * STANDARD_G * (h2 or 0.0)
        return {"p2": value2 - 0.5 * density * v2 ** 2, "v2": v2,
                "h2": h2 or 0.0, "constant": head1}
    return {"p2": p2, "v2": v2,
            "h2": (head1 - p2 - 0.5 * density * v2 ** 2) / (density * STANDARD_G),
            "constant": head1}


def atomiser_speed(pressure_difference: float, density: float = 1.0e3) -> float:
    """Speed of the air jet in a scent atomiser or a sprayer.

    The squeezed air accelerates as its pressure drops, and the faster jet
    entrains liquid from the tube and carries it out as a fine spray.
    """
    return math.sqrt(2.0 * pressure_difference / density) if pressure_difference >= 0 else float("nan")


def magnus_lift(speed: float, circulation: float, density: float = 1.225) -> float:
    """Magnus force ``F = rho v Gamma`` on a spinning ball.

    A ball spinning in flight drags air round with it. The air moves faster on
    one side, so the pressure there is lower and the ball curves - the same
    mechanism that makes a struck cricket ball swing.
    """
    return density * speed * circulation


def venturi_pressure(p1: float, v1: float, area_ratio: float,
                     density: float = 1.0e3) -> float:
    """Pressure after a constriction where the area has fallen to ``area_1 / area_ratio``.

    Pressure drops as the flow speeds up; the difference between the two ends of
    a venturi meter is what actually measures the flow rate.
    """
    v2 = v1 * area_ratio
    return p1 - 0.5 * density * (v2 ** 2 - v1 ** 2)


# --------------------------------------------------------------------------
# 6.5  Viscous fluids and fluid friction
# --------------------------------------------------------------------------

VISCOUS_FLUIDS = [
    {"liquid": "Water", "eta_pa_s": 1.0e-3, "relative": "1",
     "feel": "Pours quickly; the fall is nearly a clean stream at first."},
    {"liquid": "Glycerine", "eta_pa_s": 1.5, "relative": "1500",
     "feel": "Runs slowly and thickly; air bubbles rise slowly through it."},
    {"liquid": "Honey", "eta_pa_s": 2.0e1, "relative": "20000",
     "feel": "Barely flows at all; a falling bead keeps its shape."},
    {"liquid": "Air", "eta_pa_s": 1.8e-5, "relative": "0.018",
     "feel": "Almost invisible as a fluid, but a very light body falls slowly "
             "because of it."},
    {"liquid": "Helium (liquid, 4 K)", "eta_pa_s": 0.0, "relative": "0",
     "feel": "Superfluid: it climbs the wall of its container and never stops "
             "spinning once started."},
]


def drag_ratio(density_a: float, viscosity_a: float,
               density_b: float, viscosity_b: float,
               radius: float = 1.0e-3, speed: float = 1.0) -> dict:
    """Compare the retarding force on the same sphere falling through two fluids.

    The same ball dropped into honey and into air feels very different forces.
    Viscous drag dominates the honey (it is roughly a thousand times more
    viscous) while the buoyant upthrust is what dominates the air, because air
    is about 800 times less dense than honey.
    """
    drag_a = 6.0 * math.pi * viscosity_a * radius * speed
    drag_b = 6.0 * math.pi * viscosity_b * radius * speed
    lift_a = upthrust(density_a, 4.0 / 3.0 * math.pi * radius ** 3)
    lift_b = upthrust(density_b, 4.0 / 3.0 * math.pi * radius ** 3)
    return {"drag_a": drag_a, "drag_b": drag_b,
            "upthrust_a": lift_a, "upthrust_b": lift_b,
            "drag_ratio": drag_b / drag_a if drag_a else float("inf"),
            "upthrust_ratio": lift_b / lift_a if lift_a else float("inf"),
            "note": "Viscosity decides the drag; density decides the upthrust. "
                    "They are independent, which is why a light, viscous liquid "
                    "and a heavy, runny one feel nothing alike."}


def drag_relation(density: float, viscosity: float, radius: float, speed: float) -> dict:
    """The retarding force of a fluid, ``F = 6 pi eta r v`` for low Reynolds number.

    This is the ``drag proportional to v`` law that holds for a small sphere
    moving slowly and steadily through a fluid (Stokes' law). At higher speeds
    the drag grows faster than linearly because the wake behind the body grows.
    """
    re_number = reynolds_number(density, speed, 2.0 * radius, viscosity)
    stokes_force = 6.0 * math.pi * viscosity * radius * speed
    return {"force": stokes_force, "reynolds": re_number,
            "regime": flow_regime(re_number)["regime"],
            "note": "Valid while the flow round the body is laminar; at large "
                    "Reynolds numbers the drag rises faster than linearly."}


def superfluidity() -> list:
    """What superfluid helium does that no ordinary liquid does."""
    return [
        {"property": "Zero viscosity",
         "evidence": "A stirred bath of superfluid helium never slows down.",
         "explanation": "There is no viscosity, so no energy is transferred to "
                        "the walls as heat."},
        {"property": "Creeping up the walls",
         "evidence": "A superfluid climbs out of its container and forms a film "
                     "on the glass.",
         "explanation": "The film is only a few hundred atomic layers thick and "
                        "carries its own superflow."},
        {"property": "Fountain effect",
         "evidence": "Heating a point inside the liquid makes a jet shoot upwards.",
         "explanation": "The heated region becomes less dense, so it rises; the "
                        "surface layer rushes in to replace it."},
        {"property": "Quantised circulation",
         "evidence": "A bucket of superfluid spins forever once started.",
         "explanation": "Its circulation is locked to whole multiples of h/m, "
                        "exactly as in superconductors."},
    ]
