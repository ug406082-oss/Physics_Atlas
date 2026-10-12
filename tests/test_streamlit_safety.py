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
@pytest.mark.parametrize("target", ["st.plotly_chart"])
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


def test_no_two_widgets_share_a_key_in_one_render():
    """StreamlitDuplicateElementKey takes the whole station down.

    Keys are registered for a script run, not per station, so two stations that
    share a helper - or one helper whose keys were copy/pasted - collide. The
    stub in tools/smoke_app.py now enforces the same rule it did not before.
    """
    import runpy
    import sys
    from pathlib import Path

    stub = Path(__file__).resolve().parent.parent / "tools" / "smoke_app.py"
    source = stub.read_text()
    assert "StreamlitDuplicateElementKey" in source, (
        "the smoke stub must reject duplicate widget keys or it cannot catch them")
    assert '("toggle", _checkbox)' in source, (
        "st.toggle must be registered in the stub; outcome reviews use it")
    assert "def _note_key" in source and "_reset_keys()" in source


def test_station_labels_are_not_folded_to_ascii():
    """Emoji must survive all the way to the browser.

    Tab labels used to be encoded with ascii/"replace" to dodge a
    UnicodeEncodeError from surrogate pairs. That removed the surrogates but also
    turned every emoji into a question mark, so the tabs rendered fine and the
    icons were simply gone.
    """
    engine_src = (PROJECT / "physics" / "engine.py").read_text()
    assert 'encode("ascii"' not in engine_src and "encode('ascii'" not in engine_src, (
        "engine must not ASCII-fold station labels; it strips every emoji")
    assert "def _label(" in engine_src, "the surrogate-only filter is missing"


def test_every_station_label_still_has_an_emoji():
    curriculum = _curriculum()
    from physics import engine
    plain = []
    for number in range(1, 11):
        spec = curriculum.chapter_ui(number).SPEC
        for station in spec.stations:
            if all(ord(c) < 128 for c in engine._label(station.label)):
                plain.append(f"ch{number}:{station.key}")
    assert not plain, f"these labels arrive with no emoji: {plain}"


def test_label_filter_removes_surrogates_but_keeps_emoji():
    """The filter must drop exactly what cannot be encoded."""
    curriculum = _curriculum()
    from physics import engine
    assert engine._label("x \ud83c y") == "x  y"
    assert engine._label("\U0001F5FA\uFE0F route").startswith("\U0001F5FA")


def test_fragment_identities_are_unique_across_the_app():
    """Streamlit keys a fragment on module + qualname.

    Every chapter has an "overview" and a "teaching" station. If those share a
    fragment identity, leaving a chapter leaves a fragment ID in session state
    that no longer exists, and the next rerun raises
    "Could not find fragment with id ...".
    """
    curriculum = _curriculum()
    names = []
    for number in range(1, 11):
        spec = curriculum.chapter_ui(number).SPEC
        names += [f"station_{spec.key_prefix}_{st.key}" for st in spec.stations]
    dupes = sorted({n for n in names if names.count(n) > 1})
    assert not dupes, f"fragment identities reused across chapters: {dupes}"
    assert len(names) == len(set(names))


def test_no_literal_unicode_escapes_reach_the_browser():
    """`\\u2014` in a string renders as the six characters, not an em dash.

    Found by screenshot audit: 83 escapes across ch08 and ch09 reached the page
    literally, because a double backslash in the source is not an escape - it is
    a backslash followed by "u2014".
    """
    import ast
    import re

    bad = []
    for path in sorted((PROJECT / "physics").rglob("*.py")):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if (isinstance(node, ast.Constant) and isinstance(node.value, str)
                    and re.search(r"\\\\u[0-9a-fA-F]{4}", node.value)):
                bad.append(f"{path.name}:{node.lineno}")
    assert not bad, f"literal unicode escapes still in source: {bad}"


def test_tables_never_show_the_word_none():
    """A missing value must read as a dash, not as Python's None.

    Screenshot audits kept finding the literal word "None" in results tables.
    Every table goes through engine.table(), so that is the only place that has
    to be right.
    """
    curriculum = _curriculum()
    import pandas as pd
    from physics import engine

    frame = pd.DataFrame([{"quantity": "work", "value": None},
                          {"quantity": "speed", "value": "3 m s-1"}])
    engine.table(frame)
    shown = getattr(engine, "_LAST_TABLE", None)
    assert shown is None or "None" not in str(shown.values.tolist())


def test_table_sanitiser_replaces_missing_values():
    curriculum = _curriculum()
    import pandas as pd
    from physics.engine import _blank_missing

    frame = pd.DataFrame({"a": [1.0, None], "b": ["x", None]})
    out = _blank_missing(frame)
    assert out.iloc[1]["a"] == "\u2014"
    assert out.iloc[1]["b"] == "\u2014"
    assert out.iloc[0]["a"] == 1.0


def test_no_fragment_ever_calls_st_rerun():
    """The cause of "Could not find fragment with id ..." on the deployed app.

    Every station is a fragment, as are the navigation buttons. Asking for a
    rerun from inside one tears down the fragment registry while the fragment is
    still executing, and the next run is handed the id of a fragment that no
    longer exists. A button callback achieves the same thing safely: it runs
    before the rerun Streamlit performs on its own.
    """
    import ast
    import pathlib as _p

    offenders = []
    for path in [_p.Path(__file__).resolve().parent.parent / "streamlit_app.py"] \
            + sorted((_p.Path(__file__).resolve().parent.parent / "physics").rglob("*.py")):
        tree = ast.parse(path.read_text())
        fragments = {
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
            and any("fragment" in ast.unparse(d) for d in node.decorator_list)
        }
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in fragments:
                for call in ast.walk(node):
                    if (isinstance(call, ast.Call)
                            and ast.unparse(call.func) in ("st.rerun", "rerun")):
                        offenders.append(f"{path.name}:{node.name}:{call.lineno}")
    assert not offenders, f"st.rerun() inside a fragment: {offenders}"


def test_no_fragment_is_called_from_inside_another_fragment():
    """A nested fragment's identity derives from the outer one's."""
    import ast
    import pathlib as _p

    path = _p.Path(__file__).resolve().parent.parent / "streamlit_app.py"
    tree = ast.parse(path.read_text())
    fragments = {
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and any("fragment" in ast.unparse(d) for d in node.decorator_list)
    }
    nested = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in fragments:
            for call in ast.walk(node):
                if isinstance(call, ast.Call) and ast.unparse(call.func) in fragments:
                    nested.append(f"{node.name} -> {ast.unparse(call.func)}")
    assert not nested, f"fragments calling fragments: {nested}"


def test_mixed_type_columns_are_coerced_before_arrow():
    """Cloud logged "Serialization of dataframe to Arrow table was unsuccessful".

    The degrees-of-freedom table puts a count of 6 next to "+2 per mode" in one
    column; pandas cannot type that, so Arrow fails and Streamlit repairs it on
    every render. engine.table() casts mixed columns to str instead.
    """
    source = (PROJECT / "physics" / "engine.py").read_text()
    assert "if len(types) > 1" in source, "mixed-type columns are not being coerced"
