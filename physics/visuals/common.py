"""Shared drawing helpers for the diagram library.

Every diagram in Physics Atlas is hand-written SVG returned as a string, so the
app has no image files, no network requests and no charting library in the
drawing path. The wrapper below is the only piece every diagram shares.

The diagram builders are pure functions of a handful of numbers, so they are
memoised with :func:`streamlit.cache_data`. That matters because Streamlit
re-executes the whole script on every widget interaction: without it, a slider
being dragged in one station would rebuild every diagram in every station. The
cache is keyed on the arguments, so a diagram only rebuilds when the numbers
actually drawn change.
"""

from __future__ import annotations

from streamlit import cache_data

__all__ = ["_svg", "wrap", "defs", "cached"]

#: Successive shots are spread by this angle in degrees so that points in
#: ``error_target`` never land on top of one another.
GOLDEN_ANGLE = 137.50776405


def cached(func):
    """Memoise a diagram builder.

    ``cache_data`` is used rather than ``cache_resource`` because the result is
    plain data - a string of SVG - and Streamlit hands back a copy each call so
    no caller can mutate the cached entry. ``show_spinner`` is off because a
    cache hit should be invisible.
    """
    return cache_data(show_spinner=False)(func)


def defs() -> str:
    """Shared SVG definitions: a soft glow and a drop shadow for raised cards."""
    return (
        '<defs>'
        '<filter id="atlasGlow" x="-40%" y="-40%" width="180%" height="180%">'
        f'<feGaussianBlur stdDeviation="3" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
        '</filter>'
        '<filter id="atlasSoft" x="-20%" y="-20%" width="140%" height="140%">'
        '<feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.45"/>'
        '</filter>'
        '</defs>'
    )


def _svg(body: str, width: int, height: int, label: str = "") -> str:
    role = f'role="img" aria-label="{label}"' if label else ""
    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" '
        f'style="max-width:{width}px;display:block;margin:0 auto" {role}>'
        f"{body}</svg>"
    )


def wrap(body: str, width: int, height: int, label: str = "") -> str:
    """Public alias for :func:`_svg`, used by the chapter diagram modules."""
    return _svg(body, width, height, label)
