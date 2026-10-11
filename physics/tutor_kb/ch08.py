"""Chapter 8 tutor: waves, interference, stationary waves and Doppler."""

from __future__ import annotations

import math

from ..core import waves as W

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["progressive wave", "what is a progressive wave", "travelling wave",
              "traveling wave"],
     "title": "Progressive waves",
     "answer": (
         "A **progressive (travelling) wave** carries **energy** from one point to another "
         "without permanently carrying **matter**.\n\n"
         "Proof: a cork on a pond bobs up and down but stays put; a floating boat is thrown "
         "back to the shore once the waves have passed. Energy went out, matter did not."),
     "slo": "8.1.1"},
    {"keys": ["intensity", "power over area", "intensity amplitude squared",
              "intensity proportional"],
     "title": "Intensity",
     "answer": (
         "**I = P/A** — power per unit area, in W m⁻².\n\n"
         "And the result that matters: **I is proportional to A²**. Doubling the amplitude "
         "quadruples the intensity; tripling it makes the intensity nine times larger.\n\n"
         "For a point source the area grows as 4πr², so intensity falls as 1/r²."),
     "slo": "8.1.3"},
    {"keys": ["v equals f lambda", "wave equation", "speed frequency wavelength",
              "wave speed formula"],
     "title": "v = fλ",
     "answer": (
         "**v = f λ**\n\n"
         "In one period the wave moves exactly one wavelength.\n\n"
         "**When sound enters a new medium the frequency does not change** — it is set by "
         "the source. The speed changes, so the wavelength changes instead. That is why the "
         "pitch of a note is the same in air and in water."),
     "slo": "8.1.4"},
    {"keys": ["transverse longitudinal", "difference between transverse",
              "what is a transverse wave", "compression rarefaction"],
     "title": "Transverse and longitudinal",
     "answer": (
         "**Transverse:** particles vibrate **perpendicular** to the direction of travel. "
         "Features are **crests and troughs**. Light, water ripples, S-waves in rock.\n\n"
         "**Longitudinal:** particles vibrate **along** the direction of travel. Features "
         "are **compressions and rarefactions**. Sound in air, water and solid rods; P-waves.\n\n"
         "Only transverse waves can be polarised."),
     "slo": "8.2.1"},
    {"keys": ["superposition principle", "what is superposition", "principle of superposition"],
     "title": "Principle of superposition",
     "answer": (
         "The **resultant displacement at every point is the sum of the individual "
         "displacements**.\n\n"
         "It is **linear** and **reversible**: after the waves have passed through each "
         "other, each carries on unchanged. That reversibility is what makes interference "
         "demonstrable at all."),
     "slo": "8.3.1"},
    {"keys": ["interference of sound", "constructive destructive interference",
              "why is sound loud and quiet", "path difference"],
     "title": "Interference of sound",
     "answer": (
         "* **Constructive (loud):** path difference = n λ\n"
         "* **Destructive (quiet):** path difference = (n + ½) λ\n"
         "* in between: part-way between the two\n\n"
         "Only the *fractional* part of the path difference matters — a whole number of extra "
         "wavelengths changes nothing at all."),
     "slo": "8.3.2"},
    {"keys": ["phase difference", "delta phi", "calculate phase difference"],
     "title": "Phase difference",
     "answer": (
         "**Δφ = (2π/λ) × (path difference)**, in radians.\n\n"
         "* n λ → Δφ = 2πn → **constructive**\n"
         "* (n + ½) λ → Δφ = (2n + 1)π → **destructive**\n\n"
         "Phase difference is an angle, so it is always measured in radians."),
     "slo": "8.3.3"},
    {"keys": ["beats", "beat frequency", "how beats form", "beat period",
              "beats of sound"],
     "title": "Beats",
     "answer": (
         "**f_beat = |f₁ − f₂|** and **T_beat = 1/f_beat**.\n\n"
         "Two close frequencies interfere, and the in-step pattern *drifts* along the line "
         "joining the sources, so the loudness rises and falls — once per beat.\n\n"
         "Worked: 440 and 444 Hz give 4 beats per second, one every 0.25 s. This is how a "
         "piano is tuned: the beats slow to nothing when the notes match."),
     "slo": "8.3.4"},
    {"keys": ["stationary wave", "standing wave", "what is a stationary wave",
              "formation of stationary waves"],
     "title": "Stationary waves",
     "answer": (
         "Two **identical waves travelling in opposite directions** superpose into a pattern "
         "that does not travel.\n\n"
         "* a wave sent along a string and reflected from a fixed end does exactly this\n"
         "* at a **free** end the reflection is inverted; at a **fixed** end it is not\n\n"
         "No energy is carried away — it stays, oscillating between the two stores."),
     "slo": "8.4.1"},
    {"keys": ["node antinode", "what is a node", "what is an antinode",
              "nodes and antinodes"],
     "title": "Nodes and antinodes",
     "answer": (
         "**Node:** a point that **never moves**. The two component waves are always exactly "
         "opposite there.\n\n"
         "**Antinode:** a point of **greatest swing**, where the two displacements always add.\n\n"
         "They alternate every λ/4, and node-to-node is λ/2. For a string fixed at both ends "
         "in mode n there are n+1 nodes and n antinodes."),
     "slo": "8.4.1"},
    {"keys": ["closed pipe", "open pipe", "harmonics of a pipe", "why stopped pipe",
              "air column harmonics"],
     "title": "Strings and air columns",
     "answer": (
         "**String, both ends fixed:** node–node → **fₙ = nv/2L**, all harmonics.\n"
         "**Pipe, both ends open:** antinode–antinode → **fₙ = nv/2L**, all harmonics.\n"
         "**Pipe, one end closed:** node–antinode → **fₙ = (2n−1)v/4L**, **odd only**.\n\n"
         "A stopped pipe sounds an **octave lower** than an open pipe of the same length, and "
         "has no even harmonics — which is why it sounds hollow."),
     "slo": "8.4.2"},
    {"keys": ["doppler effect", "what is the doppler effect", "why does pitch change",
              "apparent frequency"],
     "title": "Doppler's effect",
     "answer": (
         "The observed frequency changes when the **source and observer move relative to each "
         "other** — even if both are at rest in their own frames.\n\n"
         "**Approaching → higher pitch. Receding → lower pitch.**\n\n"
         "It is a *wavelength* argument: a moving source bunches the wavefronts in front and "
         "spreads them behind. The speed in the medium never changes."),
     "slo": "8.5.1"},
    {"keys": ["doppler formula", "four cases of doppler", "observer moving formula",
              "source moving formula", "apparent frequency formula"],
     "title": "The four Doppler relations",
     "answer": (
         "* **(a) observer moving, source at rest:** f′ = f(v + v₀)/v\n"
         "* **(b) source moving, observer at rest:** f′ = fv/(v − vₛ)\n"
         "* **(c) both approaching:** f′ = f(v + v₀)/(v − vₛ)\n"
         "* **(d) both receding:** f′ = f(v − v₀)/(v + vₛ)\n\n"
         "**The check that catches every mistake:** put v₀ = vₛ = 0. All four must return f."),
     "slo": "8.5.2"},
    {"keys": ["red shift blue shift", "doppler light", "redshift",
              "expansion of the universe", "astronomy doppler"],
     "title": "Red and blue shift",
     "answer": (
         "The same effect applies to **every** wave, light included.\n\n"
         "* receding → wavelengths stretched → **red shift**\n"
         "* approaching → wavelengths compressed → **blue shift**\n\n"
         "Every distant galaxy is red-shifted in proportion to its distance. That is the "
         "direct evidence that the universe is expanding.\n\n"
         "At everyday speeds the light shift is about one part in 10⁶ — undetectable without "
         "interferometry. It is the distances that make it measurable."),
     "slo": "8.5.4"},
    {"keys": ["police radar", "weather radar", "sonar", "applications of doppler",
              "doppler applications"],
     "title": "Applications of Doppler",
     "answer": (
         "* **Police radar** — the pulse is shifted **twice** (out and back), so the beat is "
         "about 2fv/c. That factor of two is what makes the tiny shift measurable.\n"
         "* **Weather radar** — reveals wind speed inside storms\n"
         "* **Sonar / ultrasound** — depth sounders and fetal heart rates\n"
         "* **Medical Doppler** — blood flow from the echo shift\n"
         "* **Satellite tracking** — orbital decay measured from the carrier shift"),
     "slo": "8.5.5"},
    {"keys": ["waves in medicine", "digital transmission", "earthquake waves",
              "tsunami", "modern uses of waves"],
     "title": "Waves in the modern world",
     "answer": (
         "* **Ultrasound** reflects at tissue boundaries, so the time delay gives depth\n"
         "* **Digital transmission** encodes information in the amplitude, frequency or phase "
         "of a carrier\n"
         "* **Storage** — a focused laser burns microscopic pits on an optical disc\n"
         "* **Earthquakes** — S-waves cannot travel through liquid, which is how the liquid "
         "outer core was found\n"
         "* **Tsunamis** — slow and low in deep ocean, fast and towering in shallow water"),
     "slo": "8.6.1"},
]


def _wavelen(v, f):
    return (f"**v = {float(v):g} m s⁻¹, f = {float(f):g} Hz**\n\n"
            f"λ = v/f = **{W.wavelength(float(v), float(f)):.4g} m**\n\n"
            f"If the speed changes but the frequency does not, the wavelength changes with "
            f"it — which is why sound keeps its pitch when it enters water.")


def _intensity(power, area):
    return (f"**P = {float(power):g} W over A = {float(area):g} m²**\n\n"
            f"I = P/A = **{W.intensity(float(power), float(area)):.4g} W m⁻²**\n\n"
            f"Remember the other half of the rule: intensity is proportional to the square of "
            f"the amplitude.")


def _beats(f1, f2):
    fb = W.beat_frequency(float(f1), float(f2))
    return (f"**f₁ = {float(f1):g} Hz, f₂ = {float(f2):g} Hz**\n\n"
            f"* beat frequency = **{fb:.4g} Hz**\n"
            f"* beat period = **{W.beat_period(float(f1), float(f2)):.4g} s**\n\n"
            f"So the loudness rises and falls {fb:.4g} times a second.")


def _doppler(case, f, v, vo, vs):
    titles = {"a": "source at rest, observer moving",
              "b": "observer at rest, source moving",
              "c": "both approaching",
              "d": "both receding"}
    check = W.doppler(float(f), float(v), 0.0, 0.0, case)
    value = W.doppler(float(f), float(v), float(vo), float(vs), case)
    return (f"**{titles[case]}**\n\n"
            f"f = {float(f):g} Hz, v = {float(v):g} m s⁻¹, "
            f"v₀ = {float(vo):g}, vₛ = {float(vs):g}\n\n"
            f"f′ = **{value:.4g} Hz** "
            f"({100 * (value / float(f) - 1):+.2g} %)\n\n"
            f"Sanity check: with both speeds zero the formula gives "
            f"{check:.4g} Hz, which matches f. ✓")


def _stationary(kind, L, v):
    if kind == "closed":
        rows = W.pipe_harmonics(float(L), "closed", float(v), 5)
        title = "closed pipe"
    else:
        rows = W.string_harmonics(float(L), float(v), 5)
        title = "string, both ends fixed"
    lines = "\n".join(f"* n = {r['n']}: **{r['f']:.4g} Hz** (λ = {r['lambda']:.4g} m)"
                      for r in rows)
    return (f"**{title}: L = {float(L):g} m, v = {float(v):g} m s⁻¹**\n\n{lines}")


CALCULATORS = [
    {"pattern": r"(?:wavelength|lambda)\s*(?:of|for)?\D*?([\d.]+)\s*(?:m s-?1)?\s*"
                r"(?:and|,)\s*([\d.]+)", "reply": _wavelen},
    {"pattern": r"intensity\s*=\s*([\d.]+)\s*(?:W)?\s*(?:over|,|/|on)\s*([\d.]+)", "reply": _intensity},
    {"pattern": r"beats?\s*(?:between)?\s*([\d.]+)\s*(?:and|,)\s*([\d.]+)", "reply": _beats},
    {"pattern": r"beat\s+frequency\s+(?:of|between)\s+([\d.]+)\s*(?:and|,)\s*([\d.]+)", "reply": _beats},
    {"pattern": r"doppler\s+case\s+([abcd])\D*?([\d.]+)\s*(?:,|and|over)\s*([\d.]+)\s*"
                r"(?:,|and|with)\s*([\d.]+)\s*(?:,|and|vo)\s*([\d.]+)\s*(?:,|and|vs)\s*([\d.]+)",
     "reply": lambda c, f, v, vo, vs: _doppler(c, f, v, vo, vs)},
    {"pattern": r"(closed pipe|open pipe|string)\s*(?:of)?\s*(?:length\s*)?([\d.]+)\s*m?\s*"
                r"(?:,|and|with)\s*([\d.]+)", "reply": _stationary},
]
