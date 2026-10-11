"""Chapter 9 tutor: interference, diffraction, X-rays and polarisation."""

from __future__ import annotations

import math

from ..core import optics as P9

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["wave particle duality", "nature of light", "theory of light",
              "newton corpuscular", "huygens wave theory", "is light a wave or particle"],
     "title": "The nature of light",
     "answer": (
         "Each theory explained something the previous one could not:\n\n"
         "* **Newton (corpuscular)** explained straight lines and shadows, but **not** "
         "interference or diffraction.\n"
         "* **Huygens (wave in an aether)** explained interference and diffraction, but light "
         "travels perfectly well through a vacuum.\n"
         "* **Maxwell (electromagnetic)** fixed that — light needs no medium — and predicted "
         "the whole spectrum. Still silent about particles.\n"
         "* **Einstein (photons)** explained the photoelectric effect, where electrons need a "
         "**minimum frequency** however faint the beam.\n"
         "* **Today**: duality. 'Which is it?' is the wrong question — every experiment can be "
         "predicted by one picture or the other."),
     "slo": "9.1.1"},
    {"keys": ["wavefront", "what is a wavefront", "wave front"],
     "title": "Wavefronts",
     "answer": (
         "A **wavefront** is a surface joining all the points the wave has reached at the "
         "same instant.\n\n"
         "It always travels **normal (perpendicular) to itself** at every point, which is why "
         "circular wavefronts from a pebble spread out radially.\n\n"
         "Circular ones come from a point source; straight ones from a distant plane source "
         "such as a loudspeaker or a slit."),
     "slo": "9.1.2"},
    {"keys": ["huygens principle", "what is huygens principle", "secondary wavelets",
              "huygens"],
     "title": "Huygens' principle",
     "answer": (
         "1. **Every point on a wavefront acts as a source of a new secondary wavelet.**\n"
         "2. Each wavelet spreads at the wave speed, in all directions.\n"
         "3. The new wavefront is the **envelope** that just touches all of them.\n\n"
         "That one construction gives reflection, refraction and diffraction — and explains "
         "why a shadow has a sharp edge."),
     "slo": "9.1.3"},
    {"keys": ["coherent sources", "what is coherence", "monochromatic",
              "coherence and monochromatic"],
     "title": "Coherent and monochromatic",
     "answer": (
         "**Coherent**: the two sources keep a **constant** phase difference. Two lamps at the "
         "same frequency are **not** coherent — they drift in and out of step, so the fringes "
         "smear away.\n\n"
         "**Monochromatic**: one wavelength, so the fringes are clean.\n\n"
         "To get real coherence, split **one** wavefront into two — which is exactly what "
         "Young's two slits do."),
     "slo": "9.2.1"},
    {"keys": ["interference of light", "what is interference", "conditions for interference",
              "why fringes disappear"],
     "title": "Interference of light",
     "answer": (
         "Superposition of two coherent light waves gives bright and dark fringes.\n\n"
         "**Conditions:**\n"
         "1. coherent sources\n"
         "2. the same frequency\n"
         "3. comparable amplitudes\n"
         "4. a path difference within the coherence length\n\n"
         "Break coherence and the pattern moves too fast to see, averaging to a uniform glow."),
     "slo": "9.2.3"},
    {"keys": ["fringe spacing", "dy equals lambda l over d", "fringe width",
              "young double slit formula"],
     "title": "Fringe spacing",
     "answer": (
         "**dy = λL/d**\n\n"
         "* bright fringes at **y = n λL/d**\n"
         "* dark fringes at **y = (n + ½) λL/d** — exactly halfway between\n\n"
         "Proportional to λ and L, and **inversely** proportional to d. Make the slits closer "
         "and the fringes spread out."),
     "slo": "9.2.5"},
    {"keys": ["michelson interferometer", "what is michelson", "beam splitter",
              "how michelson works"],
     "title": "Michelson's interferometer",
     "answer": (
         "A half-silvered mirror at 45° splits the beam into two perfectly coherent copies down "
         "a fixed arm and a movable arm, then recombines them to give a circular fringe "
         "pattern.\n\n"
         "Moving the mirror by **x** changes the path by **2x**, because the light makes the "
         "round trip. So one fringe passes per **λ/2** of movement — an extraordinarily "
         "sensitive length measure.\n\n"
         "Michelson and Morley's search for the 'ether wind' found **nothing**, and that null "
         "result became a pillar of special relativity."),
     "slo": "9.3.1"},
    {"keys": ["gravitational waves", "what are gravitational waves", "ligo",
              "spacetime distortion"],
     "title": "Gravitational waves",
     "answer": (
         "Ripples in **spacetime itself**, predicted by Einstein in 1915 and detected in 2015.\n\n"
         "* They are **not** electromagnetic, so they pass straight through matter without being "
         "scattered.\n"
         "* They are extraordinarily weak: a passing wave changes a length by a part in 10²¹.\n"
         "* A passing wave **stretches one direction and squeezes the perpendicular one**.\n\n"
         "LIGO's 4 km arms detect that because nothing can provide a larger strain."),
     "slo": "9.3.2"},
    {"keys": ["diffraction", "what is diffraction", "single slit", "narrow slit"],
     "title": "Diffraction and the single slit",
     "answer": (
         "**Diffraction** is light spreading past an obstacle or through an opening. It is "
         "unavoidable — every opening has a finite width.\n\n"
         "For a single slit of width a:\n"
         "* **minima** at **a sinθ = mλ**, m = 1, 2, 3, ...\n"
         "* **central maximum** is **2λL/a** wide — twice every other band, because it runs "
         "minimum to minimum\n"
         "* there is **no** minimum at m = 0\n\n"
         "Wider pattern for longer λ and narrower slits."),
     "slo": "9.4.3"},
    {"keys": ["diffraction grating", "grating equation", "resolving power",
              "dividing into sin"],
     "title": "Diffraction gratings",
     "answer": (
         "**d sinθ = mλ**\n\n"
         "Only orders with mλ ≤ d exist at all — sinθ cannot exceed 1, and that is how you find "
         "the highest possible order.\n\n"
         "The maxima are **sharp** because they come from thousands of wavelets arriving in step; "
         "a slight angle destroys that. Hence a high **resolving power R = mN**, where N is the "
         "number of ruled lines."),
     "slo": "9.4.2"},
    {"keys": ["bragg law", "braggs law", "x ray diffraction", "xray diffraction",
              "2 d sin theta"],
     "title": "Bragg's law",
     "answer": (
         "**2 d sinθ = mλ**\n\n"
         "The lower ray travels an extra **2d sinθ** on the way down to the next plane and back "
         "up. For the reflections to add, that must be a whole number of wavelengths.\n\n"
         "**θ is the glancing angle to the plane**, not the normal — which is why detectors are "
         "quoted at **2θ**.\n\n"
         "The pattern is a fingerprint of the atomic arrangement, which is how minerals are "
         "identified and how DNA's double helix was found."),
     "slo": "9.5.1"},
    {"keys": ["polarisation", "what is polarisation", "unpolarised polarised",
              "plane polarised"],
     "title": "Polarisation",
     "answer": (
         "**Polarised** light vibrates in **one plane**. **Unpolarised** light vibrates in every "
         "plane at once.\n\n"
         "It is produced by a polaroid, by reflection at **Brewster's angle** (tanθB = n₂/n₁), "
         "and by scattering at 90°.\n\n"
         "It is used in sunglasses, photography, LCD screens and 3-D films."),
     "slo": "9.6.1"},
    {"keys": ["why only transverse", "can sound be polarised",
              "longitudinal polarisation"],
     "title": "Why only transverse waves",
     "answer": (
         "Polarisation selects a **plane of vibration**. A longitudinal wave's particles vibrate "
         "**along** the direction of travel, so there is no plane to select.\n\n"
         "That is why sound in air can never be polarised, and why only transverse waves are."),
     "slo": "9.6.2"},
    {"keys": ["malus law", "i equals i0 cos squared", "malus"],
     "title": "Malus's law",
     "answer": (
         "**I = I₀ cos²θ**\n\n"
         "* 0° → all passes\n"
         "* 45° → half passes\n"
         "* 90° → nothing passes\n\n"
         "Note the **squaring**. Halving the angle does not halve the intensity.\n\n"
         "And unpolarised light loses **half** at the first polaroid — that is a different rule, "
         "about the input rather than the angle."),
     "slo": "9.6.5"},
    {"keys": ["three polarisers", "third polaroid", "crossed polarisers",
              "why does adding a polariser help"],
     "title": "Three polarisers",
     "answer": (
         "Two crossed polarisers give a **black** view. Insert a third at **45°** and light "
         "gets through again.\n\n"
         "The middle polariser lets through the 45° of vibration it allows, and the final one "
         "then passes half of *that*.\n\n"
         "A filter cannot do this — so it is the clearest proof that polarisers work by "
         "**re-orienting** vibrations rather than absorbing them."),
     "slo": "9.6.4"},
]


def _fringe(lam, dist, sep):
    return (f"**λ = {float(lam):.3g} m, L = {float(dist):.3g} m, d = {float(sep):.3g} m**\n\n"
            f"dy = λL/d = **{P9.fringe_width(float(lam), float(dist), float(sep)):.4g} m**\n\n"
            f"The nth bright fringe is at y = n·dy, and the dark ones fall exactly halfway "
            f"between.")


def _slit_minima(width, lam, m):
    r = P9.single_slit_minima(float(width), float(lam), int(m))
    if "error" in r:
        return f"That minimum cannot exist. {r['error']}"
    return (f"**a = {float(width):.3g} m, λ = {float(lam):.3g} m, m = {int(m)}**\n\n"
            f"sinθ = {r['sin_theta']:.4g}, so **θ = {r['theta_deg']:.4g}°**\n\n"
            f"There is no minimum at m = 0 — the centre is the brightest point, which is why the "
            f"central maximum is twice as wide as every other band.")


def _grating(spacing, lam):
    rows = P9.grating_angles(float(spacing), float(lam), 5)
    lines = "\n".join(f"* m = {g['m']}: {g['note']}" +
                      (f" θ = {g['theta_deg']:.3g}°" if g["exists"] else "")
                      for g in rows)
    highest = next((g["m"] - 1 for g in rows if not g["exists"]), rows[-1]["m"])
    return (f"**d = {float(spacing):.3g} m, λ = {float(lam):.3g} m**\n\n{lines}\n\n"
            f"Highest order that exists: **{highest}**. Beyond it sinθ would exceed 1.")


def _bragg(spacing, lam, m):
    r = P9.bragg_angle(float(spacing), float(lam), int(m))
    if "error" in r:
        return f"That order cannot exist. {r['error']}"
    return (f"**d = {float(spacing):.3g} m, λ = {float(lam):.3g} m, m = {int(m)}**\n\n"
            f"θ = arcsin(mλ/2d) = **{r['theta_deg']:.4g}°**\n\n"
            f"Detectors are quoted at **2θ = {r['twice_theta_deg']:.4g}°**, because that is the "
            f"angle between the incident and reflected beams.")


def _malus(i0, theta):
    return (f"**I₀ = {float(i0):.3g} W m⁻² at θ = {float(theta):.3g}°**\n\n"
            f"I = I₀ cos²θ = **{P9.malus_law(float(i0), float(theta)):.4g} W m⁻²**\n\n"
            f"That is {100 * math.cos(math.radians(float(theta))) ** 2:.1f} % of the input.")


def _brewster(n1, n2):
    r = P9.brewster_angle(float(n1), float(n2))
    return (f"**n₁ = {float(n1):.3g}, n₂ = {float(n2):.3g}**\n\n"
            f"θ_B = arctan(n₂/n₁) = **{r['theta_b_deg']:.4g}°**\n\n"
            f"At that angle the reflected and refracted rays are at right angles, and the "
            f"reflected light is completely plane-polarised.")


CALCULATORS = [
    {"pattern": r"fringe\s+(?:spacing|width)\D*?([\d.eE+-]+)\s*(?:m)?\s*(?:and|,|/|L)\s*"
                r"([\d.eE+-]+)\s*(?:m)?\s*(?:and|,|/|d)\s*([\d.eE+-]+)", "reply": _fringe},
    {"pattern": r"(?:first|second|third|minimum)\s+minimum\D*?([\d.eE+-]+)\s*(?:m)?\s*"
                r"(?:and|,|/|λ)\s*([\d.eE+-]+)\s*(?:m)?(?:\s*,\s*m\s*=\s*(\d+))?", "reply": _slit_minima},
    {"pattern": r"grating\D*?([\d.eE+-]+)\s*(?:m)?\s*(?:and|,|/|λ)\s*([\d.eE+-]+)", "reply": _grating},
    {"pattern": r"bragg\D*?([\d.eE+-]+)\s*(?:m)?\s*(?:and|,|/|λ)\s*([\d.eE+-]+)\s*(?:m)?\s*"
                r"(?:,\s*m\s*=\s*(\d+))?", "reply": _bragg},
    {"pattern": r"malus\D*?([\d.eE+-]+)\s*(?:W[^ ]*)?\s*(?:and|,|/|at)\s*([\d.eE+-]+)", "reply": _malus},
    {"pattern": r"brewster\D*?([\d.eE+-]+)\s*(?:and|,)\s*([\d.eE+-]+)", "reply": _brewster},
]
