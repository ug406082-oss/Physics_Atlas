"""Two Streamlit rules that only bite at runtime.

Both of these produce an app that renders perfectly in the stubbed smoke test
and then fails in the browser, because the stub does not assign element IDs and
does not encode strings to UTF-8:

* Streamlit derives an element's internal ID from its type **and its parameters**.
  Two ``plotly_chart`` calls built from identical data therefore collide and the
  second raises ``StreamlitDuplicateElementId``, which aborts the whole station.
* A lone surrogate cannot be encoded to UTF-8. Streamlit serialises every
  string it is given, so a station label written as ``"\\ud83d\\udd2c"`` renders
  as nothing and then raises ``UnicodeEncodeError``.
"""

from __future__ import annotations

import ast
import pathlib
import re

import pytest

from physics import curriculum

PROJECT = pathlib.Path(__file__).resolve().parent.parent
CHAPTER_DIR = PROJECT / "physics" / "chapters"
PLOTLY = "st.plotly_chart"
SURROGATE = re.compile(r"\\u[dD][89ABCDEFab-cdef][0-9A-Fa-f]{2}")


def _sources():
    yield from sorted(CHAPTER_DIR.glob("*.py"))
    yield PROJECT / "physics" / "chapter1.py"
    yield PROJECT / "streamlit_app.py"


def test_no_surrogate_escapes_survive_in_any_source():
    """A surrogate pair written as two \\u escapes is not an emoji."""
    offenders = []
    for path in _sources():
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text().split("\n"), 1):
            if SURROGATE.search(line):
                offenders.append(f"{path.name}:{number}")
    assert not offenders, f"surrogate escapes left: {offenders}"


def test_every_station_label_encodes_to_utf8():
    for number in range(1, 11):
        for station in curriculum.chapter_data(number).STATIONS:
            label = station["label"]
            label.encode("utf-8")                     # must not raise
            assert any(ord(c) > 0x2000 for c in label), (
                f"chapter {number} station {station['key']} has no emoji: {label!r}")
            assert "?" not in label[:2], (
                f"chapter {number} station {station['key']} lost its emoji to a placeholder")


def test_every_station_label_is_distinct():
    """Identical labels make tabs unreadable."""
    for number in range(1, 11):
        labels = [s["label"] for s in curriculum.chapter_data(number).STATIONS]
        assert len(labels) == len(set(labels)), f"chapter {number} has duplicate station labels"


def _unkeyed_plotly(path: pathlib.Path) -> list:
    """Line numbers of plotly_chart calls with no ``key=`` in the next few lines."""
    tree = ast.parse(path.read_text())
    bad = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and ast.unparse(node.func) == PLOTLY):
            continue
        keys = [kw for kw in node.keywords if kw.arg == "key"]
        ok = bool(keys)
        if not ok:
            # a key may sit on a continuation line, so check the raw text too
            snippet = "\n".join(path.read_text().split("\n")[
                node.lineno - 1:node.lineno + 4])
            ok = "key=" in snippet
        if not ok:
            bad.append(node.lineno)
    return bad


@pytest.mark.parametrize("path", sorted(CHAPTER_DIR.glob("*.py")),
                         ids=lambda p: p.stem)
def test_every_plotly_chart_has_a_key(path):
    """StreamlitDuplicateElementId is otherwise thrown at render time."""
    bad = _unkeyed_plotly(path)
    assert not bad, f"{path.stem}: plotly_chart without a key on line(s) {bad}"


def test_chapter_one_plotly_is_keyed():
    bad = _unkeyed_plotly(PROJECT / "physics" / "chapter1.py")
    assert not bad, f"chapter1.py: plotly_chart without a key on line(s) {bad}"
