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

import re

from streamlit import cache_data

from ..theme import MUTED

__all__ = ["_svg", "wrap", "defs", "cached", "freeze", "label", "tick", "para",
           "MONO", "SANS", "GLYPH", "HashableDict", "HashableList"]

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


_TEXT = re.compile(
    r'<text(?P<attrs>[^>]*)>(?P<content>[^<]*)</text>')


def _reflow(body: str, width: int) -> str:
    """Wrap any label that would run past the edge of the diagram.

    SVG has no line wrapping: a label wider than its viewBox is simply clipped
    and the learner loses the end of the sentence. Rather than trusting every
    diagram to stay inside its box, this is enforced once, here, where the box
    is already known. Labels that fit are left exactly as they were.
    """
    def fix(match):
        attrs, content = match.group("attrs"), match.group("content")
        if not content.strip():
            return match.group(0)
        xs = re.search(r'\bx="(-?[\d.]+)"', attrs)
        ys = re.search(r'\by="(-?[\d.]+)"', attrs)
        fs = re.search(r'font-size="(\d+)"', attrs)
        if not (xs and ys and fs):
            return match.group(0)
        x, y, size = float(xs.group(1)), float(ys.group(1)), int(fs.group(1))
        anchor = re.search(r'text-anchor="(\w+)"', attrs)
        anchor = anchor.group(1) if anchor else "start"
        if fits(x, content, size, width, anchor):
            return match.group(0)

        chars = max(int((width - x - 6) / (size * GLYPH)), 8)
        words, lines, current = content.split(), [], ""
        for word in words:
            if len(current) + len(word) + 1 > chars and current:
                lines.append(current)
                current = word
            else:
                current = f"{current} {word}".strip()
        if current:
            lines.append(current)
        gap = size + 3
        return "".join(
            f'<text{attrs[:xs.start()]}x="{x}" y="{y + i * gap:.1f}"{attrs[xs.end():]}'
            f'{line}</text>' for i, line in enumerate(lines))

    return _TEXT.sub(fix, body)


def _svg(body: str, width: int, height: int, label: str = "") -> str:
    role = f'role="img" aria-label="{label}"' if label else ""
    return (
        f'<svg viewBox="0 0 {width} {height}" width="100%" '
        f'style="max-width:{width}px;display:block;margin:0 auto" {role}>'
        f"{_reflow(body, width)}</svg>"
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


def text_extent(x, y, text, size=10, anchor="start"):
    """Approximate the box a piece of text will occupy.

    SVG will not tell us where a string ends, so width is estimated from the
    average glyph width. That is good enough to keep labels apart, which is all
    it is for.
    """
    width = len(str(text)) * GLYPH * size
    if anchor == "middle":
        x -= width / 2
    elif anchor == "end":
        x -= width
    return {"x": x, "y": y - size, "w": width, "h": size * 1.25}


def overlaps(a, b, pad=2.0):
    """Do two text boxes collide?"""
    return (a["x"] < b["x"] + b["w"] + pad and b["x"] < a["x"] + a["w"] + pad
            and a["y"] < b["y"] + b["h"] + pad and b["y"] < a["y"] + a["h"] + pad)


def declutter(boxes, pad=3.0, step=12.0, max_rounds=14, bounds=None):
    """Nudge labels apart so none of them sit on top of another.

    Marks on a scientific plot sit at fixed data positions - a most-probable
    speed and a mean speed are close together by definition - so placing their
    labels at those positions guarantees a collision. This walks the labels in
    reading order and lifts each one clear of the ones already placed, keeping
    it within the plot's vertical bounds where they are given.

    Shared deliberately: the Maxwell-Boltzmann curve, the P-V process paths and
    the phase diagrams all hit this, and patching each one separately is how
    they drifted apart in the first place.
    """
    boxes = [dict(b) for b in boxes]
    placed = []
    for box in boxes:
        for _ in range(max_rounds):
            clash = next((p for p in placed if overlaps(box, p, pad)), None)
            if clash is None:
                break
            box["y"] = clash["y"] + clash["h"] + step
        placed.append(box)

    # Clamping each overflowing label to the limit on its own piles them all on
    # the same line, which is the collision we started with. Move the whole
    # stack instead, so the lanes stay distinct however tight the band is.
    if bounds:
        top, bottom = bounds
        lowest = max(b["y"] + b["h"] for b in placed)
        if lowest > bottom:
            shift = lowest - bottom
            for b in placed:
                b["y"] -= shift
        highest = min(b["y"] for b in placed)
        if highest < top:
            lift = top - highest
            for b in placed:
                b["y"] += lift
    return boxes


def stacked_labels(x_of, y_of, marks, pad=3.0, bounds=None, **style):
    """Place a set of ``(data_x, text, colour)`` marks without collisions.

    Each mark gets a vertical leader line down to the axis so it stays attached
    to the value it names even after its label has been lifted.
    """
    boxes = [text_extent(x_of(vx), text, anchor="middle", **style)
             for vx, text, _colour in marks]
    placed = declutter(boxes, pad=pad, bounds=bounds)
    out = []
    for (vx, text, colour), box in zip(marks, placed):
        out.append({"x": x_of(vx), "text": text, "colour": colour, "y": box["y"]})
    return out


def tick(x, y, text, fill=MUTED, size=9, anchor="middle"):
    """A short axis mark with its label beneath."""
    return (f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y + 4:.1f}" '
            f'stroke="{fill}" stroke-width="1"/>'
            + label(x, y + 14, text, fill, size, anchor))


#: Average glyph width as a fraction of font size. Used to size and wrap text.
GLYPH = 0.60


def para(x, y, text, width_chars=48, fill=None, size=10, family=None,
         line_gap=13, anchor="start"):
    """A block of prose, wrapped so it cannot run off the edge of the diagram.

    ``st.markdown`` will happily accept one long ``<text>`` element, but SVG
    does not wrap: anything wider than the viewBox is simply clipped, and the
    learner loses the end of the sentence. This breaks the text into lines of
    ``width_chars`` and returns one ``<text>`` per line, growing downwards.
    """
    fill = fill or MUTED
    words, lines, current = text.split(), [], ""
    for word in words:
        if len(current) + len(word) + 1 > width_chars and current:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    return "".join(label(x, y + i * line_gap, line, fill, size, anchor, family)
                   for i, line in enumerate(lines))


def fits(x, text, size, box_width, anchor="start"):
    """Whether a single label at ``x`` stays inside ``box_width``.

    Diagrams call this through the test suite so a label that would be clipped
    is caught at build time rather than in a browser.
    """
    span = len(text) * size * GLYPH
    left = x if anchor == "start" else (x - span / 2 if anchor == "middle" else x - span)
    return left >= -3 and left + span <= box_width + 3
