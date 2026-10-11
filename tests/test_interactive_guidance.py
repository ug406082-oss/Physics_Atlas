"""Every interactive station must tell the learner what to do with it.

The brief for this app is that a student should be able to work through it
without the book. A slider with no explanation of what to change is not a
teaching aid, it is decoration, so each station that has controls opens with a
`how_to` line saying what the controls do.
"""

from __future__ import annotations

import ast
import pathlib

import pytest

CHAPTER_FILES = sorted(pathlib.Path("physics/chapters").glob("ch*.py"))
WIDGET_CALLS = {"st.slider", "st.number_input", "st.selectbox", "st.multiselect",
                "st.radio", "st.checkbox", "st.toggle"}


def _has_widgets(fn: ast.FunctionDef) -> bool:
    return any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
               and ast.unparse(n.func) in WIDGET_CALLS for n in ast.walk(fn))


def _mentions_how_to(fn: ast.FunctionDef) -> bool:
    for n in ast.walk(fn):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            if n.func.id == "how_to":
                return True
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            if ast.unparse(n.func).endswith(".how_to"):
                return True
        if isinstance(n, ast.Name) and n.id == "how_to":
            return True
    return False


def _station_functions(path: pathlib.Path):
    """Functions used as station renderers, which are the ones a learner opens."""
    tree = ast.parse(path.read_text())
    src = path.read_text()
    out = []
    for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
        # a station renderer is referenced in the RENDERERS mapping
        if f': {fn.name},' in src or f": lambda: {fn.name}(" in src:
            if _has_widgets(fn):
                out.append(fn)
    return out


def test_the_helper_exists():
    """engine imports Streamlit, which is absent here, so read it as source."""
    src = pathlib.Path("physics/engine.py").read_text()
    assert "def how_to(" in src
    assert "HOWTO = {" in src
    assert src.count('"sliders"') + src.count("'sliders'") >= 1


@pytest.mark.parametrize("path", CHAPTER_FILES, ids=lambda p: p.stem)
def test_every_interactive_station_explains_itself(path):
    missing = [fn.name for fn in _station_functions(path) if not _mentions_how_to(fn)]
    assert not missing, f"{path.stem}: {missing} use widgets but never call how_to()"
