"""Chapter 5 - Deformation in Solids.

Types of solid, the elastic limit, stress, strain, Young's modulus and the
elastic potential energy stored in a deformed material.

Pure Python: no Streamlit, pandas, NumPy or Plotly.
"""

from __future__ import annotations

import math

__all__ = [
    "SOLID_CLASSES", "MATERIALS", "stress", "strain", "young_modulus",
    "length_change", "stress_strain_series", "region_of", "elastic_limit",
    "linear_extension", "elastic_energy_from_force", "elastic_energy_from_k",
    "energy_density", "wire_energy", "strain_energy_in_column",
]


# --------------------------------------------------------------------------
# 5.1  Types of solids
# --------------------------------------------------------------------------

SOLID_CLASSES = [
    {"class": "Crystalline", "order": "Long-range regular",
     "examples": "Quartz, diamond, ice, sodium chloride, most metals",
     "behaviour": "Sharp melting point; may be brittle or ductile",
     "example": "Sugar dissolves as crystals; a diamond is the hardest natural solid."},
    {"class": "Amorphous", "order": "No long-range order",
     "examples": "Glass, wax, plastics, rubber",
     "behaviour": "Softens gradually over a range instead of melting sharply",
     "example": "Old window glass is thicker at the bottom because it has flowed "
                "slowly over centuries - a sign it is not crystalline."},
    {"class": "Polymeric", "order": "Very long chains, cross-linked or not",
     "examples": "Polyethene, rubber, nylon, PVC, proteins",
     "behaviour": "Chains slide past one another; large reversible extension "
                  "before breaking",
     "example": "Stretching rubber warms it: stretching a polymer does work on "
                "its molecules, which raises their energy."},
]


# --------------------------------------------------------------------------
# 5.4  Stress, strain and Young's modulus
# --------------------------------------------------------------------------

#: Representative engineering values at room temperature. Young's modulus is in
#: pascals; yield stress is the point where the curve first bends away from
#: the straight line. Values vary with purity, processing and temperature, so
#: they are teaching figures rather than specification data.
MATERIALS = [
    {"name": "Steel", "youngs_modulus": 2.0e11, "yield_stress": 2.5e8,
     "ultimate_stress": 5.0e8, "fracture_strain": 0.22,
     "note": "Stiff and strong; springs and structural beams are made of it."},
    {"name": "Copper", "youngs_modulus": 1.1e11, "yield_stress": 7.0e7,
     "ultimate_stress": 2.2e8, "fracture_strain": 0.45,
     "note": "Very ductile - it stretches more than 40 % before breaking."},
    {"name": "Aluminium", "youngs_modulus": 7.0e10, "yield_stress": 2.8e8,
     "ultimate_stress": 4.0e8, "fracture_strain": 0.20,
     "note": "Light and stiff for its density, which is why aircraft use it."},
    {"name": "Glass", "youngs_modulus": 5.5e10, "yield_stress": 5.0e8,
     "ultimate_stress": 5.0e8, "fracture_strain": 0.001,
     "note": "Almost no plastic region - it is brittle and shatters."},
    {"name": "Wood (along the grain)", "youngs_modulus": 1.1e10, "yield_stress": 4.0e7,
     "ultimate_stress": 1.0e8, "fracture_strain": 0.02,
     "note": "Very different stiffness across the grain - a material property "
             "that depends on direction."},
    {"name": "Rubber (natural)", "youngs_modulus": 5.0e6, "yield_stress": 2.0e6,
     "ultimate_stress": 3.0e7, "fracture_strain": 7.0,
     "note": "Enormously extensible and almost perfectly elastic; the curve is "
             "strongly non-Hookean beyond small strains."},
]


def stress(force: float, area: float) -> float:
    """Stress ``sigma = F / A``, in pascals.

    Stress is force spread over the cross-section that resists it. Doubling the
    area halves the stress for the same load.
    """
    return force / area if area else float("inf")


def strain(change_in_length: float, original_length: float) -> float:
    """Strain ``epsilon = dL / L``. It has no unit and is often quoted as a percentage."""
    return change_in_length / original_length if original_length else float("nan")


def young_modulus(normal_stress: float, tensile_strain: float) -> float:
    """Young's modulus ``Y = stress / strain``, in pascals.

    It is large for stiff materials: a steel wire stretches about 1 mm under
    1 kg per square millimetre, while rubber stretches by the same fraction
    many thousands of times over.
    """
    return normal_stress / tensile_strain if tensile_strain else float("inf")


def length_change(force: float, original_length: float, cross_section: float,
                  modulus: float) -> float:
    """Extension of a uniform wire: ``dL = F L / (A Y)``."""
    return force * original_length / (cross_section * modulus) if cross_section * modulus else float("inf")


def elastic_limit(series) -> float:
    """The largest strain still on the straight part of the curve."""
    return series["elastic_strain"]


def region_of(series, strain_value: float) -> dict:
    """Which part of the stress-strain curve a given strain lies in."""
    if strain_value <= series["elastic_strain"]:
        name, note = "Elastic", ("Remove the load and the wire returns exactly to "
                                 "its original length.")
    elif strain_value <= series["yield_strain"]:
        name, note = "Yielding", ("Past the elastic limit the wire no longer returns "
                                   "to its original length.")
    elif strain_value <= series["ultimate_strain"]:
        name, note = "Plastic (strain hardening)", ("The wire keeps stretching but the "
                                                    "stress rises more slowly.")
    else:
        name, note = "Necking and fracture", ("A thin neck forms, then the wire snaps.")
    return {"region": name, "note": note, "strain": strain_value}


def stress_strain_series(material, samples: int = 140) -> dict:
    """A realistic force-extension curve for one of :data:`MATERIALS`.

    Three regions are joined: a straight elastic rise, a yield knee followed by
    strain hardening, and a final drop as a neck forms and the bar breaks.

    A brittle material such as glass is handled separately: its calculated yield
    strain would fall beyond its fracture strain, which is exactly what "brittle"
    means - it snaps while still on the straight line and never reaches a yield
    point at all. Those curves are drawn as elastic throughout and labelled
    ``brittle``.

    The curve is generated from the material's yield stress and a chosen
    strain-hardening behaviour rather than fitted to measured data, and is
    labelled as simulated wherever it is shown.
    """
    if isinstance(material, str):
        material = next(m for m in MATERIALS if m["name"] == material)
    modulus = material["youngs_modulus"]
    yield_stress = material["yield_stress"]
    ultimate = material["ultimate_stress"]
    fracture = material["fracture_strain"]
    n = max(4, int(samples))

    elastic_strain = yield_stress / modulus
    brittle = elastic_strain >= fracture
    if brittle:
        # The stress reached at fracture is set by Hooke's law all the way along.
        ultimate = modulus * fracture
        elastic_limit = fracture
        yield_point = fracture
        ultimate_strain = fracture
    else:
        elastic_limit = elastic_strain
        yield_point = elastic_strain * 1.25
        ultimate_strain = min(0.55 * fracture, yield_point * 1.6)

    # The elastic region can be a thousandth of the total strain (steel) or most
    # of it (rubber), so a uniform grid either hides the elastic branch or wastes
    # the plot. Sample geometrically close to zero, then at every landmark the
    # station teaches, then uniformly out to fracture.
    near_zero = [fracture * 0.0005 * (1.6 ** i) for i in range(12)]
    evenly = [fracture * i / (n - 1) for i in range(n)]
    marks = sorted({round(min(x, fracture), 12)
                    for x in near_zero + [elastic_limit, yield_point, ultimate_strain,
                                          fracture] + evenly})

    strains, stresses, regions = [], [], []
    for e in marks:
        if brittle or e <= elastic_limit:
            s = modulus * e
            regions.append("Elastic")
        elif e <= yield_point:
            span = ultimate_strain - elastic_limit
            blend = (e - elastic_limit) / span if span else 0.0
            s = yield_stress + (ultimate - yield_stress) * (0.35 * blend + 0.65 * blend ** 2)
            regions.append("Plastic")
        elif e <= ultimate_strain:
            span = ultimate_strain - yield_point
            blend = (e - yield_point) / span if span else 0.0
            s = yield_stress + (ultimate - yield_stress) * (0.35 + 0.65 * blend ** 1.4)
            regions.append("Plastic")
        else:
            span = fracture - ultimate_strain
            fall = (e - ultimate_strain) / span if span else 0.0
            s = ultimate * (1.0 - 0.62 * fall ** 1.6)
            regions.append("Fracture")
        strains.append(e)
        stresses.append(s)

    return {
        "material": material["name"], "strain": strains, "stress": stresses,
        "regions": regions, "youngs_modulus": modulus,
        "elastic_strain": elastic_limit, "yield_strain": yield_point,
        "ultimate_strain": ultimate_strain, "fracture_strain": fracture,
        "yield_stress": yield_stress, "ultimate_stress": ultimate,
        "brittle": brittle,
        "resilience": yield_stress ** 2 / (2.0 * modulus),
        "modulus": modulus, "fracture_stress": stresses[-1],
    }


# --------------------------------------------------------------------------
# 5.5  Elastic potential energy
# --------------------------------------------------------------------------

def elastic_energy_from_force(maximum_force: float, extension: float) -> float:
    """``E = (1/2) F x`` - the area under the straight part of an F-x graph."""
    return 0.5 * maximum_force * extension


def elastic_energy_from_k(k: float, extension: float) -> float:
    """``E = (1/2) k x^2`` for a material obeying Hooke's law."""
    return 0.5 * k * extension ** 2


def energy_density(normal_stress: float, tensile_strain: float) -> float:
    """Elastic energy per unit volume ``u = (1/2) sigma epsilon``, in J m^-3."""
    return 0.5 * normal_stress * tensile_strain


def wire_energy(force: float, original_length: float, cross_section: float,
                modulus: float) -> dict:
    """Energy stored in a uniformly stretched wire.

    Using ``dL = F L / (A Y)`` and ``E = (1/2) F dL`` gives
    ``E = F^2 L / (2 A Y)``.
    """
    dL = length_change(force, original_length, cross_section, modulus)
    energy = 0.5 * force * dL
    return {"extension": dL, "energy": energy,
            "energy_density": energy_density(stress(force, cross_section),
                                             strain(dL, original_length)),
            "resilience_percent": 100.0 * energy_density(stress(force, cross_section),
                                                         strain(dL, original_length))
            / (stress(force, cross_section) ** 2 / (2.0 * modulus))}


def strain_energy_in_column(mass: float, height: float, base_area: float,
                            g: float = 9.8) -> dict:
    """Gravitational energy of a uniform column, for comparison with elastic energy."""
    total = mass * g * height
    return {"weight": mass * g, "energy": total, "height": height,
            "base_area": base_area,
            "pressure": mass * g / base_area if base_area else float("inf")}
