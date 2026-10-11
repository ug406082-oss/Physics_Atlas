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


def _unkeyed(path: pathlib.Path, target: str) -> list:
    """Line numbers of calls to ``target`` with no ``key=`` nearby."""
    tree = ast.parse(path.read_text())
    lines = path.read_text().split("\n")
    bad = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and ast.unparse(node.func) == target):
            continue
        if any(kw.arg == "key" for kw in node.keywords):
            continue
        window = "\n".join(lines[max(0, node.lineno - 2):node.end_lineno + 1])
        if "key=" not in window:
            bad.append(node.lineno)
    return bad


@pytest.mark.parametrize("path", sorted(CHAPTER_DIR.glob("*.py")) + [PROJECT / "physics" / "chapter1.py"],
                         ids=lambda p: p.stem)
@pytest.mark.parametrize("target", ["st.plotly_chart", "st.tabs"])
def test_every_registering_element_has_a_key(path, target):
    """StreamlitDuplicateElementId is otherwise thrown at render time."""
    bad = _unkeyed(path, target)
    assert not bad, f"{path.stem}: {target} without a key on line(s) {bad}"


def test_no_dataframe_is_called_bare():
    """`st.dataframe` must go through engine.table(), which supplies the key.

    Streamlit registers a dataframe element ID from its type and options, so two
    unkeyed dataframes with the same options collide and abort the station.
    """
    engine_src = (PROJECT / "physics" / "engine.py").read_text()
    assert "def table(" in engine_src, "engine.table() is missing"
    for path in sorted(CHAPTER_DIR.glob("*.py")) + [PROJECT / "physics" / "chapter1.py"]:
        source = path.read_text()
        assert "st.dataframe(" not in source, (
            f"{path.name} calls st.dataframe directly; use table() so it gets a key")
