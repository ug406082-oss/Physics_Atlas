"""Validate inspect_screenshots.py against images with known defects.

Pixel heuristics are easy to write and easy to get quietly wrong - a detector
that fires on every page is worse than none, because it turns a clean report
into noise nobody reads. These tests build synthetic images where the answer is
known by construction, then check the detector finds the planted defect and,
just as importantly, stays quiet on the control.
"""
import pathlib
import struct
import sys
import zlib

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "tools"))
import inspect_screenshots as ins  # noqa: E402

BG = (16, 24, 38)
INK = (222, 234, 248)


def write_png(path, w, h, rows):
    raw = bytearray()
    for row in rows:
        raw.append(0)
        for r, g, b in row:
            raw += bytes((r, g, b))

    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(bytes(raw), 6))
           + chunk(b"IEND", b""))
    path.write_bytes(png)


def blank(w, h, bg=BG):
    return [[bg] * w for _ in range(h)]


def glyph_rows(rows, y, x0, x1, y0, y1, gap=6, width=2):
    """A row of separate 'glyphs' - the shape of normal, readable text."""
    x = x0
    while x < x1:
        if x + width > x1:
            break
        for yy in range(y0, y1):
            for xx in range(x, x + width):
                rows[yy][xx] = INK
        x += width + gap


def merged_rows(rows, y0, y1, x0, x1):
    """A solid strip: what two lines of text drawn on top of each other look like."""
    for yy in range(y0, y1):
        for xx in range(x0, x1):
            rows[yy][xx] = INK


def test_plain_text_is_not_flagged_as_a_collision(tmp_path):
    rows = blank(600, 200)
    for y0 in (40, 80, 120):
        glyph_rows(rows, y0, 40, 540, y0, y0 + 12)
    p = tmp_path / "clean.png"
    write_png(p, 600, 200, rows)

    result = ins.analyse(p, max_width=600)
    kinds = {f["kind"] for f in result["findings"] if f["severity"] != "none"}
    assert "glyph_collision" not in kinds, (
        "normal text must not be reported as overlapping glyphs")


def test_a_band_filled_like_overlapping_text_is_flagged(tmp_path):
    rows = blank(600, 200)
    glyph_rows(rows, 40, 40, 540, 40, 52)      # normal text, must stay quiet
    merged_rows(rows, 120, 134, 40, 540)       # the planted defect
    p = tmp_path / "collide.png"
    write_png(p, 600, 200, rows)

    result = ins.analyse(p, max_width=600)
    hits = [f for f in result["findings"] if f["kind"] == "glyph_collision"]
    assert hits, "a text band filled like overlapping text was not flagged"
    top = max(hits, key=lambda f: f["location"]["y"])
    assert top["location"]["y"] >= 100, (
        f"detection landed on the wrong band: {top['location']}")
    assert top["confidence"] == "low", (
        "a screenshot cannot prove overlap; confidence must stay low")


def test_content_running_off_the_right_edge_is_detected(tmp_path):
    rows = blank(400, 200)
    glyph_rows(rows, 40, 40, 360, 40, 52)
    for yy in range(40, 180):               # a panel overflowing the edge
        for xx in range(386, 400):
            rows[yy][xx] = INK
    p = tmp_path / "clip.png"
    write_png(p, 400, 200, rows)

    result = ins.analyse(p, max_width=400)
    sides = {f["location"].get("side")
             for f in result["findings"] if f["kind"] == "viewport_clip"}
    assert "right" in sides, f"right-edge overflow missed; got {sides}"


def test_background_gradient_does_not_become_content(tmp_path):
    """The regression that made every earlier reading meaningless."""
    rows = []
    for y in range(200):
        shade = 16 + y // 8                      # a smooth vertical gradient
        rows.append([(shade, shade + 8, shade + 22)] * 600)
    p = tmp_path / "gradient.png"
    write_png(p, 600, 200, rows)

    result = ins.analyse(p, max_width=600)
    frac = result["diagnostics"]["content_fraction"]
    assert frac < 0.10, f"gradient read as {frac:.0%} content; should be near zero"


def test_a_real_app_screenshot_measures_sane(tmp_path):
    """Guard against the whole class of bug at once, on a captured screenshot."""
    shots = pathlib.Path("/workspace/Screenshots")
    if not shots.is_dir():
        pytest.skip("no captured screenshots available")
    shot = sorted(shots.glob("*.png"))[0]
    result = ins.analyse(shot, max_width=960)
    frac = result["diagnostics"]["content_fraction"]
    assert 0.01 < frac < 0.45, (
        f"content fraction {frac:.2f} is implausible for a normal page")
    assert result["text_bands"] >= 3, "no text found on a real app screenshot"