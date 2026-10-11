"""Chapter 1 content.

Chapter 1 predates the :mod:`physics.chapters` layout and keeps its data in
:mod:`physics.data`. This module is the bridge, so the registry can treat every
chapter the same way.
"""

from __future__ import annotations

from ..data import (BOARD, DERIVED_QUANTITIES, HOMOGENEITY_EXAMPLES,
                    INSTRUMENTS, PRACTICE_QUESTIONS, REFERENCES,
                    SI_BASE_QUANTITIES, SI_PREFIXES, SLOS, SYLLABUS,
                    SYLLABUS_SOURCE, WORKED_PROBLEMS)

__all__ = ["BOARD", "SYLLABUS", "SYLLABUS_SOURCE", "SLOS", "SI_BASE_QUANTITIES",
           "DERIVED_QUANTITIES", "HOMOGENEITY_EXAMPLES", "INSTRUMENTS",
           "SI_PREFIXES", "PRACTICE_QUESTIONS", "WORKED_PROBLEMS", "REFERENCES",
           "STATIONS", "BIG_IDEAS", "ROUTE", "TAG", "INTRO"]

#: The chapter's stations, and which outcomes each one teaches.
#: Every outcome appears exactly once, so nothing is left untaught and nothing is
#: claimed twice.
STATIONS = [
    {"key": "overview", "label": "🗺️ Your route & outcomes", "slos": []},
    {"key": "quantities", "label": "📏 Units & quantities",
     "slos": ["1.1.1", "1.1.2", "1.1.3", "1.1.4"]},
    {"key": "dimensions", "label": "🧭 Dimensions",
     "slos": ["1.1.5", "1.2.1", "1.2.2", "1.2.3", "1.2.4"]},
    {"key": "accuracy", "label": "🎯 Accuracy & precision",
     "slos": ["1.3.1", "1.3.2"]},
    {"key": "uncertainty", "label": "➕ Uncertainty & sig figs",
     "slos": ["1.4.1", "1.4.2"]},
    {"key": "worked", "label": "🧮 Worked problems", "slos": []},
    {"key": "practice", "label": "🧠 Practice", "slos": []},
    {"key": "tutor", "label": "🤖 Atlas Tutor (offline AI)", "slos": []},
    {"key": "references", "label": "📚 References", "slos": []},
]

BIG_IDEAS = [
    ("Numbers need units.",
     "A measurement is a number plus a unit — “5” alone is meaningless."),
    ("Seven units build everything.",
     "The SI system has seven base units; every other unit is made from them."),
    ("Dimensions check equations.",
     "M, L and T describe the kind of a quantity, so we can test whether a "
     "formula is even possible before we test whether it is right."),
    ("Nothing is exact.",
     "Every reading has a small range, described by accuracy, precision and "
     "significant figures."),
]

ROUTE = ("Units → Dimensions → Accuracy &amp; precision → Uncertainty &amp; sig figs → "
         "Worked problems → Practice.")

TAG = "CHAPTER 1 · OPEN"

INTRO = (
    "How do we describe the world with numbers? This chapter covers four ideas: "
    "numbers with units, dimensions, accuracy and precision, and uncertainty with "
    "significant figures. Open a station in the bar below."
)
