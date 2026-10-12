/*
 * overlap_probe.js - find genuinely overlapping elements in the live DOM.
 *
 * How to use:
 *   1. Open the station that shows the overlap.
 *   2. Open devtools (F12) -> Console.
 *   3. Paste this whole file and press Enter.
 *   4. Read the console table, then copy the JSON that ends the output:
 *        copy(JSON.stringify(window.__overlaps))
 *      Save it as overlap.json next to the app.
 *
 * It deliberately reports only *real* overlap: ancestor/child pairs are
 * skipped (a button inside its panel is not a collision), near-adjacent
 * edges are skipped (shared borders are normal), and invisible or empty
 * elements are skipped. What remains is a box that visibly sits on top of
 * another, which is what "overlapping other elements" means on screen.
 *
 * Run it again after interacting (dragging a slider, opening a tab) to see
 * overlap that only appears once the layout settles.
 */
(function overlapProbe() {
  const MIN_OVERLAP_PX = 8;      // ignore hairline touches
  const MIN_AREA_RATIO = 0.02;   // ignore slivers of incidental intersection

  const SKIP_TAGS = new Set([
    "SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE", "HEAD", "META", "LINK", "TITLE", "BR"
  ]);

  function isVisible(el) {
    if (!(el instanceof Element)) return false;
    if (SKIP_TAGS.has(el.tagName)) return false;
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden") return false;
    if (parseFloat(cs.opacity || "1") < 0.05) return false;
    const r = el.getBoundingClientRect();
    return r.width > 2 && r.height > 2;
  }

  // A short, human-meaningful handle for the element.
  function describe(el) {
    const testid = el.getAttribute("data-testid");
    let role = "";
    if (el.tagName === "INPUT") role = el.type ? `input[${el.type}]` : "input";
    else if (el.tagName === "TEXTAREA") role = "textarea";
    else if (el.tagName === "SELECT") role = "select";
    else if (el.tagName === "BUTTON") role = "button";
    else if (el.tagName === "IMG") role = "img";
    else if (el.tagName === "SVG") role = "svg";
    else if (testid) role = testid;
    else role = el.tagName.toLowerCase();

    const label = (el.getAttribute("aria-label") ||
                   (el.labels && el.labels[0] && el.labels[0].innerText) ||
                   (el.textContent || "")).trim().replace(/\s+/g, " ");
    return { role, label: label.slice(0, 60), testid: testid || null };
  }

  function area(r) { return Math.max(0, r.width) * Math.max(0, r.height); }

  function intersection(a, b) {
    const x = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
    const y = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
    return { w: x, h: y, px: x * y };
  }

  // Leaves the DOM but keeps every visible box with a readable description.
  const boxes = [];
  document.querySelectorAll("*").forEach((el) => {
    if (!isVisible(el)) return;
    const r = el.getBoundingClientRect();
    boxes.push({ el, rect: r, area: area(r), info: describe(el) });
  });

  const results = [];
  for (let i = 0; i < boxes.length; i++) {
    for (let j = i + 1; j < boxes.length; j++) {
      const A = boxes[i], B = boxes[j];

      // Containment is not overlap: a control inside its own panel is fine.
      if (A.el.contains(B.el) || B.el.contains(A.el)) continue;

      // Identical boxes are stacked duplicates (e.g. a ghost overlay) - flag hard.
      const sameBox =
        Math.abs(A.rect.left - B.rect.left) < 1 &&
        Math.abs(A.rect.top - B.rect.top) < 1 &&
        Math.abs(A.rect.width - B.rect.width) < 1 &&
        Math.abs(A.rect.height - B.rect.height) < 1;

      const ix = intersection(A.rect, B.rect);
      if (!sameBox) {
        if (ix.w < MIN_OVERLAP_PX || ix.h < MIN_OVERLAP_PX) continue;
        const smaller = Math.min(A.area, B.area) || 1;
        if (ix.px / smaller < MIN_AREA_RATIO) continue;
      }

      const severity = sameBox ? 1.0 : ix.px / Math.max(1, Math.min(A.area, B.area));
      results.push({
        severity: Number(severity.toFixed(3)),
        stacked: sameBox,
        overlapPx: Math.round(ix.px),
        a: A.info,
        b: B.info,
        aRect: A.rect.toJSON(),
        bRect: B.rect.toJSON()
      });
    }
  }

  results.sort((x, y) => y.severity - x.severity);

  console.log(
    `%c[overlap] ${results.length} overlapping pair(s) among ${boxes.length} visible elements`,
    "color:#0f0;font-weight:bold"
  );
  if (results.length) {
    console.table(results.map((r) => ({
      severity: r.severity,
      stacked: r.stacked,
      px: r.overlapPx,
      a: `${r.a.role} "${r.a.label}"`,
      b: `${r.b.role} "${r.b.label}"`
    })));
  } else {
    console.log("[overlap] none found on this screen.");
  }
  window.__overlaps = results;
  console.log(
    "[overlap] to save: copy(JSON.stringify(window.__overlaps))  ->  overlap.json"
  );
  return results;
})();