# Screenshot audit

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

- images analysed: **12**
- decoder: **stdlib png**

## Totals

- worst severity across all images: **medium**
- high: 0 images · medium: 1 · low: 11

| finding | images affected |
|---|---|
| `band_too_tall` | 12 |
| `dense_region` | 12 |
| `glyph_collision` | 2 |
| `header_collision` | 1 |
| `viewport_clip` | 1 |

## Per image

### `Screenshot_20261012_143340.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 6, worst ink band: 0.00, coloured glyph clusters: 248
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=44, w=1920, h=226 | continuous text-like region spans 113px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `band_too_tall` | x=0, y=338, w=1920, h=388 | continuous text-like region spans 194px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=396, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=484, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=572, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=660, y=44, w=68, h=68 | 93% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143356.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 8, worst ink band: 0.45, coloured glyph clusters: 114
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `glyph_collision` | x=0, y=862, w=1920, h=102 | band y=431-481 is 45% ink with only 369 background gaps; readable body text sits around 15-30% | candidate: marks filled in by something drawn over them, or two elements sharing the same rows. Pixels cannot separate these - confirm with tools/overlap_probe.js on the live DOM |
| low | `band_too_tall` | x=0, y=44, w=1920, h=226 | continuous text-like region spans 113px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=396, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1452, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1540, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1628, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143435.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 13, worst ink band: 0.00, coloured glyph clusters: 76
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=44, w=1920, h=256 | continuous text-like region spans 128px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `band_too_tall` | x=0, y=678, w=1920, h=304 | continuous text-like region spans 152px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=396, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1452, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1540, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1628, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143441.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 13, worst ink band: 0.00, coloured glyph clusters: 58
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=44, w=1920, h=450 | continuous text-like region spans 225px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=396, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1452, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1540, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1628, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143453.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 14, worst ink band: 0.00, coloured glyph clusters: 74
- worst severity: **medium**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| medium | `viewport_clip` | side=top | 70% of the top edge is content, so something is cut off there | an element wider or taller than its container; the container needs overflow handling or the element needs to shrink |
| low | `band_too_tall` | x=0, y=0, w=1920, h=272 | continuous text-like region spans 136px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `band_too_tall` | x=0, y=360, w=1920, h=180 | continuous text-like region spans 90px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=440, y=0, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=528, y=0, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=616, y=0, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=704, y=0, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `header_collision` | x=0, y=0, w=1920, h=48 | 3 coloured cluster(s) in the top 24px | content scrolling under the Streamlit header |

### `Screenshot_20261012_143502.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 11, worst ink band: 0.00, coloured glyph clusters: 38
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=44, w=1920, h=254 | continuous text-like region spans 127px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `band_too_tall` | x=0, y=310, w=1920, h=286 | continuous text-like region spans 143px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=396, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1452, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1540, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1628, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143627.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 13, worst ink band: 0.00, coloured glyph clusters: 85
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=44, w=1920, h=226 | continuous text-like region spans 113px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `band_too_tall` | x=0, y=576, w=1920, h=274 | continuous text-like region spans 137px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=396, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1452, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1540, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1628, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143643.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 22, worst ink band: 0.00, coloured glyph clusters: 66
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=84, w=1920, h=186 | continuous text-like region spans 93px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=0, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=88, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=176, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=264, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143650.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 12, worst ink band: 0.00, coloured glyph clusters: 40
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=480, w=1920, h=302 | continuous text-like region spans 151px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=0, y=110, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=88, y=110, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=176, y=110, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=264, y=110, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143701.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 14, worst ink band: 0.00, coloured glyph clusters: 247
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=84, w=1920, h=186 | continuous text-like region spans 93px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=0, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=88, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=176, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=264, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143718.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 25, worst ink band: 0.00, coloured glyph clusters: 70
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `band_too_tall` | x=0, y=84, w=1920, h=186 | continuous text-like region spans 93px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=0, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=88, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=176, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=264, y=66, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |

### `Screenshot_20261012_143731.png`

- size: 1920x1080 (desktop/laptop)
- text bands: 13, worst ink band: 0.56, coloured glyph clusters: 80
- worst severity: **low**

| severity | finding | where | detail | likely cause |
|---|---|---|---|---|
| low | `glyph_collision` | x=0, y=924, w=1920, h=56 | band y=462-489 is 56% ink with only 56 background gaps; readable body text sits around 15-30% | candidate: marks filled in by something drawn over them, or two elements sharing the same rows. Pixels cannot separate these - confirm with tools/overlap_probe.js on the live DOM |
| low | `band_too_tall` | x=0, y=44, w=1920, h=260 | continuous text-like region spans 130px | several stacked elements with no gap, or a chart and a table sharing vertical space |
| low | `dense_region` | x=396, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1452, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1540, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
| low | `dense_region` | x=1628, y=44, w=68, h=68 | 100% ink in a 34x34 dark region; may be a deliberate chart or panel rather than an obstruction | one element painted over another; check fixed heights and column widths |
