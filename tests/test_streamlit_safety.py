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


def _curriculum():
    """The chapter modules pull in pandas/numpy via streamlit.

    A wheel built for a different interpreter can be installed and still
    unimportable, which says nothing about these tests - skip rather than fail.
    """
    try:
        from physics import curriculum
        # chapter_ui() imports each chapter's UI module on first use, and those
        # pull in pandas/numpy. Warm them here so a bad wheel skips the test
        # instead of blowing up half way through it.
        for number in range(1, 11):
            curriculum.chapter_ui(number)
    except ImportError as exc:
        pytest.skip(f"numeric stack unavailable in this environment: {exc}")
    return curriculum


def test_no_station_renders_the_same_outcome_twice():
    """Streamlit raises StreamlitDuplicateElementKey on a repeated widget key.

    An outcome may legitimately appear in more than one station, but each
    rendering gets its own key, or the second one aborts the whole station.
    """
    import collections

    curriculum = _curriculum()

    for number in range(1, 11):
        ui = curriculum.chapter_ui(number)
        stations = getattr(ui, "STATIONS", None) or ui.SPEC.stations
        seen = collections.Counter()
        for station in stations:
            for slo in ui.SPEC.slos:
                if slo["id"] in station.slos:
                    seen[f"{ui.SPEC.key_prefix}ans_{station.key}_{slo['id']}"] += 1
        dupes = {k: v for k, v in seen.items() if v > 1}
        assert not dupes, f"chapter {number} renders these twice: {dupes}"


def test_overview_stations_claim_no_outcomes():
    """The overview lists outcomes; it does not teach them.

    Giving it the whole chapter's outcomes makes the engine's per-station review
    render every lesson on the overview *and* again on each teaching station.
    """
    curriculum = _curriculum()
    for number in range(1, 11):
        ui = curriculum.chapter_ui(number)
        stations = getattr(ui, "STATIONS", None) or ui.SPEC.stations
        overview = [s for s in stations if s.key == "overview"][0]
        assert not overview.slos, (
            f"chapter {number} overview claims {overview.slos}")
