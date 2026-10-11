"""Chapter 10 tutor: heat, the molecular model, gas laws, the first and second laws."""

from __future__ import annotations

import math

from ..core.thermo import (boyles_law, carnot_efficiency, charles_law, cp_cv,
                           entropy_change_process, ideal_gas_pressure, mean_speed,
                           most_probable_speed, refrigerator_cop, rms_speed,
                           to_kelvin, work_by_gas)

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["temperature", "what is temperature", "is temperature heat",
              "difference between heat and temperature"],
     "title": "Temperature",
     "answer": (
         "**Temperature** measures the *average kinetic energy* of the molecules.\n\n"
         "**Heat** is the energy transferred because of a temperature difference.\n\n"
         "Temperature is a property of a body; heat is a journey. A hot body contains "
         "internal energy, and contains heat only while that energy is in transit.\n\n"
         "Temperature is measured in **kelvin** in every gas formula. Celsius and kelvin "
         "differences are the same size; their readings are not."),
     "slo": "10.1.1"},
    {"keys": ["zeroth law", "thermal equilibrium", "what is the zeroth law"],
     "title": "Thermal equilibrium and the zeroth law",
     "answer": (
         "Two bodies are in **thermal equilibrium** when no net heat would flow between "
         "them — which means they share one temperature.\n\n"
         "**Zeroth law:** if A = B and B = C in temperature, then A = C.\n\n"
         "That is what makes a thermometer worth having: it lets you find an unknown body by "
         "comparing it with two you already know."),
     "slo": "10.1.3"},
    {"keys": ["absolute zero", "kelvin scale", "why kelvin", "zero kelvin"],
     "title": "Absolute zero and the kelvin scale",
     "answer": (
         "**0 K = −273.15 °C**, and it is the floor of the scale.\n\n"
         "It is found, not assumed: plot volume against temperature for several gases at "
         "constant pressure, and every isobar is a straight line whose extrapolation "
         "intercepts the temperature axis at the same point.\n\n"
         "Since 2019 the kelvin has been **defined** by fixing k = 1.380649 × 10⁻²³ J K⁻¹ "
         "exactly, so 273.15 now carries unlimited significant figures."),
     "slo": "10.1.4"},
    {"keys": ["liquid in glass thermometer", "how does a thermometer work",
              "clinical thermometer", "constriction"],
     "title": "Thermometers",
     "answer": (
         "A **liquid** expands far more than the glass around it, so the column climbs a "
         "narrow capillary.\n\n"
         "* The capillary is narrow so a small volume change lifts the column a long way.\n"
         "* Between 0 °C and 100 °C the liquid expands about **100 times** faster than the "
         "glass, so the glass correction is real but small.\n"
         "* A **clinical** thermometer has a constriction above the bulb, which stops the "
         "mercury running back down so the reading can be taken. It must be shaken down "
         "after use."),
     "slo": "10.1.5"},
    {"keys": ["kinetic molecular theory", "postulates of kmt",
              "assumptions of the molecular model"],
     "title": "Kinetic molecular theory",
     "answer": (
         "1. A very large number of tiny molecules, total volume negligible beside the "
         "container.\n"
         "2. Constant **random** motion in all directions.\n"
         "3. All collisions, with each other and with the walls, are perfectly **elastic**.\n"
         "4. The time between collisions is negligible, so molecules travel in straight "
         "lines.\n"
         "5. Attractive forces are negligible except at the instant of collision.\n"
         "6. The average kinetic energy depends **only on the temperature**."),
     "slo": "10.2.1"},
    {"keys": ["what is pressure", "explain pressure", "molecular explanation of pressure"],
     "title": "Where pressure comes from",
     "answer": (
         "Each collision changes a molecule's momentum from +mv to −mv, so Δp = 2mv.\n\n"
         "Add up the collisions per second and divide by the wall area: that is a force, "
         "and a force per unit area is a **pressure**.\n\n"
         "Nothing mysterious is happening. It is bookkeeping of impacts."),
     "slo": "10.2.2"},
    {"keys": ["derive pv equals one third n m v squared", "kinetic relation",
              "derive pv n m v squared"],
     "title": "The kinetic relation",
     "answer": (
         "1. One molecule: Δp = 2mv.\n"
         "2. All N molecules on a face of area A: F = Nm v²/A.\n"
         "3. P = F/A = Nm ⟨v²⟩ / 3V — the **3** is there because motion is in three "
         "dimensions.\n"
         "4. So **PV = (1/3) N m ⟨v²⟩**.\n"
         "5. Substituting ⟨v²⟩ = 3RT/M and N = nN_A reduces it exactly to PV = nRT."),
     "slo": "10.2.3"},
    {"keys": ["why temperature depends on energy not gas", "does mass matter",
              "same temperature different gases"],
     "title": "Temperature is energy, not speed",
     "answer": (
         "From ½ m ⟨v²⟩ = (3/2) kT, the **m cancels out**.\n\n"
         "A heavy molecule is slower, but carries proportionally more momentum, and the "
         "two effects cancel exactly. So every gas at 300 K has the same average molecular "
         "energy — while hydrogen moves at about 2030 m s⁻¹ and carbon dioxide at 408."),
     "slo": "10.2.4"},
    {"keys": ["boyles law", "p1 v1 equals p2 v2"],
     "title": "Boyle's law",
     "answer": (
         "At **constant temperature**, **P₁V₁ = P₂V₂**.\n\n"
         "On a P–V graph the isotherms are rectangular hyperbolae; the steeper the curve, "
         "the colder the gas.\n\n"
         "Note that doubling the volume repeatedly does not halve the pressure repeatedly: "
         "V → 2V → 4V gives P, P/2, **P/4**."),
     "slo": "10.3.1"},
    {"keys": ["charles law", "v over t equals v over t", "charles law celsius"],
     "title": "Charles's law",
     "answer": (
         "At **constant pressure**, **V₁/T₁ = V₂/T₂**, with **both temperatures in "
         "kelvin**.\n\n"
         "This is why the kelvin scale exists: plotted against Celsius, the line "
         "intercepts at −273.15 °C. That intercept *is* absolute zero.\n\n"
         "Using Celsius is not a small error — it is a **false statement**. 17 °C to 47 °C "
         "in Celsius would nearly triple the volume, which is absurd."),
     "slo": "10.3.2"},
    {"keys": ["ideal gas equation", "pv equals nrt", "what is a mole", "avogadro"],
     "title": "The ideal gas equation",
     "answer": (
         "**PV = nRT**, with R = 8.314462 J mol⁻¹ K⁻¹.\n\n"
         "A **mole** is 6.022 × 10²³ particles; R is just the same constant per particle "
         "(the Boltzmann constant k) multiplied by Avogadro's number.\n\n"
         "Every gas law is this one line restricted: hold n and T and you have Boyle's "
         "law; hold P and n and you have Charles's law."),
     "slo": "10.3.3"},
    {"keys": ["rms speed", "root mean square speed", "derive rms speed"],
     "title": "rms speed",
     "answer": (
         "**v_rms = √(3RT/M)**, in m s⁻¹, with **M in kg mol⁻¹**.\n\n"
         "It is the square root of the mean *square* speed — equivalently, the speed a "
         "molecule would have if all its energy were translational.\n\n"
         "Two traps: use kg mol⁻¹ not g mol⁻¹ (that is a factor of 1000), and remember "
         "speed ∝ √T and ∝ 1/√M."),
     "slo": "10.4.1"},
    {"keys": ["compare rms mean and most probable", "which is largest",
              "v rms v mean v mp"],
     "title": "The three characteristic speeds",
     "answer": (
         "**v_mp < v_mean < v_rms**, always, for any gas at any temperature.\n\n"
         "* v_mp = √(2RT/M) — the peak of the distribution, the commonest single speed\n"
         "* v_mean = √(8RT/πM) — the ordinary average\n"
         "* v_rms = √(3RT/M) — gives extra weight to the few fastest molecules\n\n"
         "The ratios are fixed constants, so the order never changes. Only the common "
         "scale factor, √(T/M), does."),
     "slo": "10.4.3"},
    {"keys": ["internal energy", "u equals f over 2 nrt", "degrees of freedom"],
     "title": "Internal energy",
     "answer": (
         "**U = (f/2) nRT** — the total kinetic energy of the molecules.\n\n"
         "* f = 3 monatomic (He, Ne, Ar)\n"
         "* f = 5 diatomic at room temperature (N₂, O₂)\n"
         "* f = 6 non-linear polyatomic (H₂O)\n\n"
         "Each degree of freedom contributes (1/2) kT. That one rule is the whole of this "
         "formula, and of every heat capacity in the chapter."),
     "slo": "10.5.1"},
    {"keys": ["work done by a gas", "work p delta v", "area under pv diagram"],
     "title": "Work done by a gas",
     "answer": (
         "**W = P ΔV** at constant pressure, and more generally the **area under the path** "
         "on the P–V diagram.\n\n"
         "Expansion is positive (the gas does work); compression is negative.\n\n"
         "When the pressure varies you need the trapezium rule: W = Σ ½(Pᵢ+Pᵢ₊₁)(Vᵢ₊₁−Vᵢ)."),
     "slo": "10.5.2"},
    {"keys": ["first law", "delta u equals q minus w", "law of conservation of energy"],
     "title": "The first law",
     "answer": (
         "**ΔU = Q − W**, with W measured as work done **by** the gas.\n\n"
         "Heat added to the gas either raises its internal energy or is spent pushing the "
         "surroundings. There is no third option.\n\n"
         "And ΔU is a **state function**: it depends only on the two end states. The work "
         "depends on the path; ΔU never does."),
     "slo": "10.5.3"},
    {"keys": ["adiabatic process", "isochoric", "isobaric", "isothermal",
              "difference between the four processes"],
     "title": "The four processes",
     "answer": (
         "| process | held | ΔU | W | Q |\n"
         "|---|---|---|---|---|\n"
         "| isothermal | T | **0** | nRT ln(V₂/V₁) | = W |\n"
         "| adiabatic | Q = 0 | nC_v ΔT | −ΔU | **0** |\n"
         "| isobaric | P | nC_v ΔT | P ΔV | nC_p ΔT |\n"
         "| isochoric | V | nC_v ΔT | **0** | nC_v ΔT |\n\n"
         "Isothermal means ΔU = 0 *exactly*, because U depends on T alone for an ideal gas."),
     "slo": "10.5.4"},
    {"keys": ["specific heat capacity", "molar heat capacity", "c equals q over m dt"],
     "title": "Heat capacities",
     "answer": (
         "**specific**: c = Q / (m ΔT), in J kg⁻¹ K⁻¹\n"
         "**molar**: C = Q / (n ΔT), in J mol⁻¹ K⁻¹\n\n"
         "C = Mc, so multiply the specific value by the molar mass in kg mol⁻¹.\n\n"
         "A ΔT in Celsius is the same size as one in kelvin, so **no conversion is needed "
         "here** — unlike every gas law."),
     "slo": "10.6.1"},
    {"keys": ["mayers relation", "cp minus cv equals r", "proof of mayers relation"],
     "title": "Mayer's relation",
     "answer": (
         "**Cp − Cv = R**\n\n"
         "1. Heating 1 mol at constant **pressure** by dT needs Cp dT.\n"
         "2. Heating 1 mol at constant **volume** by dT needs Cv dT.\n"
         "3. The difference (Cp − Cv)dT went into the work of expansion.\n"
         "4. For one mole at constant pressure, P dV = R dT.\n"
         "5. Therefore (Cp − Cv)dT = R dT, so **Cp − Cv = R**."),
     "slo": "10.6.3"},
    {"keys": ["gamma", "cp over cv", "ratio of heat capacities"],
     "title": "γ = Cp/Cv",
     "answer": (
         "**γ = (f + 2)/f**\n\n"
         "* monatomic: 5/3 = 1.667\n"
         "* diatomic: 7/5 = 1.400\n"
         "* polyatomic: 4/3 = 1.333\n\n"
         "It is the exponent in **PV^γ = constant** on an adiabat, which is why an adiabat "
         "is steeper than an isotherm through the same point."),
     "slo": "10.6.2"},
    {"keys": ["reversible process", "what is reversible", "irreversible examples"],
     "title": "Reversible processes",
     "answer": (
         "A process is **reversible** if it can be undone with no net change anywhere in "
         "the universe.\n\n"
         "That needs no friction and no finite temperature or pressure difference. A "
         "frictionless slow piston qualifies; a gas expanding into a vacuum, tea cooling, "
         "a candle flame, friction and mixing do not.\n\n"
         "No real process is exactly reversible. Carnot is the **limit** real processes "
         "approach — which is what makes it useful."),
     "slo": "10.7.1"},
    {"keys": ["second law", "kelvin planck statement", "clausius statement"],
     "title": "The second law",
     "answer": (
         "**Kelvin–Planck:** no device can take heat from a single reservoir and convert "
         "it wholly into work.\n\n"
         "**Clausius:** heat cannot pass spontaneously from a colder body to a hotter one.\n\n"
         "**Entropy form:** the entropy of an isolated system can never decrease.\n\n"
         "All three say the same thing. The first law is happy with 100 % heat→work "
         "conversion; it only forbids creating energy. The second forbids destroying the "
         "**quality** of it."),
     "slo": "10.7.2"},
    {"keys": ["why no engine is perfect", "why engines waste heat", "100 percent efficient"],
     "title": "Why no engine is perfect",
     "answer": (
         "An engine must take in heat and reject heat: Q_h = W + Q_c.\n\n"
         "To run at all it needs a temperature difference, and any heat it dumps into the "
         "cold reservoir is gone from the working cycle. A perfect engine would take heat "
         "from one reservoir and turn all of it into work — which is exactly what the "
         "second law forbids.\n\n"
         "The Carnot bound 1 − T_c/T_h is the tightest possible statement of that."),
     "slo": "10.7.3"},
    {"keys": ["what is entropy", "define entropy", "entropy meaning"],
     "title": "Entropy",
     "answer": (
         "Entropy measures **how many microscopic arrangements are compatible with the "
         "macroscopic state**.\n\n"
         "A gas filling a room has enormously more available arrangements than the same "
         "gas in a corner, so it has more entropy — with identical energy, temperature and "
         "pressure.\n\n"
         "Units are **J K⁻¹**, which is the giveaway that it is a *capacity* for heat, not "
         "an amount of it."),
     "slo": "10.8.1"},
    {"keys": ["entropy never decreases", "second law entropy", "does entropy decrease"],
     "title": "The entropy law",
     "answer": (
         "The entropy of an **isolated** system can never decrease — and the universe "
         "counts as isolated.\n\n"
         "Entropy *can* fall locally: your desk tidies, ice forms, you warm up when you "
         "exercise. No violation, because the surroundings gain more entropy than the "
         "region loses. The **total** is what never falls."),
     "slo": "10.8.2"},
    {"keys": ["heat engine", "efficiency of an engine", "eta equals w over q"],
     "title": "Heat engines",
     "answer": (
         "A heat engine takes heat Q_h from a hot reservoir, does work W, and rejects Q_c "
         "into a cold reservoir.\n\n"
         "**Q_h = W + Q_c**, so **η = W/Q_h = 1 − Q_c/Q_h**.\n\n"
         "Two reservoirs are not optional: without a cold one the engine has nowhere to "
         "put the heat it is converting."),
     "slo": "10.9.1"},
    {"keys": ["carnot cycle", "four processes of the carnot cycle"],
     "title": "The Carnot cycle",
     "answer": (
         "Two **isotherms** joined by two **adiabats**, on a P–V diagram:\n\n"
         "1 → 2 isothermal expansion at T_h (takes in Q_h)\n"
         "2 → 3 adiabatic expansion (cools to T_c)\n"
         "3 → 4 isothermal compression at T_c (rejects Q_c)\n"
         "4 → 1 adiabatic compression (heats back to T_h)\n\n"
         "The **enclosed area is the net work** done in one cycle."),
     "slo": "10.9.2"},
    {"keys": ["carnot efficiency", "one minus tc over th", "derive carnot efficiency"],
     "title": "Carnot efficiency",
     "answer": (
         "**η = 1 − T_c/T_h**, both temperatures in **kelvin**.\n\n"
         "Derivation: on the two adiabats no heat passes, so the heat rejected on the cold "
         "isotherm exactly cancels the change in internal energy on the way down and the "
         "same quantity on the way back up. What is left is Q_c/T_c = Q_h/T_h, which turns "
         "η = 1 − Q_c/Q_h into **η = 1 − T_c/T_h**.\n\n"
         "Every gas property has cancelled out. The efficiency depends on nothing but the "
         "two temperatures — and no engine can beat it."),
     "slo": "10.9.3"},
    {"keys": ["refrigerator", "coefficient of performance", "cop", "how a fridge works"],
     "title": "Refrigerators",
     "answer": (
         "A refrigerator is a heat engine **run backwards**: it takes Q_c out of a cold "
         "space and dumps Q_h into the room, using work W.\n\n"
         "**COP = Q_c/W = T_c/(T_h − T_c)** for an ideal one.\n\n"
         "A COP of 5 means it moves 5 J of heat per joule spent. That is **not** an "
         "efficiency — heat is being *moved*, not created, so COP may exceed 1 and usually "
         "does."),
     "slo": "10.9.4"},
]


def _kelvin(value):
    return f"**{float(value):g} °C = {to_kelvin(float(value)):.2f} K**"


def _boyles(p1, v1, v2):
    result = boyles_law(float(p1), float(v1), float(v2))
    return (f"**P₁ = {float(p1):.4g} Pa, V₁ = {float(v1):.4g} m³, V₂ = {float(v2):.4g} m³**"
            f"\n\nP₂ = P₁V₁/V₂ = **{result:.5g} Pa**\n\n"
            f"Volume {'rose' if float(v2) > float(v1) else 'fell'} by a factor "
            f"{float(v2) / float(v1):.3g}, so the pressure moved the other way by the same "
            f"factor.")


def _charles(v1, t1, t2):
    k1, k2 = to_kelvin(float(t1)), to_kelvin(float(t2))
    result = charles_law(float(v1), k1, k2)
    return (f"**V₁ = {float(v1):.4g} m³, T₁ = {float(t1):g} °C = {k1:.2f} K, "
            f"T₂ = {float(t2):g} °C = {k2:.2f} K**\n\n"
            f"V₂ = V₁ T₂/T₁ = **{result:.5g} m³**\n\n"
            f"Both temperatures in kelvin — that is the only reason this works. Doing it in "
            f"Celsius would give {float(v1) * float(t2) / float(t1):.4g} m³, which is "
            f"nonsense.")


def _ideal(p, v, n, t):
    result = ideal_gas_pressure(float(n), float(t), float(v))
    return (f"**n = {float(n):.4g} mol, T = {float(t):.4g} K, V = {float(v):.4g} m³**\n\n"
            f"P = nRT/V = **{result:.5g} Pa**\n\n"
            f"That is {result / 101325:.2f} atmospheres.")


def _rms(t, m):
    v = rms_speed(float(t), float(m))
    return (f"**T = {float(t):.4g} K, M = {float(m):.4g} kg mol⁻¹**\n\n"
            f"v_rms = √(3RT/M) = **{v:.5g} m s⁻¹**\n\n"
            f"v_mean = {mean_speed(float(t), float(m)):.5g} m s⁻¹ and "
            f"v_mp = {most_probable_speed(float(t), float(m)):.5g} m s⁻¹ — the order "
            f"v_mp < v_mean < v_rms never changes.\n\n"
            f"Check the molar mass is in **kg mol⁻¹**. Using g mol⁻¹ gives a speed 1000 "
            f"times too large.")


def _cp(f):
    result = cp_cv(int(f))
    return (f"**f = {int(f)} degrees of freedom**\n\n"
            f"Cv = (f/2)R = **{result['cv']:.4g} J mol⁻¹ K⁻¹**\n"
            f"Cp = Cv + R = **{result['cp']:.4g} J mol⁻¹ K⁻¹**\n"
            f"γ = Cp/Cv = **{result['gamma']:.4g}**\n\n"
            f"Cp − Cv = {result['difference']:.4g} J mol⁻¹ K⁻¹ = R, exactly as Mayer's "
            f"relation requires.")


def _carnot(th, tc):
    result = carnot_efficiency(float(th), float(tc))
    if "error" in result:
        return f"That pair of reservoirs will not work. {result['error']}"
    return (f"**T_h = {float(th):.4g} K, T_c = {float(tc):.4g} K**\n\n"
            f"η = 1 − T_c/T_h = **{result['efficiency']:.5g} = "
            f"{result['efficiency_percent']:.2f} %**\n\n"
            f"{result['note']}\n\n"
            f"The Carnot engine is the best engine that can exist between these two "
            f"temperatures. Every real engine is worse.")


def _cop(tc, th):
    result = refrigerator_cop(float(tc), float(th))
    if "error" in result:
        return f"That will not work. {result['error']}"
    return (f"**T_c = {float(tc):.4g} K, T_h = {float(th):.4g} K**\n\n"
            f"COP = T_c/(T_h − T_c) = **{result['cop']:.5g}**\n\n"
            f"{result['note']}\n\n"
            f"Read that carefully: it removes {result['cop']:.2g} J of heat from the cold "
            f"space for **every joule** of electricity. Heat is moved, not created.")


def _entropy(q, t):
    return (f"**Q_rev = {float(q):.4g} J at T = {float(t):.4g} K**\n\n"
            f"ΔS = Q_rev/T = **{entropy_change_process(1.0, float(q), float(t)):.5g} "
            f"J K⁻¹**\n\n"
            f"The units J K⁻¹ tell you entropy is a *capacity* for heat, not an amount of "
            f"it. Twice the heat at the same temperature doubles ΔS.")


def _work(p, dv):
    verdict = ("Positive, because the gas expanded and pushed the surroundings."
               if float(dv) > 0 else
               "Negative, because the surroundings squeezed the gas.")
    return (f"**P = {float(p):.4g} Pa, ΔV = {float(dv):.4g} m³**\n\n"
            f"W = P ΔV = **{work_by_gas(float(p), float(dv)):.5g} J**\n\n"
            f"{verdict}")


CALCULATORS = [
    {"pattern": r"(-?\d+(?:\.\d+)?)\s*(?:°|degrees?)?\s*c\s*(?:to|in|as)\s*kelvin",
     "reply": lambda a: _kelvin(a[0])},
    {"pattern": r"boyle\D*?([\d.eE+-]+)\D+?([\d.eE+-]+)\D+?([\d.eE+-]+)",
     "reply": lambda a: _boyles(*a[:3])},
    {"pattern": r"charles\D*?([\d.eE+-]+)\D+?(-?[\d.]+)\D+?(-?[\d.]+)", "reply": lambda a: _charles(*a[:3])},
    {"pattern": r"ideal gas\D*?([\d.eE+-]+)\D+?([\d.eE+-]+)\D+?([\d.eE+-]+)\D+?([\d.eE+-]+)",
     "reply": lambda a: _ideal(*a[:4])},
    {"pattern": r"rms\D*?([\d.eE+-]+)\D+?([\d.eE+-]+)", "reply": lambda a: _rms(*a[:2])},
    {"pattern": r"(?:cp|cv|gamma|heat capacit\w+)\D*?(\d+)", "reply": lambda a: _cp(a[0])},
    {"pattern": r"carnot\D*?([\d.eE+-]+)\D+?([\d.eE+-]+)", "reply": lambda a: _carnot(*a[:2])},
    {"pattern": r"(?:cop|refrigerator|coefficient of performance)\D*?([\d.eE+-]+)\D+?"
                r"([\d.eE+-]+)", "reply": lambda a: _cop(*a[:2])},
    {"pattern": r"entropy\D*?([\d.eE+-]+)\D+?([\d.eE+-]+)", "reply": lambda a: _entropy(*a[:2])},
    {"pattern": r"work\D*?([\d.eE+-]+)\D+?(-?[\d.eE+-]+)", "reply": lambda a: _work(*a[:2])},
]