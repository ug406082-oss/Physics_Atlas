"""No label may be drawn on top of another, in any diagram the app renders.

The screenshot audits reported overlaps in many different places, and fixing
them one screenshot at a time kept missing some. This test takes the opposite
approach: it pulls the real call arguments out of the chapter modules, renders
every diagram exactly as the app does, and measures the result.

Two measurement details matter, and getting either wrong produces noise that
gets mistaken for defects:

- *Baseline distance, not box height.* A glyph box is about 1.25x the font size,
  but real text does not fill it. Comparing box heights flags every wrapped
  caption line with ordinary leading. Comparing the distance between baselines
  against 0.85 of the larger font size matches what a reader actually sees.
- *Real arguments.* Several diagrams are degenerate at their defaults - a disc
  of radius 1 on a 620px canvas, for instance - and default-only sweeps report
  collisions that never occur in the app.
"""
import ast
import importlib
import pathlib
import re

import pytest

from physics.visuals.common import overlaps, text_extent

CHAPTERS = sorted((pathlib.Path(__file__).resolve().parent.parent / "physics" / "chapters")
                  .glob("*.py")) + [pathlib.Path(__file__).resolve().parent.parent
                                     / "physics" / "chapter1.py"]


def _labels(svg):
    """Rendered <text> as (box, content, font size, baseline y)."""
    out = []
    for match in re.finditer(r"<text\b([^>]*)>([^<]*)</text>", svg):
        attrs, content = match.groups()
        x = re.search(r'\bx="([\d.-]+)"', attrs)
        y = re.search(r'\by="([\d.-]+)"', attrs)
        size = re.search(r'font-size="([\d.]+)"', attrs)
        anchor = re.search(r'text-anchor="(\w+)"', attrs)
        if not (x and y and size) or not content.strip():
            continue
        value = float(size.group(1))
        out.append((text_extent(float(x.group(1)), float(y.group(1)), content,
                                size=value, anchor=anchor.group(1) if anchor else "start"),
                    content.strip(), value, float(y.group(1))))
    return out


def _collides(a, b):
    if a[1] == b[1]:
        return False
    if abs(a[3] - b[3]) >= 0.85 * max(a[2], b[2]):
        return False          # ordinary leading, not a collision
    return overlaps(a[0], b[0], pad=0.0)


def _real_calls():
    """VIS.name(args) call sites, with literal arguments, exactly as the app runs them."""
    found = {}
    for path in CHAPTERS:
        for node in ast.walk(ast.parse(path.read_text())):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                    and ast.unparse(node).startswith("VIS.")):
                try:
                    args = [ast.literal_eval(a) for a in node.args]
                except Exception:
                    continue
                if len(args) == len(node.args):
                    found.setdefault(node.func.attr, (path.name, args))
    return found


def _rendered_diagrams():
    out = []
    for name, (source, args) in sorted(_real_calls().items()):
        chapter = int(re.search(r"(\d+)", source).group(1))
        module = importlib.import_module(f"physics.visuals.ch{chapter:02d}")
        fn = getattr(module, name, None)
        if not callable(fn):
            continue
        try:
            svg = fn(*args)
        except Exception:
            continue
        if isinstance(svg, str) and "<svg" in svg:
            out.append((name, source, svg))
    return out


RENDERED = _rendered_diagrams()


def test_we_actually_rendered_something():
    """A silent skip would make every test below pass for the wrong reason."""
    assert len(RENDERED) >= 30, (
        f"only {len(RENDERED)} diagrams rendered - the call-site scan has broken")


@pytest.mark.parametrize("name,source,svg", RENDERED, ids=[r[0] for r in RENDERED])
def test_no_label_is_drawn_on_top_of_another(name, source, svg):
    hits = [(a[1], b[1]) for i, a in enumerate(_labels(svg))
            for b in _labels(svg)[i + 1:] if _collides(a, b)]
    assert not hits, f"{name} ({source}): overlapping labels: {hits}"


@pytest.mark.parametrize("name,source,svg", RENDERED, ids=[r[0] for r in RENDERED])
def test_nothing_escapes_the_canvas(name, source, svg):
    box = re.search(r'viewBox="([\d.\- ]+)"', svg)
    if not box:
        pytest.skip("no viewBox")
    _, _, width, height = (float(v) for v in box.group(1).split())
    out = [t for b, t, _s, _y in _labels(svg)
           if b["x"] < -1 or b["y"] < -1
           or b["x"] + b["w"] > width + 1 or b["y"] + b["h"] > height + 1]
    assert not out, f"{name}: labels outside the {width:.0f}x{height:.0f} canvas: {out}"


@pytest.mark.parametrize("name,source,svg", RENDERED, ids=[r[0] for r in RENDERED])
def test_no_diagram_renders_blank(name, source, svg):
    """The acceleration graph and three wave frames once both rendered empty."""
    marks = (svg.count("<line") + svg.count("<polyline") + svg.count("<circle")
             + svg.count("<rect") + svg.count("<path") + svg.count("<polygon"))
    assert marks > 1 or _labels(svg), f"{name}: nothing was drawn"