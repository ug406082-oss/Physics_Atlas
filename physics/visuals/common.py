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

from ..theme import MUTED

__all__ = ["_svg", "wrap", "defs", "cached", "freeze", "label", "tick",
           "MONO", "SANS", "HashableDict", "HashableList"]

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


class HashableDict(dict):
    """A read-only ``dict`` that can be hashed, so it can cross ``st.cache_data``.

    Converting a dict to a tuple of items would make it hashable but the drawing
    code inside the diagram would lose ``mapping["key"]``. This keeps the dict
    interface and only adds ``__hash__``.
    """

    __slots__ = ("_hash",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hash = hash(frozenset((k, freeze(v)) for k, v in self.items()))

    def _immutable(self, *a, **k):
        raise TypeError("HashableDict is a read-only cache argument")

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    pop = _immutable
    popitem = _immutable
    setdefault = _immutable
    update = _immutable

    def __hash__(self):
        return self._hash


class HashableList(list):
    """A read-only ``list`` that can be hashed. Same reasoning as HashableDict."""

    __slots__ = ("_hash",)

    def __init__(self, iterable=()):
        super().__init__(iterable)
        self._hash = hash(tuple(freeze(v) for v in self))

    def _immutable(self, *a, **k):
        raise TypeError("HashableList is a read-only cache argument")

    append = _immutable
    extend = _immutable
    insert = _immutable
    remove = _immutable
    pop = _immutable
    clear = _immutable
    sort = _immutable
    reverse = _immutable
    __setitem__ = _immutable
    __delitem__ = _immutable
    __iadd__ = _immutable

    def __hash__(self):
        return self._hash


def freeze(value):
    """Make ``value`` hashable while keeping it a ``dict``/``list`` where it was.

    ``st.cache_data`` hashes every argument to build its cache key and raises
    ``StreamlitAPIException`` when one is unhashable. Several diagrams are
    naturally parameterised by lists of readings and dicts of sample points, so
    those have to be frozen before they cross the decorator. Returning tuples
    instead would break the very code doing the drawing, which still wants to do
    ``series["position"]`` and ``for row in rows``.
    """
    if isinstance(value, HashableDict) or isinstance(value, HashableList):
        return value
    if isinstance(value, dict):
        return HashableDict({k: freeze(v) for k, v in value.items()})
    if isinstance(value, (list, tuple)):
        return HashableList(freeze(v) for v in value)
    if isinstance(value, set):
        return frozenset(freeze(v) for v in value)
    return value


#: Font stacks used across the diagram library.
MONO = "JetBrains Mono, monospace"
SANS = "Inter, system-ui, sans-serif"


def label(x, y, text, fill=MUTED, size=10, anchor="start", family=None):
    """One SVG ``<text>`` element."""
    family = family or MONO
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{fill}" '
            f'font-size="{size}" font-family="{family}">{text}</text>')


def tick(x, y, text, fill=MUTED, size=9, anchor="middle"):
    """A short axis mark with its label beneath."""
    return (f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y + 4:.1f}" '
            f'stroke="{fill}" stroke-width="1"/>'
            + label(x, y + 14, text, fill, size, anchor))
