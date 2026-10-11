"""Chapter 10 interface: Thermodynamics.

Thirty-five outcomes, nine sections, and only one idea underneath them: pressure
is not a property of a gas, it is a description of what its molecules are doing.

The station instrument that matters most here is the **P-V bench**, which draws
the path of any process you describe and shades the area under it. Work, the
first law, the four named processes and the Carnot cycle are all the same
picture with a different curve on it.
"""

from __future__ import annotations

import math

import pandas as pd
import streamlit as st

from .. import ai_tutor
from ..core import thermo as T
from ..engine import (ChapterSpec, EXAM_TIP, HONEST_LIMIT, TRY_IT, WATCH_OUT,
                      Station, guidance, overview_station, practice,
                      references, worked_problems)
from ..theme import AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, metric_row
from ..visuals import ch10 as VIS
from . import ch10_data as D

_N = 10
P = f"c{_N}_"

PROCESS_KEYS = ["isothermal", "adiabatic", "isobaric", "isochoric"]


# --------------------------------------------------------------------------
# 10.1  Heat and temperature
# --------------------------------------------------------------------------

def _temperature() -> None:
    st.subheader("10.1 · Heat, temperature and thermal equilibrium")
    st.markdown(
        "**Temperature** is a measure of the average kinetic energy of the molecules. "
        "**Heat** is the energy that passes from a hotter body to a colder one because "
        "of the temperature difference between them. Neither one is a substance: a hot "
        "body contains internal energy, and it contains heat only for as long as that "
        "energy is in transit on its way somewhere else.")

    reading = st.slider("the reading on your thermometer (°C)", -60.0, 120.0, 25.0, 1.0,
                        key=f"{P}1read")
    st.markdown(VIS.temperature_scales(reading=reading), unsafe_allow_html=True)

    st.markdown("\n\n".join(f"**{s['step']}** — {s['detail']}"
                            for s in D.THERMOMETER_STEPS))
    st.markdown(VIS.thermometer_cutaway(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"type": t["name"], "range": t["range"], "why this one": t["why"]}
        for t in D.THERMOMETER_TYPES
    ]), use_container_width=True, hide_index=True)

    st.subheader("Thermal equilibrium and the zeroth law")
    st.markdown(VIS.equilibrium_contact(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"situation": e["situation"],
         "in equilibrium?": "yes" if e["in_equilibrium"] else "no",
         "what happens": e["what_happens"]} for e in D.EQUILIBRIUM_EXAMPLES
    ]), use_container_width=True, hide_index=True)
    st.write("**The zeroth law.** If A is in thermal equilibrium with B, and B with C, "
              "then A is in thermal equilibrium with C. That is what makes a thermometer "
              "worth having: it lets you find an unknown body's temperature by comparing "
              "it with two others you already know.")
    guidance(WATCH_OUT, "Hotter means faster, not more of anything",
             "Temperature is a measure of the *average* kinetic energy of the molecules. A "
             "single molecule in a very hot gas can be moving more slowly than one in a "
             "cool gas. Any question about 'the speed of the molecules' means the average.")


# --------------------------------------------------------------------------
# 10.2  Kinetic molecular theory
# --------------------------------------------------------------------------

def _molecules() -> None:
    st.subheader("10.2 · The molecular model, and where pressure comes from")
    st.markdown(VIS.molecular_box(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"assumption": p["postulate"], "what it gives you": p["consequence"]}
        for p in D.POSTULATE_LINKS
    ]), use_container_width=True, hide_index=True)

    st.subheader("Pressure is a rate of momentum transfer")
    speed = st.slider("molecule speed hitting the wall (m s⁻¹)", 50, 1500, 400, 50,
                      key=f"{P}2speed")
    st.markdown(VIS.pressure_collisions(speed), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"factor": f["factor"], "effect": f["effect"], "why": f["why"]}
        for f in D.PRESSURE_FACTORS
    ]), use_container_width=True, hide_index=True)

    st.subheader("Deriving PV = (1/3) N m ⟨v²⟩")
    st.markdown(VIS.derivation_ladder(), unsafe_allow_html=True)
    st.markdown("\n\n".join(f"**{d['step']}** — {d['detail']}"
                            for d in D.DERIVATION_KINETIC))

    n_col, m_col, v_col, v2_col = st.columns(4)
    with n_col:
        n_mol = st.number_input("N (molecules)", 1e20, 1e24, 2.0e23, 1e21, format="%.1e",
                                key=f"{P}2n")
    with m_col:
        mass = st.number_input("m (kg)", 1e-28, 1e-24, 4.65e-26, 1e-28, format="%.2e",
                               key=f"{P}2m")
    with v_col:
        v2 = st.number_input("⟨v²⟩ (m² s⁻²)", 1.0, 5.0e5, 4.0e3, 1.0, key=f"{P}2v2")
    with v2_col:
        volume = st.number_input("V (m³)", 1e-4, 1.0, 1.0e-3, 1e-4, format="%.0e",
                                 key=f"{P}2vol")
    pv = T.kinetic_pressure_volume(n_mol, mass, v2)
    pressure = T.kinetic_pressure(n_mol, mass, v2, volume)
    st.latex(rf"PV = \tfrac{{1}}{{3}} N m \langle v^2\rangle = "
             rf"\tfrac{{1}}{{3}}({n_mol:.3g})({mass:.3g})({v2:.3g}) = {pv:.5g}\ \mathrm{{J}}")
    st.latex(rf"P = \frac{{PV}}{{V}} = {pressure:.5g}\ \mathrm{{Pa}}")
    st.caption("P V is an energy, so joules are the right units for the first line. This is "
               "the identity the syllabus asks you to derive, and it is not an extra "
               "assumption — it falls out of the collisions.")
    guidance(HONEST_LIMIT, "The factor of one third",
             "Molecules move in three dimensions, so at any instant only about a third of "
             "them are travelling in any one direction. That 3 in the denominator is "
             "dimensional bookkeeping, and it disappears the moment you write the answer in "
             "terms of the root-mean-square speed.")


# --------------------------------------------------------------------------
# 10.3  Gas laws
# --------------------------------------------------------------------------

def _gases() -> None:
    st.subheader("10.3 · Boyle's law, Charles's law and the ideal gas equation")
    st.markdown(VIS.gas_law_grid(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"law": g["law"], "condition": g["condition"], "relation": g["relation"],
         "note": g["note"]} for g in D.GAS_LAW_NOTES
    ]), use_container_width=True, hide_index=True)

    st.subheader("Solve any gas-law problem")
    law = st.radio("which law?", ["Boyle (P V = constant, T constant)",
                                  "Charles (V / T = constant, P constant)",
                                  "Ideal gas equation (P V = n R T)"],
                   key=f"{P}3law")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        p1 = st.number_input("P₁ (Pa)", 0.0, 1e8, 1.0e5, 1.0e3, format="%.2e", key=f"{P}3p1")
    with c2:
        v1 = st.number_input("V₁ (m³)", 1e-6, 1.0, 2.0e-3, 1e-4, format="%.2e", key=f"{P}3v1")
    with c3:
        t1 = st.number_input("T₁ (K)", 1.0, 2000.0, 300.0, 1.0, key=f"{P}3t1")
    with c4:
        extra = st.number_input(
            "V₂ (m³) if Boyle, T₂ (K) if Charles, V₂ (m³) if ideal" if law != "Boyle (P V = constant, T constant)"
            else "V₂ (m³)", 1e-6, 100.0,
            1.0e-3 if "Boyle" in law or "ideal" in law else 400.0,
            1e-4, format="%.2e", key=f"{P}3x")

    if law.startswith("Boyle"):
        result = T.boyles_law(p1, v1, extra)
        st.latex(rf"P_2 = \frac{{P_1 V_1}}{{V_2}} = \frac{{({p1:.4g})({v1:.4g})}}{{{extra:.4g}}}"
                 rf" = {result:.5g}\ \mathrm{{Pa}}")
        st.caption("No unit conversion is needed for the volumes: they cancel in the ratio.")
    elif law.startswith("Charles"):
        result = T.charles_law(v1, t1, extra)
        st.latex(rf"V_2 = V_1 \frac{{T_2}}{{T_1}} = ({v1:.4g}) \frac{{{extra:.4g}}}"
                 rf"{{{t1:.4g}}} = {result:.5g}\ \mathrm{{m^3}}")
        st.caption("Both temperatures entered in kelvin. If you want to work in Celsius, "
                   "convert both to kelvin first and you will get the right answer; if you "
                   "skip that, the answer will be wildly too large.")
    else:
        moles = st.number_input("n (mol)", 0.01, 100.0, 1.0, 0.1, key=f"{P}3n")
        result = T.ideal_gas_pressure(moles, t1, extra)
        st.latex(rf"P_2 = \frac{{nRT}}{{V_2}} = \frac{{({moles:.4g})({T.GAS_CONSTANT:.4g})"
                 rf"({t1:.4g})}}{{{extra:.4g}}} = {result:.5g}\ \mathrm{{Pa}}")
        st.caption(f"nRT = n moles × R × temperature. R = {T.GAS_CONSTANT:.6f} J mol⁻¹ K⁻¹.")
    guidance(EXAM_TIP, "Convert to kelvin before anything else, not after",
             "Charles's law is not merely difficult in Celsius, it is **false**. Writing "
             "V₁/T₁ = V₂/T₂ with 17 °C and 47 °C gives more than twice the correct volume, "
             "and the error is so large it is impossible to miss if you sanity-check the "
             "size of the answer.")


# --------------------------------------------------------------------------
# 10.4  Molecular speeds
# --------------------------------------------------------------------------

def _speeds() -> None:
    st.subheader("10.4 · How fast the molecules move")
    mass_label = st.selectbox("the gas", list(D.MOLAR_MASSES), key=f"{P}4gas")
    molar_mass = D.MOLAR_MASSES[mass_label]
    temperature = st.slider("temperature (K)", 50.0, 1200.0, 300.0, 10.0, key=f"{P}4t")
    st.markdown(VIS.speed_distribution(temperature, molar_mass), unsafe_allow_html=True)

    v_mp, v_mean, v_rms = (T.most_probable_speed(temperature, molar_mass),
                           T.mean_speed(temperature, molar_mass),
                           T.rms_speed(temperature, molar_mass))
    metric_row([("v_mp", f"{v_mp:.0f} m s⁻¹"),
                ("v_mean", f"{v_mean:.0f} m s⁻¹"),
                ("v_rms", f"{v_rms:.0f} m s⁻¹"),
                ("mean energy", f"{T.average_translational_energy(temperature):.3g} J")])
    st.dataframe(pd.DataFrame([
        {"quantity": d["name"], "formula": d["formula"], "meaning": d["meaning"],
         "on the curve": d["where_on_curve"]} for d in D.SPEED_DEFINITIONS
    ]), use_container_width=True, hide_index=True)
    st.markdown("\n\n".join(f"**{s['fact']}** — {s['why']}" for s in D.SPEED_ORDERING))
    st.markdown(VIS.energy_lines(temperature), unsafe_allow_html=True)
    st.markdown("\n\n".join(f"**{e['statement']}** — {e['detail']}"
                            for e in D.ENERGY_NOTES))
    st.latex(r"\tfrac{1}{2} m \langle v^2 \rangle = \tfrac{3}{2} k T")
    st.caption("The m cancels between the two sides. That single line is the whole reason "
               "temperature is the same for every gas at the same temperature, whatever "
               "their masses.")
    guidance(TRY_IT, "Change the gas, keep the temperature, and watch the curve shift",
             "Switch to hydrogen and the peak races off to the right. The *energy* does not "
             "change at all, because the molecules are lighter and the mass has gone into "
             "making them faster instead.")


# --------------------------------------------------------------------------
# 10.5  First law
# --------------------------------------------------------------------------

def _firstlaw() -> None:
    st.subheader("10.5 · Internal energy, work and the first law")
    st.write("**Internal energy** U is the sum of the kinetic energies of all the molecules. "
             "For an ideal gas it depends only on the temperature and on the number of "
             "degrees of freedom: U = (f/2) n R T. For the same reason, **dU is a state "
             "function** — it depends on where the gas started and finished, never on the "
             "route taken between them.")

    deg = st.selectbox("degrees of freedom", [3, 5, 6], index=1, key=f"{P}5f")
    n_col, t_col = st.columns(2)
    with n_col:
        moles = st.number_input("n (mol)", 0.1, 50.0, 1.0, 0.1, key=f"{P}5n")
    with t_col:
        temp = st.slider("temperature (K)", 50.0, 1500.0, 300.0, 10.0, key=f"{P}5t")
    st.latex(rf"U = \frac{{{deg}}}{{2}} nRT = \frac{{{deg}}}{{2}} \times {moles:g} \times "
             rf"{T.GAS_CONSTANT:.4f} \times {temp:g} = "
             rf"{T.internal_energy(moles, temp, deg):.5g}\ \mathrm{{J}}")
    st.caption(f"f = {deg}: three translational degrees of freedom for a monatomic gas, "
               f"{'three translational plus two rotational for a diatomic one' if deg == 5 else 'three translational plus three rotational for a non-linear molecule'}. "
               "Vibrations stay frozen out at ordinary temperatures.")

    st.subheader("Work is an area")
    st.markdown(VIS.pv_area(), unsafe_allow_html=True)
    st.latex(r"W = P \Delta V \qquad\text{(constant pressure)}")
    st.caption(f"Here W = {T.work_by_gas(1.0e5, 0.0010):.4g} J for the first, constant-"
               "pressure step alone. On a P-V diagram the work is the whole area under the "
               "path, not the rectangle you would get if the pressure stayed put.")
    path = st.slider("number of points on the path", 2, 6, 3, 1, key=f"{P}5pts")
    rows = []
    for i in range(path):
        rows.append({"P (Pa)": 1.0e5 / (i + 1), "V (m³)": 0.001 * (i + 1)})
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    points = [(row["P (Pa)"], row["V (m³)"]) for row in rows]
    area = T.work_series(points)
    st.latex(rf"W = \sum \tfrac{{(P_i + P_{{i+1}})}}{{2}} (V_{{i+1}} - V_i) = {area:.5g}\ \mathrm{{J}}")
    st.caption("The trapezium rule, because the pressure is not constant along the path. "
               "This is the area under the curve, added up in strips.")

    st.subheader("The first law")
    st.latex(r"\Delta U = Q - W")
    q_col, w_col = st.columns(2)
    with q_col:
        heat = st.number_input("heat supplied Q (J)", -5000.0, 5000.0, 1000.0, 50.0,
                               key=f"{P}5q")
    with w_col:
        work = st.number_input("work done by the gas W (J)", -5000.0, 5000.0, 300.0, 50.0,
                               key=f"{P}5w")
    balance = T.first_law(heat, work, n=moles)
    st.latex(rf"\Delta U = Q - W = ({heat:g}) - ({work:g}) = {balance['delta_U']:g}\ \mathrm{{J}}")
    st.write(balance["statement"])
    if balance["delta_U"] > 0:
        st.success(f"The internal energy **rose** by {balance['delta_U']:g} J. Of the "
                   f"{heat:g} J supplied, {balance['delta_U']:g} J stayed and {work:g} J "
                   "left as work.")
    elif balance["delta_U"] < 0:
        st.warning(f"The internal energy **fell** by {abs(balance['delta_U']):g} J.")
    else:
        st.info("The internal energy is unchanged. Every joule of heat supplied left as work.")

    st.subheader("The four processes")
    st.markdown(VIS.process_quadrant(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"process": p["process"], "dU": p["dU"], "W": p["W"], "Q": p["Q"],
         "picture": p["picture"], "what it means": p["insight"]}
        for p in D.WORK_NOTES
    ]), use_container_width=True, hide_index=True)
    st.markdown("\n\n".join(f"**{p['mistake']}** — {p['why_it_happens']} "
                            f"*Fix:* {p['fix']}" for p in D.FIRST_LAW_PITFALLS))
    guidance(WATCH_OUT, "Write your sign convention once, at the top of the page",
             "dU = Q − W with W measured as work done **by** the gas. Some books use the "
             "opposite sign. Decide which one you are using, write it down, and then never "
             "think about it again. Marks are lost on conventions, not on physics.")


# --------------------------------------------------------------------------
# 10.6  Specific heats
# --------------------------------------------------------------------------

def _heatcap() -> None:
    st.subheader("10.6 · Specific heat, molar heat capacity and Mayer's relation")
    st.markdown(VIS.heat_capacity_bars(), unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([
        {"quantity": h["quantity"], "definition": h["definition"], "formula": h["formula"],
         "units": h["units"], "note": h["note"]} for h in D.HEAT_CAP_NOTES
    ]), use_container_width=True, hide_index=True)
    st.dataframe(pd.DataFrame([
        {"molecule": d["molecule"], "f": d["f"],
         "Cv": d.get("cv_formula", d.get("cv", "—")),
         "γ": d.get("gamma", d.get("g", "—")),
         "why": d["why"]} for d in D.DEGREES_OF_FREEDOM
    ]), use_container_width=True, hide_index=True)

    st.subheader("Mayer's relation")
    st.markdown("\n\n".join(f"**{m['step']}.** {m['text']}" for m in D.MAYS_NOTES))
    proof = T.mayers_relation(5)
    st.latex(r"C_p - C_v = R")
    st.latex(rf"= {proof['cp']:.4f} - {proof['cv']:.4f} = {proof['difference']:.4f}\ "
             rf"\mathrm{{J\,mol^{-1}K^{-1}}}")
    st.caption(proof["result"])
    st.info("The two boxes of a gas molecule draw 3R/2, 5R/2 and 3R are not three different "
            "facts. They are the same single rule — one degree of freedom contributes R/2 — "
            "counted three, five and six times.")

    st.subheader("Heat-capacity problems")
    mode = st.selectbox("what are you finding?", ["Heat supplied (Q = n C dT)",
                                                   "Molar heat capacity (C = Q / n dT)",
                                                   "Molar heat capacity (c = Q / m dT)"],
                        key=f"{P}6mode")
    c1, c2, c3 = st.columns(3)
    with c1:
        q_in = st.number_input("heat Q (J)", 0.0, 1e6, 2500.0, 50.0, key=f"{P}6q")
    with c2:
        amount = st.number_input("moles n (mol)", 0.01, 100.0, 2.0, 0.1, key=f"{P}6n")
    with c3:
        dtemp = st.number_input("temperature change (K)", 0.1, 1000.0, 50.0, 1.0,
                                key=f"{P}6dt")
    if mode.startswith("Heat"):
        capacity = st.radio("at constant", ["volume (Cv)", "pressure (Cp)"], key=f"{P}6which")
        degs = st.selectbox("the gas", [3, 5, 6], index=1, key=f"{P}6f")
        caps = T.cp_cv(degs)
        value = caps["cv"] if capacity == "volume (Cv)" else caps["cp"]
        st.latex(rf"Q = nC\Delta T = ({amount:g})({value:.4f})({dtemp:g}) = "
                 rf"{amount * value * dtemp:.5g}\ \mathrm{{J}}")
        st.caption("A temperature *change* is the same size in Celsius and kelvin, so no "
                   "conversion is needed for ΔT — only for T itself.")
    elif mode.startswith("Molar"):
        value = T.molar_heat_capacity(amount, q_in, dtemp)
        st.latex(rf"C = \frac{{Q}}{{n \Delta T}} = \frac{{{q_in:g}}}{{({amount:g})({dtemp:g})}}"
                 rf" = {value:.5g}\ \mathrm{{J\,mol^{-1}K^{-1}}}")
        st.caption("Compare it with the table above. A few tens of J mol⁻¹ K⁻¹ means an "
                   "ordinary gas; a few hundred means a metal.")
    else:
        mass_kg = st.number_input("mass m (kg)", 1e-4, 100.0, 0.5, 0.1, key=f"{P}6m")
        value = q_in / (mass_kg * dtemp)
        st.latex(rf"c = \frac{{Q}}{{m \Delta T}} = \frac{{{q_in:g}}}{{({mass_kg:g})"
                 rf"({dtemp:g})}} = {value:.5g}\ \mathrm{{J\,kg^{-1}K^{-1}}}")
        st.caption(f"That is C = M c, so the molar value would be "
                   f"{value * mass_kg / amount:.4g} J mol⁻¹ K⁻¹ for this mass and amount.")
    guidance(EXAM_TIP, "Celsius degrees and kelvin are the same size for a difference",
             "A ΔT of 5 °C is a ΔT of 5 K. That is why no conversion appears anywhere in "
             "the heat-capacity formulas, even though every gas *law* needs a kelvin "
             "temperature. The two are not the same thing: the **difference** is, the "
             "**reading** is not.")


# --------------------------------------------------------------------------
# 10.7 and 10.8  The second law and entropy
# --------------------------------------------------------------------------

def _secondlaw() -> None:
    st.subheader("10.7 · Reversible processes and the second law")
    st.markdown(VIS.reversible_split(), unsafe_allow_html=True)
    for note in D.REVERSIBILITY_NOTES:
        with st.expander(note["question"]):
            st.markdown(note["answer"])
    st.markdown("\n\n".join(
        f"**{s['form']}** — {s['statement']} *In daily life:* {s['everyday']}"
        for s in D.SECOND_LAW_STATEMENTS))
    st.write(T.heat_engine_summary()["second_law"])
    guidance(HONEST_LIMIT, "Reversible is a limit, not an achievement",
             "Not one real process is exactly reversible — friction, a finite temperature "
             "difference and a finite pressure difference are all unavoidable. Carnot's "
             "engine is the bound that real engines approach and never reach, and that is "
             "precisely what makes it useful.")


def _entropy() -> None:
    st.subheader("10.8 · Entropy")
    fraction = st.slider("fraction of the room the gas can reach", 0.05, 1.0, 0.25, 0.05,
                         key=f"{P}8frac")
    st.markdown(VIS.entropy_room(fraction), unsafe_allow_html=True)
    st.write("**Entropy** measures how many microscopic arrangements are compatible with the "
             "macroscopic state of a system. A gas that has spread through a whole room has "
             "vastly more arrangements available to it than the same gas confined to a "
             "corner, and so it has a larger entropy — even though nothing about its energy, "
             "temperature or pressure has changed.")
    st.dataframe(pd.DataFrame([
        {"process": e["process"], "entropy": e["dS"], "why": e["why"]}
        for e in D.ENTROPY_EXAMPLES
    ]), use_container_width=True, hide_index=True)

    n_col, q_col, t_col = st.columns(3)
    with n_col:
        moles = st.number_input("n (mol)", 0.01, 50.0, 1.0, 0.1, key=f"{P}8n")
    with q_col:
        heat = st.number_input("heat Q (J), reversible", 0.0, 1e5, 2000.0, 100.0,
                               key=f"{P}8q")
    with t_col:
        temp = st.number_input("temperature T (K)", 10.0, 2000.0, 400.0, 10.0, key=f"{P}8t")
    st.latex(rf"\Delta S = \frac{{Q_{{rev}}}}{{T}} = \frac{{{heat:g}}}{{{temp:g}}} = "
             rf"{T.entropy_change_process(moles, heat, temp):.5g}\ \mathrm{{J\,K^{-1}}}")
    st.caption("The units J K⁻¹ are the giveaway that entropy is a *capacity* for heat, not "
               "an amount of it. Heating something twice as much at the same temperature "
               "doubles its entropy change.")
    st.subheader("Ideal gas, two states")
    t1 = st.slider("T₁ (K)", 50.0, 1500.0, 300.0, 10.0, key=f"{P}8t1")
    t2 = st.slider("T₂ (K)", 50.0, 1500.0, 600.0, 10.0, key=f"{P}8t2")
    v1 = st.number_input("V₁ (m³)", 1e-4, 10.0, 1.0e-3, 1e-4, format="%.0e", key=f"{P}8v1")
    v2 = st.number_input("V₂ (m³)", 1e-4, 10.0, 4.0e-3, 1e-4, format="%.0e", key=f"{P}8v2")
    degs = st.selectbox("degrees of freedom", [3, 5, 6], index=0, key=f"{P}8f")
    ds = T.entropy_change_ideal_gas(moles, t1, t2, v1, v2, degs)
    st.latex(rf"\Delta S = nC_v \ln\frac{{T_2}}{{T_1}} + nR \ln\frac{{V_2}}{{V_1}} = {ds:.5g}"
             rf"\ \mathrm{{J\,K^{-1}}}")
    st.caption("Entropy is a state function, so this depends only on the two end points and "
               "not on the route. That is exactly what makes it a state function at all.")
    st.dataframe(pd.DataFrame([
        {"issue": note["issue"], "the entropy story": note["entropy_link"]}
        for note in T.environment_notes
    ]), use_container_width=True, hide_index=True)
    guidance(WATCH_OUT, "Entropy can fall locally — that is not a loophole",
             "Your desk tidies, ice forms, and you feel warmer when you exercise. All of "
             "those lower the entropy of one region. The second law is about the **total**, "
             "and the surroundings gain more than the region loses, every time.")


# --------------------------------------------------------------------------
# 10.9  Heat engines, Carnot and refrigerators
# --------------------------------------------------------------------------

def _carnot() -> None:
    st.subheader("10.9 · Heat engines, the Carnot cycle and refrigerators")
    st.write(T.heat_engine_summary()["balance"])
    efficiency = st.slider("efficiency to illustrate", 0.0, 1.0, 0.40, 0.05, key=f"{P}9eta")
    st.markdown(VIS.engine_blocks(efficiency), unsafe_allow_html=True)

    st.subheader("The Carnot cycle")
    st.markdown(VIS.carnot_cycle_plot(), unsafe_allow_html=True)
    series = T.carnot_cycle_series()
    st.dataframe(pd.DataFrame([
        {"step": leg["step"], "name": leg["name"], "what happens": leg["what"],
         "how to check it": leg["check"]} for leg in T.carnot_cycle(1.0e5, 1.0, 4.0)
    ]), use_container_width=True, hide_index=True)
    st.latex(rf"\text{{enclosed area}} = {series['enclosed_area']:.5g}\ \mathrm{{J}}")
    st.caption("That is the net work done in one cycle, found by adding the area under each "
               "of the four legs. It is not a number taken from a table — it is the area of "
               "the shape drawn above.")

    st.subheader("Carnot efficiency")
    st.latex(r"\eta = 1 - \frac{T_c}{T_h}")
    th = st.slider("hot reservoir T_h (K)", 100.0, 1500.0, 500.0, 10.0, key=f"{P}9th")
    tc = st.slider("cold reservoir T_c (K)", 1.0, 1400.0, 300.0, 10.0, key=f"{P}9tc")
    if tc >= th:
        st.error("The cold reservoir cannot be hotter than the hot one. Lower T_c or raise "
                 "T_h — Carnot efficiency is only defined for an engine that runs.")
    else:
        carnot = T.carnot_efficiency(th, tc)
        st.latex(rf"\eta = 1 - \frac{{{tc:g}}}{{{th:g}}} = {carnot['efficiency']:.5g}"
                 rf" = {carnot['efficiency_percent']:.2f}\%")
        st.caption(carnot["note"])
        metric_row([("efficiency", f"{carnot['efficiency_percent']:.1f} %"),
                    ("heat wasted", f"{100 - carnot['efficiency_percent']:.1f} %")])
    st.write("**Derivation.** On the two adiabats no heat is exchanged, so the heat "
             "rejected on the cold isotherm exactly balances the change in internal energy "
             "on the way down, and cancels the same quantity on the way back up. What is "
             "left is that Q_c/T_c = Q_h/T_h, which turns "
             "eta = 1 − Q_c/Q_h into eta = 1 − T_c/T_h. Every gas law from Chapter 10.3 is "
             "used in that one step, and all the gas properties have cancelled out — which "
             "is why the efficiency depends on nothing but the two temperatures.")

    st.subheader("Refrigerators")
    st.markdown(VIS.refrigerator_blocks(th - tc), unsafe_allow_html=True)
    if tc < th:
        cop = T.refrigerator_cop(tc, th)
        st.latex(rf"\mathrm{{COP}} = \frac{{T_c}}{{T_h - T_c}} = \frac{{{tc:g}}}"
                 rf"{{{th:g} - {tc:g}}} = {cop['cop']:.5g}")
        st.caption(cop["note"])
        st.info("A coefficient of performance is **not** an efficiency. It is heat moved "
                "per joule of work, so it may exceed 1 — and it does, routinely.")
    guidance(TRY_IT, "Drop the cold reservoir a little and watch what happens",
             "A refrigerator gets dramatically worse as its set temperature falls, because "
             "the temperature gap it has to push against grows. That gap is the whole "
             "problem in the physics of every cold chain you have ever used.")


RENDERERS = {
    "overview": lambda: overview_station(SPEC),
    "temperature": _temperature,
    "molecules": _molecules,
    "gases": _gases,
    "speeds": _speeds,
    "firstlaw": _firstlaw,
    "heatcap": _heatcap,
    "secondlaw": _secondlaw,
    "entropy": _entropy,
    "carnot": _carnot,
    "worked": lambda: worked_problems(SPEC),
    "practice": lambda: practice(SPEC),
    "tutor": lambda: ai_tutor.render(_N),
    "references": lambda: references(SPEC),
}

STATIONS = [Station(row["key"], row["label"], RENDERERS[row["key"]], row["slos"])
            for row in D.STATIONS]

SPEC = ChapterSpec(
    number=_N,
    title="Thermodynamics",
    blurb="Heat and temperature, ideal gases, kinetic molecular theory, the first and second "
          "laws, specific heats, Carnot engines, refrigerators and entropy.",
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