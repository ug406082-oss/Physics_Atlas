"""The chapter registry for the whole book.

This module is deliberately free of Streamlit. It knows the ten chapters, how
many learning outcomes each carries, and how to reach the data and user-interface
modules for a chapter without importing them until they are actually needed.

Chapter data files live in :mod:`physics.chapters` and hold nothing but content -
learning outcomes, tables, worked problems and practice questions - so that all
of it can be imported and checked by a plain Python interpreter.
"""

from __future__ import annotations

import importlib

from .board import BOARD, GRADE, PART, SYLLABUS, SYLLABUS_SOURCE

__all__ = [
    "BOARD", "SYLLABUS", "SYLLABUS_SOURCE", "PART", "GRADE",
    "CHAPTERS", "TOTAL_OUTCOMES", "chapter", "chapter_data", "chapter_ui",
    "chapter_slots", "slo_ids", "outcomes", "total_slo_ids",
]


#: Every chapter of the syllabus. ``available`` is the single source of truth for
#: whether the chapter picker offers the chapter or shows it as locked.
#: ``module`` is the stem of the data and user-interface modules in
#: :mod:`physics.chapters`.
CHAPTERS = [
    {"number": 1, "title": "Physical Quantities and Measurement", "available": True,
     "module": "ch01", "blurb": "Magnitudes and units, the SI system, dimensions, accuracy, precision and uncertainty."},
    {"number": 2, "title": "Scalars and Vectors", "available": True,
     "module": "ch02", "blurb": "Scalars versus vectors, rectangular components, scalar and vector products."},
    {"number": 3, "title": "Motion in One Dimension", "available": True,
     "module": "ch03", "blurb": "Equations of motion, conservation of momentum, work and the work-energy theorem."},
    {"number": 4, "title": "Motion in Two Dimensions", "available": True,
     "module": "ch04", "blurb": "Projectile motion, angular motion, centripetal force, moment of inertia and angular momentum."},
    {"number": 5, "title": "Deformation in Solids", "available": True,
     "module": "ch05", "blurb": "Types of solids, elastic and plastic deformation, stress, strain and Young's modulus."},
    {"number": 6, "title": "Fluids Dynamics", "available": True,
     "module": "ch06", "blurb": "Upthrust and floatation, streamline and turbulent flow, continuity and Bernoulli's equation."},
    {"number": 7, "title": "Oscillations", "available": True,
     "module": "ch07", "blurb": "Simple harmonic motion, uniform circular motion, mass-spring systems and the simple pendulum."},
    {"number": 8, "title": "Waves", "available": True,
     "module": "ch08", "blurb": "Wave motion and energy, superposition, beats, stationary waves and the Doppler effect."},
    {"number": 9, "title": "Physical Optics", "available": True,
     "module": "ch09", "blurb": "Wavefronts, interference, diffraction, Bragg's law and polarisation."},
    {"number": 10, "title": "Thermodynamics", "available": True,
     "module": "ch10", "blurb": "Heat, ideal gases, kinetic molecular theory, the laws, engines and entropy."},
]

#: Filled in lazily by :func:`outcomes`; the arithmetic total of the syllabus.
TOTAL_OUTCOMES = 167


def chapter(number: int) -> dict:
    """The registry entry for one chapter."""
    for entry in CHAPTERS:
        if entry["number"] == number:
            return entry
    raise KeyError(f"there is no chapter {number} in the syllabus")


def chapter_module(number: int):
    """The :mod:`physics.chapters` subpackage holding this chapter's files."""
    return importlib.import_module(f".chapters.{chapter(number)['module']}",
                                   package=__package__)


def chapter_data(number: int):
    """The pure data module for one chapter (learning outcomes, tables, questions)."""
    return importlib.import_module(f".chapters.{chapter(number)['module']}_data",
                                   package=__package__)


def chapter_ui(number: int):
    """The Streamlit module for one chapter. Imported only when a learner opens it."""
    return importlib.import_module(f".chapters.{chapter(number)['module']}",
                                   package=__package__)


def chapter_slots() -> list:
    """The full slot list for the chapter picker, including the outcome count.

    The count is read from the data module so the picker can never disagree with
    the chapter itself.
    """
    slots = []
    for entry in CHAPTERS:
        row = dict(entry)
        try:
            row["slo_count"] = len(outcomes(entry["number"]))
            row["stations"] = chapter_ui(entry["number"]).station_count()
        except Exception:                       # a chapter still being written
            row["slo_count"] = None
            row["stations"] = None
        slots.append(row)
    return slots


def outcomes(number: int) -> list:
    """The learning-outcome records for one chapter, in syllabus order."""
    return chapter_data(number).SLOS


def slo_ids(number: int) -> list:
    """Just the identifiers for one chapter, e.g. ``['3.1.1', '3.1.2', ...]``."""
    return [row["id"] for row in outcomes(number)]


def total_slo_ids() -> list:
    """Every outcome identifier in the whole syllabus."""
    ids = []
    for entry in CHAPTERS:
        ids.extend(slo_ids(entry["number"]))
    return ids
