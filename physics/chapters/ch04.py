"""Chapter 4 interface: Motion in Two Dimensions.

The chapter owns two studios of its own: a **trajectory studio**, where launch
speed and angle sweep a whole family of paths at once so the 45-degree maximum
can be *seen* rather than looked up, and a **rotation bench**, where every
moment of inertia in the syllabus is spun on the same axle.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..visuals.common import freeze
from ..core import motion2d as M
from ..engine import (table, how_to, ChapterSpec, EXAM_TIP, HONEST_LIMIT, Station, TRY_IT,
                      WATCH_OUT, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, card, metric_row
from ..visuals import ch04 as VIS
from . import ch04_data as D

_N = 4
P = f"c{_N}_"


def _studio() -> None:
    """The trajectory studio."""
    st.caption("Move the controls and the whole family of paths redraws. The 45-degree "
               "curve is visibly the longest.")

    c1, c2, c3 = st.columns(3)
    with c1:
        u = st.number_input("launch speed u (m s⁻¹)", 5.0, 100.0, 30.0, 1.0, key=f"{P}su")
    with c2:
        theta = st.slider("launch angle θ (°)", 0.0, 90.0, 30.0, 1.0, key=f"{P}sth")
    with c3:
        g = st.number_input("g (m s⁻²)", 1.0, 30.0, 9.8, 0.1, key=f"{P}sg")

    shot = M.projectile(u, theta, g)
    metric_row([("Time of flight T", f"{shot['time_of_flight']:.3g} s"),
                ("Max height H", f"{shot['max_height']:.3g} m"),
                ("Range R", f"{shot['range']:.3g} m"),
                ("Longest possible R_max", f"{shot['max_range']:.3g} m"),
                ("This launch, as % of R_max",
                 f"{100 * shot['range'] / shot['max_range']:.0f} %")])

    sweep = st.slider("draw angles from ... to ...", 5, 85, (5, 85), key=f"{P}srange")
    angles = [a for a in range(sweep[0], sweep[1] + 1, max(1, (sweep[1] - sweep[0]) // 9))]
    st.markdown(VIS.trajectory_family(freeze([u]), freeze(angles), g), unsafe_allow_html=True)
    st.markdown(VIS.component_split(u, theta, g), unsafe_allow_html=True)

    table(pd.DataFrame([
        {"angle": f"{a}°", "T (s)": f"{M.projectile(u, a, g)['time_of_flight']:.3g}",
         "H (m)": f"{M.projectile(u, a, g)['max_height']:.3g}",
         "R (m)": f"{M.projectile(u, a, g)['range']:.3g}"}
        for a in angles
    ]), use_container_width=True, hide_index=True)
    guidance(EXAM_TIP, "Two angles, one distance",
             "Any pair of angles adding to 90° gives the same range, because R ∝ sin 2θ "
             "and sin 60° = sin 120°. The higher of the two stays in the air longer, which "
             "is useful for clearing a wall and useless for landing in a small space.")


def _projectile() -> None:
    st.subheader("4.1 · Projectile motion")
    card("Two motions in a trench coat",
         "<p>Horizontally there is no force, so the horizontal velocity never changes. "
         "Vertically, gravity takes over and the velocity changes steadily. Neither part "
         "notices the other.</p>", "THE IDEA")
    st.write(
        "A **projectile** is any body given an initial velocity and then left alone under "
        "gravity alone. It may be thrown upwards, sideways or downwards; the description is "
        "the same. What is *not* a projectile is a ball rolling down a ramp, because air "
        "resistance and, more importantly, a normal force are acting."
    )
    st.markdown(VIS.component_split(30.0, 35.0), unsafe_allow_html=True)
    table(pd.DataFrame([
        {"component": "horizontal", "velocity": "u cos θ", "acceleration": "0",
         "behaviour": "constant speed, no change at all"},
        {"component": "vertical", "velocity": "u sin θ − gt", "acceleration": "−g",
         "behaviour": "speeds up, slows, then speeds up again"},
    ]), use_container_width=True, hide_index=True)
    guidance(WATCH_OUT, "A satellite is not a projectile",
             "A satellite has a large sideways speed, but gravity is always pulling it "
             "towards the Earth's *centre*, not straight down — and it never reaches the "
             "ground. The flat-Earth projectile picture only works when the flight is short "
             "compared with the radius of the Earth.")


def _relations() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("4.1.2 & 4.1.3 · The four relations")
    st.latex(r"T = \frac{2u\sin\theta}{g}, \qquad H = \frac{u^2\sin^2\theta}{2g}, "
             r"\qquad R = \frac{u^2\sin 2\theta}{g}, \qquad R_{\max} = \frac{u^2}{g}")
    table(pd.DataFrame([
        {"symbol": r["symbol"], "name": r["name"], "formula": r["formula"],
         "where it comes from": r["from"], "what it depends on": r["depends_on"]}
        for r in D.PROJECTILE_RELATIONS
    ]), use_container_width=True, hide_index=True)
    st.markdown("**Deriving them, in order.**")
    for index, step in enumerate(D.PROJECTILE_DERIVATION, start=1):
        st.markdown(f"{index}. {step}")

    st.subheader("Solve them")
    c1, c2, c3 = st.columns(3)
    with c1:
        u = st.number_input("u (m s⁻¹)", 1.0, 200.0, 30.0, 1.0, key=f"{P}ru")
    with c2:
        theta = st.slider("θ (°)", 0.0, 90.0, 30.0, 1.0, key=f"{P}rth")
    with c3:
        g = st.number_input("g (m s⁻²)", 1.0, 30.0, 9.8, 0.1, key=f"{P}rg")
    result = M.projectile(u, theta, g)
    st.latex(rf"T = {result['time_of_flight']:.4g}\ \text{{s}}, \qquad "
             rf"H = {result['max_height']:.4g}\ \text{{m}}, \qquad "
             rf"R = {result['range']:.4g}\ \text{{m}}")
    st.latex(rf"R_{{\max}} = {result['max_range']:.4g}\ \text{{m, at }}\theta = 45^\circ")
    vx, vy = result["components"]
    table(pd.DataFrame([
        {"quantity": "horizontal component u cos θ", "value": f"{vx:.4g} m s⁻¹"},
        {"quantity": "vertical component u sin θ", "value": f"{vy:.4g} m s⁻¹"},
        {"quantity": "time to apex", "value": f"{result['time_to_peak']:.4g} s"},
        {"quantity": "time of flight", "value": f"{result['time_of_flight']:.4g} s"},
        {"quantity": "maximum height", "value": f"{result['max_height']:.4g} m"},
        {"quantity": "range", "value": f"{result['range']:.4g} m"},
        {"quantity": "maximum range", "value": f"{result['max_range']:.4g} m"},
        {"quantity": "check: uₓ × T", "value": f"{vx * result['time_of_flight']:.4g} m"},
    ]), use_container_width=True, hide_index=True)
    if abs(vx * result["time_of_flight"] - result["range"]) < 1e-6:
        st.success("The independent route R = uₓ × T agrees with sin 2θ exactly, which is "
                   "the consistency check on the derivation.")


def _drag() -> None:
    st.subheader("4.1.4 · Air resistance")
    card("Drag changes the picture, but not the rules",
         "<p>Air resistance always opposes the velocity, so it can only remove speed. "
         "Predicting the result exactly would need a differential equation, so what the "
         "syllabus asks for is the qualitative direction of each change — and that is "
         "genuinely answerable from first principles.</p>", "THE IDEA")
    table(pd.DataFrame([
        {"quantity": r["quantity"], "in a vacuum": r["without"],
         "in air": r["with"], "why": r["why"]} for r in D.AIR_RESISTANCE
    ]), use_container_width=True, hide_index=True)
    st.markdown(VIS.trajectory_family(freeze([30]), freeze([20, 30, 45, 60, 75])), unsafe_allow_html=True)
    st.caption("These are vacuum trajectories. With air resistance each one would land "
               "short, peak lower, and take longer to come down.")
    guidance(HONEST_LIMIT, "Why the path tilts",
             "Near the apex the vertical speed is nearly zero, so the total speed is small "
             "and drag is relatively strong there. It shortens the rise more than the fall, "
             "so the descending limb is steeper than the ascending one — the symmetry of the "
             "vacuum parabola is lost.")


def _angular() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("4.2 · Angular motion")
    st.latex(r"s = r\theta, \qquad v = r\omega, \qquad a_t = r\alpha")
    table(pd.DataFrame([
        {"quantity": q["quantity"], "linear": q["linear"], "angular": q["angular"],
         "relation": q["relation"], "note": q["note"]} for q in D.ANGULAR_QUANTITIES
    ]), use_container_width=True, hide_index=True)
    for item in D.ANGULAR_CONVERSION:
        with st.expander(item["topic"]):
            st.markdown(item["note"])

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        r = st.number_input("radius r (m)", 0.01, 10.0, 0.5, 0.05, key=f"{P}ar")
    with c2:
        theta_deg = st.slider("θ (°)", 0.0, 720.0, 90.0, 5.0, key=f"{P}ath")
    with c3:
        omega = st.number_input("ω (rad s⁻¹)", 0.0, 200.0, 4.0, 0.5, key=f"{P}aw")
    with c4:
        alpha = st.number_input("α (rad s⁻²)", 0.0, 100.0, 1.0, 0.5, key=f"{P}aa")
    theta = math.radians(theta_deg)
    lin = M.linear_from_angular(r, theta, omega, alpha)
    st.markdown(VIS.angular_dials(theta, omega, alpha), unsafe_allow_html=True)
    st.markdown(VIS.rotation_disc(r, omega, alpha), unsafe_allow_html=True)
    table(pd.DataFrame([
        {"quantity": "θ", "value": f"{theta:.4g} rad = {theta_deg:.4g}°"},
        {"quantity": "s = rθ", "value": f"{lin['s']:.4g} m"},
        {"quantity": "v = rω", "value": f"{lin['v']:.4g} m s⁻¹"},
        {"quantity": "a_t = rα", "value": f"{lin['a_t']:.4g} m s⁻²"},
        {"quantity": "a_c = ω²r", "value": f"{omega ** 2 * r:.4g} m s⁻²"},
        {"quantity": "total acceleration",
         "value": f"{math.hypot(lin['a_t'], omega ** 2 * r):.4g} m s⁻²"},
        {"quantity": "revolutions", "value": f"{math.degrees(theta) / 360:.4g}"},
    ]), use_container_width=True, hide_index=True)
    guidance(WATCH_OUT, "θ must be in radians for s = rθ to work",
             "90° is π/2 rad, not 90. Writing s = r × 90 overstates the arc by a factor of "
             "2π — about six times too big.")


def _centripetal() -> None:
    how_to("numbers"),
    st.subheader("4.3 · Centripetal force and acceleration")
    st.latex(r"a_c = \frac{v^2}{r}, \qquad F_c = \frac{mv^2}{r}")
    card("Uniform does not mean unaccelerated",
         "<p>In uniform circular motion the speed is constant, but the *direction* of the "
         "velocity turns every instant. Acceleration is the rate of change of velocity, and "
         "velocity is a vector, so changing only its direction is still an acceleration.</p>",
         "THE IDEA")
    st.markdown("**Deriving a = v²/r.**")
    for index, step in enumerate(D.CENTRIPETAL_DERIVATION, start=1):
        st.markdown(f"{index}. {step}")

    c1, c2, c3 = st.columns(3)
    with c1:
        v = st.number_input("speed v (m s⁻¹)", 0.1, 500.0, 10.0, 0.5, key=f"{P}cv")
    with c2:
        r = st.number_input("radius r (m)", 0.1, 1000.0, 5.0, 0.5, key=f"{P}cr")
    with c3:
        m = st.number_input("mass m (kg)", 0.1, 10000.0, 2.0, 0.5, key=f"{P}cm")
    st.markdown(VIS.centripetal_circle(v, r, m), unsafe_allow_html=True)
    a_c = M.centripetal_acceleration(v, r)
    table(pd.DataFrame([
        {"quantity": "a_c = v²/r", "value": f"{a_c:.4g} m s⁻²"},
        {"quantity": "F_c = mv²/r", "value": f"{M.centripetal_force(m, v, r):.4g} N"},
        {"quantity": "period T = 2πr/v", "value": f"{2 * math.pi * r / v:.4g} s"},
        {"quantity": "frequency", "value": f"{v / (2 * math.pi * r):.4g} Hz"},
        {"quantity": "work done by F_c", "value": "0 J — F is perpendicular to v"},
    ]), use_container_width=True, hide_index=True)
    guidance(TRY_IT, "Watch the satellite",
             "A satellite in circular orbit moves at about 7.8 km/s and needs no engine at "
             "all, because the centripetal force does no work. It keeps moving because it is "
             "falling — see the next station.")


def _centrifuge() -> None:
    how_to("sliders"),
    st.subheader("4.3.3 · The centrifuge")
    st.markdown("\n\n".join(f"**{index}. {p['point']}**\n{p['detail']}"
                            for index, p in enumerate(D.CENTRIFUGE_POINTS, start=1)))
    omega = st.slider("spin rate ω (rad s⁻¹)", 5.0, 200.0, 60.0, 5.0, key=f"{P}cfw")
    samples = [
        {"kind": "light", "ratio": 0.25, "density": 1000},
        {"kind": "medium", "ratio": 0.60, "density": 2400},
        {"kind": "dense", "ratio": 0.92, "density": 3700},
    ]
    st.markdown(VIS.centrifuge_tube(
        omega, 0.12, freeze([(f"ρ = {s['density']:g}", s) for s in samples])),
        unsafe_allow_html=True)
    table(pd.DataFrame([
        {"material": f"ρ = {s['density']:g} kg m⁻³",
         "settles at fraction of the radius": s["ratio"],
         "a = ω²r there (m s⁻²)": omega ** 2 * 0.12 * s["ratio"]}
        for s in samples
    ]), use_container_width=True, hide_index=True)
    table(pd.DataFrame([
        {"practical use": "separating blood components in a clinical lab",
         "why it works": "red cells, white cells and plasma have different densities"},
        {"practical use": "separating isotopes in a centrifuge",
         "why it works": "uranium isotopes differ by less than 1 % in mass, so the tube is "
                        "run for many hours at very high speed"},
        {"practical use": "measuring the size of fine particles",
         "why it works": "settling speed depends on size, so the position after a fixed "
                        "time gives the distribution"},
        {"practical use": "spinning down DNA",
         "why it works": "ethanol plus salt raises the effective density of the sample "
                        "enough for DNA to move outward"},
    ]), use_container_width=True, hide_index=True)
    guidance(HONEST_LIMIT, "Why the supernatant must be poured off carefully",
             "The sediment is packed hard against the outside wall at a very large multiple "
             "of gravity. Opening a spinning centrifuge is dangerous precisely because of the "
             "effect this station explains.")


def _orbit() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("4.3.4 & 4.3.5 · Orbit, weightlessness and artificial gravity")
    altitude = st.slider("altitude above the surface (km)", 100.0, 35786.0, 400.0, 100.0,
                         key=f"{P}alt")
    st.markdown(VIS.weightless_orbit(altitude), unsafe_allow_html=True)
    data = M.apparent_weight(70.0, altitude * 1000.0)
    table(pd.DataFrame([
        {"quantity": "g at that altitude", "value": f"{data['g']:.4g} m s⁻²"},
        {"quantity": "fraction of surface gravity", "value": f"{data['fraction_of_surface_weight']:.3f}"},
        {"quantity": "weight of a 70 kg astronaut", "value": f"{data['weight']:.4g} N"},
        {"quantity": "orbital speed there", "value": f"{data['orbital_speed']:.4g} m s⁻¹"},
    ]), use_container_width=True, hide_index=True)
    for fact in D.ORBIT_FACTS:
        st.markdown(f"**{fact['fact']}** — {fact['detail']}")

    st.subheader("Artificial gravity")
    radius = st.number_input("habitat radius (m)", 3.0, 500.0, 30.0, 1.0, key=f"{P}hR")
    target = st.number_input("gravity wanted at the rim (m s⁻²)", 0.1, 30.0, 9.8, 0.1,
                             key=f"{P}hA")
    omega = math.sqrt(target / radius)
    period = 2 * math.pi / omega
    st.latex(r"\omega = \sqrt{\frac{a}{R}} = \sqrt{%g / %g} = %g\ \text{rad s}^{-1}"
             % (target, radius, omega))
    st.latex(r"T = \frac{2\pi}{\omega} = %g\ \text{s}"
             "\quad (%g\ \text{rev per minute})" % (period, period / 60))
    if period / 60 > 2.0:
        st.warning("That rotation rate is above about 2 rev/min, where Coriolis effects make "
                   "walking and eating genuinely difficult. Real designs therefore use a larger "
                   "radius and a slower spin, not a small one and a fast one.")
    else:
        st.success("That rate is slow enough for crew to walk and work normally.")


def _inertia() -> None:
    how_to("numbers"),
    st.subheader("4.4 · Moment of inertia")
    st.latex(r"I = \sum m r^2 \qquad \text{unit: kg m}^2 \qquad \text{dimension: } [ML^2]")
    card("The rotational measure of 'how much stuff'",
         "<p>Mass measures how hard it is to accelerate a body in a straight line. Moment of "
         "inertia measures how hard it is to *turn* one — and unlike mass it depends on where "
         "you look from.</p>", "THE IDEA")
    for note in D.MOMENT_OF_INERTIA_NOTES:
        with st.expander(note["idea"]):
            st.markdown(note["detail"])

    st.markdown(VIS.inertia_shapes(freeze(M.MOI_SHAPES)), unsafe_allow_html=True)
    table(pd.DataFrame([
        {"shape": r["shape"], "axis": r["axis"],
         "I / (mR²)": f"{r['coefficient'][0]}/{r['coefficient'][1]}",
         "why": r["note"]} for r in M.MOI_SHAPES
    ]), use_container_width=True, hide_index=True)

    body = st.selectbox("shape", ["ring", "rod", "disc", "sphere", "shell", "semi"],
                        key=f"{P}ib")
    c1, c2, c3 = st.columns(3)
    with c1:
        m = st.number_input("mass m (kg)", 0.01, 1000.0, 2.0, 0.1, key=f"{P}im")
    with c2:
        size = st.number_input("radius R (or rod length L) (m)", 0.01, 50.0, 0.2, 0.05,
                               key=f"{P}ir")
    with c3:
        axis = st.selectbox("axis", ["centre", "end"], key=f"{P}iax") \
            if body == "rod" else "centre"
    value = M.moment_of_inertia(body, m, size, size, axis)
    st.metric("I", f"{value:.4g} kg m²")
    st.caption("Dimension [ML²]: multiply by rad s⁻¹ and you get the unit of angular "
               "momentum, kg m² s⁻¹.")


def _torque() -> None:
    how_to("sliders"), how_to("numbers"),
    st.subheader("4.4.3 & 4.4.4 · Torque and angular acceleration")
    st.latex(r"\tau = rF\sin\theta, \qquad \tau = I\alpha")
    c1, c2, c3 = st.columns(3)
    with c1:
        r = st.number_input("moment arm r (m)", 0.01, 10.0, 0.4, 0.05, key=f"{P}tr")
    with c2:
        f = st.number_input("force F (N)", 0.0, 2000.0, 30.0, 1.0, key=f"{P}tf")
    with c3:
        phi = st.slider("angle between r and F (°)", 0.0, 180.0, 70.0, 1.0, key=f"{P}tphi")
    tau = M.torque(r, f, phi)
    body = st.selectbox("body", ["ring", "disc", "sphere", "shell"], key=f"{P}tbody")
    spec = {"ring": 1.0, "disc": 0.5, "sphere": 0.4, "shell": 2 / 3}[body]
    radius = st.number_input("body radius (m)", 0.01, 10.0, 0.25, 0.05, key=f"{P}tR")
    mass = st.number_input("body mass (kg)", 0.01, 1000.0, 2.0, 0.1, key=f"{P}tm")
    inertia = spec * mass * radius ** 2
    alpha = M.rotational_acceleration(tau, inertia)
    st.latex(rf"\tau = rF\sin\phi = {tau:.4g}\ \text{{N\,m}}")
    st.latex(rf"I = {inertia:.4g}\ \text{{kg\,m^2}}, \qquad "
             rf"\alpha = \frac{{\tau}}{{I}} = {alpha:.4g}\ \text{{rad s}}^{{-2}}")
    table(pd.DataFrame([
        {"quantity": "perpendicular force F sin φ", "value": f"{f * math.sin(math.radians(phi)):.4g} N"},
        {"quantity": "torque τ", "value": f"{tau:.4g} N m"},
        {"quantity": "moment of inertia I", "value": f"{inertia:.4g} kg m²"},
        {"quantity": "angular acceleration α = τ/I", "value": f"{alpha:.4g} rad s⁻²"},
        {"quantity": "linear analogue: F = ma with F = τ/r",
         "value": f"{tau / r:.4g} N"},
    ]), use_container_width=True, hide_index=True)
    if abs(phi - 90) < 2:
        st.success("A perpendicular force gives the largest torque possible for this moment "
                   "arm — this is why brakes and steering wheels are pushed sideways.")
    guidance(EXAM_TIP, "τ = rF is only ever true at 90°",
             "Always write τ = rF sin θ. The textbook diagram of a force applied to a "
             "spanner almost always shows the perpendicular case without saying so, and "
             "dropping the sine there is a silent factor-of-ten error.")


def _angularmomentum() -> None:
    how_to("numbers"),
    st.subheader("4.5 · Angular momentum")
    st.latex(r"L = I\omega \qquad \text{unit: kg m}^2\text{ s}^{-1} \qquad "
             r"\text{dimension: } [ML^2T^{-1}]")
    c1, c2 = st.columns(2)
    with c1:
        inertia = st.number_input("moment of inertia I (kg m²)", 0.0, 500.0, 2.0, 0.1,
                                  key=f"{P}li")
    with c2:
        omega = st.number_input("angular velocity ω (rad s⁻¹)", 0.0, 500.0, 5.0, 0.5,
                                key=f"{P}lw")
    st.metric("L = Iω", f"{M.angular_momentum(inertia, omega):.4g} kg m² s⁻¹")

    st.subheader("Conservation — the skater")
    a1, a2 = st.columns(2)
    with a1:
        i1 = st.number_input("I before (kg m²)", 0.01, 100.0, 1.6, 0.05, key=f"{P}l1")
    with a2:
        i2 = st.number_input("I after arms in (kg m²)", 0.01, 100.0, 0.4, 0.05, key=f"{P}l2")
    w1 = st.number_input("ω before (rad s⁻¹)", 0.0, 200.0, 12.6, 0.1, key=f"{P}lw1")
    result = M.conserve_angular_momentum(i1, w1, i2)
    st.markdown(VIS.skater_spin(i1, w1, i2), unsafe_allow_html=True)
    table(pd.DataFrame([
        {"quantity": "L before", "value": f"{result['angular_momentum_before']:.4g} kg m² s⁻¹"},
        {"quantity": "L after", "value": f"{result['angular_momentum_after']:.4g} kg m² s⁻¹"},
        {"quantity": "ω before", "value": f"{result['omega_before']:.4g} rad s⁻¹"},
        {"quantity": "ω after", "value": f"{result['omega_after']:.4g} rad s⁻¹"},
        {"quantity": "spin rate factor", "value": f"{result['speed_factor']:.4g}"},
        {"quantity": "rotational energy before", "value": f"{result['energy_before']:.4g} J"},
        {"quantity": "rotational energy after", "value": f"{result['energy_after']:.4g} J"},
    ]), use_container_width=True, hide_index=True)
    st.info("Note that L is conserved but the kinetic energy is not — the extra energy came "
            "from her muscles. This is the one place in the chapter where momentum and energy "
            "disagree.")

    st.subheader("Applications")
    table(pd.DataFrame([
        {"application": a["application"], "how it works": a["idea"]}
        for a in M.flywheel_note()
    ]), use_container_width=True, hide_index=True)


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "projectile": _projectile,
    "relations": _relations,
    "drag": _drag,
    "angular": _angular,
    "centripetal": _centripetal,
    "centrifuge": _centrifuge,
    "orbit": _orbit,
    "inertia": _inertia,
    "torque": _torque,
    "angularmomentum": _angularmomentum,
    "worked": lambda: worked_problems(SPEC),
    "practice": lambda: practice(SPEC),
    "tutor": lambda: ai_tutor.render(_N),
    "references": lambda: references(SPEC),
}

STATIONS = [Station(row["key"], row["label"], RENDERERS[row["key"]], row["slos"])
            for row in D.STATIONS]

SPEC = ChapterSpec(
    number=_N,
    title="Motion in Two Dimensions",
    blurb="Projectile motion, angular motion, centripetal force, moment of inertia and angular momentum.",
    tag=D.TAG, intro=D.INTRO, stations=STATIONS, slos=D.SLOS, key_prefix=P,
    big_ideas=D.BIG_IDEAS, worked_problems=D.WORKED_PROBLEMS,
    practice_questions=D.PRACTICE_QUESTIONS, references=D.REFERENCES,
    tutor=ai_tutor.render, route=D.ROUTE, honesty_pills=D.HONESTY_PILLS,
    notes=D.NOTES,
)


def render() -> None:
    from .. import engine
    engine.render(SPEC)


def station_count() -> int:
    return len(STATIONS)