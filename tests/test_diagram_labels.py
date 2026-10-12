"""Label collisions in the physics diagrams.

Screenshot audits kept finding axis titles printed across the curves they named,
value labels poking inside the plot area, and annotation stacks piled on one
line. These tests catch all three by measuring the rendered SVG rather than by
reading it: a label collides when a plotted sample point falls inside the
label's own box.

`text_extent` estimates width from the average glyph width, so these are
approximate. They are tuned to catch clear collisions, not to be a typesetter.
"""
import math
import pathlib
import re
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "tools"))
import inspect_screenshots as stub  # noqa: F401  - installs the streamlit stub

from physics.visuals.common import overlaps, text_extent  # noqa: E402
from physics.visuals import ch04, ch07, ch10  # noqa: E402


def labels_of(svg):
    """Every rendered <text> as (box, content), honouring text-anchor."""
    out = []
    for match in re.finditer(r"<text\b([^>]*)>([^<]*)</text>", svg):
        attrs, content = match.groups()
        x = re.search(r'\bx="([\d.-]+)"', attrs)
        y = re.search(r'\by="([\d.-]+)"', attrs)
        size = re.search(r'font-size="([\d.]+)"', attrs)
        anchor = re.search(r'text-anchor="(\w+)"', attrs)
        if not (x and y and size):
            continue
        out.append((text_extent(float(x.group(1)), float(y.group(1)), content,
                                size=float(size.group(1)),
                                anchor=anchor.group(1) if anchor else "start"),
                    content))
    return out


def curve_points(svg):
    points = []
    for poly in re.findall(r'<polyline points="([^"]+)"', svg):
        for pair in poly.split():
            px, py = pair.split(",")
            points.append((float(px), float(py)))
    return points


def labels_hitting_curves(svg):
    pts = curve_points(svg)
    return [content for box, content in labels_of(svg)
            if any(box["x"] <= px <= box["x"] + box["w"]
                   and box["y"] <= py <= box["y"] + box["h"] for px, py in pts)]


def test_shm_scope_labels_do_not_cross_the_curves():
    """F-007 / "error 3.png": axis titles printed across the plotted lines.

    The bold axis title sat at x=24 and ran about 110px, which is past the plot
    edge at x=70, so it crossed the curve it was naming. The peak value label
    was anchored at x=44 and reached x=74, four pixels inside the plot.
    """
    for amplitude, period, phase in [(0.20, 1.0, 0.0), (0.50, 2.0, 0.9),
                                     (0.05, 0.5, 2.0), (1.00, 3.0, 1.4),
                                     (0.35, 0.8, 0.3), (2.00, 0.4, 0.0)]:
        svg = ch07.shm_scope(amplitude, 2 * math.pi / period, 1.5, phase)
        hits = labels_hitting_curves(svg)
        assert not hits, (
            f"A={amplitude} T={period}: labels drawn over a curve: {hits}")


def test_shm_scope_draws_all_three_traces_inside_the_canvas():
    """The acceleration graph rendered empty.

    Three panels of 118px needed 492px, but the canvas was 460px: the third was
    clipped and the two caption lines were painted straight across it.
    """
    height = int(re.search(r'viewBox="[^"]*?\s(\d+)"',
                           ch07.shm_scope(0.2, 6.0, 1.5, 0.0)).group(1))
    for amplitude, period in [(0.20, 1.0), (0.50, 2.0), (1.0, 3.0)]:
        svg = ch07.shm_scope(amplitude, 2 * math.pi / period, 1.5, 0.0)
        traces = re.findall(r'<polyline points="([^"]+)"', svg)
        assert len(traces) == 3, f"expected three traces, got {len(traces)}"
        for trace in traces:
            assert len(trace.split()) > 50, "a trace was degenerate"
            for pair in trace.split():
                assert float(pair.split(",")[1]) <= height, (
                    "a trace runs off the bottom of the canvas")


def test_maxwell_boltzmann_speed_labels_do_not_collide():
    """F-002: v_mp, v_mean and v_rms labels sat on top of each other."""
    for temperature, molar_mass in [(300.0, 0.028), (300.0, 0.044),
                                    (500.0, 0.002), (150.0, 0.071),
                                    (1000.0, 0.028), (1200.0, 0.216)]:
        svg = ch10.speed_distribution(temperature, molar_mass)
        marks = [(box, txt) for box, txt in labels_of(svg)
                 if "m s⁻¹" in txt or txt in ("most probable", "mean speed",
                                              "root-mean-square")]
        assert len(marks) == 6, f"expected 6 mark labels, got {len(marks)}"
        clashes = [(a[1], b[1]) for i, a in enumerate(marks)
                   for b in marks[i + 1:] if overlaps(a[0], b[0])]
        assert not clashes, f"T={temperature} M={molar_mass}: {clashes}"


def test_pv_process_labels_do_not_collide():
    """F-003: the four process labels overlapped each other on the curves."""
    svg = ch10.process_quadrant()
    names = {"isobaric  W = P dV", "isochoric  W = 0",
             "isothermal  Q = W", "adiabatic  Q = 0"}
    marks = [(box, txt) for box, txt in labels_of(svg) if txt in names]
    assert len(marks) == 4, f"expected 4 process labels, got {len(marks)}"
    clashes = [(a[1], b[1]) for i, a in enumerate(marks)
               for b in marks[i + 1:] if overlaps(a[0], b[0])]
    assert not clashes, f"process labels collide: {clashes}"


def test_rotation_disc_omega_label_does_not_cross_the_quantity_column():
    """F-004: the green omega value collided with the numbers beside it.

    Anchored right of the disc it started at x=406 for r=150 and ran past 500,
    straight into the quantity column that starts at x=450.
    """
    for radius in (60.0, 90.0, 120.0, 150.0, 170.0):
        svg = ch04.rotation_disc(radius, 4.0, 0.4)
        quantity_column = [box for box, txt in labels_of(svg)
                           if txt in ("r", "v = rω", "a_t = rα", "a_c = ω²r")]
        omega = [(box, txt) for box, txt in labels_of(svg) if txt.startswith("ω =")]
        assert len(omega) == 1, f"expected one omega label for r={radius}"
        assert not any(overlaps(omega[0][0], q) for q in quantity_column), (
            f"r={radius}: the omega label crosses the quantity column")

def test_progressive_wave_draws_every_frame_inside_its_panel():
    """"only t=0 shows the wave. Subsequent frames are empty."

    The panel centre line was computed as x0 + panel_w/2 - an x offset used as a
    y value. Panel 0 came out at 102 by luck; panels 1-3 drew at y=267, 432 and
    597 on a canvas 300 tall, so their waves were below the bottom edge and the
    frames read as blank.
    """
    from physics.visuals import ch08

    for amplitude in (0.05, 0.5, 2.0, 8.0):
        svg = ch08.progressive_trace(amplitude, 2.0, 4)
        traces = re.findall(r'<polyline points="([^"]+)"', svg)
        assert len(traces) == 4, f"expected 4 frames, got {len(traces)}"
        for index, trace in enumerate(traces):
            ys = [float(pair.split(",")[1]) for pair in trace.split()]
            assert 46 <= min(ys) and max(ys) <= 258, (
                f"amplitude={amplitude} frame {index} drew outside its panel "
                f"(y={min(ys):.0f}..{max(ys):.0f}, panel is 46..258)")


def _all_label_collisions(svg, pad=2.0):
    boxes = labels_of(svg)
    return [(a[1], b[1]) for i, a in enumerate(boxes)
            for b in boxes[i + 1:] if overlaps(a[0], b[0], pad)]


def test_energy_degradation_caption_clears_the_bar_labels():
    """"recovering any of it would need work..." ran into adjacent boxes.

    That closing sentence sat at y=218 while the bar captions were at y=216 and
    228, so it was drawn straight through them.
    """
    svg = ch10.degradation_scale()
    summary = [box for box, txt in labels_of(svg)
               if txt.startswith("recovering any of it")]
    captions = [box for box, txt in labels_of(svg)
                if txt in ("concentrated", "useful work", "low-grade heat",
                           "random motion")]
    assert len(summary) == 1, "the closing sentence is missing"
    for box in captions:
        assert not overlaps(summary[0], box, pad=0.0), (
            "the closing sentence overlaps a bar caption")


def test_gas_law_grid_labels_do_not_collide():
    """Isotherm labels piled up once the curves converged.

    Also fixed a subtitle line that ran from x=24 to x=612 straight through the
    "kPa" axis unit label, because the plot top sat too close under the header.
    """
    cases = [{}, {"temperatures": (150.0, 400.0)},
             {"volume": 0.0005, "pressure": 5.0e4},
             {"volume": 0.01, "pressure": 4.0e5},
             {"volume": 0.0002, "pressure": 2.0e5},
             {"temperatures": (100.0, 250.0, 600.0)}]
    for kwargs in cases:
        clashes = _all_label_collisions(ch10.gas_law_grid(**kwargs))
        assert not clashes, f"{kwargs}: {clashes}"


def test_declutter_handles_an_empty_list():
    """gas_law_grid can produce no in-range isotherm at all."""
    from physics.visuals.common import declutter
    assert declutter([]) == []


def _excursion(svg):
    ys = [float(pair.split(",")[1]) for poly in re.findall(r'<polyline points="([^"]+)"', svg)
          for pair in poly.split()]
    return max(ys) - min(ys)


@pytest.mark.parametrize("amplitude", [0.3, 0.6, 1.0, 2.0])
def test_wave_diagrams_are_not_flat(amplitude):
    """"wave diagram appears almost flat despite a nonzero amplitude".

    Amplitude is in metres and SVG coordinates are in pixels, so the number was
    being used directly: a 0.5 m wave was one pixel tall, which reads as a level
    line whatever the slider says. Both diagrams had it.
    """
    from physics.visuals import ch08

    assert _excursion(ch08.progressive_trace(amplitude, 2.0, 4)) > 25, (
        f"progressive_trace is flat at A={amplitude} m")
    assert _excursion(ch08.wave_graph_annotated(amplitude, 2.0)) > 25, (
        f"wave_graph_annotated is flat at A={amplitude} m")


def test_wave_scale_is_linear_up_to_the_cap():
    """Equal changes in amplitude must look equal, until the cap holds."""
    from physics.visuals.common import wave_scale
    assert wave_scale(0.2, room=1000, px_per_unit=70) == pytest.approx(70)
    assert wave_scale(0.4, room=1000, px_per_unit=70) == pytest.approx(70)
    assert wave_scale(1.0, room=1000, px_per_unit=70) == pytest.approx(70)
    assert wave_scale(100.0, room=100) < wave_scale(50.0, room=100)


def test_carnot_corner_numbers_do_not_collide():
    """Report: explanatory text over the heat-engine diagram.

    The two adiabats are near-vertical, so corners 2 and 4 sit close together
    and their state numbers overlapped by a few pixels.
    """
    for hot, cold in [(600.0, 300.0), (300.0, 600.0), (800.0, 100.0), (500.0, 400.0)]:
        svg = ch10.carnot_cycle_plot(hot, cold)
        corners = [box for box, txt in labels_of(svg) if txt in ("1", "2", "3", "4")]
        assert len(corners) == 4, f"expected 4 corner numbers, got {len(corners)}"
        clashes = [(a[1], b[1]) for i, a in enumerate(corners)
                   for b in corners[i + 1:] if overlaps(a[0], b[0])]
        assert not clashes, f"T={hot}/{cold}: corner numbers collide: {clashes}"


def test_progressive_trace_frame_numbers_are_centred_per_panel():
    """Regression guard.

    Fixing the empty frames changed `mid` from an x offset to a y value, and the
    "t = N" caption still used `mid` for its x. All four captions then stacked at
    x=150 until this was caught by a whole-diagram sweep.
    """
    from physics.visuals import ch08

    svg = ch08.progressive_trace(0.6, 2.0, 4)
    xs = sorted(box["x"] for box, txt in labels_of(svg) if txt.startswith("t ="))
    assert len(xs) == 4, f"expected 4 frame captions, got {len(xs)}"
    assert len(set(round(x) for x in xs)) == 4, (
        f"frame captions share a position: {xs}")
    assert xs[-1] - xs[0] > 300, f"frame captions are not spread across panels: {xs}"
