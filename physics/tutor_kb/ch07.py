"""Chapter 7 tutor: oscillations, mass-spring and pendulum."""

from __future__ import annotations

import math

from ..core import oscillations as O

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["periodic and non periodic", "what is periodic", "periodic oscillation",
              "non periodic", "is it periodic"],
     "title": "Periodic and non-periodic",
     "answer": (
         "**Periodic** motion repeats to within a fraction of a percent. A tuning fork, a "
         "gentle pendulum swing, a car's suspension over a bump.\n"
         "**Non-periodic** never repeats. An earthquake trace, a leaf tumbling in the wind, "
         "sea level with the wind on it.\n\n"
         "Damped motion still counts as periodic: the amplitude decays but the period barely "
         "changes, and the change is far below what any clock can resolve."),
     "slo": "7.1.1"},
    {"keys": ["simple harmonic motion", "what is shm", "condition for shm", "a equals"],
     "title": "Simple harmonic motion",
     "answer": (
         "The defining condition is **a = −ω²x**.\n\n"
         "Two parts, and both matter:\n"
         "* acceleration is **proportional to displacement**\n"
         "* and it points **towards the mean position**\n\n"
         "The minus sign is what makes the body turn round. Without it the body would "
         "accelerate away from equilibrium and never return.\n\n"
         "Periodic but not simple harmonic: a bouncing ball. Its acceleration is roughly "
         "constant downwards, not proportional to displacement."),
     "slo": "7.1.2"},
    {"keys": ["amplitude period frequency", "terms of shm", "what is amplitude",
              "angular frequency", "phase difference"],
     "title": "The terms",
     "answer": (
         "* **x** displacement from the mean, m, [L]\n"
         "* **A** amplitude — the *greatest* displacement, always positive, m\n"
         "* **T** period, s\n"
         "* **f = 1/T** frequency, Hz\n"
         "* **ω = 2π/T** angular frequency, rad s⁻¹\n"
         "* **Δφ** phase difference, radians\n\n"
         "Note that Hz and rad s⁻¹ have the **same dimension** [T⁻¹] and differ only by 2π."),
     "slo": "7.2.1"},
    {"keys": ["shm and circular motion", "circular motion relation", "projection",
              "shm is a projection"],
     "title": "S.H.M. and circular motion",
     "answer": (
         "Take a point moving round a circle at **constant speed**. Its only acceleration is "
         "the centripetal one, ω²R, always towards the centre — which is exactly the S.H.M. "
         "condition.\n\n"
         "Now look at **one coordinate**. That coordinate oscillates between −R and +R "
         "following R sin ωt.\n\n"
         "So: **amplitude = radius, ω = the circular speed, T = the time for one lap.**\n\n"
         "It is useful because circular motion is easier to picture, and because the same "
         "orbit appears in the (x, v/ω) plane of any oscillator."),
     "slo": "7.2.2"},
    {"keys": ["x equals a sin", "three expressions", "instantaneous velocity",
              "sine cosine shm"],
     "title": "The three expressions",
     "answer": (
         "* **x = A sin(ωt + φ)**\n"
         "* **v = Aω cos(ωt + φ)**\n"
         "* **a = −Aω² sin(ωt + φ) = −ω²x**\n\n"
         "Differentiate x once to get v and twice to get a. The sine and cosine swap places, "
         "and each differentiation brings down another factor of ω.\n\n"
         "**Phase offsets:** v leads x by T/4, and a lags v by T/4 — so a is half a cycle "
         "behind x and always opposite in sign to it."),
     "slo": "7.2.3"},
    {"keys": ["mass spring", "spring oscillator", "t equals 2 pi square root m over k",
              "period of a spring"],
     "title": "The mass-spring system",
     "answer": (
         "Hooke's law **F = −kx** *is* the S.H.M. condition. Divide by m:\n\n"
         "**a = −(k/m)x**, and comparing with a = −ω²x gives **ω = √(k/m)**, so\n\n"
         "**T = 2π√(m/k)**\n\n"
         "* heavier mass → slower, by √m\n"
         "* stiffer spring → faster\n"
         "* **amplitude does not appear at all**\n\n"
         "Energy: **E = ½kA² = ½mω²A²**, shared between kinetic and elastic potential."),
     "slo": "7.3.2"},
    {"keys": ["pendulum period", "simple pendulum", "t equals 2 pi square root l over g",
              "period of a pendulum"],
     "title": "The simple pendulum",
     "answer": (
         "**T = 2π√(L/g)** — for **small** swings only.\n\n"
         "It comes from approximating sin θ ≈ θ in radians, which turns the restoring force "
         "into something proportional to displacement.\n\n"
         "* the **mass cancels** — both the force and the inertia scale with m\n"
         "* the **amplitude does not appear**, except through the approximation failing\n"
         "* doubling L only multiplies T by √2\n\n"
         "**How small is small enough?** 0.19 % error at 10°, 1.7 % at 30°, 7 % at 60°, 18 % "
         "at 90°. The error grows as the *square* of the angle."),
     "slo": "7.4.2"},
    {"keys": ["why is the pendulum not shm", "is a pendulum shm", "small angle",
              "pendulum approximation"],
     "title": "Is a pendulum simple harmonic?",
     "answer": (
         "**Only approximately.**\n\n"
         "The restoring force is mg sin θ, not mgθ. For small θ, sin θ ≈ θ in radians, and "
         "since the arc displacement is x = Lθ, the force becomes roughly proportional to x — "
         "which is the S.H.M. condition.\n\n"
         "At larger angles the exact period *exceeds* 2π√(L/g): by 0.19 % at 10°, 1.7 % at 30° "
         "and 18 % at 90°. So a big-amplitude pendulum is periodic but not simple harmonic."),
     "slo": "7.4.1"},
    {"keys": ["how to measure g", "timing pendulum", "measure gravity"],
     "title": "Measuring g with a pendulum",
     "answer": (
         "Time **many** oscillations and divide: **T = t / n**, then **g = 4π²L / T²**.\n\n"
         "Two deliberate choices:\n"
         "* **keep the swing small** — the amplitude error grows as θ² and cannot be "
         "averaged out, because it is systematic\n"
         "* **count many cycles** — that divides the random error in the stopwatch by n\n\n"
         "Worked example: L = 1.00 m, 20 oscillations in 39.2 s. T = 1.96 s, so g = "
         "4π²(1.00)/1.96² = 10.3 m s⁻². That is about 5 % high, and the usual cause is a "
         "swing that was too wide."),
     "slo": "7.4.3"},
]


def _period(kind, a, b, c=None):
    if kind == "spring":
        return (f"**Mass-spring: m = {float(a):g} kg, k = {float(b):g} N m⁻¹**\n\n"
                f"* ω = √(k/m) = **{math.sqrt(float(b) / float(a)):.4g} rad s⁻¹**\n"
                f"* T = 2π√(m/k) = **{O.mass_spring_period(float(a), float(b)):.4g} s**\n"
                f"* f = **{O.mass_spring_frequency(float(a), float(b)):.4g} Hz**\n\n"
                f"The amplitude does not appear — pull the spring twice as far and it "
                f"oscillates at exactly the same rate.")
    return (f"**Pendulum: L = {float(a):g} m, g = {float(b):g} m s⁻²**\n\n"
            f"* T = 2π√(L/g) = **{O.pendulum_period(float(a), float(b)):.4g} s**\n"
            f"* f = **{O.pendulum_frequency(float(a), float(b)):.4g} Hz**\n"
            f"* length needed for a 1 s period: "
            f"**{float(b) * (1 / (2 * math.pi)) ** 2:.4g} m**\n\n"
            f"The mass of the bob cancels out entirely.")


def _at_time(A, omega, t):
    x = O.displacement(float(A), float(omega), float(t))
    v = O.velocity(float(A), float(omega), float(t))
    a = O.acceleration(float(A), float(omega), float(t))
    return (f"**A = {float(A):g} m, ω = {float(omega):g} rad s⁻¹, t = {float(t):g} s**\n\n"
            f"* x = A sin ωt = **{x:.4g} m**\n"
            f"* v = Aω cos ωt = **{v:.4g} m s⁻¹**\n"
            f"* a = −Aω² sin ωt = **{a:.4g} m s⁻²**\n\n"
            f"Check: −ω²x = **{-float(omega) ** 2 * x:.4g} m s⁻²**, which matches a, as it "
            f"must at every instant.")


def _small_angle(angle):
    return (f"**A swing of {float(angle):g}°**\n\n"
            f"* error in T = 2π√(L/g): **{O.pendulum_accuracy(1.0, float(angle)):.3g} %**\n"
            f"* the true period is **{O.pendulum_accuracy(1.0, float(angle)):.3g} % longer** "
            f"than the small-angle formula says\n\n"
            f"The error grows as the square of the angle, so it is worth keeping swings "
            f"below about 10°.")


CALCULATORS = [
    {"pattern": r"(?:mass[- ]spring|spring)\D*?([\d.]+)\s*(?:kg)?\s*(?:and|,|/|k\s*=)\s*"
                r"([\d.]+)", "reply": lambda m, k: _period("spring", m, k)},
    {"pattern": r"pendulum\D*?([\d.]+)\s*(?:m)?\s*(?:and|,|/|g\s*=)\s*([\d.]+)", "reply": _period},
    {"pattern": r"at\s+t\s*=\s*([\d.]+)\s*\D*?([\d.]+)\s*(?:rad)?\s*(?:and|,|/|ω)\s*([\d.]+)",
     "reply": lambda w, t, A: _at_time(A, w, t)},
    {"pattern": r"displacement\D*?([\d.]+)\s*(?:and|,|/)ω\s*=\s*([\d.]+)\s*(?:and|,|/)t\s*=\s*([\d.]+)",
     "reply": lambda A, w, t: _at_time(A, w, t)},
    {"pattern": r"small\s+angle\D*?([\d.]+)", "reply": _small_angle},
]
