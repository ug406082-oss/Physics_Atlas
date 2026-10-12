#!/usr/bin/env python3
"""inspect_screenshots.py - audit app screenshots for layout defects.

Point it at a PNG (or a folder of PNGs) and it writes a detailed report of
everything it can tell from the pixels alone:

  * content clipped by the viewport edge (horizontal/vertical overflow)
  * glyphs that have merged - overlapping text drawn on top of other text
  * collision bands, ranked by how badly the ink fills the line
  * coloured glyph clusters inside text lines (emoji that did or did not render)
  * text too close in brightness to its background (unreadable)
  * opaque blocks dense enough to hide what is underneath them
  * page furniture (header/toolbar) sitting on top of app content
  * repeated ink signatures, a hint of duplicated or stacked overlays

It cannot know a widget's name or intent - that needs the DOM. What it can do
is say exactly *where* something is wrong, to the pixel, and how sure it is.
Pair it with tools/overlap_probe.js for names.

Usage:
    python tools/inspect_screenshots.py shot.png
    python tools/inspect_screenshots.py ~/Screenshots/ -o report_dir
    python tools/inspect_screenshots.py ~/Screenshots/ --max 20 --min-severity low

No third-party packages required. Pillow is used for speed if installed.
"""

import argparse
import json
import math
import pathlib
import struct
import sys
import zlib
from collections import Counter, defaultdict

# ---------------------------------------------------------------------------
# image loading: Pillow when available, otherwise a small PNG decoder
# ---------------------------------------------------------------------------

try:
    from PIL import Image  # noqa: F401
    HAVE_PIL = True
except Exception:
    HAVE_PIL = False


class Raster:
    """Row-major RGB pixels plus its size."""

    __slots__ = ("w", "h", "rows")

    def __init__(self, w, h, rows):
        self.w, self.h, self.rows = w, h, rows

    def pixel(self, x, y):
        return self.rows[y][x]


def _load_pillow(path, max_width):
    from PIL import Image

    im = Image.open(path).convert("RGB")
    if im.width > max_width:
        scale = max_width / im.width
        im = im.resize((max_width, max(1, int(im.height * scale))), Image.BILINEAR)
    w, h = im.size
    data = list(im.tobytes())
    rows = [[tuple(data[(y * w + x) * 3:(y * w + x) * 3 + 3]) for x in range(w)]
            for y in range(h)]
    return Raster(w, h, rows), (w / max_width if max_width else 1.0)


def _decode_png(data, max_width):
    """Minimal PNG decoder: 8-bit, non-interlaced, grey/RGB/palette/alpha."""
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    pos, idat, w, h, depth, ctype, interlace, palette = 8, bytearray(), 0, 0, 8, 2, 0, None
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctag = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + length]
        if ctag == b"IHDR":
            w, h, depth, ctype, _comp, _filt, interlace = struct.unpack(">IIBBBBB", chunk)
            if depth != 8:
                raise ValueError(f"unsupported bit depth {depth}")
            if interlace:
                raise ValueError("interlaced PNG not supported")
        elif ctag == b"PLTE":
            palette = chunk
        elif ctag == b"IDAT":
            idat += chunk
        elif ctag == b"IEND":
            break
        pos += 12 + length

    raw = zlib.decompress(bytes(idat))
    nch = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ctype]
    stride = w * nch
    out = bytearray(h * stride)
    prev = bytearray(stride)
    p = 0
    for y in range(h):
        filt = raw[p]
        p += 1
        line = bytearray(raw[p:p + stride])
        p += stride
        if filt == 1:
            for i in range(nch, stride):
                line[i] = (line[i] + line[i - nch]) & 255
        elif filt == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 255
        elif filt == 3:
            for i in range(stride):
                a = line[i - nch] if i >= nch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif filt == 4:
            for i in range(stride):
                a = line[i - nch] if i >= nch else 0
                b = prev[i]
                c = prev[i - nch] if i >= nch else 0
                pp = a + b - c
                pa, pb, pc = abs(pp - a), abs(pp - b), abs(pp - c)
                pred = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pred) & 255
        out[y * stride:(y + 1) * stride] = line
        prev = line

    step = max(1, w // max_width) if max_width else 1
    ow, oh = w // step, h // step
    rows = []
    for y in range(0, h, step):
        base = y * stride
        row = []
        for x in range(0, w, step):
            i = base + x * nch
            if ctype == 2:
                row.append((out[i], out[i + 1], out[i + 2]))
            elif ctype == 6:
                row.append((out[i], out[i + 1], out[i + 2]))
            elif ctype == 0:
                g = out[i]
                row.append((g, g, g))
            elif ctype == 4:
                g = out[i]
                row.append((g, g, g))
            else:  # palette
                j = out[i] * 3
                row.append((palette[j], palette[j + 1], palette[j + 2]))
        rows.append(row)
    return Raster(ow, oh, rows[:oh]), float(step)


def load(path, max_width=960):
    if HAVE_PIL:
        return _load_pillow(str(path), max_width)
    return _decode_png(path.read_bytes(), max_width)


# ---------------------------------------------------------------------------
# analysis
# ---------------------------------------------------------------------------

def _lum(c):
    return (0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]) / 255.0


def _sat(c):
    mx, mn = max(c), min(c)
    return 0.0 if mx == 0 else (mx - mn) / mx


class Field:
    """Derived per-pixel measurements, computed once."""

    def __init__(self, img):
        self.w, self.h, self.rows = img.w, img.h, img.rows
        self.lum = [[0.0] * self.w for _ in range(self.h)]
        self.sat = [[0.0] * self.w for _ in range(self.h)]
        for y in range(self.h):
            lr, sr, row = self.lum[y], self.sat[y], self.rows[y]
            for x in range(self.w):
                c = row[x]
                lr[x] = _lum(c)
                sr[x] = _sat(c)

        # Background must be the *page's* dominant colour. Sampling the image
        # border picks up the browser's title bar and window frame, which are a
        # different shade to the app; then every pixel of the app reads as
        # "content" and every measurement below is meaningless.
        sample = Counter()
        sy = max(1, self.h // 240)
        sx = max(1, self.w // 240)
        for y in range(0, self.h, sy):
            row = self.rows[y]
            for x in range(0, self.w, sx):
                sample[row[x]] += 1
        self.bg = sample.most_common(1)[0][0] if sample else (0, 0, 0)
        self.bg_lum = _lum(self.bg)

        # Content = "visibly different from the background *here*".
        #
        # Comparing every pixel to one global modal colour is not enough: this
        # app's page is a subtle gradient, so the modal colour matches only a
        # thin slice of the screen and the other 95% scores as content. Take the
        # dominant colour of each small cell instead and compare within it - a
        # gradient then cancels out, because every cell carries its own
        # background, and only genuine foreground marks survive.
        # Cells must be much larger than the marks they are measuring, or a
        # solid element becomes the background of its own cell and vanishes.
        cw = max(64, self.w // 4)
        chh = max(48, self.h // 4)
        bgmap = []
        for cy in range(0, self.h, chh):
            rowbg = []
            for cx in range(0, self.w, cw):
                tally = Counter()
                for y in range(cy, min(cy + chh, self.h), 2):
                    r = self.rows[y]
                    for x in range(cx, min(cx + cw, self.w), 2):
                        tally[r[x]] += 1
                rowbg.append(tally.most_common(1)[0][0] if tally else self.bg)
            bgmap.append(rowbg)

        tol = 0.05
        self.content = [[False] * self.w for _ in range(self.h)]
        for y in range(self.h):
            bgcell = bgmap[min(y // chh, len(bgmap) - 1)]
            cr, lr, sr, raw = self.content[y], self.lum[y], self.sat[y], self.rows[y]
            for x in range(self.w):
                bgc = bgcell[min(x // cw, len(bgcell) - 1)]
                if (abs(lr[x] - _lum(bgc)) > tol
                        or abs(sr[x] - _sat(bgc)) > 0.35
                        or max(abs(raw[x][i] - bgc[i]) for i in range(3)) > 38):
                    cr[x] = True

    def ink(self, y):
        c = self.content[y]
        return sum(c) / self.w


def detect_chrome_top(field, tol=0.05, min_rows=8):
    """Rows of browser UI above the page, if the screenshot includes any.

    A screenshot of a browser window starts with tabs and an address bar in a
    different colour to the app. Counting them as page content produces a wall
    of false collisions, so find the boundary by looking for the first row whose
    dominant colour is the page's own.
    """
    first = None
    for y in range(min(field.h - 1, min_rows * 12)):
        row = Counter(field.rows[y][x] for x in range(field.w))
        if not row:
            continue
        dom, n = row.most_common(1)[0]
        if n / field.w >= 0.35 and abs(_lum(dom) - field.bg_lum) <= tol:
            first = y
            break
    return first or 0


def find_text_bands(field, min_density=0.008, max_density=1.0):
    """Rows that look like a line of text, grouped into bands.

    max_density is 1.0 on purpose. Capping it looked tidier but threw away the
    worst case: two lines of text drawn on top of each other fill the band
    completely, so a density ceiling silently discarded the exact thing being
    hunted for. Density is used to rank a band afterwards, not to exclude it.
    """
    bands, start, peak = [], None, 0.0
    for y in range(field.h):
        d = field.ink(y)
        if d >= min_density:
            if start is None:
                start, peak = y, d
            else:
                peak = max(peak, d)
        else:
            if start is not None:
                if y - start >= 3 and peak <= max_density:
                    bands.append((start, y - 1))
                start, peak = None, 0.0
    if start is not None and field.h - start >= 3:
        bands.append((start, field.h - 1))
    return bands


def band_stats(field, y0, y1):
    """Ink ratio and background-hole count for one text band."""
    ink = total = 0
    holes = 0
    for y in range(y0, y1 + 1):
        row = field.content[y]
        run_bg = False
        for x in range(field.w):
            total += 1
            if row[x]:
                ink += 1
                run_bg = False
            elif not run_bg:
                holes += 1
                run_bg = True
    return (ink / total if total else 0.0), holes


def edge_clipping(field, band=8, density=0.60, top_skip=0):
    """Content pressed against the viewport edge means it is being cut off.

    The band is 8px wide and the bar is high on purpose. A 3px band at 22% fired
    on every single screenshot, because Streamlit's own furniture - the scrollbar
    and the "Manage app" button - lives in the outermost few pixels. A finding
    that appears on every page is noise, not a defect, and it buries the pages
    that genuinely overflow.
    """
    findings = []
    ys = range(top_skip, field.h)
    sides = {
        "left":   [(x, y) for y in ys for x in range(band)],
        "right":  [(field.w - 1 - x, y) for y in ys for x in range(band)],
        "top":    [(x, y) for y in range(band) for x in range(field.w)],
        "bottom": [(x, field.h - 1 - y) for y in range(band) for x in range(field.w)],
    }
    for side, cells in sides.items():
        n = len(cells)
        hits = sum(1 for (x, y) in cells if field.content[y][x])
        d = hits / n if n else 0.0
        if d >= density:
            findings.append((side, d))
    return findings


def opaque_blocks(field, win=34, density=0.72, max_lum=0.30):
    """Dense, dark patches: content piled on top of content."""
    out, step = [], max(6, win // 3)
    for y in range(0, field.h - win, step):
        for x in range(0, field.w - win, step):
            ink = tot = 0
            lum = 0.0
            for yy in range(y, y + win):
                row, lr = field.content[yy], field.lum[yy]
                for xx in range(x, x + win):
                    tot += 1
                    if row[xx]:
                        ink += 1
                    lum += lr[xx]
            if tot and ink / tot >= density and (lum / tot) <= max_lum:
                out.append((x, y, win, win, ink / tot))
    # merge overlapping detections
    merged = []
    for bx, by, bw, bh, d in out:
        for m in merged:
            if abs(m[0] - bx) < win and abs(m[1] - by) < win:
                m[4] = max(m[4], d)
                break
        else:
            merged.append([bx, by, bw, bh, d])
    return merged


def low_contrast_text(field, bands, delta=0.16):
    """Text ink that is almost the same brightness as what is behind it."""
    out = []
    for y0, y1 in bands:
        inks = []
        for y in range(y0, y1 + 1):
            for x in range(field.w):
                if field.content[y][x]:
                    inks.append(field.lum[y][x])
        if len(inks) < 40:
            continue
        inks.sort()
        med = inks[len(inks) // 2]
        contrast = abs(med - field.bg_lum)
        if delta <= contrast < 0.16:
            out.append((0, y0, field.w, y1 - y0 + 1, contrast))
    return out


def coloured_glyphs(field, bands, sat_min=0.45, val_min=0.30):
    """Saturated blobs sitting inside text lines - what an emoji looks like."""
    out = []
    for y0, y1 in bands:
        run = None
        for y in range(y0, y1 + 1):
            for x in range(field.w):
                if field.sat[y][x] > sat_min and field.lum[y][x] > val_min:
                    run = run or [x, x, y, y]
                    run[0] = min(run[0], x)
                    run[1] = max(run[1], x)
                    run[2] = min(run[2], y)
                    run[3] = max(run[3], y)
                elif run and x - run[1] > 12:
                    if run[1] - run[0] >= 4:
                        out.append(tuple(run))
                    run = None
        if run and run[1] - run[0] >= 4:
            out.append(tuple(run))
    return out


SEV_ORDER = {"none": 0, "low": 1, "medium": 2, "high": 3}


def analyse(path, max_width=960):
    img, scale = load(path, max_width)
    f = Field(img)
    findings = []

    # browser tabs and the address bar are not app content
    chrome = detect_chrome_top(f)
    if chrome:
        for y in range(chrome):
            f.content[y] = [False] * f.w

    for side, d in edge_clipping(f, top_skip=chrome):
        if d < 0.60:
            continue
        findings.append({
            "kind": "viewport_clip",
            "severity": "high" if d > 0.85 else "medium",
            "confidence": "high",
            "location": {"side": side},
            "detail": f"{d:.0%} of the {side} edge is content, so something is cut off there",
            "likely_cause": "an element wider or taller than its container; the container "
                            "needs overflow handling or the element needs to shrink",
        })

    bands = find_text_bands(f)
    collisions = []
    # A text line is short. A tall, solid region is a panel or a chart, and
    # opaque_blocks() reports those instead.
    line_h = max(56, int(f.h * 0.08))
    for y0, y1 in bands:
        ink, holes = band_stats(f, y0, y1)
        if ink > 0.44 and (y1 - y0 + 1) <= line_h:
            collisions.append((ink, holes, y0, y1))
    collisions.sort(reverse=True)

    for ink, holes, y0, y1 in collisions[:12]:
        sev = "high" if ink > 0.72 else ("medium" if ink > 0.58 else "low")
        findings.append({
            "kind": "glyph_collision",
            "severity": sev,
            "confidence": "low",
            "location": {"x": 0, "y": y0, "w": f.w, "h": y1 - y0 + 1},
            "detail": f"band y={y0}-{y1} is {ink:.0%} ink with only {holes} background "
                      f"gaps; readable body text sits around 15-30%",
            "likely_cause": "candidate: marks filled in by something drawn over them, or "
                            "two elements sharing the same rows. Pixels cannot separate "
                            "these - confirm with tools/overlap_probe.js on the live DOM",
        })

    if bands:
        tall = [(a, b) for a, b in bands if b - a > f.h * 0.16]
        for y0, y1 in tall[:6]:
            findings.append({
                "kind": "band_too_tall",
                "severity": "low",
                "confidence": "low",
                "location": {"x": 0, "y": y0, "w": f.w, "h": y1 - y0 + 1},
                "detail": f"continuous text-like region spans {y1 - y0 + 1}px",
                "likely_cause": "several stacked elements with no gap, or a chart and a "
                                "table sharing vertical space",
            })

    for x, y, w, h, d in opaque_blocks(f)[:4]:
        findings.append({
            "kind": "dense_region",
            "severity": "low",
            "confidence": "low",
            "location": {"x": x, "y": y, "w": w, "h": h},
            "detail": f"{d:.0%} ink in a {w}x{h} dark region; may be a deliberate chart "
                      f"or panel rather than an obstruction",
            "likely_cause": "one element painted over another; check fixed heights and "
                            "column widths",
        })

    for x, y, w, h, d in low_contrast_text(f, bands)[:6]:
        findings.append({
            "kind": "low_contrast_text",
            "severity": "medium",
            "confidence": "medium",
            "location": {"x": x, "y": y, "w": w, "h": h},
            "detail": f"text brightness within {d:.2f} of its background",
            "likely_cause": "a text colour chosen for a different background",
        })

    emoji = coloured_glyphs(f, bands)
    header_h = max(24, int(f.h * 0.045))
    in_text = [e for e in emoji if not (e[2] < header_h)]
    in_header = [e for e in emoji if e[2] < header_h]
    findings.append({
        "kind": "emoji_presence",
        "severity": "none" if in_text else "low",
        "confidence": "high",
        "location": {"count": len(in_text)},
        "detail": (f"{len(in_text)} coloured glyph cluster(s) inside text lines"
                   if in_text else
                   "no coloured glyph clusters found in text lines - emoji may not be "
                   "rendering, or the palette in use is monochrome"),
        "likely_cause": "" if in_text else "check that labels are not ASCII-folded "
                                           "(physics/engine.py _label)",
    })
    if in_header:
        findings.append({
            "kind": "header_collision",
            "severity": "low",
            "confidence": "medium",
            "location": {"x": 0, "y": 0, "w": f.w, "h": header_h},
            "detail": f"{len(in_header)} coloured cluster(s) in the top {header_h}px",
            "likely_cause": "content scrolling under the Streamlit header",
        })

    # scale coordinates back to the original image
    for item in findings:
        loc = item.get("location", {})
        for k in ("x", "y", "w", "h"):
            if k in loc:
                loc[k] = int(loc[k] * scale)

    frac = sum(1 for y in range(f.h) for x in range(f.w) if f.content[y][x])
    frac = frac / float(f.w * f.h) if f.w and f.h else 0.0
    return {
        "file": path.name,
        "path": str(path),
        "diagnostics": {
            "background_rgb": list(f.bg),
            "background_lum": round(f.bg_lum, 3),
            "content_fraction": round(frac, 3),
            "chrome_rows_skipped": chrome,
            "analysis_size": [img.w, img.h],
            "scale": scale,
            "decoder": "pillow" if HAVE_PIL else "stdlib png",
        },
        "size": {"w": img.w * int(scale) if scale >= 1 else img.w,
                 "h": img.h * int(scale) if scale >= 1 else img.h},
        "analysed_at": {"w": img.w, "h": img.h},
        "device_guess": ("desktop/laptop" if img.w * scale >= 1200 else
                         "tablet" if img.w * scale >= 700 else "phone"),
        "text_bands": len(bands),
        "coloured_glyph_clusters": len(emoji),
        "worst_ink_band": round(collisions[0][0], 3) if collisions else 0.0,
        "findings": findings,
        "summary": summarise(findings),
    }


def summarise(findings):
    by_sev = Counter(f["severity"] for f in findings if f["kind"] != "emoji_presence")
    worst = "none"
    for f in findings:
        if SEV_ORDER.get(f["severity"], 0) > SEV_ORDER[worst]:
            worst = f["severity"]
    kinds = sorted({f["kind"] for f in findings
                    if f["kind"] != "emoji_presence" and f["severity"] != "none"})
    return {
        "worst_severity": worst,
        "high": by_sev.get("high", 0),
        "medium": by_sev.get("medium", 0),
        "low": by_sev.get("low", 0),
        "kinds": kinds,
    }


# ---------------------------------------------------------------------------
# reporting
# ---------------------------------------------------------------------------

LIMITATIONS = """
## What this report can and cannot tell you

Detected from pixels with reasonable confidence: content clipped by the
viewport edge, text too close in brightness to its background, whether emoji
glyphs rendered at all, and how many text bands a page has.

Suggested but NOT proven: `glyph_collision` (a text band filled too densely for
readable text) and `dense_region` (an area too solid to read through). A
diagrammatic chart looks exactly like an obstruction in a screenshot. These are
candidates for a human to look at, not verdicts.

Not detectable from a screenshot at all: what the marks actually are, or whether
one element is genuinely drawn over another. Two lines of text overlapping by a
few pixels and a perfectly solid panel differ in ways a screenshot does not
record. For overlap you need the live DOM - paste tools/overlap_probe.js into the
browser console. That names the elements exactly; this report only says where to
look.
"""


def write_report(results, outdir, meta):
    outdir = pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "report.json").write_text(json.dumps(
        {"generated_by": meta, "images": results}, indent=2))

    lines = ["# Screenshot audit", "", LIMITATIONS.strip(), ""]
    lines += [f"- images analysed: **{len(results)}**",
              f"- decoder: **{meta['decoder']}**", ""]

    agg = Counter()
    for r in results:
        agg[r["summary"]["worst_severity"]] += 1
        for k in r["summary"]["kinds"]:
            agg["kind:" + k] += 1
    worst_all = max((r["summary"]["worst_severity"] for r in results),
                    key=lambda s_: SEV_ORDER.get(s_, 0), default="none")
    lines += ["## Totals", "",
              f"- worst severity across all images: **{worst_all}**",
              f"- high: {agg.get('high', 0)} images · "
              f"medium: {agg.get('medium', 0)} · low: {agg.get('low', 0)}", ""]
    kinds = {k[5:]: v for k, v in agg.items() if k.startswith("kind:")}
    if kinds:
        lines += ["| finding | images affected |", "|---|---|"]
        for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]):
            lines.append(f"| `{k}` | {v} |")
        lines.append("")

    lines += ["## Per image", ""]
    for r in results:
        s = r["summary"]
        lines += [f"### `{r['file']}`", "",
                  f"- size: {r['size']['w']}x{r['size']['h']} "
                  f"({r['device_guess']})",
                  f"- text bands: {r['text_bands']}, "
                  f"worst ink band: {r['worst_ink_band']:.2f}, "
                  f"coloured glyph clusters: {r['coloured_glyph_clusters']}",
                  f"- worst severity: **{s['worst_severity']}**", ""]
        rows = [f for f in r["findings"] if f["severity"] != "none"]
        if not rows:
            lines += ["No layout defect detected.", ""]
            continue
        lines += ["| severity | finding | where | detail | likely cause |",
                  "|---|---|---|---|---|"]
        for f in sorted(rows, key=lambda x: -SEV_ORDER[x["severity"]]):
            loc = f.get("location", {})
            where = ", ".join(f"{k}={v}" for k, v in loc.items() if k != "count") \
                or (f"count={loc['count']}" if "count" in loc else "-")
            detail = f["detail"].replace("|", "/")
            cause = (f.get("likely_cause") or "").replace("|", "/")
            lines.append(f"| {f['severity']} | `{f['kind']}` | {where} | "
                         f"{detail} | {cause} |")
        lines.append("")

    (outdir / "report.md").write_text("\n".join(lines))
    return outdir / "report.md", outdir / "report.json"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="a PNG file or a folder of PNGs")
    ap.add_argument("-o", "--outdir", default="screenshots_report")
    ap.add_argument("--max", type=int, default=0, help="limit how many images")
    ap.add_argument("--min-severity", default="low",
                    choices=["low", "medium", "high"],
                    help="only report images at or above this severity")
    ap.add_argument("--width", type=int, default=960, help="analysis width")
    args = ap.parse_args()

    target = pathlib.Path(args.target)
    if target.is_dir():
        files = sorted(target.glob("*.png")) + sorted(target.glob("*.jpg"))
    else:
        files = [target]
    if not files:
        sys.exit(f"no images found in {target}")
    if args.max:
        files = files[:args.max]

    results = []
    for i, p in enumerate(files, 1):
        try:
            results.append(analyse(p, args.width))
        except Exception as exc:
            results.append({"file": p.name, "path": str(p),
                            "findings": [{"kind": "analysis_failed", "severity": "low",
                                          "confidence": "high", "location": {},
                                          "detail": f"{type(exc).__name__}: {exc}",
                                          "likely_cause": "unsupported image format"}],
                            "summary": summarise([]), "text_bands": 0,
                            "coloured_glyph_clusters": 0, "worst_ink_band": 0.0,
                            "device_guess": "unknown",
                            "size": {"w": 0, "h": 0}, "analysed_at": {"w": 0, "h": 0}})
        print(f"  [{i}/{len(files)}] {p.name}")

    # The floor trims which findings get listed. Clean images stay in the report:
    # "this one is fine" is a result too, and dropping it hides how much was
    # actually checked.
    floor = SEV_ORDER[args.min_severity]
    for r in results:
        kept = [f for f in r["findings"]
                if f["kind"] == "emoji_presence"
                or SEV_ORDER.get(f["severity"], 0) >= floor]
        r["findings"] = kept
        r["summary"] = summarise(kept)
        r["summary"]["suppressed"] = len(r["findings_original"]) - len(kept) \
            if "findings_original" in r else 0

    md, js = write_report(results, args.outdir,
                          {"decoder": "pillow" if HAVE_PIL else "stdlib png",
                           "width": args.width, "min_severity": args.min_severity})
    worst = Counter(r["summary"]["worst_severity"] for r in results)
    flagged = sum(1 for r in results
                  if SEV_ORDER.get(r["summary"]["worst_severity"], 0) >= floor)
    print(f"\nanalysed {len(results)} image(s); {flagged} with findings at or above "
          f"{args.min_severity}, {len(results) - flagged} clean")
    print("worst severities:", dict(worst) or "none")
    print(f"wrote {md}\nwrote {js}")


if __name__ == "__main__":
    main()