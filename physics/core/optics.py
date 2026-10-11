"""Chapter 9 - Physical Optics.

The wave-front and Huygens' principle, interference of light, Young's double
slit, Michelson's interferometer and gravitational waves, diffraction by slits
and gratings, Bragg's law and polarisation.

Pure Python: no Streamlit, pandas, NumPy or Plotly.
"""

from __future__ import annotations

import math

__all__ = [
    "WAVELENGTHS", "LIGHT_VIEWS", "HUYGENS_STEPS", "huygens_point",
    "huygens_secondary", "COHERENCE_CONDITIONS", "fringe_width",
    "fringe_positions", "optical_path", "constructive_condition",
    "destructive_condition", "single_slit_minima", "central_maximum_width",
    "grating_angles", "grating_resolving_power", "BRAGG_EXAMPLES",
    "bragg_angle", "bragg_order", "xray_diffraction_series", "MALUS_TABLE",
    "malus_law", "two_polarisers", "brewster_angle", "polarisation_uses",
    "lens_image", "magnification", "interference_pattern",
]

#: Representative visible wavelengths, in metres.
WAVELENGTHS = [
    {"colour": "Violet", "wavelength": 3.8e-7, "range": "380-450 nm",
     "note": "The shortest visible wavelength."},
    {"colour": "Blue", "wavelength": 4.5e-7, "range": "450-495 nm", "note": ""},
    {"colour": "Green", "wavelength": 5.3e-7, "range": "495-570 nm",
     "note": "The eye is most sensitive here, so green looks brightest."},
    {"colour": "Yellow", "wavelength": 5.7e-7, "range": "570-590 nm", "note": ""},
    {"colour": "Orange", "wavelength": 6.2e-7, "range": "590-620 nm", "note": ""},
    {"colour": "Red", "wavelength": 6.5e-7, "range": "620-750 nm",
     "note": "The longest visible wavelength."},
    {"colour": "Infrared", "wavelength": 1.0e-6, "range": "beyond 750 nm",
     "note": "Felt as heat; used in remote controls and thermal imaging."},
    {"colour": "Ultraviolet", "wavelength": 4.0e-8, "range": "below 380 nm",
     "note": "Sunburn, sterilisation and the ozone layer."},
    {"colour": "X-rays", "wavelength": 1.0e-10, "range": "about 0.1 nm",
     "note": "Diffraction through crystals revealed the structure of DNA."},
    {"colour": "Gamma rays", "wavelength": 1.0e-12, "range": "about 1 pm",
     "note": "From radioactive nuclei; the shortest wavelengths of all."},
]


# --------------------------------------------------------------------------
# 9.1  Nature of light and Huygens' principle
# --------------------------------------------------------------------------

LIGHT_VIEWS = [
    {"view": "Newton's corpuscular theory (1672)",
     "claim": "Light is a stream of tiny particles.",
     "evidence_for": "Straight-line travel, shadows and the speed of light in vacuum "
                     "are all explained by particles.",
     "evidence_against": "It cannot explain interference, diffraction or why light "
                         "bends as it passes from air into water."},
    {"view": "Huygens' wave theory (1678)",
     "claim": "Light is a wave in a continuous medium called the aether.",
     "evidence_for": "Explains interference, diffraction and refraction.",
     "evidence_against": "Light travels through a vacuum, where there is supposedly "
                         "no aether to carry the wave."},
    {"view": "Maxwell's electromagnetic theory (1864)",
     "claim": "Light is an electromagnetic wave that needs no medium at all.",
     "evidence_for": "Predicts the speed of light from electric and magnetic "
                     "constants, and predicts the whole spectrum including radio waves.",
     "evidence_against": "Says nothing about why light behaves as particles in some "
                         "experiments."},
    {"view": "Einstein's quantum theory (1905)",
     "claim": "Light is exchanged in packets called photons, each of energy h f.",
     "evidence_for": "Explains the photoelectric effect, where electrons are ejected "
                     "only when the frequency is high enough, however weak the beam.",
     "evidence_against": "Photons are not localised lumps on their own; they behave "
                         "as particles only in detection events."},
    {"view": "Wave-particle duality (today)",
     "claim": "Light is neither: quantum electrodynamics treats light as quantum "
              "fields whose excitations are photons, and every prediction can be made "
              "either in wave terms or photon terms.",
     "evidence_for": "Interference gives way to a definite detection event one photon "
                     "at a time, and the pattern builds up photon by photon.",
     "evidence_against": "No experiment separates the two pictures - which is the point."},
]

HUYGENS_STEPS = [
    "Every point on a wavefront acts as a source of tiny secondary wavelets.",
    "Each wavelet spreads out in all directions at the speed of the wave in that medium.",
    "After a short time the new position of the wavefront is the envelope touching "
    "all the secondary wavelets - the common tangent to them.",
    "The direction of the envelope gives the new direction of travel, so the wavefront "
    "bends where it enters a new medium.",
]


def huygens_point(radius: float, distance: float, phase: float = 0.0,
                  samples: int = 60) -> dict:
    """Positions of secondary wavelets from points along a wavefront.

    ``radius`` is the size of the original wavefront, ``distance`` how far the
    wavelets have travelled. Only points on the wavefront send out wavelets,
    which is why the new wavefront is narrower than a full circle.
    """
    n = max(3, int(samples))
    points = []
    for i in range(n):
        angle = math.pi * i / (n - 1)
        points.append((radius * math.cos(angle) - distance,
                       radius * math.sin(angle), math.pi * i / (n - 1) + phase))
    return {"source_points": points, "radius": radius, "distance": distance,
            "wavefront_x": radius - distance}


def huygens_secondary(front_radius: float, distance: float) -> list:
    """The secondary wavelets themselves, as circles ready for drawing."""
    n = 9
    circles = []
    for i in range(n):
        y = -front_radius + 2.0 * front_radius * i / (n - 1)
        span = math.sqrt(max(front_radius ** 2 - y ** 2, 0.0))
        circles.append({"y": y, "x": span, "origin_x": 0.0, "distance": distance})
    return circles


# --------------------------------------------------------------------------
# 9.2  Interference of light
# --------------------------------------------------------------------------

COHERENCE_CONDITIONS = [
    {"condition": "Coherent sources",
     "requirement": "The two sources must keep a constant phase difference.",
     "why": "Interference needs a fixed relationship between the two waves. Two "
            "ordinary lamps drift in phase with each other many times a second, so "
            "the bright and dark bands wash out into a steady glow."},
    {"condition": "Same frequency",
     "requirement": "Both waves must have the same wavelength.",
     "why": "If the frequencies differ, the pattern moves rather than standing still."},
    {"condition": "Comparable amplitude",
     "requirement": "The two amplitudes should be of the same order.",
     "why": "With very different amplitudes the minima never reach zero and the "
            "fringes are hard to see."},
    {"condition": "Small path difference compared with the coherence length",
     "requirement": "The two paths must be nearly equal.",
     "why": "Any optical path difference includes light scattered from the source, "
            "which destroys the phase relationship for large differences."},
]


def fringe_width(wavelength_value: float, distance: float, slit_separation: float) -> float:
    """Fringe spacing in Young's experiment: ``dy = lambda L / d``."""
    return wavelength_value * distance / slit_separation if slit_separation else float("nan")


def fringe_positions(wavelength_value: float, distance: float, slit_separation: float,
                     count: int = 9) -> list:
    """Positions of the bright fringes, measured from the central maximum."""
    width = fringe_width(wavelength_value, distance, slit_separation)
    return [{"n": n, "y": n * width, "kind": "bright"} for n in range(-count, count + 1)]


def optical_path(wavelength_value: float, path: float) -> float:
    """Number of wavelengths contained in a path: used to spot the fringe order."""
    return path / wavelength_value if wavelength_value else float("nan")


def constructive_condition(path_difference: float, wavelength_value: float) -> bool:
    """Bright fringe when the path difference is a whole number of wavelengths."""
    if wavelength_value == 0:
        return False
    return math.isclose((path_difference % wavelength_value) / wavelength_value, 0.0, abs_tol=1e-9)


def destructive_condition(path_difference: float, wavelength_value: float) -> bool:
    """Dark fringe when the path difference is a half number of wavelengths."""
    if wavelength_value == 0:
        return False
    return math.isclose((path_difference % wavelength_value) / wavelength_value, 0.5, abs_tol=1e-9)


def interference_pattern(wavelength_value: float, slit_separation: float,
                         screen_distance: float, extent: float = 0.006,
                         samples: int = 500) -> dict:
    """The bright-and-dark intensity pattern of Young's double slit."""
    n = max(3, int(samples))
    step = 2.0 * extent / (n - 1)
    ys = [i * step - extent for i in range(n)]
    return {
        "y": ys,
        "intensity": [math.cos(math.pi * slit_separation * y
                               / (wavelength_value * screen_distance)) ** 2
                      for y in ys],
        "fringe_width": fringe_width(wavelength_value, screen_distance, slit_separation),
    }


# --------------------------------------------------------------------------
# 9.4  Diffraction
# --------------------------------------------------------------------------

def single_slit_minima(slit_width: float, wavelength_value: float, m: int = 1) -> dict:
    """``a sin(theta) = m lambda`` - the direction of the m-th dark fringe."""
    ratio = m * wavelength_value / slit_width
    if abs(ratio) > 1:
        return {"error": f"Order m = {m} cannot occur; a sin(theta) cannot exceed {ratio:.3g}."}
    theta = math.degrees(math.asin(ratio))
    return {"m": m, "theta_deg": theta, "sin_theta": ratio,
            "position_ratio": ratio,
            "note": "sin(theta) = m lambda / a, so the pattern widens with wavelength "
                    "and narrows with slit width."}


def central_maximum_width(slit_width: float, wavelength_value: float) -> dict:
    """Angular width of the central bright band: ``2 lambda / a``."""
    first = single_slit_minima(slit_width, wavelength_value, 1)
    if "error" in first:
        return first
    return {"width_ratio": 2.0 * first["sin_theta"],
            "width_deg": 2.0 * first["theta_deg"],
            "note": "The central maximum is twice as wide as every other bright band, "
                    "because it is bounded by minima on both sides."}


def grating_angles(grating_element: float, wavelength_value: float,
                   max_order: int = 4) -> list:
    """Directions of the principal maxima of a diffraction grating, ``d sin(theta) = m lambda``."""
    rows = []
    for m in range(0, max(1, int(max_order)) + 1):
        ratio = m * wavelength_value / grating_element
        if ratio > 1:
            rows.append({"m": m, "exists": False,
                         "note": "This order cannot exist: sin(theta) would exceed 1."})
        else:
            rows.append({"m": m, "exists": True, "sin_theta": ratio,
                         "theta_deg": math.degrees(math.asin(ratio)),
                         "note": "Sharp and bright, because many slits contribute in phase."})
    return rows


def grating_resolving_power(order: int, lines: int) -> dict:
    """``R = lambda / dlambda = m N`` - how close two wavelengths a grating can separate."""
    return {"R": order * lines, "order": order, "lines": lines,
            "separates": f"Two wavelengths differing by about 1/{order * lines} of their "
                         f"mean value can just be told apart."}


# --------------------------------------------------------------------------
# 9.5  Bragg's law
# --------------------------------------------------------------------------

BRAGG_EXAMPLES = [
    {"crystal": "Sodium chloride (NaCl)", "d": 5.64e-10, "note": "Cubic lattice; the "
     "first reflection from the (100) planes gives a well-known 22.9 degree peak."},
    {"crystal": "Diamond", "d": 3.57e-10, "note": "Its tetrahedral arrangement gives the "
     "characteristic double peak that fingerprints carbon."},
    {"crystal": "Quartz (silicon dioxide)", "d": 4.91e-10, "note": "Used to identify "
     "clays and sands from their diffraction fingerprint."},
]


def bragg_angle(plane_spacing: float, wavelength_value: float, m: int = 1) -> dict:
    """Solve ``2 d sin(theta) = m lambda`` for the glancing angle ``theta``."""
    ratio = m * wavelength_value / (2.0 * plane_spacing)
    if ratio > 1:
        return {"error": f"Order m = {m} is impossible for this d and lambda; "
                         f"2 d sin(theta) would need sin(theta) = {ratio:.3g}."}
    return {"theta_deg": math.degrees(math.asin(ratio)), "sin_theta": ratio,
            "m": m, "d": plane_spacing, "lambda": wavelength_value,
            "twice_theta_deg": 2.0 * math.degrees(math.asin(ratio)),
            "note": "Here theta is the angle between the beam and the crystal plane, "
                    "so the scattering angle is 2 theta - which is why detectors "
                    "usually work at 2 theta."}


def bragg_order(plane_spacing: float, theta_deg: float, wavelength_value: float) -> float:
    """Solve ``2 d sin(theta) = m lambda`` for the order ``m``."""
    return 2.0 * plane_spacing * math.sin(math.radians(theta_deg)) / wavelength_value


def xray_diffraction_series(plane_spacing: float, wavelength_value: float,
                            max_order: int = 5) -> list:
    """Peak positions for the first few orders of a crystal."""
    rows = []
    for m in range(1, max(1, int(max_order)) + 1):
        result = bragg_angle(plane_spacing, wavelength_value, m)
        rows.append({"m": m, **result})
    return rows


# --------------------------------------------------------------------------
# 9.6  Polarisation
# --------------------------------------------------------------------------

MALUS_TABLE = [
    {"theta_deg": 0, "fraction": 1.0, "note": "Transmission axes parallel - all the light passes."},
    {"theta_deg": 30, "fraction": 0.75, "note": "Three quarters of the light passes."},
    {"theta_deg": 45, "fraction": 0.5, "note": "Exactly half passes."},
    {"theta_deg": 60, "fraction": 0.25, "note": "Only a quarter passes."},
    {"theta_deg": 90, "fraction": 0.0, "note": "Axes crossed - the view goes black."},
]


def malus_law(initial_intensity: float, theta_deg: float) -> float:
    """Malus's law: ``I = I_0 cos^2(theta)``.

    The transmitted intensity always lies between 0 and ``I_0`` and never
    exceeds it, because the polariser can only remove light.
    """
    return initial_intensity * math.cos(math.radians(theta_deg)) ** 2


def two_polarisers(initial_intensity: float, theta1_deg: float, theta2_deg: float) -> dict:
    """Two polarisers: the first unpolarises, the second selects.

    Unpolarised light loses half its intensity in the first polariser. The
    second then applies Malus's law at the angle between the two axes. Putting a
    third polariser between them, turned at an angle, can make more light get
    through than with two - which is the clearest demonstration that
    interference is happening rather than simple filtering.
    """
    after_first = initial_intensity / 2.0
    after_second = malus_law(after_first, theta2_deg - theta1_deg)
    angle = 45.0
    with_three = malus_law(malus_law(after_first, angle), angle - theta2_deg)
    return {"after_first": after_first, "after_second": after_second,
            "final": after_second, "with_three_polarisers": with_three,
            "gain": with_three > after_second,
            "angle_between": theta2_deg - theta1_deg,
            "note": "Crossing the axes gives a black view. Slipping a third "
                    "polariser in at 45 degrees lets light through again, because "
                    "it re-orients the vibrations before they reach the last filter."}


def brewster_angle(n1: float, n2: float) -> dict:
    """``tan(theta_B) = n2 / n1`` - the angle of incidence giving fully polarised reflection."""
    theta = math.degrees(math.atan(n2 / n1))
    refracted = 90.0 - theta
    return {"theta_b_deg": theta, "refracted_deg": refracted,
            "n1": n1, "n2": n2,
            "note": f"At {theta:.1f} degrees the reflected and refracted rays are at "
                    f"right angles, and the reflected light is completely polarised "
                    f"in the plane of incidence."}


POLARISATION_USES = [
    {"application": "Sunglasses",
     "how": "A polarising sheet, or a sheeting that reflects off a horizontal surface.",
     "why": "Glare from a road or water is mostly polarised, so it is blocked, while "
            "the light scattered by the objects you want to see is much less so."},
    {"application": "Photography",
     "how": "A circular polariser screwed on the lens.",
     "why": "It darkens blue skies and removes reflections from leaves and wet stone."},
    {"application": "LCD screens",
     "how": "Two polarisers with a liquid crystal layer between them; the crystal "
            "rotates the polarisation by an amount set by the voltage across each pixel.",
     "why": "Changing the angle changes how much light passes the second polariser, "
            "so each pixel becomes a dimmer or brighter window."},
    {"application": "Three-dimensional films",
     "how": "Two images are projected through polarisers at right angles; each eye "
            "sees one through its own polariser.",
     "why": "Each eye receives a different image, and the brain reads the pair as depth."},
    {"application": "Photography with a LCD screen",
     "how": "The preview screen is polarised, and the sensor has a filter in front of it.",
     "why": "Without matching the filter's axis to the screen, every photo would "
            "look too dark - the same effect that makes sunglasses darken an LCD."},
]


# --------------------------------------------------------------------------
# Lenses and optical instruments (used by the Michelson and astronomy sections)
# --------------------------------------------------------------------------

def lens_image(focal_length: float, object_distance: float) -> dict:
    """The thin-lens formula ``1/f = 1/u + 1/v``."""
    if object_distance == 0:
        return {"error": "The object cannot sit at the lens."}
    image_distance = 1.0 / (1.0 / focal_length - 1.0 / object_distance)
    if image_distance < 0:
        return {"image_distance": image_distance, "type": "virtual, upright",
                "note": "The image is on the same side as the object."}
    kind = "real, inverted" if object_distance > focal_length else "virtual, upright"
    return {"image_distance": image_distance, "type": kind,
            "magnification": -image_distance / object_distance}


def magnification(focal_length: float, object_distance: float) -> float:
    """``m = v / u`` (negative means inverted)."""
    result = lens_image(focal_length, object_distance)
    return result.get("magnification", float("nan"))
