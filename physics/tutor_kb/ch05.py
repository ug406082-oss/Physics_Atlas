"""Chapter 5 tutor: solids, deformation, stress and elastic energy."""

from __future__ import annotations

import math

from ..core import solids as S

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["crystalline", "amorphous", "polymeric", "types of solid",
              "difference between crystalline and amorphous"],
     "title": "The three classes of solid",
     "answer": (
         "**Crystalline** — a regular lattice repeating over long distances (diamond, "
         "quartz, sodium chloride). Melts at a sharp temperature.\n"
         "**Amorphous** — no long-range order (glass, wax, rubber). Softens gradually "
         "instead of melting sharply.\n"
         "**Polymeric** — very long chains, often cross-linked (polyethene, nylon, rubber).\n\n"
         "The lovely piece of evidence for amorphous glass: medieval window panes are thicker "
         "at the bottom, because centuries of gravity have let the viscous glass flow "
         "downwards. A crystalline pane would not have done that."),
     "slo": "5.1.1"},
    {"keys": ["elastic deformation", "plastic deformation", "elastic limit",
              "what is elastic", "what is plastic"],
     "title": "Elastic and plastic deformation",
     "answer": (
         "**Elastic:** remove the load and the body returns exactly to its original shape. "
         "The straight part of the stress–strain curve.\n"
         "**Plastic:** it stays deformed. Everything past the elastic limit.\n\n"
         "The **elastic limit** is the boundary. If a body recovers completely it never "
         "went past that limit; if it snapped, it went far past it.\n\n"
         "At the microscopic level: elastic deformation stretches the atomic spacing, "
         "plastic deformation slides whole layers of atoms past one another."),
     "slo": "5.3.1"},
    {"keys": ["stress and strain", "what is stress", "what is strain", "youngs modulus",
              "definition of young modulus"],
     "title": "Stress, strain and Young's modulus",
     "answer": (
         "* **stress σ = F/A** — force spread over the area resisting it, in pascals\n"
         "* **strain ε = ΔL/L** — fractional change in length, no unit\n"
         "* **Young's modulus Y = σ/ε** — in pascals, and it is the **gradient of the "
         "straight part of a stress–strain graph**\n\n"
         "Y measures how stiff a material is. Steel is about 2 × 10¹¹ Pa; rubber is about "
         "5 × 10⁶ Pa, some forty thousand times less."),
     "slo": "5.4.1"},
    {"keys": ["extension of a wire", "how far does it stretch", "f l over a y",
              "length change formula"],
     "title": "Extension of a loaded wire",
     "answer": (
         "Rearranging Y = FL/(AΔL) gives\n\n"
         "**ΔL = F L / (A Y)**\n\n"
         "So it stretches more if it is longer, if the force is bigger, or if it is thinner "
         "or made of a less stiff material.\n\n"
         "Watch the units: A must be in **m²** and Y in **Pa**. A diameter left in "
         "millimetres gives an extension a million times too small."),
     "slo": "5.2.1"},
    {"keys": ["elastic potential energy", "energy stored in a spring", "half k x squared",
              "why half"],
     "title": "Elastic potential energy",
     "answer": (
         "**E = ½Fx = ½kx²**\n\n"
         "It is simply the **area under the force–extension graph**. The force starts at "
         "zero and rises linearly, so the shape is a **triangle**, not a rectangle — which "
         "is where the ½ comes from.\n\n"
         "Energy goes as **x²**, so doubling the stretch stores four times the energy. That "
         "is why a hard squash on a trampoline feels so different from a gentle one."),
     "slo": "5.5.1"},
    {"keys": ["why does steel conduct", "which properties matter", "tensile strength",
              "elastic limit stress"],
     "title": "Reading a stress–strain curve",
     "answer": (
         "From bottom to top:\n\n"
         "* **straight elastic region** — slope = Y\n"
         "* **elastic limit** — the last point that fully recovers\n"
         "* **yield point** — the sharp knee; permanent deformation begins\n"
         "* **plastic region** — strain hardening, rising slowly\n"
         "* **ultimate stress** — the highest point on the curve\n"
         "* **necking** — stress falls while a thin neck forms and the bar breaks\n\n"
         "Glass never reaches a yield point: it is brittle and snaps while still on the "
         "straight line."),
     "slo": "5.4.1"},
    {"keys": ["types of deformation", "tensile", "compressive", "shear deformation",
              "torsion"],
     "title": "The four kinds of deformation",
     "answer": (
         "**Tensile** — pulled apart, it stretches\n"
         "**Compressive** — pushed together, it squashes\n"
         "**Shear** — a force parallel to the surface slides one layer past another\n"
         "**Torsional** — a turning force twists it\n\n"
         "This chapter works with tensile deformation, because it is the one with a clean "
         "one-dimensional formula."),
     "slo": "5.2.1"},
]


def _stress(force, area_cm2):
    a = float(area_cm2) * 1e-4
    return (f"**σ = {S.stress(float(force), a):.4g} Pa**\n\n"
            f"σ = F/A = {float(force):g} / {a:.4g} m² = {S.stress(float(force), a):.4g} Pa\n\n"
            f"That is about {S.stress(float(force), a) / 101325:.3g} atmospheres.")


def _youngs(stress_pa, strain):
    value = S.young_modulus(float(stress_pa), float(strain))
    return (f"**Y = {value:.4g} Pa**\n\n"
            f"Y = σ/ε = {float(stress_pa):g} / {float(strain):g} = {value:.4g} Pa\n\n"
            f"For reference: steel ≈ 2 × 10¹¹, copper ≈ 1.1 × 10¹¹, "
            f"aluminium ≈ 0.7 × 10¹¹, rubber ≈ 5 × 10⁶.")


def _extension(force, length, area_cm2, youngs):
    L, a = float(length), float(area_cm2) * 1e-4
    dL = S.length_change(float(force), L, a, float(youngs))
    return (f"**ΔL = {dL:.4g} m** ({dL * 1000:.4g} mm)\n\n"
            f"ΔL = F L / (A Y) = ({float(force):g} × {L:g}) / "
            f"({a:.4g} × {float(youngs):g}) = {dL:.4g} m\n\n"
            f"That is a strain of {dL / L:.4g}, or {100 * dL / L:.3g} %.")


def _energy(k, x):
    return (f"**E = {S.elastic_energy_from_k(float(k), float(x)):.4g} J**\n\n"
            f"E = ½kx² = ½ × {float(k):g} × ({float(x):g})² = "
            f"{S.elastic_energy_from_k(float(k), float(x)):.4g} J\n\n"
            f"The maximum force is kx = {float(k) * float(x):.4g} N, and the average "
            f"force over the stretch is half of that.")


CALCULATORS = [
    {"pattern": r"stress\s*=\s*([\d.]+)\s*(?:N)?\s*(?:/|over|on)\s*([\d.]+)\s*(?:cm2|cm²)?",
     "reply": _stress},
    {"pattern": r"young'?s?\s*modulus.*?([\d.]+)\s*(?:Pa)?\s*(?:and|/|over|at a strain of)\s*"
                r"([\d.]+)", "reply": _youngs},
    {"pattern": r"(?:extension|stretch)\D*?([\d.]+)\s*N\D*?([\d.]+)\s*m\D*?([\d.]+)\s*"
                r"(?:cm2|cm²)?\D*?([\d.]+)", "reply": _extension},
    {"pattern": r"energy\s+(?:stored\s+)?in\s+a\s+spring\D*?([\d.]+)\s*(?:N/m)?\s*"
                r"(?:and|by|at|over)\s*([\d.]+)", "reply": _energy},
    {"pattern": r"half\s*k\s*x\s*squared\s*=\s*([\d.]+)\s*([\d.]+)", "reply": _energy},
]
