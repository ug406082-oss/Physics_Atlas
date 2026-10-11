"""Backwards-compatible access to the Chapter 1 measurement helpers.

The real code now lives in :mod:`physics.core.measurement`. This module is kept
so that ``from physics import physics_core as pc`` and
``from .physics_core import dims`` keep working unchanged.
"""

from __future__ import annotations

from .core.measurement import *  # noqa: F401,F403
