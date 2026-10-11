"""Chapter 7 - Oscillations.

Simple harmonic motion and its link to uniform circular motion, the
mass-spring oscillator and the simple pendulum.

Pure Python: no Streamlit, pandas, NumPy or Plotly.
"""

from __future__ import annotations

import math

__all__ = [
    "STANDARD_G", "PERIODIC_EXAMPLES", "is_periodic", "angular_frequency",
    "period_from_angular_frequency", "frequency", "displacement",
    "velocity", "acceleration", "amplitude_from", "energy", "phase",
    "shm_series", "shm_phase_lag", "circular_projection", "mass_spring_period",
    "mass_spring_frequency", "mass_spring_series", "pendulum_period",
    "pendulum_frequency", "pendulum_series", "pendulum_accuracy",
    "comparison_table", "energy_loss_damped",
]

STANDARD_G = 9.8


# --------------------------------------------------------------------------
# 7.1  Periodic and non-periodic oscillations
# --------------------------------------------------------------------------

PERIODIC_EXAMPLES = [
    {"system": "Simple pendulum on a long string", "periodic": True,
     "reason": "It repeats to within a fraction of a percent; small damping is the "
               "only thing that changes it."},
    {"system": "A tuning fork", "periodic": True,
     "reason": "The fork vibrates at a steady frequency, decaying only slowly."},
    {"system": "A car on a level road", "periodic": True,
     "reason": "The up-and-down motion of the suspension repeats each time a wheel "
               "goes over a bump."},
    {"system": "A beating heart", "periodic": True,
     "reason": "Regular, though the rate is not constant over a lifetime."},
    {"system": "A swinging earthquake trace", "periodic": False,
     "reason": "Each tremor has a different size and duration, so the pattern never "
               "repeats exactly."},
    {"system": "A falling leaf tumbling in the wind", "periodic": False,
     "reason": "Air currents push it differently every time."},
    {"system": "The height of the sea at one beach", "periodic": False,
     "reason": "Wind and atmospheric pressure add slow, irregular changes on top of "
               "the tide."},
]


def is_periodic(samples, tolerance: float = 1e-9) -> bool:
    """True when a list of samples repeats within ``tolerance``.

    Used to let learners test whether their own recorded series is periodic.
    """
    values = [v for v in samples if v == v]
    n = len(values)
    if n < 2:
        return False
    period = n // 2
    return all(math.isclose(values[i], values[i + period], abs_tol=tolerance)
               for i in range(period))


# --------------------------------------------------------------------------
# 7.2  S.H.M. and uniform circular motion
# --------------------------------------------------------------------------

def angular_frequency(period: float) -> float:
    """``omega = 2 pi / T`` in rad s^-1."""
    return 2.0 * math.pi / period if period else float("nan")


def period_from_angular_frequency(omega: float) -> float:
    """``T = 2 pi / omega``."""
    return 2.0 * math.pi / omega if omega else float("nan")


def frequency(period: float) -> float:
    """``f = 1 / T`` in hertz."""
    return 1.0 / period if period else float("nan")


def displacement(amplitude: float, omega: float, t: float, phase: float = 0.0) -> float:
    """``x = A sin(omega t + phi)``."""
    return amplitude * math.sin(omega * t + phase)


def velocity(amplitude: float, omega: float, t: float, phase: float = 0.0) -> float:
    """``v = A omega cos(omega t + phi)``."""
    return amplitude * omega * math.cos(omega * t + phase)


def acceleration(amplitude: float, omega: float, t: float, phase: float = 0.0) -> float:
    """``a = -A omega^2 sin(omega t + phi) = -omega^2 x``."""
    return -amplitude * omega ** 2 * math.sin(omega * t + phase)


def amplitude_from(position: float, velocity_value: float, omega: float) -> float:
    """``A = sqrt(x^2 + (v/omega)^2)``, which is constant throughout S.H.M."""
    return math.hypot(position, velocity_value / omega) if omega else float("nan")


def phase(position: float, velocity_value: float, amplitude: float) -> float:
    """Phase of the oscillator, in radians, from ``tan(phi) = (v/omega) / x``."""
    if amplitude == 0:
        return float("nan")
    omega_part = velocity_value
    return math.atan2(omega_part, position) if omega_part or position else 0.0


def energy(amplitude: float, omega: float, mass: float = 1.0,
           k: float = None) -> float:
    """Total mechanical energy of an oscillator ``E = (1/2) k A^2 = (1/2) m omega^2 A^2``."""
    stiffness = k if k is not None else mass * omega ** 2
    return 0.5 * stiffness * amplitude ** 2


def shm_series(amplitude: float, omega: float, periods: float = 1.0,
               samples: int = 300, phase: float = 0.0) -> dict:
    """Displacement, velocity and acceleration over a whole number of periods."""
    n = max(3, int(samples))
    period = period_from_angular_frequency(omega)
    t_max = period * max(periods, 0.25)
    step = t_max / (n - 1)
    times = [i * step for i in range(n)]
    return {
        "t": times,
        "x": [displacement(amplitude, omega, t, phase) for t in times],
        "v": [velocity(amplitude, omega, t, phase) for t in times],
        "a": [acceleration(amplitude, omega, t, phase) for t in times],
        "period": period, "omega": omega, "amplitude": amplitude,
    }


def shm_phase_lag(omega: float, period: float) -> dict:
    """The fixed phase relationships between x, v and a.

    Displacement leads velocity by a quarter cycle, and acceleration is exactly
    a quarter cycle out of step with displacement.
    """
    quarter = period / 4.0
    return {
        "x_to_v": quarter, "v_to_a": quarter, "x_to_a": period / 2.0,
        "statement": f"Velocity leads displacement by T/4 = {quarter:.4g} s, and "
                     f"acceleration is a further T/4 behind velocity, so acceleration "
                     f"is always opposite in sign to displacement.",
        "omega": omega, "period": period,
    }


def circular_projection(radius: float, omega: float, t: float) -> dict:
    """S.H.M. is the shadow of uniform circular motion.

    A point moving round a circle at constant speed has a horizontal
    coordinate ``x = R sin(omega t)`` - exactly the displacement of an S.H.M.
    """
    x = radius * math.sin(omega * t)
    y = radius * math.cos(omega * t)
    return {"x": x, "y": y, "v": radius * omega * math.cos(omega * t),
            "amplitude": radius, "omega": omega,
            "speed": radius * omega,
            "statement": "The vertical coordinate, taken from the centre, is the "
                         "amplitude and the horizontal coordinate is the displacement."}


# --------------------------------------------------------------------------
# 7.3  Mass-spring system
# --------------------------------------------------------------------------

def mass_spring_period(mass: float, k: float) -> float:
    """``T = 2 pi sqrt(m / k)`` in seconds."""
    return 2.0 * math.pi * math.sqrt(mass / k) if k else float("nan")


def mass_spring_frequency(mass: float, k: float) -> float:
    """``f = (1/2 pi) sqrt(k / m)`` in hertz."""
    return math.sqrt(k / mass) / (2.0 * math.pi) if mass else float("nan")


def mass_spring_series(mass: float, k: float, extension: float,
                       samples: int = 300) -> dict:
    """A complete oscillation of a spring with a given starting extension."""
    omega = math.sqrt(k / mass)
    series = shm_series(extension, omega, periods=1.0, samples=samples)
    series.update({"mass": mass, "k": k, "period": mass_spring_period(mass, k),
                   "frequency": mass_spring_frequency(mass, k),
                   "max_speed": extension * omega,
                   "max_acceleration": extension * omega ** 2,
                   "energy": 0.5 * k * extension ** 2})
    return series


# --------------------------------------------------------------------------
# 7.4  Simple pendulum
# --------------------------------------------------------------------------

def pendulum_period(length: float, g: float = STANDARD_G) -> float:
    """``T = 2 pi sqrt(L / g)`` in seconds, for small oscillations."""
    return 2.0 * math.pi * math.sqrt(length / g) if g else float("nan")


def pendulum_frequency(length: float, g: float = STANDARD_G) -> float:
    """``f = (1/2 pi) sqrt(g / L)`` in hertz."""
    return math.sqrt(g / length) / (2.0 * math.pi) if length else float("nan")


def pendulum_accuracy(length: float, angle_deg: float,
                      g: float = STANDARD_G) -> float:
    """How far the large-angle period departs from ``2 pi sqrt(L/g)``.

    The small-angle formula is only an approximation. The exact pendulum period
    grows with amplitude; at 20 degrees the error is already about 0.5 %, and at
    90 degrees it reaches 18 %.
    """
    theta = math.radians(abs(angle_deg))
    if theta == 0:
        return 0.0
    correction = 1.0 + theta ** 2 / 16.0 + 11.0 * theta ** 4 / 3072.0
    exact = pendulum_period(length, g) * correction
    simple = pendulum_period(length, g)
    return 100.0 * (exact - simple) / simple


def pendulum_series(length: float, start_deg: float, g: float = STANDARD_G,
                    damping: float = 0.0, samples: int = 400) -> dict:
    """A realistic pendulum trace, integrating ``theta'' = -(g/L) sin(theta)``.

    The small-angle formula is used only when the swing is genuinely small; for
    larger angles the full sine is integrated so the period lengthens correctly.
    Air resistance can be added as a damping coefficient.
    """
    small = abs(start_deg) < 5.0
    if small:
        series = shm_series(math.radians(start_deg),
                            math.sqrt(g / length), periods=1.0, samples=samples)
        series["small_angle_approx"] = True
        return series

    dt = period_from_angular_frequency(math.sqrt(g / length)) / 40.0
    theta = math.radians(start_deg)
    omega = 0.0
    times, angles, speeds = [], [], []
    t = 0.0
    for _ in range(samples):
        times.append(t)
        angles.append(theta)
        speeds.append(omega)
        accel = -(g / length) * math.sin(theta) - 2.0 * damping * omega
        omega += accel * dt
        theta += omega * dt
        t += dt
    return {"t": times, "x": angles, "theta": angles, "v": speeds,
            "amplitude": max(abs(a) for a in angles), "small_angle_approx": False,
            "period": period_from_angular_frequency(math.sqrt(g / length)),
            "length": length, "g": g}


def comparison_table() -> list:
    """The mass-spring oscillator and the simple pendulum side by side."""
    return [
        {"system": "Mass on a spring", "period": "T = 2 pi sqrt(m / k)",
         "independent_of": "amplitude (within the elastic limit)",
         "depends_on": "mass m and spring constant k",
         "restoring_law": "F = -k x, so a = -(k/m) x",
         "amplitude_limit": "Must stay inside the elastic limit, or the spring no "
                           "longer obeys Hooke's law and the motion stops being "
                           "exactly periodic."},
        {"system": "Simple pendulum", "period": "T = 2 pi sqrt(L / g)",
         "independent_of": "mass of the bob",
         "depends_on": "length L and g",
         "restoring_law": "F = -m g sin(theta), which for small angles is "
                          "approximately -m g theta",
         "amplitude_limit": "Only for small angles. Beyond about 10 degrees the "
                           "period lengthens measurably, so T = 2 pi sqrt(L/g) "
                           "over-predicts the frequency."},
    ]


def energy_loss_damped(energy0: float, damping: float, period: float) -> dict:
    """Energy after one period of a damped oscillator."""
    amplitude_factor = math.exp(-damping * period)
    return {"energy_after": energy0 * amplitude_factor ** 2,
            "amplitude_factor": amplitude_factor,
            "note": "The energy falls as the square of the amplitude factor, so a "
                    "slowly dying oscillator loses energy very quickly at first."}
