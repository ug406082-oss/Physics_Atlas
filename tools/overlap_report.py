#!/usr/bin/env python3
"""Turn overlap.json from overlap_probe.js into a grouped, readable summary.

Usage:
    python tools/overlap_report.py overlap.json
    python tools/overlap_report.py overlap.json --top 5
"""
import argparse
import json
import pathlib
import sys
from collections import Counter, defaultdict

TESTIDS = {
    "stSlider": "slider",
    "stSliderTickBarMin": "slider tick",
    "stNumberInput": "number input",
    "stTextInput": "text input",
    "stSelectbox": "select box",
    "stRadio": "radio group",
    "stCheckbox": "checkbox",
    "stToggleButton": "toggle",
    "stTabs": "tab bar",
    "stTab": "tab",
    "stExpander": "expander",
    "stDataFrame": "data table",
    "stPlotlyChart": "plotly chart",
    "stImage": "image",
    "stButton": "button",
    "stMarkdown": "markdown",
    "stLatex": "equation",
    "stCaption": "caption",
    "stSubheader": "subheader",
    "stHeader": "header",
    "stMetric": "metric",
}


def friendly(info):
    """Human name for one side of a pair."""
    tid = info.get("testid")
    if tid and tid in TESTIDS:
        base = TESTIDS[tid]
    else:
        base = (info.get("role") or "?").replace("st", "st_")
    label = (info.get("label") or "").strip()
    return f"{base} “{label}”" if label else base


def classify(pair):
    """Group a pair by the two Streamlit widget kinds involved."""
    a, b = pair["a"], pair["b"]
    return tuple(sorted([
        (a.get("testid") or a.get("role") or "?").replace("st", "st_"),
        (b.get("testid") or b.get("role") or "?").replace("st", "st_"),
    ]))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_file", help="overlap.json saved from the browser")
    ap.add_argument("--top", type=int, default=15, help="how many pairs to show")
    args = ap.parse_args()

    path = pathlib.Path(args.json_file)
    if not path.exists():
        sys.exit(f"not found: {path}")

    pairs = json.loads(path.read_text())
    if not pairs:
        print("No overlapping pairs recorded - nothing to fix in this capture.")
        return

    print(f"Overlap report for {path.name}")
    print(f"{len(pairs)} overlapping pair(s)\n")

    stacked = sum(1 for p in pairs if p.get("stacked"))
    if stacked:
        print(f"  {stacked} pair(s) are fully stacked (duplicate/ghost overlays) "
              f"- these are almost always the worst kind.\n")

    print("Most frequent collisions")
    counts = Counter(classify(p) for p in pairs)
    for (a, b), n in counts.most_common(8):
        print(f"  {n:3d}×  {a}  ↔  {b}")
    print()

    print(f"Worst {min(args.top, len(pairs))} pairs")
    for i, p in enumerate(pairs[:args.top], 1):
        flag = "STACKED" if p.get("stacked") else f"{p['overlapPx']}px"
        print(f"  {i:2d}. [{flag}] {friendly(p['a'])}")
        print(f"      overlaps    {friendly(p['b'])}")


if __name__ == "__main__":
    main()