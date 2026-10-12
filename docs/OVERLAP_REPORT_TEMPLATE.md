# Overlap report template

Copy this block, fill it in, send it back. Three things matter most: **which
station**, **what overlaps what**, and **the device**. A screenshot is the
single most useful extra — but please also say what it *shows*, because a
picture of the problem is easier to act on than a picture of the screen.

```
Chapter:            (e.g. 7)
Station:            (the tab name, e.g. "Graphs from expressions")
What overlaps what: (e.g. "the amplitude slider sits on top of the graph")
Device:             (laptop / tablet / phone)
Browser:            (Chrome / Firefox / Edge / Safari)
Window size:        (full screen, or roughly how wide - this matters, see note)
Zoom level:         (100%? or browser-zoomed?)
When it happens:    (on first load / after dragging a slider / after opening a tab)
Also seen on:       (list other stations with the same problem, if any)
```

## Getting the precise answer (optional, best)

If you can, open the station that overlaps, press **F12** -> **Console**, and
paste the contents of `tools/overlap_probe.js`. It prints a table in the
console. Then in the same console type:

```js
copy(JSON.stringify(window.__overlaps))
```

Save the clipboard as `overlap.json` and send it. That file names the exact
overlapping widgets, so nobody has to guess which two things are colliding.

To turn it into a summary on your machine:

```bash
python tools/overlap_report.py overlap.json
```

## Why the details matter

Two overlaps that look the same on screen often have different causes: one is
a fixed height clipping a widget, another is two wide elements sharing a row,
another is a label wrapping into its neighbour. The chapter, station, device,
and "when it happens" are what separate those quickly. Overlap that only shows
up *after* a slider moves, for example, points somewhere different from overlap
that is there the moment the page loads.