"""Chapter 8 - Waves.

Progressive waves and energy transfer, transverse and longitudinal waves,
superposition, interference, beats, stationary waves and the Doppler effect
for sound and for light.

Pure Python: no Streamlit, pandas, NumPy or Plotly.
"""

from __future__ import annotations

import math

__all__ = [
    "SPEED_OF_SOUND", "SPEED_OF_LIGHT", "TRANSVERSE_EXAMPLES",
    "LONGITUDINAL_EXAMPLES", "wave_speed", "wavelength", "period", "amplitude",
    "intensity", "intensity_from_amplitudes", "displacement",
    "sum_of_waves", "superposition_series", "path_difference",
    "phase_difference", "interference_intensity", "interference_kind",
    "beat_frequency", "beat_period", "beats_series", "standing_wave",
    "node_positions", "string_harmonics", "pipe_harmonics", "PIPE_TYPES",
    "doppler", "DOPPLER_CASES", "doppler_shift", "radar_round_trip",
    "MODERN_USES",
]

SPEED_OF_SOUND = 340.0      # m s^-1, about 20 degrees C in dry air
SPEED_OF_LIGHT = 3.0e8      # m s^-1, exact by definition


TRANSVERSE_EXAMPLES = [
    {"wave": "Light", "medium": "None needed - light needs no material medium",
     "particles_vibrate": "Electric and magnetic fields, not particles",
     "note": "This is why light travels through a vacuum and sound does not."},
    {"wave": "Ripples on water", "medium": "Water surface",
     "particles_vibrate": "Up and down, perpendicular to the direction of travel",
     "note": "A cork on the surface bobs up and down but drifts only slowly "
             "sideways: matter is not carried far with the wave."},
    {"wave": "Waves on a rope", "medium": "A stretched string or rope",
     "particles_vibrate": "Side to side", "note": "Easy to see with a rope and a hand."},
    {"wave": "S waves in an earthquake", "medium": "Rock and soil",
     "particles_vibrate": "Perpendicular to the direction of travel",
     "note": "S waves cannot pass through liquid, which is how the interior of "
             "the Earth was shown to be liquid."},
]

LONGITUDINAL_EXAMPLES = [
    {"wave": "Sound in air", "medium": "Air",
     "particles_vibrate": "Along the line of travel, producing compressions and rarefactions",
     "note": "A compression is a region where the particles are pushed together; a "
             "rarefaction is where they are spread apart."},
    {"wave": "Sound in water", "medium": "Water",
     "particles_vibrate": "Along the line of travel",
     "note": "Sound travels about four times faster in water than in air."},
    {"wave": "Sound in a solid rod", "medium": "Metal",
     "particles_vibrate": "Along the rod",
     "note": "The fastest of all: steel carries sound about fifteen times faster "
             "than air does."},
    {"wave": "Pressure wave in a liquid", "medium": "Water in a closed pipe",
     "particles_vibrate": "Along the pipe", "note": "This is what a piston sends down."},
]


# --------------------------------------------------------------------------
# 8.1  Wave motion and energy
# --------------------------------------------------------------------------

def wave_speed(frequency_value: float, wavelength_value: float) -> float:
    """``v = f lambda`` - the speed of a progressive wave."""
    return frequency_value * wavelength_value


def wavelength(speed: float, frequency_value: float) -> float:
    """``lambda = v / f``."""
    return speed / frequency_value if frequency_value else float("nan")


def period(frequency_value: float) -> float:
    """``T = 1 / f``."""
    return 1.0 / frequency_value if frequency_value else float("nan")


def amplitude(crest_to_trough: float) -> float:
    """Half the crest-to-trough height."""
    return crest_to_trough / 2.0


def intensity(power: float, area: float) -> float:
    """Intensity ``I = power / area``, in W m^-2."""
    return power / area if area else float("inf")


def intensity_from_amplitudes(reference_intensity: float, reference_amplitude: float,
                              new_amplitude: float) -> float:
    """``I is proportional to A^2``, so doubling the amplitude quadruples the intensity."""
    if reference_amplitude == 0:
        return float("nan")
    return reference_intensity * (new_amplitude / reference_amplitude) ** 2


def displacement(amplitude_value: float, k: float, omega: float, t: float,
                 x: float = 0.0, phase: float = 0.0) -> float:
    """``y = A sin(kx - omega t + phi)`` for a travelling wave."""
    return amplitude_value * math.sin(k * x - omega * t + phase)


def sum_of_waves(waves, x: float, t: float = 0.0) -> float:
    """Superposition: the resultant displacement is the sum of the displacements.

    Each wave is given as ``{"A": float, "f": float, "lambda": float,
    "phase": float}`` in radians.
    """
    total = 0.0
    for wave in waves:
        k = 2.0 * math.pi / wave["lambda"]
        omega = 2.0 * math.pi * wave["f"]
        total += wave["A"] * math.sin(k * x - omega * t + wave.get("phase", 0.0))
    return total


def superposition_series(waves, x_max: float = 4.0, samples: int = 500) -> dict:
    """Each individual wave plus their sum, over a stretch of medium."""
    n = max(3, int(samples))
    step = x_max / (n - 1)
    xs = [i * step for i in range(n)]
    return {
        "x": xs,
        "components": [{"x": xs,
                        "y": [sum_of_waves([w], x) for x in xs]} for w in waves],
        "sum": [sum_of_waves(waves, x) for x in xs],
    }


# --------------------------------------------------------------------------
# 8.3  Superposition and interference
# --------------------------------------------------------------------------

def path_difference(d: float, angle_deg: float) -> float:
    """The extra distance travelled by the second wave: ``d sin(theta)``."""
    return d * math.sin(math.radians(angle_deg))


def phase_difference(delta: float, wavelength_value: float) -> float:
    """Phase difference in radians from a path difference: ``2 pi delta / lambda``."""
    return 2.0 * math.pi * delta / wavelength_value if wavelength_value else float("nan")


def interference_intensity(i1: float, i2: float, delta: float,
                           wavelength_value: float) -> dict:
    """Intensity from two coherent waves of unequal amplitude.

    ``I = I1 + I2 + 2 sqrt(I1 I2) cos(2 pi delta / lambda)``
    """
    phi = phase_difference(delta, wavelength_value)
    total = i1 + i2 + 2.0 * math.sqrt(i1 * i2) * math.cos(phi)
    constructive = max(i1, i2) * 4.0
    destructive = (math.sqrt(i1) - math.sqrt(i2)) ** 2
    return {"intensity": total, "phase": phi,
            "maximum": constructive, "minimum": destructive,
            "kind": interference_kind(delta, wavelength_value),
            "visibility": (constructive - destructive) / constructive if constructive else 0.0}


def interference_kind(delta: float, wavelength_value: float) -> str:
    """Constructive, destructive or in-between, from the path difference."""
    if wavelength_value == 0:
        return "undefined"
    fraction = (delta % wavelength_value) / wavelength_value
    if math.isclose(fraction, 0.0, abs_tol=1e-9):
        return "Constructive (bright) - path difference is a whole number of wavelengths"
    if math.isclose(fraction, 0.5, abs_tol=1e-9):
        return "Destructive (dark) - path difference is a half number of wavelengths"
    return "Partly constructive - the resultant lies between the bright and dark values"


def beat_frequency(f1: float, f2: float) -> float:
    """``f_beat = |f1 - f2|``."""
    return abs(f1 - f2)


def beat_period(f1: float, f2: float) -> float:
    """How long one complete rise-and-fall of loudness takes: ``1 / f_beat``."""
    fb = beat_frequency(f1, f2)
    return 1.0 / fb if fb else float("inf")


def beats_series(f1: float, f2: float, duration: float = 1.0,
                 samples: int = 600) -> dict:
    """The summed displacement of two close frequencies, showing the beats.

    The envelope is ``|2 A cos(pi (f1 - f2) t)|``, which falls to zero once per
    beat period.
    """
    n = max(3, int(samples))
    step = duration / (n - 1)
    times = [i * step for i in range(n)]
    sums = [math.sin(2.0 * math.pi * f1 * t) + math.sin(2.0 * math.pi * f2 * t)
            for t in times]
    envelope = [abs(2.0 * math.cos(math.pi * (f1 - f2) * t)) for t in times]
    return {"t": times, "sum": sums, "envelope": envelope,
            "beat_frequency": beat_frequency(f1, f2), "beat_period": beat_period(f1, f2)}


# --------------------------------------------------------------------------
# 8.4  Stationary waves
# --------------------------------------------------------------------------

PIPE_TYPES = [
    {"column": "Both ends closed", "condition": "node at both ends",
     "harmonics": "f_n = n v / 2L", "allowed_n": "n = 1, 2, 3, ...",
     "note": "All the harmonics are present."},
    {"column": "Both ends open", "condition": "antinode at both ends",
     "harmonics": "f_n = n v / 2L", "allowed_n": "n = 1, 2, 3, ...",
     "note": "Same frequencies as the closed pipe; an open pipe is a musical octave "
             "below a closed one of the same length when they are coupled."},
    {"column": "One end closed, one open", "condition": "node at the closed end, "
                                                       "antinode at the open end",
     "harmonics": "f_n = (2n - 1) v / 4L", "allowed_n": "n = 1, 3, 5, ...",
     "note": "Only the odd harmonics exist, so the note sounds an octave above the "
             "fundamental of a closed pipe twice its length."},
]


def node_positions(length: float, mode: int, both_ends_fixed: bool = True) -> dict:
    """Where the nodes and antinodes sit for one mode of a standing wave.

    For a string with both ends fixed, mode ``n`` has ``n + 1`` nodes at
    multiples of ``L / n`` and ``n`` antinodes halfway between them.
    """
    n = max(1, int(mode))
    if not both_ends_fixed:
        # Half-wave pattern from a closed end to an open end.
        nodes = [(2 * i - 1) * length / (2 * n) for i in range(1, n + 1)]
        antinodes = [i * length / n for i in range(n)]
    else:
        nodes = [i * length / n for i in range(n + 1)]
        antinodes = [(i + 0.5) * length / n for i in range(n)]
    return {"nodes": nodes, "antinodes": antinodes, "mode": n,
            "length": length, "segments": n,
            "node_definition": "a point that always stays still",
            "antinode_definition": "a point of greatest swing"}


def standing_wave(length: float, mode: int, amplitude_value: float = 1.0,
                  both_ends_fixed: bool = True, samples: int = 400) -> dict:
    """The stationary-wave shape: ``y = A sin(n pi x / L)``, unchanged in time.

    Unlike a progressive wave, this pattern does not travel along the string.
    """
    n = max(1, int(mode))
    total = length * n
    count = max(3, int(samples))
    step = total / (count - 1)
    xs = [i * step for i in range(count)]
    ys = [amplitude_value * math.sin(n * math.pi * x / length) for x in xs]
    return {"x": xs, "y": ys, **node_positions(length, n, both_ends_fixed)}


def string_harmonics(length: float, wave_speed_value: float = SPEED_OF_SOUND,
                     count: int = 5) -> list:
    """Frequencies of the first few harmonics of a string fixed at both ends."""
    fundamental = wave_speed_value / (2.0 * length)
    return [{"n": n, "f": n * fundamental, "mode": n,
             "lambda": 2.0 * length / n}
            for n in range(1, max(1, int(count)) + 1)]


def pipe_harmonics(length: float, kind: str = "closed", wave_speed_value: float = SPEED_OF_SOUND,
                   count: int = 5) -> list:
    """Frequencies of the first few harmonics of an air column.

    ``kind`` is ``closed`` (one end closed) or ``open`` (both ends open).
    """
    rows = []
    if kind == "closed":
        base = wave_speed_value / (4.0 * length)
        for i in range(1, max(1, int(count)) + 1):
            n = 2 * i - 1
            rows.append({"n": n, "f": n * base, "mode": i, "lambda": 4.0 * length / n})
    else:
        base = wave_speed_value / (2.0 * length)
        for i in range(1, max(1, int(count)) + 1):
            rows.append({"n": i, "f": i * base, "mode": i,
                         "lambda": 2.0 * length / i})
    return rows


# --------------------------------------------------------------------------
# 8.5  Doppler's effect
# --------------------------------------------------------------------------

DOPPLER_CASES = [
    {"case": "a", "title": "Source at rest, observer moving",
     "formula": "f' = f (v + v_o) / v",
     "sign": "Moving towards the source increases the frequency; moving away decreases it.",
     "example": "A cyclist approaching a parked fire engine hears a higher pitch."},
    {"case": "b", "title": "Observer at rest, source moving",
     "formula": "f' = f v / (v - v_s)",
     "sign": "Approaching shortens the wavelength; receding lengthens it.",
     "example": "The pitch drops as a siren passes you and recedes."},
    {"case": "c", "title": "Both moving towards each other",
     "formula": "f' = f (v + v_o) / (v - v_s)",
     "sign": "The two effects add, giving the largest shift.",
     "example": "Two vehicles meeting head-on hear each other's sirens rise sharply."},
    {"case": "d", "title": "Both moving away from each other",
     "formula": "f' = f (v - v_o) / (v + v_s)",
     "sign": "The two effects subtract, giving the smallest shift.",
     "example": "A receding ambulance's pitch falls as you follow it."},
]


def doppler(f: float, wave_speed_value: float, v_observer: float = 0.0,
            v_source: float = 0.0, case: str = "a") -> float:
    """Apparent frequency for one of the four classical cases.

    Speeds are given as positive numbers together with the case letter, which
    records whether each body is approaching (+) or receding (-).
    """
    table = {
        "a": lambda: f * (wave_speed_value + v_observer) / wave_speed_value,
        "b": lambda: f * wave_speed_value / (wave_speed_value - v_source),
        "c": lambda: f * (wave_speed_value + v_observer) / (wave_speed_value - v_source),
        "d": lambda: f * (wave_speed_value - v_observer) / (wave_speed_value + v_source),
    }
    if case not in table:
        raise ValueError(f"unknown Doppler case {case!r}; use 'a', 'b', 'c' or 'd'")
    return table[case]()


def doppler_shift(f: float, f_observed: float) -> dict:
    """What a change in frequency tells you about the motion of the source."""
    shift = f_observed - f
    return {"shift": shift, "percentage": 100.0 * shift / f if f else float("nan"),
            "rising": shift > 0, "falling": shift < 0,
            "verdict": ("The source is approaching the observer" if shift > 0
                        else "The source is moving away from the observer" if shift < 0
                        else "There is no relative motion along the line of sight")}


def radar_round_trip(target_speed: float, wave_speed_value: float = SPEED_OF_LIGHT,
                     f: float = 1.0e10) -> dict:
    """Double Doppler shift from a radar pulse reflected off a moving target.

    The pulse is shifted twice - once as it reaches the target and once as the
    reflection returns - so the measured beat frequency is roughly
    ``2 f v / c``.
    """
    shift = 2.0 * f * target_speed / wave_speed_value
    return {"f_emitted": f, "f_received": f + shift, "shift": shift,
            "target_speed": target_speed,
            "note": "This is how police radar and Doppler weather radar measure "
                    "speed. The factor of two comes from the round trip."}


# --------------------------------------------------------------------------
# 8.6  Waves in the modern world
# --------------------------------------------------------------------------

MODERN_USES = [
    {"field": "Medicine", "wave": "Ultrasound",
     "how": "A probe sends a 20 kHz to 1 MHz pulse into the body and times the echo.",
     "why_it_works": "The echo returns only if the sound meets a boundary between "
                     "tissues, so the delay reveals the depth and size of the fetus, "
                     "a gall stone or a tumour."},
    {"field": "Digital transmission", "wave": "Radio, microwaves, fibre-optic light",
     "how": "Information is encoded by switching a carrier on and off, or by "
            "changing its amplitude, frequency or phase.",
     "why_it_works": "A change in any of those properties can be detected at the "
                     "receiver and turned back into data."},
    {"field": "Storage", "wave": "Light in optical discs and magnetic domains",
     "how": "A laser spot is focused to a spot a fraction of a micrometre across "
            "and burns a pit, or changes the magnetic orientation of a domain.",
     "why_it_works": "The focused spot packs an enormous number of readable and "
                     "writable positions onto one disc."},
    {"field": "Monitoring earthquakes", "wave": "Seismic P, S and surface waves",
     "how": "Seismographs record the arrival times and amplitudes of the waves at "
            "many stations.",
     "why_it_works": "S waves are slower and cannot travel through liquid, so their "
                     "behaviour reveals the liquid outer core; the pattern of "
                     "arrivals locates the epicentre."},
    {"field": "Monitoring tsunamis", "wave": "Long-wavelength shallow-water waves",
     "how": "Deep-ocean pressure sensors and satellite altimeters watch the sea "
            "surface height.",
     "why_it_works": "A tsunami travels at about 700 km/h in deep water but slows "
                     "to walking pace in shallow water and stands up into a wall "
                     "of water at the coast."},
    {"field": "Astronomy", "wave": "All of the electromagnetic spectrum",
     "how": "Telescopes detect radio, infrared, visible, ultraviolet, X-ray and "
            "gamma-ray emission from the same objects.",
     "why_it_works": "The universe is not dark: it glows in wavelengths our eyes "
                     "cannot see."},
]
