"""Per-chapter knowledge bases for the offline tutor.

Each ``chNN`` module holds the entries the tutor uses to answer questions about
its own chapter, and optionally a list of calculators. A calculator is a
dictionary with a ``pattern`` (a regular expression) and a ``reply`` callable
that receives the matched groups and returns the answer as text.

Entry format::

    {"keys": ["canonical phrase", "another trigger"],
     "title": "Human-readable heading",
     "answer": "Markdown reply",
     "slo": "3.2.1" or None}

Chapter 1 keeps its knowledge base in :mod:`physics.ai_tutor`, which predates
this layout.

These modules import nothing from Streamlit, so every knowledge base can be
checked by a bare Python interpreter.
"""

from __future__ import annotations

__all__ = ["ch02", "ch03", "ch04", "ch05", "ch06", "ch07", "ch08", "ch09", "ch10"]
