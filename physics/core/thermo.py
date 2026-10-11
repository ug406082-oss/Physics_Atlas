"""Chapter 10 - Thermodynamics.

Heat and temperature, the ideal gas laws, kinetic molecular theory, internal
energy and work, the first and second laws, specific heats, Carnot engines,
refrigerators and entropy.

Constants are the exact SI values where they exist.
"""

from __future__ import annotations

import math

__all__ = [
    "BOLTZMANN", "GAS_CONSTANT", "AVOGADRO", "STANDARD_G", "T_ABSOLUTE",
    "to_kelvin", "to_celsius", "thermal_equilibrium", "HEAT_EXPERIMENTS",
    "boyles_law", "charles_law", "ideal_gas_pressure", "ideal_gas_state",
    "KMT_POSTULATES", "rms_speed", "mean_speed", "most_probable_speed",
    "kinetic_pressure", "kinetic_pressure_volume", "average_translational_energy", "average_molecular_energy",
    "KMT_COMPARISON", "internal_energy", "dU_isothermal", "dU_isobaric",
    "dU_isochoric", "work_by_gas", "work_series", "first_law", "PROCESSES",
    "molar_heat_capacity", "cp_cv", "mayers_relation", "HEAT_CAPACITIES",
    "REVERSIBLE_PROCESSES", "carnot_efficiency", "carnot_cycle",
    "carnot_cycle_series", "heat_engine_summary", "refrigerator_cop",
    "entropy_change_ideal_gas", "entropy_change_process", "ENTROPY_POINTS",
    "energy_degradation", "environment_notes", "DESIGN_TASK",
]

BOLTZMANN = 1.380649e-23       # J K^-1, exact
GAS_CONSTANT = 8.314462618     # J mol^-1 K^-1, exact
AVOGADRO = 6.02214076e23       # mol^-1, exact
STANDARD_G = 9.8
T_ABSOLUTE = 273.15            # 0 degrees Celsius, exactly


# --------------------------------------------------------------------------
# 10.1  Heat and temperature
# --------------------------------------------------------------------------

def to_kelvin(value: float, scale: str = "C") -> float:
    """Convert a temperature to kelvin. ``scale`` is ``C``, ``F`` or ``K``."""
    if scale == "C":
        return value + T_ABSOLUTE
    if scale == "F":
        return (value - 32.0) * 5.0 / 9.0 + T_ABSOLUTE
    if scale == "K":
        return value
    raise ValueError(f"unknown temperature scale {scale!r}; use 'C', 'F' or 'K'")


def to_celsius(kelvin: float) -> float:
    """Convert kelvin to degrees Celsius."""
    return kelvin - T_ABSOLUTE


def thermal_equilibrium(temperatures, heat_capacity_ish=None) -> dict:
    """Whether a set of bodies is in thermal equilibrium.

    Thermal equilibrium means no net heat would flow between any two bodies in
    the set - which, by the zeroth law, means they all share one temperature.
    """
    values = [t for t in temperatures if t is not None]
    same = all(math.isclose(t, values[0], rel_tol=1e-9) for t in values) if values else False
    return {"in_equilibrium": same, "temperatures": values,
            "common_temperature": values[0] if same else None,
            "net_heat_flow": "none" if same else "from the hotter body to the colder one",
            "note": "Temperature is the quantity that decides the direction of heat "
                    "flow; heat is the energy that actually moves."}


HEAT_EXPERIMENTS = [
    {"experiment": "Two metal blocks, different temperatures, in contact",
     "observation": "A cold-handled thermometer warms; the warm block cools.",
     "conclusion": "Thermal energy passes from the hotter body to the colder one "
                   "even though no matter is transferred."},
    {"experiment": "A closed box with a fan switched on",
     "observation": "The temperature rises while the total energy inside is fixed.",
     "conclusion": "Energy is being shuffled about rather than created; the rise is "
                   "an increase in internal energy."},
    {"experiment": "Mixing hot and cold water in a calorimeter",
     "observation": "The final temperature settles between the two starting values.",
     "conclusion": "The energy that left the hot water entered the cold water: total "
                   "energy stayed constant (the first law in disguise)."},
    {"experiment": "A metal ball dropped into oil",
     "observation": "The oil warms and the ball cools until both settle.",
     "conclusion": "Heat is a form of transit energy: it has a source and a sink, "
                   "not just a temperature."},
    {"experiment": "Two thermometers dipped into the same beaker of water",
     "observation": "Both eventually read the same value and stay there.",
     "conclusion": "That shared reading is a temperature: a property of the state of "
                   "the body, not of the thermometer."},
]


# --------------------------------------------------------------------------
# 10.2  Ideal gas
# --------------------------------------------------------------------------

def boyles_law(p1: float, v1: float, p2: float) -> float:
    """``P_1 V_1 = P_2 V_2`` at constant temperature."""
    return p1 * v1 / p2 if p2 else float("inf")


def charles_law(v1: float, t1: float, t2: float) -> float:
    """``V_1 / T_1 = V_2 / T_2`` at constant pressure. Temperatures in kelvin."""
    return v1 * t2 / t1 if t1 else float("nan")


def ideal_gas_pressure(n: float, temperature: float, volume: float) -> float:
    """``P = n R T / V``."""
    return n * GAS_CONSTANT * temperature / volume if volume else float("inf")


def ideal_gas_state(pressure: float, volume: float, n: float = 1.0,
                    temperature: float | None = None) -> dict:
    """Fill in whichever of ``P``, ``V``, ``T`` or ``n`` is missing from ``PV = nRT``."""
    if temperature is None and pressure and volume:
        temperature = pressure * volume / (n * GAS_CONSTANT)
    return {"P": pressure, "V": volume, "n": n,
            "T": temperature if temperature is not None else float("nan"),
            "moles_from_PVT": pressure * volume / (GAS_CONSTANT * temperature)
            if temperature else float("nan")}


# --------------------------------------------------------------------------
# 10.3  Kinetic molecular theory
# --------------------------------------------------------------------------

KMT_POSTULATES = [
    "A gas is made of a very large number of tiny molecules whose total volume is "
    "negligible compared with the volume of the container.",
    "The molecules are in constant, random motion, so they strike the walls "
    "continuously - and that is what gas pressure is.",
    "Collisions between molecules, and with the walls, are perfectly elastic: no "
    "energy is lost in a collision.",
    "The time between collisions is negligible, so the molecules can be treated as "
    "moving in a straight line between collisions.",
    "The forces of attraction between molecules are negligible except at the "
    "instant of collision.",
    "The average kinetic energy of the molecules depends only on the temperature, "
    "not on which gas it is.",
]


def rms_speed(temperature: float, molar_mass: float) -> float:
    """Root-mean-square speed ``v_rms = sqrt(3 R T / M)`` in m s^-1."""
    return math.sqrt(3.0 * GAS_CONSTANT * temperature / molar_mass) if molar_mass else float("nan")


def mean_speed(temperature: float, molar_mass: float) -> float:
    """Mean speed ``v_bar = sqrt(8 R T / (pi M))`` - about 0.921 of the rms value."""
    return math.sqrt(8.0 * GAS_CONSTANT * temperature / (math.pi * molar_mass)) if molar_mass else float("nan")


def most_probable_speed(temperature: float, molar_mass: float) -> float:
    """Most probable speed ``v_mp = sqrt(2 R T / M)`` - the commonest single speed."""
    return math.sqrt(2.0 * GAS_CONSTANT * temperature / molar_mass) if molar_mass else float("nan")


def kinetic_pressure(n_molecules: float, molecule_mass: float, mean_square_speed: float,
                     volume: float = 1.0) -> float:
    """Pressure from the molecular model, ``PV = (1/3) N m <v^2>``.

    Dividing by the container volume gives the pressure,
    ``P = N m <v^2> / (3 V)``. With ``<v^2> = 3RT/M`` this reduces exactly to the
    ideal-gas law ``P = nRT / V``.
    """
    return n_molecules * molecule_mass * mean_square_speed / (3.0 * volume)


def kinetic_pressure_volume(n_molecules: float, molecule_mass: float,
                            mean_square_speed: float) -> float:
    """``PV = (1/3) N m <v^2>`` itself - the identity the syllabus asks you to derive."""
    return n_molecules * molecule_mass * mean_square_speed / 3.0


def average_translational_energy(temperature: float) -> float:
    """``KE = (3/2) k T`` for a single molecule, in joules."""
    return 1.5 * BOLTZMANN * temperature


def average_molecular_energy(n: float, temperature: float) -> float:
    """``(3/2) n R T`` for ``n`` moles - the same thing per mole."""
    return 1.5 * n * GAS_CONSTANT * temperature


KMT_COMPARISON = [
    {"gas": "Hydrogen (M = 0.002016)", "note": "Lightest molecule, so the fastest: the "
     "rms speed at 300 K is about 2030 m/s."},
    {"gas": "Helium (M = 0.004003)", "note": "Heavier than hydrogen but still the "
     "second fastest, and it is monatomic so its internal energy is purely translational."},
    {"gas": "Nitrogen (M = 0.028014)", "note": "A typical diatomic molecule: about "
     "517 m/s rms at 300 K."},
    {"gas": "Carbon dioxide (M = 0.044009)", "note": "Heavier than nitrogen and so slower, "
     "about 408 m/s rms at 300 K."},
    {"gas": "Water vapour (M = 0.018015)", "note": "Its rms speed is only about "
     "1.3 times that of hydrogen even though its mass is nine times greater, because "
     "speed depends on the square root of 1/M."},
]


# --------------------------------------------------------------------------
# 10.4  Internal energy and work
# --------------------------------------------------------------------------

def internal_energy(n: float, temperature: float, degrees_of_freedom: int = 3) -> float:
    """``U = (f/2) n R T`` - the sum of the kinetic energies of the molecules.

    ``degrees_of_freedom`` is 3 for a monatomic gas, 5 for a diatomic gas at
    ordinary temperatures, and 6 for a linear triatomic gas.
    """
    return 0.5 * degrees_of_freedom * n * GAS_CONSTANT * temperature


def dU_isothermal(n: float, degrees_of_freedom: int = 3) -> float:
    """Change in internal energy in an isothermal process: exactly zero."""
    return 0.0


def dU_isobaric(n: float, temperature_change: float, degrees_of_freedom: int = 3) -> float:
    """``dU = n C_v dT`` with ``C_v = (f/2) R``."""
    return 0.5 * degrees_of_freedom * n * GAS_CONSTANT * temperature_change


def dU_isochoric(n: float, temperature_change: float, degrees_of_freedom: int = 3) -> float:
    """The same as isobaric: at constant volume no work is done, so all the heat "
    "supplied goes into internal energy."""
    return dU_isobaric(n, temperature_change, degrees_of_freedom)


def work_by_gas(pressure: float, volume_change: float) -> float:
    """``W = P dV`` - work done by the gas during a change of volume at constant pressure.

    Positive when the gas expands and pushes the surroundings; negative when the
    surroundings squeeze the gas.
    """
    return pressure * volume_change


def work_series(points) -> float:
    """Work done by a gas following a path on the P-V diagram, by the trapezium rule.

    ``points`` is a list of ``(P, V)`` pairs in order. The area under the path is
    the work done by the gas; a path that folds back on itself cancels out.
    """
    if len(points) < 2:
        return 0.0
    total = 0.0
    for i in range(len(points) - 1):
        p1, v1 = points[i]
        p2, v2 = points[i + 1]
        total += 0.5 * (p1 + p2) * (v2 - v1)
    return total


def first_law(heat_supplied: float, work_done: float, degrees_of_freedom: int = 3,
              n: float = 1.0, temperature_change: float | None = None) -> dict:
    """``dU = Q - W`` - the change in internal energy equals heat in minus work out."""
    delta_u = heat_supplied - work_done
    predicted = dU_isobaric(n, temperature_change, degrees_of_freedom) if temperature_change else None
    return {"delta_U": delta_u, "Q": heat_supplied, "W": work_done,
            "dU_from_state_function": predicted,
            "consistent": None if predicted is None
            else math.isclose(delta_u, predicted, rel_tol=1e-9, abs_tol=1e-9),
            "statement": "Energy is conserved: heat added to the gas either raises its "
                         "internal energy or is spent pushing the surroundings."}


# --------------------------------------------------------------------------
# 10.5  The four common processes
# --------------------------------------------------------------------------

PROCESSES = [
    {"process": "Isothermal", "held_constant": "Temperature",
     "dU": 0, "W": "n R T ln(V2/V1)",
     "Q": "equals W",
     "why": "The internal energy of an ideal gas depends only on temperature, so "
            "with T fixed the internal energy cannot change. Heat supplied is spent "
            "entirely on work."},
    {"process": "Adiabatic", "held_constant": "No heat enters or leaves (Q = 0)",
     "dU": "n C_v dT", "W": "-dU, so W = (P1V1 - P2V2)/(gamma - 1)",
     "Q": 0,
     "why": "With no heat exchanged, the gas cools as it expands and heats as it is "
            "compressed. PV^gamma stays constant, so the curve is steeper than an "
            "isotherm."},
    {"process": "Isobaric", "held_constant": "Pressure",
     "dU": "n C_v dT", "W": "P dV", "Q": "n C_p dT",
     "why": "The gas pushes the surroundings out as it expands, so part of the heat "
            "supplied leaves as work."},
    {"process": "Isochoric", "held_constant": "Volume",
     "dU": "n C_v dT", "W": 0, "Q": "n C_v dT",
     "why": "The container is rigid, so the gas cannot expand and does no work. "
            "Every joule of heat supplied raises the temperature."},
]


# --------------------------------------------------------------------------
# 10.6  Specific heats
# --------------------------------------------------------------------------

HEAT_CAPACITIES = [
    {"gas": "Monatomic (He, Ne, Ar)", "cv": "3R/2", "cp": "5R/2", "gamma": 1.667,
     "cv_j": 12.47, "cp_j": 20.79,
     "why": "Three translational degrees of freedom and no rotation."},
    {"gas": "Diatomic (N2, O2, CO)", "cv": "5R/2", "cp": "7R/2", "gamma": 1.400,
     "cv_j": 20.79, "cp_j": 29.10,
     "why": "Three translational plus two rotational degrees of freedom. Vibrations "
            "stay frozen out at ordinary temperatures."},
    {"gas": "Polyatomic (CO2, H2O vapour)", "cv": "3R", "cp": "4R", "gamma": 1.333,
     "cv_j": 24.94, "cp_j": 33.26,
     "why": "Three translational plus three rotational degrees of freedom."},
]


def molar_heat_capacity(n_moles: float, heat_supplied: float,
                        temperature_change: float) -> float:
    """Molar heat capacity ``C = Q / (n dT)``, in J mol^-1 K^-1."""
    denominator = n_moles * temperature_change
    return heat_supplied / denominator if denominator else float("nan")


def cp_cv(degrees_of_freedom: int) -> dict:
    """``C_p``, ``C_v`` and ``gamma = C_p / C_v`` for a given number of degrees of freedom."""
    cv = 0.5 * degrees_of_freedom * GAS_CONSTANT
    cp = cv + GAS_CONSTANT
    return {"cv": cv, "cp": cp, "gamma": cp / cv, "degrees_of_freedom": degrees_of_freedom,
            "difference": cp - cv}


def mayers_relation(degrees_of_freedom: int = 5) -> dict:
    """``Cp - Cv = R``, proved from the first law.

    Heating one mole at constant pressure by dT needs ``Cp dT``. At constant
    volume the same rise needs ``Cv dT``; the extra ``(Cp - Cv) dT`` has gone
    into the work of expansion, which is ``P dV = R dT`` by the ideal gas law.
    """
    result = cp_cv(degrees_of_freedom)
    work_term = GAS_CONSTANT
    return {
        **result,
        "proof": [f"Heating 1 mole at constant pressure by dT needs C_p dT.",
                  f"Heating 1 mole at constant volume by dT needs C_v dT.",
                  "The difference is the work done as the gas expands: (C_p - C_v) dT.",
                  "From P dV = R dT for one mole, that work is R dT.",
                  "Therefore C_p - C_v = R."],
        "result": f"C_p - C_v = {result['difference']:.4f} J mol^-1 K^-1, "
                  f"and R = {GAS_CONSTANT:.4f} J mol^-1 K^-1.",
        "work_term": work_term,
    }


# --------------------------------------------------------------------------
# 10.7 and 10.8  Reversible processes and the second law
# --------------------------------------------------------------------------

REVERSIBLE_PROCESSES = [
    {"process": "A frictionless piston compressing a gas slowly", "reversible": True,
     "why": "With no friction and no pressure difference, an infinitesimal change "
            "can be undone exactly."},
    {"process": "Freezing water at 0 degrees C", "reversible": True,
     "why": "It happens at a single temperature, so heat can be removed again "
            "with no net change."},
    {"process": "A gas expanding into a vacuum", "reversible": False,
     "why": "Nothing external changes, so the gas cannot be pushed back without "
            "doing work it cannot recover."},
    {"process": "Friction turning kinetic energy into heat", "reversible": False,
     "why": "The heat spreads into the surroundings and cannot be collected back."},
    {"process": "A hot cup of tea cooling in a room", "reversible": False,
     "why": "Heat flows from hot to cold on its own and never the other way round."},
    {"process": "Two gases mixing", "reversible": False,
     "why": "They will not separate themselves again without work."},
    {"process": "An electric current through a resistor", "reversible": False,
     "why": "Joule heating raises the surroundings' entropy."},
]


ENTROPY_POINTS = [
    {"statement": "Entropy measures how many microscopic arrangements are compatible "
                  "with the macroscopic state.",
     "meaning": "A gas filling a room has far more accessible arrangements than the "
                "same gas confined to one corner, so it has a larger entropy."},
    {"statement": "Entropy change of an isolated system is never negative.",
     "meaning": "The total entropy of a system plus its surroundings cannot fall. "
                "This is the second law written as a single statement."},
    {"statement": "Entropy can decrease locally.",
     "meaning": "Your desk tidies itself, and water freezes into ice, because the "
                "surroundings gain more entropy than the region loses."},
    {"statement": "Heat flows from hot to cold.",
     "meaning": "If heat went the other way on its own, the total entropy of the "
                "universe would decrease, which never happens."},
    {"statement": "Friction always produces entropy.",
     "meaning": "Work that would otherwise be recoverable is degraded into heat "
                "that spreads through the environment."},
    {"statement": "An increase in temperature raises entropy.",
     "meaning": "Faster molecules have far more accessible arrangements, so the "
                "entropy of a gas rises with temperature even at constant volume."},
]


# --------------------------------------------------------------------------
# 10.9  Carnot engine
# --------------------------------------------------------------------------

def carnot_efficiency(th: float, tc: float) -> dict:
    """``eta = 1 - T_c / T_h``. Both temperatures must be in kelvin.

    A Carnot engine is the most efficient engine that can ever operate between
    two reservoirs, so no other engine can do better.
    """
    if th <= 0:
        return {"error": "The hot reservoir must be above absolute zero."}
    if tc >= th:
        return {"error": "The cold reservoir cannot be hotter than the hot one."}
    eta = 1.0 - tc / th
    return {"efficiency": eta, "efficiency_percent": 100.0 * eta,
            "th": th, "tc": tc, "carnot_temperature": -tc * eta,
            "hot_heat_in": th, "cold_heat_out": tc,
            "note": f"Even this ideal engine wastes {(1 - eta) * 100:.1f} % of the heat "
                    f"it takes in; that waste is unavoidable in principle, not just "
                    f"in practice."}


def carnot_corners(v1: float, v2: float, p1: float, adiabatic_ratio: float = 1.8,
                   gamma: float = 5.0 / 3.0) -> dict:
    """The four corner points of a Carnot cycle on a P-V diagram.

    Given the start point 1 = (V1, P1) and the end of the hot isotherm
    2 = (V2, P2) with ``P1 V1 = P2 V2``, the other two corners follow from the
    two adiabatic legs, along which ``P V^gamma`` is constant.

    Returns the corner points together with the hot and cold reservoir
    temperatures they sit at, found from ``T = P V / (n R)``.
    """
    p2 = p1 * v1 / v2
    v3 = v2 * adiabatic_ratio
    p3 = p2 * (v2 / v3) ** gamma          # adiabatic expansion 2 -> 3
    v4 = (p1 * v1 ** gamma / (p3 * v3)) ** (1.0 / (gamma - 1.0))
    p4 = p3 * v3 / v4                      # cold isotherm 3 -> 4

    return {
        "1": {"V": v1, "P": p1, "T": p1 * v1, "step": "start of the hot isothermal expansion"},
        "2": {"V": v2, "P": p2, "T": p2 * v2, "step": "end of the hot isothermal expansion"},
        "3": {"V": v3, "P": p3, "T": p3 * v3, "step": "end of the adiabatic expansion"},
        "4": {"V": v4, "P": p4, "T": p4 * v4, "step": "end of the cold isothermal compression"},
        "gamma": gamma, "adiabatic_ratio": adiabatic_ratio,
    }


def carnot_cycle(p1: float, v1: float, v2: float,
                 adiabatic_ratio: float = 1.8) -> list:
    """A description of the four processes of the Carnot cycle."""
    c = carnot_corners(v1, v2, p1, adiabatic_ratio)
    return [
        {"step": "1 -> 2", "name": "Isothermal expansion at T_h",
         "from": {"P": c["1"]["P"], "V": c["1"]["V"]},
         "to": {"P": c["2"]["P"], "V": c["2"]["V"]},
         "what": "The gas expands at the hot temperature and takes in heat Q_h. Its "
                 "internal energy does not change, so the work it does equals Q_h.",
         "check": "P1 V1 = P2 V2, so T is the same at both ends."},
        {"step": "2 -> 3", "name": "Adiabatic expansion",
         "from": {"P": c["2"]["P"], "V": c["2"]["V"]},
         "to": {"P": c["3"]["P"], "V": c["3"]["V"]},
         "what": "No heat is exchanged. The gas does work on its own account and "
                 "cools from T_h to T_c.",
         "check": "P V^gamma is constant, so this leg is steeper than the isotherm."},
        {"step": "3 -> 4", "name": "Isothermal compression at T_c",
         "from": {"P": c["3"]["P"], "V": c["3"]["V"]},
         "to": {"P": c["4"]["P"], "V": c["4"]["V"]},
         "what": "The gas is squeezed at the cold temperature and rejects heat Q_c. "
                 "The work done on it is exactly Q_c.",
         "check": "P3 V3 = P4 V4, so T is the same at both ends."},
        {"step": "4 -> 1", "name": "Adiabatic compression",
         "from": {"P": c["4"]["P"], "V": c["4"]["V"]},
         "to": {"P": c["1"]["P"], "V": c["1"]["V"]},
         "what": "No heat is exchanged. The compressed gas heats back from T_c to "
                 "T_h and the cycle closes.",
         "check": "P V^gamma is constant, and the gas returns to its starting point."},
    ]


def carnot_cycle_series(p1: float = 1.0e5, v1: float = 1.0, volume_ratio: float = 4.0,
                        adiabatic_ratio: float = 1.8, samples: int = 140) -> dict:
    """The Carnot cycle as a closed P-V path ready for plotting.

    The two adiabatic legs use ``gamma = 5/3`` for a monatomic ideal gas, so
    ``P V^gamma`` is constant along them.
    """
    n = max(8, int(samples))
    c = carnot_corners(v1, v1 * volume_ratio, p1, adiabatic_ratio)
    gamma = c["gamma"]

    def leg(v_from, v_to, p_from, mode):
        vs = [v_from + (v_to - v_from) * i / (n - 1) for i in range(n)]
        if mode == "isothermal":
            ps = [p_from * v_from / v for v in vs]
        else:
            ps = [p_from * (v_from / v) ** gamma for v in vs]
        return {"V": vs, "P": ps}

    hot = leg(c["1"]["V"], c["2"]["V"], c["1"]["P"], "isothermal")
    ad1 = leg(c["2"]["V"], c["3"]["V"], c["2"]["P"], "adiabatic")
    cold = leg(c["3"]["V"], c["4"]["V"], c["3"]["P"], "isothermal")
    ad2 = leg(c["4"]["V"], c["1"]["V"], c["4"]["P"], "adiabatic")

    # The enclosed area is the net work done in one cycle, found by the
    # trapezium rule around the closed path.
    area = 0.0
    for trace in (hot, ad1, cold, ad2):
        for i in range(len(trace["V"]) - 1):
            area += 0.5 * (trace["P"][i] + trace["P"][i + 1]) * (trace["V"][i + 1] - trace["V"][i])

    return {
        "hot_isothermal": hot,
        "adiabatic_expansion": ad1,
        "cold_isothermal": cold,
        "adiabatic_compression": ad2,
        "corners": c,
        "th": c["1"]["T"], "tc": c["4"]["T"],
        "gamma": gamma,
        "enclosed_area": area,
        "net_work_area": area,
        "note": "1->2 isothermal expansion, 2->3 adiabatic expansion, 3->4 isothermal "
                "compression, 4->1 adiabatic compression. The enclosed area is the net "
                "work done in one cycle.",
    }

def heat_engine_summary() -> dict:
    """Why an engine needs two reservoirs and can never be perfect."""
    return {
        "input": "Heat Q_h from the hot reservoir",
        "output": "Work W done by the engine",
        "waste": "Heat Q_c dumped into the cold reservoir",
        "balance": "W = Q_h - Q_c, so eta = W / Q_h = 1 - Q_c / Q_h",
        "carnot_limit": "Since Q_c / Q_h must be at least T_c / T_h, no engine can "
                        "exceed eta = 1 - T_c / T_h.",
        "second_law": "It is impossible for any device to extract heat from a single "
                      "reservoir and convert it wholly into work.",
    }


# --------------------------------------------------------------------------
# 10.10  Refrigerator
# --------------------------------------------------------------------------

def refrigerator_cop(tc: float, th: float) -> dict:
    """Coefficient of performance ``COP = Q_c / W`` for an ideal (Carnot) refrigerator."""
    if th <= tc:
        return {"error": "The inside of a refrigerator must be colder than the room."}
    gap = th - tc
    return {"cop": tc / gap, "th": th, "tc": tc,
            "note": f"A refrigerator that has to work against a {gap:.1f} K temperature "
                    f"difference has a Carnot coefficient of performance of "
                    f"{tc / gap:.1f} - and a real one does worse."}


# --------------------------------------------------------------------------
# 10.11  Entropy
# --------------------------------------------------------------------------

def entropy_change_ideal_gas(n: float, t1: float, t2: float,
                             v1: float, v2: float,
                             degrees_of_freedom: int = 3) -> float:
    """``dS = n C_v ln(T2/T1) + n R ln(V2/V1)`` in J K^-1.

    Entropy is a state function, so this depends only on the two end states and
    not on the route taken between them.
    """
    cv = 0.5 * degrees_of_freedom * GAS_CONSTANT
    return n * cv * math.log(t2 / t1) + n * GAS_CONSTANT * math.log(v2 / v1)


def entropy_change_process(n: float, heat: float, temperature: float) -> float:
    """``dS = Q_rev / T`` for a reversible change heated by ``heat`` joules."""
    return heat / temperature if temperature else float("nan")


def energy_degradation() -> list:
    """Why "energy is lost" always means energy is degraded, never destroyed."""
    return [
        {"process": "A book falling to the floor",
         "lost": "The organised movement of the book becomes random motion of air and floor.",
         "why_it_cannot_come_back": "Random microscopic motion cannot be lined up again "
                                    "by chance, so the energy cannot be made to do the "
                                    "same work again."},
        {"process": "Friction in a bicycle brake",
         "lost": "Kinetic energy becomes heat in the brake pads.",
         "why_it_cannot_come_back": "The hot pads radiate it away into the surroundings; "
                                    "gathering it back would cost more than it is worth."},
        {"process": "An electric motor",
         "lost": "A small fraction of the electrical energy becomes heat in the windings.",
         "why_it_cannot_come_back": "That heat is carried away and dispersed, so the "
                                    "quality of the energy is degraded."},
        {"process": "A battery discharging",
         "lost": "Chemical energy becomes electrical energy, then heat in the circuit.",
         "why_it_cannot_come_back": "Recharging requires at least as much work as the "
                                    "discharge delivered, because of the losses."},
    ]


environment_notes = [
    {"issue": "Pollution", "entropy_link": "Dissipating heat and spreading waste raise "
     "the entropy of the surroundings faster than any useful work can be obtained."},
    {"issue": "Resource depletion", "entropy_link": "Useful concentrated minerals are "
     "scarce and spread out when used; re-concentrating them costs energy."},
    {"issue": "Greenhouse gases", "entropy_link": "They let solar energy in but slow its "
     "escape back out, so the system heats up instead of running in equilibrium."},
    {"issue": "Species extinction", "entropy_link": "Biodiversity is an ordering of "
     "information; losing it raises the total entropy of the biosphere."},
    {"issue": "Nuclear power", "entropy_link": "It is a very high-grade source - it "
     "delivers enormously more work per joule of heat than burning fuel."},
]


DESIGN_TASK = [
    {"step": "1. Name the job", "detail": "State clearly what your device must do and "
     "what it must not do."},
    {"step": "2. Draw the energy flow", "detail": "Mark every energy stream as heat in, "
     "work out, and heat rejected to the surroundings. A complete diagram always "
     "balances: Q_h = W + Q_c."},
    {"step": "3. Check the temperature gap", "detail": "Every real device works against "
     "a temperature difference, so its efficiency is bounded by 1 - T_c / T_h."},
    {"step": "4. Look for the leaks", "detail": "Friction, heat conduction, radiation "
     "and mixing are all entropy leaks; each one makes the real efficiency lower."},
    {"step": "5. State the trade-off", "detail": "Insulating better, running colder or "
     "using a bigger heat exchanger all cost money, size or power. Say which you chose."},
    {"step": "6. Quote numbers", "detail": "Give the measured efficiency and compare it "
     "with the Carnot limit so the room for improvement is obvious."},
]
