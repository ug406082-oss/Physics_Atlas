"""Static layout check over every diagram in the library.

Streamlit cannot be run in this sandbox, so the diagrams are checked the way a
printer would: the SVG is generated, then every <text> element is measured
against the viewBox it has to fit inside. Text that runs past an edge is
clipped in the browser, and text below 9px is unreadable on a phone.

    python3 tools/check_diagrams.py
"""
from __future__ import annotations

import re
import sys

sys.path.insert(0, ".")
exec(open("tools/smoke_app.py").read().split("failures = []")[0])   # noqa: S102

import importlib

#: Average glyph width as a fraction of font size, for a monospace-ish label.
GLYPH = 0.60
SMALLEST_READABLE = 9


def measure(svg):
    """Return (overflow_right, below_bottom, too_small) for one SVG string."""
    box = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    if not box:
        return ["no viewBox"], [], []
    width, height = float(box.group(1)), float(box.group(2))
    over, below, small = [], [], []
    for tag in re.finditer(r'<text([^>]*)>([^<]*)</text>', svg):
        attrs, text = tag.group(1), tag.group(2)
        if not text.strip():
            continue
        xs = re.search(r'\bx="(-?[\d.]+)"', attrs)
        ys = re.search(r'\by="(-?[\d.]+)"', attrs)
        fs = re.search(r'font-size="(\d+)"', attrs)
        if not (xs and ys and fs):
            continue
        x, y, size = float(xs.group(1)), float(ys.group(1)), int(fs.group(1))
        anchor = re.search(r'text-anchor="(\w+)"', attrs)
        anchor = anchor.group(1) if anchor else "start"
        span = len(text) * size * GLYPH
        left = x if anchor == "start" else (x - span / 2 if anchor == "middle" else x - span)
        if left + span > width + 3:
            over.append(f"{text[:34]!r} needs {left + span:.0f}px of {width:.0f}px")
        if y > height + 2 or y - size < -2:
            below.append(f"{text[:30]!r} at y={y:.0f} in a {height:.0f}px box")
        if size < SMALLEST_READABLE:
            small.append(f"{size}px: {text[:30]!r}")
    return over, below, small


def main():
    checked, problems = 0, []
    for number in range(1, 11):
        try:
            module = importlib.import_module(f"physics.visuals.ch{number:02d}")
        except ModuleNotFoundError:
            continue
        for name in sorted(dir(module)):
            if name.startswith("_"):
                continue
            fn = getattr(module, name)
            if not callable(fn):
                continue
            try:
                svg = fn()
            except TypeError:
                continue          # needs arguments; the smoke test covers those
            except Exception:
                continue
            if not isinstance(svg, str) or not svg.startswith("<svg"):
                continue
            checked += 1
            over, below, small = measure(svg)
            for kind, items in (("text runs past the right edge", over),
                                ("text sits outside the box", below),
                                ("text too small to read", small)):
                for item in items:
                    problems.append(f"ch{number:02d}.{name}: {kind}: {item}")

    print(f"diagrams measured: {checked}")
    if not problems:
        print("layout problems: none")
        return 0
    print(f"layout problems: {len(problems)}")
    for line in problems[:40]:
        print("   ", line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
