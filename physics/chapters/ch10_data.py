"""Chapter 10 content: Thermodynamics.

Thirty-five outcomes across nine sections - the largest chapter in the book, and
the one where the arithmetic is the easiest because almost everything is a
single equation rearranged.

The running idea is that **pressure is not a property of a gas, it is a
description of what its molecules are doing**. Everything in this chapter -
Boyle's law, the ideal gas equation, the rms speed, the first law, the Carnot
efficiency - falls out of that one picture: a large number of small particles,
moving fast when they are hot, bouncing off walls.
"""

from __future__ import annotations

SLOS = [
    # ---- 10.1  Heat and temperature -------------------------------------
    {"id": "10.1.1", "text": "Define temperature and describe it as a measure of the average kinetic energy of molecules.",
     "simple": "Hotter means a higher average kinetic energy per molecule.",
     "taught": "Temperature", "activity": "Thermometer with absolute zero and the three scales",
     "check": "Guided practice: define temperature and state what it measures"},
    {"id": "10.1.2", "text": "Describe heat as the energy transferred because of a temperature difference.",
     "simple": "Heat is energy in transit, always from hotter to colder; it is not stored.",
     "taught": "Heat", "activity": "Two blocks in contact with the energy path traced",
     "check": "Guided practice: describe heat and explain why it has no direction of its own"},
    {"id": "10.1.3", "text": "Describe thermal equilibrium and state the zeroth law of thermodynamics.",
     "simple": "No net heat flows when two bodies are in thermal equilibrium; A=B and B=C then A=C.",
     "taught": "Thermal equilibrium", "activity": "Contact network with live equilibrium testing",
     "check": "Guided practice: state the zeroth law and apply it to a chain of bodies"},
    {"id": "10.1.4", "text": "Define the kelvin scale and convert temperature between the kelvin and Celsius scales.",
     "simple": "T = t + 273.15; absolute zero is -273.15 °C, the coldest possible state.",
     "taught": "The kelvin scale", "activity": "All three scales aligned on one thermometer",
     "check": "Guided practice: convert temperatures and explain the choice of absolute zero"},
    {"id": "10.1.5", "text": "Describe the working of a liquid-in-glass thermometer.",
     "simple": "A liquid expands past the melting point of the glass, so the column climbs the scale.",
     "taught": "Thermometers", "activity": "Cut-away diagram with both expansion volumes shown",
     "check": "Guided practice: describe the construction and the working of a liquid-in-glass thermometer"},

    # ---- 10.2  Kinetic molecular theory ---------------------------------
    {"id": "10.2.1", "text": "State the assumptions of kinetic molecular theory of gases.",
     "simple": "Tiny molecules, negligible volume, random motion, elastic collisions, no attractions.",
     "taught": "The molecular model", "activity": "Postulate list with each one linked to a visible consequence",
     "check": "Guided practice: state the assumptions and match each to its consequence"},
    {"id": "10.2.2", "text": "Explain pressure as the result of continuous molecular impacts on the walls of a container.",
     "simple": "Each collision changes a molecule's momentum; the total rate of momentum change per unit area is the pressure.",
     "taught": "Where pressure comes from", "activity": "Single-molecule billiard with its momentum change drawn",
     "check": "Guided practice: explain pressure in terms of molecular impacts"},
    {"id": "10.2.3", "text": "Derive PV = (1/3) N m <v^2> from the molecular model.",
     "simple": "Pressure times volume is one third of N m mean square speed.",
     "taught": "Deriving the kinetic relation", "activity": "Step-by-step derivation with each substitution named",
     "check": "Guided practice: derive PV = (1/3) N m <v^2> and show it reduces to PV = nRT"},
    {"id": "10.2.4", "text": "Explain why the average kinetic energy of molecules depends only on the temperature.",
     "simple": "Equating (1/2) m <v^2> = (3/2) k T cancels the molecule's mass entirely.",
     "taught": "Temperature is kinetic", "activity": "Two gases at one temperature with different speeds",
     "check": "Guided practice: explain why temperature depends on energy and not on the gas"},

    # ---- 10.3  Gas laws and the ideal gas equation ----------------------
    {"id": "10.3.1", "text": "State and apply Boyle's law.",
     "simple": "At constant temperature P1 V1 = P2 V2.",
     "taught": "Boyle's law", "activity": "Syringe explorer with the gas compressed on demand",
     "check": "Guided practice: state Boyle's law and solve problems on it"},
    {"id": "10.3.2", "text": "State and apply Charles's law.",
     "simple": "At constant pressure V1 / T1 = V2 / T2, with both temperatures in kelvin.",
     "taught": "Charles's law", "activity": "Two isotherms and two isobars drawn on one P-V grid",
     "check": "Guided practice: state Charles's law and solve problems on it"},
    {"id": "10.3.3", "text": "State the ideal gas equation PV = nRT and define the mole.",
     "simple": "One mole is 6.022e23 particles; R is the constant gas constant.",
     "taught": "The ideal gas equation", "activity": "Four-state solver that fills in whichever quantity is missing",
     "check": "Guided practice: state the ideal gas equation and use it in any form"},
    {"id": "10.3.4", "text": "Solve numerical problems on the gas laws and the ideal gas equation.",
     "simple": "Numerical problems on Boyle's law, Charles's law and PV = nRT.",
     "taught": "Gas-law problems", "activity": "Problem set where every answer is checked on the P-V grid",
     "check": "Guided practice: solve gas-law word problems"},

    # ---- 10.4  Molecular speeds and energies ----------------------------
    {"id": "10.4.1", "text": "Define rms speed and derive v_rms = sqrt(3RT/M).",
     "simple": "The square root of the mean square speed; the speed of a molecule at the average energy.",
     "taught": "rms speed", "activity": "Maxwell-Boltzmann curve with v_mp, v_mean and v_rms marked",
     "check": "Guided practice: define rms speed and derive the formula"},
    {"id": "10.4.2", "text": "Define the average translational energy of a molecule as (3/2) kT.",
     "simple": "Energy per molecule is proportional to absolute temperature and to nothing else.",
     "taught": "Average translational energy", "activity": "Energy against temperature for three different gases",
     "check": "Guided practice: state and use (3/2) kT"},
    {"id": "10.4.3", "text": "Compare the mean, rms and most probable speeds of the molecules of a gas.",
     "simple": "v_mp < v_mean < v_rms; they differ because of the spread of speeds.",
     "taught": "Comparing the speeds", "activity": "One distribution curve with all three speeds marked",
     "check": "Guided practice: compare the three characteristic speeds and explain the ordering"},

    # ---- 10.5  Internal energy, work and the first law ------------------
    {"id": "10.5.1", "text": "Define internal energy and express it as U = (f/2) nRT.",
     "simple": "The sum of the kinetic energies of all the molecules, depending on degrees of freedom.",
     "taught": "Internal energy", "activity": "Degrees of freedom added to a molecule as the temperature rises",
     "check": "Guided practice: define internal energy and calculate it"},
    {"id": "10.5.2", "text": "Define the work done by a gas as W = P dV and as the area under the path on the P-V diagram.",
     "simple": "Work is the area under the P-V curve; compression gives negative work.",
     "taught": "Work and the P-V diagram", "activity": "P-V diagram with the area under the path shaded live",
     "check": "Guided practice: calculate work from a P-V diagram and from P dV"},
    {"id": "10.5.3", "text": "State the first law of thermodynamics, dU = Q - W.",
     "simple": "Heat added either raises internal energy or is spent pushing the surroundings.",
     "taught": "The first law", "activity": "Energy balance with every joule accounted for",
     "check": "Guided practice: state the first law and apply it in each direction"},
    {"id": "10.5.4", "text": "Describe isothermal, adiabatic, isobaric and isochoric processes with their dU, W and Q.",
     "simple": "Four named processes, each with one quantity held constant and its own signatures.",
     "taught": "The four processes", "activity": "All four drawn on one P-V grid and tabulated",
     "check": "Guided practice: describe each process and state dU, W and Q for it"},
    {"id": "10.5.5", "text": "Solve numerical problems using the first law of thermodynamics.",
     "simple": "Numerical problems on dU = Q - W for the four processes.",
     "taught": "First-law problems", "activity": "Problem set with the energy balance diagram on every answer",
     "check": "Guided practice: solve first-law word problems"},

    # ---- 10.6  Heat capacity and Mayer's relation -----------------------
    {"id": "10.6.1", "text": "Define specific heat capacity and molar heat capacity.",
     "simple": "C = Q / (n dT); the heat needed to raise one mole by one kelvin.",
     "taught": "Heat capacities", "activity": "Heating curve with the heat capacity read off the slope",
     "check": "Guided practice: define and calculate specific and molar heat capacity"},
    {"id": "10.6.2", "text": "Relate Cv and Cp to the degrees of freedom and state Cv = (f/2) R and Cp = Cv + R.",
     "simple": "Monatomic f=3, diatomic f=5 at room temperature; Cp is always the larger.",
     "taught": "Cv, Cp and gamma", "activity": "Bar comparison of Cv, Cp and gamma for monatomic, diatomic and polyatomic",
     "check": "Guided practice: state and use Cv, Cp and gamma for the common gases"},
    {"id": "10.6.3", "text": "State and prove Mayer's relation Cp - Cv = R.",
     "simple": "The extra heat at constant pressure is exactly the work of expansion, which is R dT.",
     "taught": "Mayer's relation", "activity": "Five-line proof with each line tied to the first law",
     "check": "Guided practice: state and prove Mayer's relation"},
    {"id": "10.6.4", "text": "Solve numerical problems on specific and molar heat capacities.",
     "simple": "Numerical problems on Q = m c dT, Q = n C dT and on Cp - Cv.",
     "taught": "Heat-capacity problems", "activity": "Problem set with the molar mass read off the table",
     "check": "Guided practice: solve heat-capacity word problems"},

    # ---- 10.7  Reversible processes and the second law ------------------
    {"id": "10.7.1", "text": "Define a reversible process and give examples of reversible and irreversible processes.",
     "simple": "Reversible means the change and its inverse can both be run with no net change anywhere.",
     "taught": "Reversible processes", "activity": "Seven real processes sorted into reversible and irreversible",
     "check": "Guided practice: define reversibility and classify each process"},
    {"id": "10.7.2", "text": "State the second law of thermodynamics in its two usual forms.",
     "simple": "No device converts heat wholly into work; and entropy never decreases.",
     "taught": "The second law", "activity": "Both statements side by side with the refrigerator test",
     "check": "Guided practice: state the second law in both forms"},
    {"id": "10.7.3", "text": "Explain why no heat engine can be 100 percent efficient.",
     "simple": "An engine that rejected no heat would take in heat from one reservoir and turn it all into work.",
     "taught": "Why engines waste heat", "activity": "Energy-flow diagram with the unavoidable waste marked",
     "check": "Guided practice: explain why perfect efficiency is impossible"},

    # ---- 10.8  Entropy --------------------------------------------------
    {"id": "10.8.1", "text": "Define entropy and describe it as a measure of the number of accessible microscopic arrangements.",
     "simple": "Entropy counts arrangements; more arrangements means larger entropy.",
     "taught": "Entropy", "activity": "A gas confined to a corner and then filling the whole room",
     "check": "Guided practice: define entropy and explain it in terms of arrangements"},
    {"id": "10.8.2", "text": "State that the entropy of an isolated system can never decrease.",
     "simple": "System plus surroundings: the total entropy of the universe never falls.",
     "taught": "The entropy law", "activity": "Entropy of system and surroundings tracked separately",
     "check": "Guided practice: state the entropy law and apply it to a system and its surroundings"},
    {"id": "10.8.3", "text": "Describe qualitatively the increase of entropy in everyday life and its environmental consequences.",
     "simple": "Dissipation, mixing and pollution all raise entropy; so does resource depletion.",
     "taught": "Entropy in the world", "activity": "Everyday processes linked to the environmental issue they produce",
     "check": "Guided practice: describe the connection between entropy and environmental damage"},

    # ---- 10.9  Heat engines, Carnot and refrigerators -------------------
    {"id": "10.9.1", "text": "Describe the working of a heat engine and define its efficiency.",
     "simple": "Efficiency is the useful work divided by the heat taken in; the rest is rejected.",
     "taught": "Heat engines", "activity": "Block diagram with heat in, work out and heat rejected",
     "check": "Guided practice: describe a heat engine and calculate its efficiency"},
    {"id": "10.9.2", "text": "Describe the Carnot cycle and its four processes on a P-V diagram.",
     "simple": "Two isotherms joined by two adiabats, enclosing an area equal to the net work.",
     "taught": "The Carnot cycle", "activity": "The four legs plotted live and labelled as they are drawn",
     "check": "Guided practice: describe the four processes of the Carnot cycle"},
    {"id": "10.9.3", "text": "Derive the efficiency of a Carnot engine, eta = 1 - Tc/Th.",
     "simple": "Because Q_c / Q_h = T_c / T_h for a reversible cycle, eta = 1 - T_c / T_h.",
     "taught": "Carnot efficiency", "activity": "Derivation with the two adiabats cancelling between them",
     "check": "Guided practice: derive the Carnot efficiency and state its significance"},
    {"id": "10.9.4", "text": "Describe the working of a refrigerator and define its coefficient of performance.",
     "simple": "A refrigerator is a heat engine run backwards; COP = Q_c / W.",
     "taught": "Refrigerators", "activity": "Reversed block diagram compared with the heat engine",
     "check": "Guided practice: describe a refrigerator and calculate its coefficient of performance"},
]

STATIONS = [
    {"key": "overview", "label": "\U0001F5FA\uFE0F Your route & outcomes", "slos": []},
    {"key": "temperature", "label": "\uD83C\uDF21 Heat & temperature", "slos": ["10.1.1", "10.1.2", "10.1.3", "10.1.4", "10.1.5"]},
    {"key": "molecules", "label": "\uD83E\uDDEA The molecular model", "slos": ["10.2.1", "10.2.2", "10.2.3", "10.2.4"]},
    {"key": "gases", "label": "\uD83D\uDCA4 Gas laws & the ideal gas", "slos": ["10.3.1", "10.3.2", "10.3.3", "10.3.4"]},
    {"key": "speeds", "label": "\uD83C\uDFB3 Molecular speeds", "slos": ["10.4.1", "10.4.2", "10.4.3"]},
    {"key": "firstlaw", "label": "\u2696\uFE0F First law & work", "slos": ["10.5.1", "10.5.2", "10.5.3", "10.5.4", "10.5.5"]},
    {"key": "heatcap", "label": "\uD83C\uDF75 Specific heats", "slos": ["10.6.1", "10.6.2", "10.6.3", "10.6.4"]},
    {"key": "secondlaw", "label": "\u26D4 Reversibility & the second law", "slos": ["10.7.1", "10.7.2", "10.7.3"]},
    {"key": "entropy", "label": "\uD83C\uDF09 Entropy", "slos": ["10.8.1", "10.8.2", "10.8.3"]},
    {"key": "carnot", "label": "\uD83D\uDD25 Heat engines & Carnot", "slos": ["10.9.1", "10.9.2", "10.9.3", "10.9.4"]},
    {"key": "worked", "label": "\U0001F9EE Worked problems", "slos": []},
    {"key": "practice", "label": "\U0001F9E0 Practice", "slos": []},
    {"key": "tutor", "label": "\U0001F4E6 Atlas Tutor (offline AI)", "slos": []},
    {"key": "references", "label": "\U0001F4DA References", "slos": []},
]

BIG_IDEAS = [
    ("Pressure is not a property of a gas. It is a description of what its molecules are doing.",
     "Remove the molecules and there is no pressure. Add them and every impact on a wall is a "
     "momentum change, and the rate of those changes per unit area is the pressure. Every law "
     "in this chapter is a rearrangement of that one idea."),
    ("Work is an area, not a number.",
     "On a P-V diagram, the work done by a gas is the area under its path. That single picture "
     "explains why an isothermal expansion does work while an isochoric change does not, and "
     "why the path a gas takes changes the work but never the change in internal energy."),
    ("The second law is a rounding law.",
     "The first law says energy is conserved exactly. The second says some of it is spread too "
     "thinly to ever be gathered back. Nothing is destroyed; the quality is degraded."),
]

TAG = "CHAPTER 10 \u00B7 OPEN"
INTRO = (
    "Thirty-five outcomes and nine sections \u2014 the widest chapter in the book, and the one "
    "with the most algebra per idea. The apparatus disappears completely: after the first "
    "station there is nothing physical left but a box of molecules and a number. That is the "
    "point of the chapter. Pressure, the gas laws, molecular speed, internal energy, the "
    "efficiency of an engine and the existence of entropy are all the same picture seen from "
    "different angles."
)
ROUTE = ("Heat and temperature \u2192 The molecular model \u2192 Gas laws and the ideal gas \u2192 "
         "Molecular speeds \u2192 First law and work \u2192 Specific heats \u2192 Reversibility and "
         "the second law \u2192 Entropy \u2192 Heat engines and Carnot \u2192 Worked problems \u2192 "
         "Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("R = 8.314 exactly, by definition of the kelvin", "good"),
                 ("All curves computed from the formulas", "mute"),
                 ("Ideal gases only; real gases deviate", "warn")]

NOTES = [
    ("\u26A0 WATCH OUT", "Degrees Celsius will not work inside a gas law",
     "Charles's law in particular is simply false in Celsius. 1 \u00b0C is not twice as hot as "
     "0 \u00b0C \u2014 it is 274 K against 273 K. Every temperature in a gas formula must be in "
     "kelvin, and converting at the last minute is the commonest single error in this chapter."),
    ("\uD83C\uDFAF EXAM TIP", "Write the sign convention on the question paper, once",
     "dU = Q \u2212 W with W measured as work done **by** the gas. Some books use the opposite "
     "sign. Decide which one you are using, write it at the top of the page, and never think "
     "about it again. Marks are lost on sign conventions, not on physics."),
    ("\uD83D\uDD2E HONEST LIMIT", "Every gas here is ideal",
     "The ideal gas ignores the volume of the molecules themselves and every force between "
     "them. That is a very good approximation at ordinary pressures, and a poor one near "
     "absolute zero or at enormous pressure, where real gases condense. Nothing in this "
     "chapter models condensation."),
]


# --------------------------------------------------------------------------
# 10.1  Heat and temperature
# --------------------------------------------------------------------------

THERMOMETER_STEPS = [
    {"step": "1. A bulb of thin glass holds a liquid",
     "detail": "Mercury or coloured alcohol. A **liquid** is used because it expands far more "
               "than the glass around it."},
    {"step": "2. The liquid runs up a narrow capillary tube",
     "detail": "The tube is very thin so that a small change in volume lifts the column a long "
               "way, which makes the thermometer sensitive."},
    {"step": "3. The glass expands too \u2014 and it cancels most of the effect",
     "detail": "Between the ice point and the boiling point of water the liquid expands about "
               "100 times faster than the glass. The glass correction is real but small, and "
               "thermometers are calibrated to absorb it."},
    {"step": "4. The scale is marked at two fixed points",
     "detail": "0 \u00b0C at the ice point and 100 \u00b0C at the steam point, at standard "
               "atmospheric pressure. Everything between is interpolated."},
    {"step": "5. A constriction just above the bulb stops the mercury falling back",
     "detail": "This is what makes a **clinical** thermometer. Shake it down after use; an "
               "ordinary thermometer has no constriction because it must reset itself as the "
               "liquid cools."},
]

THERMOMETER_TYPES = [
    {"name": "Mercury-in-glass", "range": "\u221269 \u00b0C to 357 \u00b0C",
     "why": "Mercury does not wet glass, so the meniscus is clean and the column stays in the "
            "capillary instead of climbing the walls."},
    {"name": "Alcohol-in-glass", "range": "about \u221200 \u00b0C to 100 \u00b0C",
     "why": "Alcohol has a much lower freezing point than mercury, so it is the thermometer "
            "for cold weather \u2014 which is why most weather stations use one."},
    {"name": "Clinical", "range": "35 \u00b0C to 42 \u00b0C",
     "why": "One degree between 35 and 42 is a clinically important change, so the scale is "
            "expanded there and the constriction holds the reading."},
    {"name": "Resistance thermometer (platinum)", "range": "very wide",
     "why": "A platinum coil's **resistance** rises predictably with temperature. It is more "
            "accurate than liquid, survives industrial conditions, and is what most laboratory "
            "thermometers actually are."},
    {"name": "Thermocouple", "range": "\u2212250 \u00b0C to 1500 \u00b0C",
     "why": "Two dissimilar metals joined at a junction generate a small voltage. It responds "
            "fastly, which makes it the choice for furnaces, engines and rockets."},
]

EQUILIBRIUM_EXAMPLES = [
    {"situation": "A cold spoon in a cup of tea",
     "in_equilibrium": False,
     "reading": "The spoon starts cold, the tea starts hot.",
     "what_happens": "Heat flows from the tea into the spoon until the spoon reaches the same "
                     "temperature as the tea. Then neither changes."},
    {"situation": "Two thermometers left in the same beaker",
     "in_equilibrium": True,
     "reading": "They agree, and stay agreed.",
     "what_happens": "Two different bodies agreeing on a reading means that reading is a "
                     "property of the beaker, not of either thermometer. That is what makes it "
                     "worth writing down."},
    {"situation": "A room with a heater in one corner",
     "in_equilibrium": False,
     "reading": "The wall near the heater reads higher than the far wall.",
     "what_happens": "Eventually convection and conduction even the temperature out. Until "
                     "then, the room has no single temperature at all."},
    {"situation": "Tea and coffee, both allowed to stand",
     "in_equilibrium": False,
     "reading": "Both were poured at the same temperature.",
     "what_happens": "They reach room temperature at different times because they have "
                     "different masses, surface areas and evaporation rates \u2014 not because "
                     "one was hotter to begin with."},
]


# --------------------------------------------------------------------------
# 10.2  Kinetic molecular theory
# --------------------------------------------------------------------------

POSTULATE_LINKS = [
    {"postulate": "A gas is a very large number of tiny molecules whose own total volume is "
                  "negligible beside the container.",
     "consequence": "Makes P V independent of the size of the molecules themselves, which is "
                    "why argon and helium at the same P, V and T behave alike."},
    {"postulate": "The molecules move continuously and randomly in all directions.",
     "consequence": "Every impact on a wall is a momentum change, and the sum of those "
                    "changes per unit area per second is the pressure."},
    {"postulate": "All collisions between molecules, and with the walls, are perfectly elastic.",
     "consequence": "Collisions redistribute energy without dissipating it, which is why a gas "
                    "keeps the same temperature indefinitely in a perfectly insulated box."},
    {"postulate": "The time between collisions is negligible, so molecules travel in straight "
                  "lines between collisions.",
     "consequence": "Makes it legitimate to treat each molecule as moving along a straight line "
                    "between collisions, with the collisions themselves taking no time."},
    {"postulate": "The forces of attraction between molecules are negligible except at the "
                  "instant of collision.",
     "consequence": "Makes the path between collisions long, so a gas fills its container "
                    "uniformly instead of clumping in the corners."},
    {"postulate": "The average kinetic energy of the molecules depends only on the temperature.",
     "consequence": "This is the statement that connects temperature to energy, and the reason "
                    "two gases at one temperature have the same average kinetic energy however "
                    "different their masses."},
]

DERIVATION_KINETIC = [
    {"step": "1. Momentum change at one wall",
     "detail": "A molecule of mass m approaching the wall at speed v in the x direction "
               "rebounds to \u2212v, so its momentum changes by 2 m v."},
    {"step": "2. Force from all the molecules",
     "detail": "If N molecules each change their momentum by 2 m v twice in one second on a "
               "face of area A, the total force on that face is F = N m v\u00b2 / A."},
    {"step": "3. Pressure is force per unit area",
     "detail": "P = F / A = N m <v\u00b2> / (3 V). The 3 appears because the molecules are "
               "moving randomly in three dimensions, so only a third of them are moving in "
               "any one direction at any instant."},
    {"step": "4. The kinetic relation",
     "detail": "Rearranging gives **P V = (1/3) N m <v\u00b2>** \u2014 the equation the "
               "molecular picture produces."},
    {"step": "5. It is the ideal gas law in disguise",
     "detail": "With <v\u00b2> = 3 R T / M and N = n N_A, the right-hand side becomes "
               "(1/3) \u00d7 n N_A \u00d7 (M / N_A) \u00d7 3 R T / M = n R T. The molecular "
               "model and the ideal gas equation are the same statement."},
]

PRESSURE_FACTORS = [
    {"factor": "Number of molecules N",
     "effect": "Double N and the pressure doubles.",
     "why": "Twice as many impacts on each wall in the same time, each of the same size."},
    {"factor": "Temperature T",
     "effect": "Double T and the pressure doubles.",
     "why": "The molecules move faster, so each impact is bigger *and* they arrive more often."},
    {"factor": "Volume V",
     "effect": "Halve V and the pressure doubles.",
     "why": "The same molecules hit the same area twice as often."},
    {"factor": "Mass of a molecule m",
     "effect": "Heavier molecules at the same T give the same pressure.",
     "why": "They are slower, but they carry proportionally more momentum, and the two "
            "effects cancel exactly."},
    {"factor": "Nature of the gas",
     "effect": "No effect at all, ideally.",
     "why": "This is the deepest consequence of the model, and the reason a real gas is "
            "described as **ideal**."},
]


# --------------------------------------------------------------------------
# 10.3  Gas laws
# --------------------------------------------------------------------------

GAS_LAW_NOTES = [
    {"law": "Boyle's law", "condition": "Temperature constant", "relation": "P\u2081V\u2081 = P\u2082V\u2082",
     "graph": "P against V gives a family of rectangular hyperbolae; the steeper the curve, "
              "the colder the gas.",
     "note": "Doubling the volume halves the pressure. Going from V to 2V to 4V gives P, "
             "P/2, P/4 \u2014 the pressure does **not** halve again each time."},
    {"law": "Charles's law", "condition": "Pressure constant", "relation": "V\u2081/T\u2081 = V\u2082/T\u2082",
     "graph": "V against T is a straight line through the origin \u2014 but only on a "
              "**kelvin** axis.",
     "note": "On a Celsius axis the line intercepts at \u2212273.15 \u00b0C, which is absolute "
             "zero. That intercept is the experimental evidence for the kelvin scale."},
    {"law": "Gay-Lussac's law", "condition": "Volume constant", "relation": "P\u2081/T\u2081 = P\u2082/T\u2082",
     "graph": "P against T is a straight line through the origin on a kelvin axis.",
     "note": "The same intercept appears, measured a third way."},
    {"law": "Ideal gas equation", "condition": "Nothing held constant", "relation": "P V = n R T",
     "graph": "One equation containing every gas law as a special case.",
     "note": "Set n constant and you have PV = const; set P constant and you have Charles's "
             "law. Every gas-law problem in the examination is this one line rearranged."},
]

GAS_SOLVER_FIELDS = ["P (Pa)", "V (m\u00b3)", "n (mol)", "T (K)"]


# --------------------------------------------------------------------------
# 10.4  Molecular speeds
# --------------------------------------------------------------------------

SPEED_DEFINITIONS = [
    {"name": "Most probable speed v_mp",
     "formula": "sqrt(2 R T / M)",
     "meaning": "The speed at which the distribution peaks \u2014 the single speed the largest "
                "number of molecules actually have.",
     "where_on_curve": "Left of centre."},
    {"name": "Mean speed v_mean",
     "formula": "sqrt(8 R T / (pi M))",
     "meaning": "The ordinary arithmetic average of every molecule's speed.",
     "where_on_curve": "Slightly right of the peak."},
    {"name": "Root-mean-square speed v_rms",
     "formula": "sqrt(3 R T / M)",
     "meaning": "The square root of the mean square speed \u2014 equivalently, the speed a "
                "single molecule would have if all its energy were translational.",
     "where_on_curve": "Right of centre, always the largest of the three."},
]

SPEED_ORDERING = [
    {"fact": "v_mp < v_mean < v_rms, always",
     "why": "Speed is not an average of a molecule's energy. Taking the root of a mean square "
            "gives more weight to the few very fast molecules, so the order can only ever be "
            "this one."},
    {"fact": "The ratios do not depend on the gas or the temperature",
     "why": "The three formulas differ only in a constant, so once the 1, 2 and 3 are fixed the "
            "order is fixed too. At 300 K in nitrogen they sit at 493, 517 and 534 m s\u207b\u00b9."},
    {"fact": "At higher temperature the whole curve shifts right and flattens",
     "why": "Every speed scales as the square root of T, so a 4-fold rise in absolute "
            "temperature only doubles the speeds. This is why doubling the kelvin "
            "temperature is a mild change."},
    {"fact": "Lighter gases have faster molecules at the same T",
     "why": "Speed scales as 1/sqrt(M), so hydrogen at 300 K reaches about 2030 m s\u207b\u00b9 "
            "while carbon dioxide manages about 408 m s\u207b\u00b9."},
    {"fact": "A gas has no single speed at all",
     "why": "The curve is continuous. Any one molecule's speed changes at every collision, "
            "which is exactly why the average is the only thing that is worth calculating."},
]

ENERGY_NOTES = [
    {"statement": "Average translational energy per molecule = (3/2) k T",
     "detail": "k is the Boltzmann constant, 1.380649e\u221223 J K\u207b\u00b9. The molecule's "
               "mass is nowhere in this expression."},
    {"statement": "Average translational energy per mole = (3/2) R T",
     "detail": "Exactly the same statement multiplied by Avogadro's number."},
    {"statement": "The mass cancels out entirely",
     "detail": "A heavy molecule is slower but carries proportionally more momentum, so the "
               "two effects cancel. That is the whole content of the postulate."},
    {"statement": "It is only ever about the average",
     "detail": "Individual molecules have a spread of energies \u2014 the Boltzmann "
               "distribution. (3/2) k T is the mean of that spread, not any one molecule's "
               "value."},
    {"statement": "One degree of freedom always contributes (1/2) k T",
     "detail": "That single rule is what makes every formula in this chapter follow: a "
               "monatomic gas has f = 3, so (3/2) k T, and a diatomic gas at room temperature "
               "has f = 5, so (5/2) k T."},
]


# --------------------------------------------------------------------------
# 10.5  Internal energy, work and the first law
# --------------------------------------------------------------------------

WORK_NOTES = [
    {"process": "Isothermal", "dU": "0", "W": "nRT ln(V\u2082/V\u2081)",
     "Q": "nRT ln(V\u2082/V\u2081)",
     "picture": "A curve running down and to the right; the area under it is the work.",
     "insight": "Temperature fixed means internal energy fixed, so **every** joule of heat in "
                "comes straight back out as work."},
    {"process": "Adiabatic", "dU": "n C_v dT", "W": "\u2212dU",
     "Q": "0",
     "picture": "A steeper curve falling faster than an isotherm through the same point.",
     "insight": "Nothing is allowed in or out, so the gas pays for the work it does by cooling."},
    {"process": "Isobaric", "dU": "n C_v dT", "W": "P dV", "Q": "n C_p dT",
     "picture": "A horizontal line to the right.",
     "insight": "The gas pushes the piston out, so part of the heat supplied leaves as work."},
    {"process": "Isochoric", "dU": "n C_v dT", "W": "0", "Q": "n C_v dT",
     "picture": "A vertical line.",
     "insight": "A rigid container cannot expand, so every joule of heat goes into raising the "
                "temperature. This is why a sealed jar of air bursts in a fire."},
]

FIRST_LAW_PITFALLS = [
    {"mistake": "Using Q = W dU instead of dU = Q \u2212 W",
     "why_it_happens": "The signs are easy to lose track of once you are juggling three letters.",
     "fix": "Say it as a sentence: heat **in** either raises internal energy or is spent "
            "**out** as work. Subtract what leaves."},
    {"mistake": "Forgetting that dU is a state function",
     "why_it_happens": "It is tempting to treat the change in U as though it depended on the route.",
     "fix": "The change in U depends **only** on the two end points. The work done depends on "
            "the path; the change in U never does."},
    {"mistake": "Sign errors on compression",
     "why_it_happens": "It is natural to call a compression work 'done' without attaching a sign.",
     "fix": "With W measured as work by the gas, compression is negative. An isochoric process "
            "has W = 0 no matter how violently the gas is heated."},
    {"mistake": "Taking dU as non-zero in an isothermal process",
     "why_it_happens": "The gas clearly does work, so it 'must' be losing energy.",
     "fix": "For an ideal gas U depends on T alone. With T fixed, dU is exactly zero, and the "
            "work comes entirely from the heat supplied."},
]


# --------------------------------------------------------------------------
# 10.6  Heat capacities
# --------------------------------------------------------------------------

HEAT_CAP_NOTES = [
    {"quantity": "Specific heat capacity c",
     "definition": "Heat needed to raise **one kilogram** of a substance by one kelvin.",
     "formula": "c = Q / (m dT)", "units": "J kg\u207b\u00b9 K\u207b\u00b9",
     "note": "Celsius degrees have the same size as kelvin, so no conversion is needed here."},
    {"quantity": "Molar heat capacity C",
     "definition": "Heat needed to raise **one mole** of a substance by one kelvin.",
     "formula": "C = Q / (n dT)", "units": "J mol\u207b\u00b9 K\u207b\u00b9",
     "note": "C = M c, so the molar form is just the specific form multiplied by the molar "
             "mass in kg mol\u207b\u00b9."},
    {"quantity": "C_v",
     "definition": "Molar heat capacity at **constant volume**.",
     "formula": "C_v = (f/2) R", "units": "J mol\u207b\u00b9 K\u207b\u00b9",
     "note": "No work is done, so all the heat goes into raising the temperature."},
    {"quantity": "C_p",
     "definition": "Molar heat capacity at **constant pressure**.",
     "formula": "C_p = C_v + R = ((f+2)/2) R", "units": "J mol\u207b\u00b9 K\u207b\u00b9",
     "note": "Always the larger of the two, because the gas also has to pay for its expansion."},
    {"quantity": "gamma",
     "definition": "The ratio C_p / C_v.",
     "formula": "gamma = (f + 2) / f", "units": "dimensionless",
     "note": "1.667 monatomic, 1.400 diatomic, 1.333 polyatomic. It is the exponent in "
             "PV^gamma = constant on an adiabat."},
]

MAYS_NOTES = [
    {"step": "1", "text": "Heating one mole at constant pressure by dT needs C_p dT."},
    {"step": "2", "text": "Heating one mole at constant volume by the same dT needs C_v dT."},
    {"step": "3", "text": "The difference, (C_p \u2212 C_v) dT, has gone into the work done "
                         "as the gas expanded at constant pressure."},
    {"step": "4", "text": "For one mole at constant pressure, P dV = R dT by the ideal gas "
                         "law."},
    {"step": "5", "text": "So (C_p \u2212 C_v) dT = R dT, and therefore "
                         "**C_p \u2212 C_v = R**."},
]

DEGREES_OF_FREEDOM = [
    {"molecule": "Monatomic (He, Ne, Ar)", "f": 3, "cv_formula": "3R/2", "gamma": "5/3",
     "why": "Three translational directions and nothing else. No rotation is possible for a "
            "single atom."},
    {"molecule": "Diatomic (N\u2082, O\u2082, CO)", "f": 5, "cv_formula": "5R/2", "gamma": "7/5",
     "why": "Three translational plus two rotational degrees of freedom. The third rotation, "
            "about the bond axis, is blocked by the tiny moment of inertia of two atoms."},
    {"molecule": "Linear triatomic (CO\u2082)", "f": 5, "cv_formula": "5R/2", "gamma": "7/5",
     "why": "Still a line, so still only two rotations are available at ordinary temperatures."},
    {"molecule": "Non-linear polyatomic (H\u2082O vapour)", "f": 6, "cv_formula": "3R",
     "gamma": "4/3",
     "why": "Three translational plus **three** rotations, because a bent shape can be turned "
            "about any of three axes."},
    {"molecule": "Vibrations frozen out", "f": "+2 per mode",
     "gamma": "\u2014",
     "why": "Each vibrational mode adds a kinetic and a potential part, so 2 per mode \u2014 "
            "but only at high enough temperature to excite them, which is why C_v is not "
            "constant over an unlimited range."},
]


# --------------------------------------------------------------------------
# 10.7 and 10.8  Reversibility, the second law and entropy
# --------------------------------------------------------------------------

SECOND_LAW_STATEMENTS = [
    {"form": "Kelvin-Planck statement",
     "statement": "It is impossible for any device to take heat from a single reservoir and "
                  "convert it wholly into work.",
     "everyday": "You cannot warm your room by dragging a fridge through it and unplugging it. "
                 "That would turn one reservoir's heat entirely into work."},
    {"form": "Clausius statement",
     "statement": "It is impossible for heat to pass spontaneously from a colder body to a "
                  "hotter body.",
     "everyday": "Heat moves from hot to cold on its own, never the other way round, which is "
                 "exactly why a refrigerator needs a power supply."},
    {"form": "Entropy statement",
     "statement": "The entropy of an isolated system can never decrease.",
     "everyday": "Nothing ever tidies itself up without being told to. A shattered cup does "
                 "not reassemble."},
]

REVERSIBILITY_NOTES = [
    {"question": "What has to be true for a process to be reversible?",
     "answer": "It has to be free of friction, free of any finite temperature or pressure "
               "difference, and free of dissipation of any kind. Then an infinitesimal change "
               "can be undone exactly."},
    {"question": "Is a reversible process ever actually achieved?",
     "answer": "No. Not even the most careful experiment gets rid of every friction and every "
               "temperature difference. **Reversible is a limit that bounds every real "
               "process**, and it is a useful limit precisely because real machines approach it."},
    {"question": "Why does an ideal gas expand into a vacuum irreversibly?",
     "answer": "Nothing outside the gas changes, so there is no stored work with which to push "
               "the gas back. To restore the original volume you must do work from outside, "
               "and the gas will not return it."},
    {"question": "Why is a candle flame irreversible?",
     "answer": "It radiates heat into a room full of air. Re-collecting that heat from a room "
               "at 300 K and delivering it to a flame at 1200 K would need a refrigerator, "
               "which needs power from outside."},
]

ENTROPY_EXAMPLES = [
    {"process": "Gas expanding into a vacuum",
     "dS": "increases", "why": "The gas has access to a far larger volume, so vastly more "
                               "arrangements are available to it."},
    {"process": "Ice melting in a warm room",
     "dS": "increases overall", "why": "The ice loses entropy, but the room gains more as it "
                                      "gives up heat. The total never falls."},
    {"process": "A hot cup of tea cooling",
     "dS": "increases", "why": "The tea loses entropy, the room gains more. Spontaneous "
                               "transfer is always net positive."},
    {"process": "A gas expanding reversibly at constant temperature",
     "dS": "increases", "why": "A reversible isothermal expansion of an ideal gas increases "
                               "its entropy by n R ln(V\u2082/V\u2081) even though dU is zero."},
    {"process": "Two gases mixing irreversibly",
     "dS": "increases", "why": "Each gas now has the whole container available to it. They "
                               "will not separate again on their own."},
    {"process": "Water freezing at 0 \u00b0C",
     "dS": "decreases locally, increases overall", "why": "This is not a violation. The heat "
                                                       "removed from the water goes into the "
                                                       "surroundings, which gains more entropy "
                                                       "than the water loses."},
    {"process": "A well-organised desk becoming untidy",
     "dS": "increases", "why": "The number of arrangements consistent with 'untidy' vastly "
                               "outnumbers those consistent with 'tidy'."},
]


# --------------------------------------------------------------------------
# Worked problems
# --------------------------------------------------------------------------

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "Temperature conversions, the ones that catch people",
     "level": "Foundation", "slos": ["10.1.4"],
     "question": "Convert \u221240 \u00b0C and 25 \u00b0C to kelvin, and \u2212196 \u00b0F to "
                 "kelvin.",
     "known": ["t = \u221240 \u00b0C", "t = 25 \u00b0C", "t = \u2212196 \u00b0F"],
     "find": "Three temperatures in kelvin",
     "equation": r"T = t + 273.15 \qquad T = \frac{t_F - 32}{1.8} + 273.15",
     "conversions": ["Fahrenheit to Celsius: t = (t_F \u2212 32) / 1.8. Then add 273.15. Or go "
                     "straight to kelvin with T = (t_F \u2212 32)/1.8 + 273.15."],
     "substitution": r"T_1 = -40 + 273.15, \quad T_2 = 25 + 273.15, \quad T_3 = \frac{-196-32}{1.8} + 273.15",
     "calculation": [
         "Step 1 \u2014 \u221240 \u00b0C: T = \u221240 + 273.15 = **233.15 K**.",
         "Step 2 \u2014 25 \u00b0C: T = 25 + 273.15 = **298.15 K**.",
         "Step 3 \u2014 \u2212196 \u00b0F: first to Celsius, (\u2212196 \u2212 32)/1.8 = "
         "\u2212126.67 \u00b0C, then T = \u2212126.67 + 273.15 = **146.48 K**.",
         "Step 4 \u2014 a check worth doing: \u221240 \u00b0C and \u221240 \u00b0F are the same "
         "temperature, and both give 233.15 K. If your Fahrenheit conversion does not give that, "
         "it is wrong.",
     ],
     "unit_check": r"[\text{temperature}] = [\text{temperature}]",
     "answer": r"T_1 = 233.15\ \mathrm{K},\quad T_2 = 298.15\ \mathrm{K},\quad T_3 = 146.48\ \mathrm{K}",
     "sig_fig_note": "Five figures here because 273.15 is exact \u2014 it is now part of the "
                     "definition of the kelvin. Any answer quoted to three figures is fine in "
                     "the examination.",
     "assumptions": ["273.15 is exact by the SI definition, so it carries unlimited "
                     "significant figures."]},

    {"id": "WP2", "title": "Boyle's law with a syringe",
     "level": "Foundation", "slos": ["10.3.1", "10.3.4"],
     "question": "A gas in a syringe is at 1.00 \u00d7 10\u2075 Pa in a volume of "
                 "20.0 cm\u00b3. The plunger is pushed until the volume is 5.00 cm\u00b3, at "
                 "the same temperature. Find the new pressure.",
     "known": ["P\u2081 = 1.00 \u00d7 10\u2075 Pa", "V\u2081 = 20.0 cm\u00b3",
               "V\u2082 = 5.00 cm\u00b3", "temperature constant"],
     "find": "P\u2082",
     "equation": r"P_1 V_1 = P_2 V_2",
     "conversions": ["The volume units cancel in P\u2081V\u2081 = P\u2082V\u2082, so they may be "
                     "left in cm\u00b3 \u2014 which is worth noticing."],
     "substitution": r"P_2 = \frac{P_1 V_1}{V_2} = \frac{(1.00 \times 10^5)(20.0)}{5.00}",
     "calculation": [
         "Step 1 \u2014 is anything else changing? The temperature is stated as constant, so "
         "this is Boyle's law and nothing else.",
         "Step 2 \u2014 rearrange for the unknown: P\u2082 = P\u2081V\u2081/V\u2082.",
         "Step 3 \u2014 substitute: P\u2082 = (1.00 \u00d7 10\u2075 \u00d7 20.0)/5.00 = "
         "**4.00 \u00d7 10\u2075 Pa**.",
         "Step 4 \u2014 sanity check: the volume fell to a quarter, so the pressure must rise "
         "to four times. It did. A quick ratio check like this catches most slips.",
     ],
     "unit_check": r"P = \frac{\mathrm{Pa\,m^3}}{\mathrm{m^3}} = \mathrm{Pa}",
     "answer": r"P_2 = 4.00 \times 10^5\ \mathrm{Pa}",
     "sig_fig_note": "Three figures throughout.",
     "assumptions": ["The gas stays at constant temperature, so no heat is exchanged fast "
                     "enough to matter.",
                     "The gas is ideal at this pressure."]},

    {"id": "WP3", "title": "Charles's law and the Celsius trap",
     "level": "Foundation", "slos": ["10.3.2", "10.3.4"],
     "question": "A gas at constant pressure occupies 1.00 dm\u00b3 at 17 \u00b0C. Find its "
                 "volume at 47 \u00b0C.",
     "known": ["V\u2081 = 1.00 dm\u00b3", "t\u2081 = 17 \u00b0C", "t\u2082 = 47 \u00b0C",
               "pressure constant"],
     "find": "V\u2082",
     "equation": r"\frac{V_1}{T_1} = \frac{V_2}{T_2}",
     "conversions": ["**Both temperatures must be in kelvin.** T\u2081 = 17 + 273.15 = "
                     "290.15 K; T\u2082 = 47 + 273.15 = 320.15 K."],
     "substitution": r"V_2 = \frac{V_1 T_2}{T_1} = \frac{(1.00)(320.15)}{290.15}",
     "calculation": [
         "Step 1 \u2014 convert first. This is the whole problem.",
         "Step 2 \u2014 rearrange for V\u2082: V\u2082 = V\u2081 T\u2082/T\u2081.",
         "Step 3 \u2014 substitute: V\u2082 = 1.00 \u00d7 320.15/290.15 = **1.103 dm\u00b3**.",
         "Step 4 \u2014 what the wrong answer looks like: using Celsius directly gives "
         "1.00 \u00d7 47/17 = 2.76 dm\u00b3, a 30 cm\u00b3 rise. Physically absurd \u2014 heating "
         "by 30 \u00b0C cannot nearly triple the volume. The Celsius answer is always recognisable "
         "because it is wildly too big.",
     ],
     "unit_check": r"V = \mathrm{dm^3}, unchanged throughout",
     "answer": r"V_2 = 1.103\ \mathrm{dm^3}",
     "sig_fig_note": "Three figures, set by V\u2081 and the temperatures.",
     "assumptions": ["Constant pressure, so the container must be free to expand \u2014 a "
                     "sealed rigid vessel would give a different answer.",
                     "The gas is ideal over this range."]},

    {"id": "WP4", "title": "The ideal gas equation",
     "level": "Foundation", "slos": ["10.3.3", "10.3.4"],
     "question": "A 2.00 mol sample of an ideal gas occupies 0.0500 m\u00b3 at 27 \u00b0C. "
                 "Find its pressure.",
     "known": ["n = 2.00 mol", "V = 0.0500 m\u00b3", "t = 27 \u00b0C"],
     "find": "P",
     "equation": r"PV = nRT",
     "conversions": ["T = 27 + 273.15 = 300.15 K. R = 8.314 J mol\u207b\u00b9 K\u207b\u00b9."],
     "substitution": r"P = \frac{nRT}{V} = \frac{(2.00)(8.314)(300.15)}{0.0500}",
     "calculation": [
         "Step 1 \u2014 kelvin, always. T = 300.15 K.",
         "Step 2 \u2014 rearrange PV = nRT for P: P = nRT/V.",
         "Step 3 \u2014 substitute: P = 2.00 \u00d7 8.314 \u00d7 300.15 / 0.0500 = "
         "**9.98 \u00d7 10\u2074 Pa**.",
         "Step 4 \u2014 sense check: 2 moles in 50 litres is a gas at about one atmosphere and "
         "a bit, so roughly 10\u2075 Pa. Correct.",
     ],
     "unit_check": r"P = \frac{\mathrm{mol \times J\,mol^{-1}K^{-1} \times K}}{\mathrm{m^3}} = \mathrm{J\,m^{-3}} = \mathrm{Pa}",
     "answer": r"P = 9.98 \times 10^4\ \mathrm{Pa}",
     "sig_fig_note": "Three figures.",
     "assumptions": ["The gas is ideal.",
                     "No dissociation or reaction changes the number of moles."]},

    {"id": "WP5", "title": "rms speed, and why the mass cancels",
     "level": "Developing", "slos": ["10.4.1", "10.4.2", "10.2.4"],
     "question": "Find the rms speed of nitrogen molecules (M = 0.0280 kg mol\u207b\u00b9) at "
                 "300 K, and the average translational energy of one molecule.",
     "known": ["T = 300 K", "M = 0.0280 kg mol\u207b\u00b9", "k = 1.380649 \u00d7 10\u207b\u00b2\u00b3 J K\u207b\u00b9"],
     "find": "v_rms, and the average energy per molecule",
     "equation": r"v_{rms} = \sqrt{\frac{3RT}{M}} \qquad E = \frac{3}{2} k T",
     "conversions": ["M must be in **kg mol\u207b\u00b9**, not g mol\u207b\u00b9. Using 0.0280 g "
                     "mol\u207b\u00b9 gives a speed 1000 times too large."],
     "substitution": r"v_{rms} = \sqrt{\frac{3 \times 8.314 \times 300}{0.0280}}, \qquad E = 1.5 \times 1.380649 \times 10^{-23} \times 300",
     "calculation": [
         "Step 1 \u2014 check the molar mass unit. Nitrogen is 28 g mol\u207b\u00b9 = **0.0280 "
         "kg mol\u207b\u00b9**.",
         "Step 2 \u2014 v_rms = sqrt(3 \u00d7 8.314 \u00d7 300 / 0.0280) = sqrt(2.672 \u00d7 "
         "10\u2075) = **517 m s\u207b\u00b9**.",
         "Step 3 \u2014 the energy: E = 1.5 \u00d7 1.380649 \u00d7 10\u207b\u00b2\u00b3 \u00d7 300 = "
         "**6.21 \u00d7 10\u207b\u00b2\u00b1 J**.",
         "Step 4 \u2014 notice what happened in step 3: the mass of a nitrogen molecule never "
         "appeared. That is the postulate \u2014 average kinetic energy depends on temperature "
         "alone.",
     ],
     "unit_check": r"v = \sqrt{\frac{\mathrm{J\,mol^{-1}K^{-1} \times K}}{\mathrm{kg\,mol^{-1}}}} = \sqrt{\mathrm{m^2\,s^{-2}}} = \mathrm{m\,s^{-1}}",
     "answer": r"v_{rms} = 517\ \mathrm{m\,s^{-1}}, \qquad E = 6.21 \times 10^{-21}\ \mathrm{J}",
     "sig_fig_note": "Three figures.",
     "assumptions": ["The gas is ideal and rotationally frozen out is irrelevant here \u2014 "
                     "v_rms as defined uses translational energy only.",
                     "T = 300 K exactly for the purpose of the calculation."]},

    {"id": "WP6", "title": "The first law on an isothermal expansion",
     "level": "Developing", "slos": ["10.5.3", "10.5.4", "10.5.5"],
     "question": "5.00 mol of an ideal monatomic gas expand isothermally at 300 K from "
                 "0.0100 m\u00b3 to 0.0500 m\u00b3. Find the heat supplied and the work done.",
     "known": ["n = 5.00 mol", "T = 300 K", "V\u2081 = 0.0100 m\u00b3",
               "V\u2082 = 0.0500 m\u00b3", "monatomic"],
     "find": "Q and W",
     "equation": r"W = nRT \ln\frac{V_2}{V_1} \qquad \Delta U = 0 \qquad \Delta U = Q - W",
     "conversions": ["The logarithm argument V\u2082/V\u2081 = 5.00 must be **dimensionless**, "
                     "which it is, because it is a ratio of like units."],
     "substitution": r"W = (5.00)(8.314)(300)\ln 5.00",
     "calculation": [
         "Step 1 \u2014 isothermal, so dU = 0 exactly. That is the defining property of an "
         "ideal gas: U depends on T and nothing else.",
         "Step 2 \u2014 work is not a rectangle here, because the pressure falls as the gas "
         "expands. So W = nRT ln(V\u2082/V\u2081) = 5.00 \u00d7 8.314 \u00d7 300 \u00d7 ln 5.00 = "
         "12471 \u00d7 1.6094 = **2.01 \u00d7 10\u2074 J**.",
         "Step 3 \u2014 the first law: 0 = Q \u2212 W, so Q = W = **2.01 \u00d7 10\u2074 J**.",
         "Step 4 \u2014 the point of the problem: the gas did 2.01 kJ of work, but its internal "
         "energy did not change by a single joule. Every joule of that work was paid for out of "
         "the heat supplied.",
     ],
     "unit_check": r"W = \mathrm{mol \times J\,mol^{-1}K^{-1} \times K \times (\text{dimensionless})} = \mathrm{J}",
     "answer": r"W = Q = 2.01 \times 10^4\ \mathrm{J}, \qquad \Delta U = 0",
     "sig_fig_note": "Three figures. Note ln 5.00 = 1.609.",
     "assumptions": ["The expansion is slow enough to be reversible, so the isothermal formula "
                     "for W applies.",
                     "The gas is ideal.",
                     "Work is taken as done **by** the gas, positive."]},

    {"id": "WP7", "title": "Heating at constant volume",
     "level": "Developing", "slos": ["10.5.4", "10.5.5"],
     "question": "2.00 mol of a diatomic ideal gas at constant volume absorbs 5.00 \u00d7 10\u00b3 J "
                 "of heat. Find its temperature change.",
     "known": ["n = 2.00 mol", "Q = 5.00 \u00d7 10\u00b3 J", "diatomic (f = 5)",
               "constant volume"],
     "find": "dT",
     "equation": r"Q = n C_v \Delta T \qquad C_v = \frac{f}{2}R = \frac{5}{2}R",
     "conversions": ["No kelvin conversion is needed: a temperature **difference** is the same "
                     "size in Celsius and kelvin."],
     "substitution": r"\Delta T = \frac{Q}{n C_v} = \frac{5.00 \times 10^3}{(2.00)(5 \times 8.314 / 2)}",
     "calculation": [
         "Step 1 \u2014 constant volume means the container is rigid, so **W = 0** and "
         "dU = Q.",
         "Step 2 \u2014 C_v for a diatomic gas: (5/2)(8.314) = 20.79 J mol\u207b\u00b9 K\u207b\u00b9.",
         "Step 3 \u2014 dT = Q / (n C_v) = 5000 / (2.00 \u00d7 20.79) = **120 K**.",
         "Step 4 \u2014 why the gas type mattered: if this had been monatomic, C_v = 12.47 and "
         "dT would have been 200 K. The degrees of freedom are the whole difference.",
     ],
     "unit_check": r"\Delta T = \frac{\mathrm{J}}{\mathrm{mol \times J\,mol^{-1}K^{-1}}} = \mathrm{K}",
     "answer": r"\Delta T = 120\ \mathrm{K}",
     "sig_fig_note": "Three figures.",
     "assumptions": ["The vessel is rigid, so no work is done.",
                     "The gas stays in the diatomic regime, so vibrations are still frozen out.",
                     "No energy leaves through the walls."]},

    {"id": "WP8", "title": "Carnot efficiency",
     "level": "Challenge", "slos": ["10.9.1", "10.9.3", "10.9.4"],
     "question": "A Carnot engine takes in heat at 500 K and rejects it at 300 K. Find its "
                 "efficiency, and the coefficient of performance of a refrigerator working "
                 "between the same two reservoirs.",
     "known": ["T_h = 500 K", "T_c = 300 K"],
     "find": "eta and COP",
     "equation": r"\eta = 1 - \frac{T_c}{T_h} \qquad \mathrm{COP} = \frac{T_c}{T_h - T_c}",
     "conversions": ["Both temperatures must be in kelvin. 500 K = 227 \u00b0C and 300 K = "
                     "27 \u00b0C, so the Celsius values are not interchangeable here."],
     "substitution": r"\eta = 1 - \frac{300}{500} \qquad \mathrm{COP} = \frac{300}{500 - 300}",
     "calculation": [
         "Step 1 \u2014 efficiency: eta = 1 \u2212 300/500 = 1 \u2212 0.6 = **0.40**, or 40 %.",
         "Step 2 \u2014 the waste: 60 % of the heat taken in has to be dumped into the cold "
         "reservoir. No engine can improve on that.",
         "Step 3 \u2014 COP: 300/(500 \u2212 300) = 300/200 = **1.5**.",
         "Step 4 \u2014 read that number carefully. A coefficient of performance of 1.5 means "
         "it removes 1.5 J of heat from the cold space for **every joule of electricity** "
         "supplied. It is not an efficiency and must never exceed 1 in that sense \u2014 heat is "
         "being moved, not created.",
     ],
     "unit_check": r"\eta = \frac{\mathrm{K}}{\mathrm{K}} = 1 \quad (\text{dimensionless})",
     "answer": r"\eta = 0.40 \ (40\,\%), \qquad \mathrm{COP} = 1.5",
     "sig_fig_note": "Efficiency to two figures is plenty; COP to two.",
     "assumptions": ["Both machines are **Carnot**, i.e. perfectly reversible. A real engine "
                     "would be worse than 40 %, and a real refrigerator worse than a COP of 1.5.",
                     "The reservoirs are the only heat exchanges, so nothing is lost to the "
                     "surroundings."]},
]


# --------------------------------------------------------------------------
# Practice questions
# --------------------------------------------------------------------------

PRACTICE_QUESTIONS = [
    # ---- 10.1 Heat and temperature --------------------------------------
    {"id": "P1", "category": "Temperature", "type": "mcq", "slo": "10.1.1",
     "prompt": "Two gases are at the same temperature. The molecules of one are heavier and "
               "slower. The average kinetic energy of the molecules...",
     "options": ["is greater for the heavier gas", "is the same for both gases",
                 "is greater for the lighter gas", "cannot be compared without the masses"],
     "answer": 1,
     "hint": "Write (1/2) m v\u00b2 = (3/2) k T and ask what happens when m goes up.",
     "explanation": "The same. A heavier molecule is slower, but its mass compensates exactly, "
                    "so <v\u00b2> falls as 1/m and the product stays at (3/2) k T. That is the "
                    "deepest single result of kinetic molecular theory."},
    {"id": "P2", "category": "Heat", "type": "mcq", "slo": "10.1.2",
     "prompt": "Which statement about heat is correct?",
     "options": ["Heat is a substance contained in every body",
                 "Heat is the energy transferred because of a temperature difference",
                 "Heat flows from cold to hot on its own",
                 "A body contains a fixed amount of heat until it is used up"],
     "answer": 1,
     "hint": "Consider what is actually moving when a spoon warms.",
     "explanation": "Heat is energy **in transit**, not a substance stored in a body. A hot "
                    "body contains internal energy; it does not contain heat until some of it "
                    "moves somewhere else."},
    {"id": "P3", "category": "Thermal equilibrium", "type": "mcq", "slo": "10.1.3",
     "prompt": "Body A is in thermal equilibrium with B, and B is in thermal equilibrium with "
               "C. Then...",
     "options": ["A and C may still be at different temperatures",
                 "A and C must be at the same temperature",
                 "nothing can be concluded without knowing the heat capacities",
                 "A and C are in thermal equilibrium only if they are touching"],
     "answer": 1,
     "hint": "This is exactly what the zeroth law asserts.",
     "explanation": "A = B and B = C, so A = C. The zeroth law is what makes a thermometer "
                    "worth having: it lets you measure one unknown body by comparison with two "
                    "others."},
    {"id": "P4", "category": "Temperature", "type": "numeric", "slo": "10.1.4",
     "prompt": "Convert 85 \u00b0C to kelvin. Enter the number only.",
     "answer": 358.15, "tolerance": 0.5, "unit": "K",
     "hint": "Add 273.15. For a difference between temperatures, no conversion is needed.",
     "explanation": "T = 85 + 273.15 = 358.15 K. Use kelvin in every gas formula."},
    {"id": "P5", "category": "Temperature", "type": "numeric", "slo": "10.1.4",
     "prompt": "What temperature in kelvin corresponds to absolute zero on the Celsius scale? "
               "Enter the number only.",
     "answer": 0.0, "tolerance": 0.05, "unit": "K",
     "hint": "Absolute zero is \u2212273.15 \u00b0C.",
     "explanation": "T = \u2212273.15 + 273.15 = 0 K. Absolute zero is the floor of the scale, "
                    "which is exactly why it is called the absolute scale."},
    {"id": "P6", "category": "Temperature", "type": "mcq", "slo": "10.1.4",
     "prompt": "A temperature difference of 5 \u00b0C is equivalent to...",
     "options": ["5 K", "278.15 K", "5 \u00b0F", "268.15 K"],
     "answer": 0,
     "hint": "A difference of two Celsius readings cancels the 273.15.",
     "explanation": "5 K. Temperature **differences** are identical in Celsius and kelvin, which "
                    "is why dT needs no conversion even though T always does."},
    {"id": "P7", "category": "Thermometers", "type": "mcq", "slo": "10.1.5",
     "prompt": "The constriction just above the bulb of a clinical thermometer serves to...",
     "options": ["make the mercury expand more quickly",
                 "prevent the mercury falling back so the reading is retained",
                 "calibrate the thermometer at the ice point",
                 "allow the thermometer to be used at high temperatures"],
     "answer": 1,
     "hint": "It is a deliberate narrow point in the tube.",
     "explanation": "It traps the column. Without it, the mercury would drop back to the bulb "
                    "as the thermometer cooled and the reading would vanish before it could be "
                    "taken."},

    # ---- 10.2 Kinetic molecular theory ---------------------------------
    {"id": "P8", "category": "Kinetic theory", "type": "mcq", "slo": "10.2.1",
     "prompt": "Which of these is **not** an assumption of kinetic molecular theory?",
     "options": ["Collisions are perfectly elastic",
                 "Molecular forces of attraction are negligible",
                 "All molecules of a gas travel at the same speed",
                 "The molecules are in constant random motion"],
     "answer": 2,
     "hint": "Only one of these would make the model far too simple.",
     "explanation": "Molecules have a whole **distribution** of speeds, not one speed. "
                    "Assuming a single speed would kill thermal energy and make the model "
                    "useless."},
    {"id": "P9", "category": "Pressure", "type": "mcq", "slo": "10.2.2",
     "prompt": "The pressure of a gas is best described as...",
     "options": ["a force the gas exerts on its container",
                 "the rate of change of momentum of the molecules striking unit area of the "
                 "container walls",
                 "the weight of the gas divided by the floor area",
                 "the total kinetic energy of the molecules"],
     "answer": 1,
     "hint": "Each collision changes a molecule's momentum. Add them all up per unit area.",
     "explanation": "It is the rate of momentum transfer to the walls per unit area. "
                    "Attributed to a gas it is simply a force on the container; the molecular "
                    "description is what explains it."},
    {"id": "P10", "category": "Pressure", "type": "mcq", "slo": "10.2.2",
     "prompt": "A gas is cooled at constant volume in a rigid container. The pressure...",
     "options": ["increases, because the molecules get smaller",
                 "stays the same, because the walls do not move",
                 "decreases, because the molecules move more slowly",
                 "decreases, because the molecules collide less often"],
     "answer": 2,
     "hint": "At constant V and N, P is proportional to T.",
     "explanation": "It decreases. Slower molecules mean smaller momentum changes **and** fewer "
                    "of them per second; both effects lower the pressure. The same gas at "
                    "constant volume follows P \u221d T."},
    {"id": "P11", "category": "Kinetic theory", "type": "numeric", "slo": "10.2.3",
     "prompt": "Calculate P V from the molecular model for 2.00 \u00d7 10\u00b2\u00b3 molecules "
               "of mass 4.65 \u00d7 10\u207b\u00b2\u2076 kg with mean square speed 4.00 \u00d7 "
               "10\u00b3 m\u00b2 s\u207b\u00b2. Use P V = (1/3) N m <v\u00b2> and enter the "
               "number only.",
     "answer": 12.4, "tolerance": 0.05, "unit": "J",
     "hint": "Multiply the three numbers together, then divide by 3.",
     "explanation": "PV = (1/3)(2.00 \u00d7 10\u00b2\u00b3)(4.65 \u00d7 10\u207b\u00b2\u2076)(4.00 \u00d7 "
                    "10\u00b3) = (1/3)(37.2) = **12.4 J**. "
                    "Watch the powers: 23 - 26 + 3 = 0, so the product is "
                    "of order unity. P V is an energy, so joules are the right units."},
    {"id": "P12", "category": "Kinetic theory", "type": "mcq", "slo": "10.2.4",
     "prompt": "The average kinetic energy of molecules depends on...",
     "options": ["the identity of the gas and the temperature",
                 "the temperature alone", "the volume of the container",
                 "the pressure and the temperature"],
     "answer": 1,
     "hint": "Write (1/2) m <v\u00b2> = (3/2) k T and look for the mass.",
     "explanation": "Temperature alone. The m cancels out of the relation entirely, which is "
                    "why every gas at 300 K has the same mean molecular energy."},

    # ---- 10.3 Gas laws --------------------------------------------------
    {"id": "P13", "category": "Boyle's law", "type": "numeric", "slo": "10.3.1",
     "prompt": "A gas at 2.00 \u00d7 10\u2075 Pa occupies 4.00 \u00d7 10\u207b\u00b3 m\u00b3. It is "
               "compressed at constant temperature until the pressure is "
               "8.00 \u00d7 10\u2075 Pa. Find the new volume. Enter the number only.",
     "answer": 1.0e-3, "tolerance": 0.05e-3, "unit": "m\u00b3",
     "hint": "P\u2081V\u2081 = P\u2082V\u2082. Notice the pressure quadruples.",
     "explanation": "V\u2082 = (2.00 \u00d7 10\u2075 \u00d7 4.00 \u00d7 10\u207b\u00b3)/(8.00 \u00d7 10\u2075) = "
                    "1.00 \u00d7 10\u207b\u00b3 m\u00b3. The volume falls to a quarter."},
    {"id": "P14", "category": "Charles's law", "type": "numeric", "slo": "10.3.2",
     "prompt": "A gas at constant pressure occupies 2.00 \u00d7 10\u207b\u00b3 m\u00b3 at 27 \u00b0C. "
               "Find its volume at 127 \u00b0C. Enter the number only.",
     "answer": 2.667e-3, "tolerance": 0.02e-3, "unit": "m\u00b3",
     "hint": "Convert both to kelvin first: 300 K and 400 K.",
     "explanation": "V\u2082 = 2.00 \u00d7 10\u207b\u00b3 \u00d7 400/300 = 2.67 \u00d7 10\u207b\u00b3 m\u00b3. "
                    "Using Celsius would give a wildly wrong answer."},
    {"id": "P15", "category": "Gas laws", "type": "mcq", "slo": "10.3.2",
     "prompt": "A graph of volume against temperature for a gas at constant pressure is a "
               "straight line that does not pass through the origin on a Celsius axis. The "
               "temperature axis intercept represents...",
     "options": ["the melting point of the gas",
                 "absolute zero", "zero degrees Celsius", "the boiling point of the gas"],
     "answer": 1,
     "hint": "Extrapolate the straight line backwards to zero volume.",
     "explanation": "Absolute zero, at \u2212273.15 \u00b0C. A gas cannot have zero volume, so the "
                    "line is extrapolated past the lowest real temperature; that intercept is "
                    "the experimental case for the kelvin scale."},
    {"id": "P16", "category": "Ideal gas equation", "type": "numeric", "slo": "10.3.3",
     "prompt": "Find the temperature of 0.500 mol of an ideal gas occupying "
               "4.00 \u00d7 10\u207b\u00b3 m\u00b3 at a pressure of 1.04 \u00d7 10\u2075 Pa. Enter "
               "the number only.",
     "answer": 100.1, "tolerance": 0.3, "unit": "K",
     "hint": "T = PV / (nR).",
     "explanation": "T = (1.04 \u00d7 10\u2075 \u00d7 4.00 \u00d7 10\u207b\u00b3)/(0.500 \u00d7 8.314) = "
                    "416/4.157 = **100.1 K**. The answer comes out in kelvin, which is "
                    "itself a useful check: if it lands near 27, or near 1, a power of "
                    "ten has gone astray."},
    {"id": "P17", "category": "Ideal gas equation", "type": "mcq", "slo": "10.3.3",
     "prompt": "One mole of any ideal gas at the same temperature and pressure occupies the "
               "same volume. This follows from...",
     "options": ["Avogadro's law", "Boyle's law", "Charles's law", "Mayer's relation"],
     "answer": 0,
     "hint": "PV = nRT rearranged with n and T fixed.",
     "explanation": "Avogadro's law: V \u221d n at constant P and T. It is the direct "
                    "consequence of the ideal gas equation and it is why the mole is such a "
                    "useful unit."},
    {"id": "P18", "category": "Gas laws", "type": "numeric", "slo": "10.3.4",
     "prompt": "A balloon holds 2.00 mol of gas at 300 K and 1.00 \u00d7 10\u2075 Pa. What "
               "pressure does it reach if it is sealed and then cooled to 150 K at constant "
               "volume? Enter the number only.",
     "answer": 5.0e4, "tolerance": 0.2e4, "unit": "Pa",
     "hint": "At constant V and n, P \u221d T. Both temperatures are already in kelvin.",
     "explanation": "P\u2082 = P\u2081 T\u2082/T\u2081 = 1.00 \u00d7 10\u2075 \u00d7 150/300 = "
                    "5.00 \u00d7 10\u2074 Pa. Halving the kelvin temperature halves the pressure."},

    # ---- 10.4 Molecular speeds ------------------------------------------
    {"id": "P19", "category": "Molecular speeds", "type": "numeric", "slo": "10.4.1",
     "prompt": "Find the rms speed of oxygen molecules (M = 0.0320 kg mol\u207b\u00b9) at "
               "300 K. Enter the number only.",
     "answer": 484.0, "tolerance": 3.0, "unit": "m s\u207b\u00b9",
     "hint": "v_rms = sqrt(3RT/M), with M in kg mol\u207b\u00b9.",
     "explanation": "v_rms = sqrt(3 \u00d7 8.314 \u00d7 300 / 0.0320) = sqrt(2.338 \u00d7 10\u2075) = "
                    "**484 m s\u207b\u00b9**. Oxygen is heavier than nitrogen (0.0320 against "
                    "0.0280 kg mol\u207b\u00b9), so its molecules are slower \u2014 484 against "
                    "517 m s\u207b\u00b9 \u2014 exactly as v \u221d 1/sqrt(M) requires."},
    {"id": "P20", "category": "Molecular speeds", "type": "mcq", "slo": "10.4.3",
     "prompt": "The correct order of the characteristic speeds of gas molecules is...",
     "options": ["v_rms < v_mean < v_mp", "v_mp < v_mean < v_rms",
                 "v_mean < v_mp < v_rms", "v_mp < v_rms < v_mean"],
     "answer": 1,
     "hint": "The root of a mean square gives extra weight to the fast molecules.",
     "explanation": "v_mp < v_mean < v_rms, always, for any gas at any temperature. The ratios "
                    "depend only on the constants 1, 8/\u03c0 and 3."},
    {"id": "P21", "category": "Molecular speeds", "type": "numeric", "slo": "10.4.2",
     "prompt": "Find the average translational energy of one molecule of an ideal gas at "
               "300 K. Use E = 1.5 k T with k = 1.380649 \u00d7 10\u207b\u00b2\u00b3 J K\u207b\u00b9. "
               "Enter the number only.",
     "answer": 6.213e-21, "tolerance": 0.05e-21, "unit": "J",
     "hint": "Multiply 1.5 by k and then by T.",
     "explanation": "E = 1.5 \u00d7 1.380649 \u00d7 10\u207b\u00b2\u00b3 \u00d7 300 = 6.21 \u00d7 10\u207b\u00b2\u00b9 J. "
                    "Tiny, but multiplied by 10\u00b2\u00b3 molecules it accounts for a "
                    "substantial pressure."},
    {"id": "P22", "category": "Molecular speeds", "type": "numeric", "slo": "10.4.1",
     "prompt": "By what factor does the rms speed of a gas increase when its absolute "
               "temperature is quadrupled? Enter the number only.",
     "answer": 2.0, "tolerance": 0.05, "unit": "",
     "hint": "v_rms \u221d sqrt(T).",
     "explanation": "Speed scales as the square root of T, so 4\u00d7 the temperature only doubles "
                    "the speed. This is why a gas is far harder to make extremely fast than "
                    "merely hot."},
    {"id": "P23", "category": "Molecular speeds", "type": "mcq", "slo": "10.4.3",
     "prompt": "The most probable speed of gas molecules...",
     "options": ["is the speed of the fastest molecules in the gas",
                 "is the speed that the largest number of molecules have",
                 "equals the rms speed", "equals the mean speed"],
     "answer": 1,
     "hint": "It is the height of the peak of the speed distribution.",
     "explanation": "It is the peak of the Maxwell-Boltzmann distribution \u2014 the speed at "
                    "which the greatest number of molecules actually travel. It is not an "
                    "average of anything."},

    # ---- 10.5 First law -------------------------------------------------
    {"id": "P24", "category": "Internal energy", "type": "numeric", "slo": "10.5.1",
     "prompt": "Find the internal energy of 2.00 mol of a monatomic ideal gas at 300 K. Use "
               "U = (3/2) nRT. Enter the number only.",
     "answer": 7482.0, "tolerance": 20.0, "unit": "J",
     "hint": "U = 1.5 \u00d7 n \u00d7 R \u00d7 T.",
     "explanation": "U = 1.5 \u00d7 2.00 \u00d7 8.314 \u00d7 300 = 7483 J. It is the total kinetic "
                    "energy of 1.20 \u00d7 10\u00b2\u00b3 molecules, about 6.2 \u00d7 10\u207b\u00b2\u00b9 J each."},
    {"id": "P25", "category": "Work", "type": "numeric", "slo": "10.5.2",
     "prompt": "A gas expands at constant pressure 2.00 \u00d7 10\u2075 Pa through a volume "
               "change of 0.00300 m\u00b3. Find the work done by the gas. Enter the number only.",
     "answer": 600.0, "tolerance": 5.0, "unit": "J",
     "hint": "W = P dV. Expansion makes dV positive, so the work is positive.",
     "explanation": "W = 2.00 \u00d7 10\u2075 \u00d7 0.00300 = 600 J. Positive, because the gas did "
                    "the work. On a P-V diagram this is the area of the rectangle under the "
                    "path."},
    {"id": "P26", "category": "First law", "type": "numeric", "slo": "10.5.3",
     "prompt": "A gas absorbs 800 J of heat and does 300 J of work. Find the change in "
               "internal energy. Enter the number only.",
     "answer": 500.0, "tolerance": 2.0, "unit": "J",
     "hint": "dU = Q \u2212 W, with W the work done by the gas.",
     "explanation": "dU = 800 \u2212 300 = +500 J. The internal energy rose. Heat in is split "
                    "between the increase in U and the work done; here 500 J went into one and "
                    "300 J into the other."},
    {"id": "P27", "category": "First law", "type": "mcq", "slo": "10.5.3",
     "prompt": "In an isothermal process for an ideal gas...",
     "options": ["dU = 0 and W = 0", "dU = 0 and Q = W",
                 "dU = 0 and Q = 0", "dU \u2260 0 and Q = W"],
     "answer": 1,
     "hint": "U of an ideal gas depends on T and nothing else.",
     "explanation": "dU = 0 and Q = W. Temperature fixed means internal energy fixed, so every "
                    "joule of heat supplied leaves as work."},
    {"id": "P28", "category": "Processes", "type": "mcq", "slo": "10.5.4",
     "prompt": "In an isochoric (constant volume) process...",
     "options": ["W = 0 and Q = dU", "W = P dV and Q = 0",
                 "W = 0 and Q = 0", "dU = 0 and Q = W"],
     "answer": 0,
     "hint": "The container is rigid. Can the gas push anything?",
     "explanation": "W = 0 and Q = dU. A rigid container cannot expand, so no work is done "
                    "and all the heat supplied raises the temperature. That is why a sealed "
                    "jar of air can burst in a fire."},
    {"id": "P29", "category": "Processes", "type": "mcq", "slo": "10.5.4",
     "prompt": "In an adiabatic process...",
     "options": ["no heat is exchanged, so the gas cools as it expands",
                 "temperature stays constant throughout",
                 "the gas does no work",
                 "pressure stays constant throughout"],
     "answer": 0,
     "hint": "Q = 0. Where does the energy for the work come from?",
     "explanation": "With Q = 0, dU = \u2212W, so any work the gas does comes out of its "
                    "internal energy and it cools. PV^\u03b3 stays constant, which is why an "
                    "adiabat is steeper than an isotherm through the same point."},
    {"id": "P30", "category": "First law", "type": "numeric", "slo": "10.5.5",
     "prompt": "A gas absorbs 2.50 \u00d7 10\u2074 J of heat at constant volume. For a diatomic "
               "ideal gas with n = 2.00 mol, find the change in internal energy. Enter the "
               "number only.",
     "answer": 25000.0, "tolerance": 100.0, "unit": "J",
     "hint": "Constant volume means W = 0, so dU = Q.",
     "explanation": "dU = Q = 2.50 \u00d7 10\u2074 J, unchanged. The gas type is irrelevant here "
                    "\u2014 that is the point of an isochoric process."},
    {"id": "P31", "category": "First law", "type": "mcq", "slo": "10.5.5",
     "prompt": "A gas goes from state A to state B by one path doing 200 J of work, and by "
               "another path doing 600 J. The change in internal energy is...",
     "options": ["200 J in the first case and 600 J in the second",
                 "the same in both cases, because dU is a state function",
                 "different in each case, because different amounts of heat were needed",
                 "zero in both cases"],
     "answer": 1,
     "hint": "Internal energy is a property of the state, not of the route.",
     "explanation": "The same in both cases. dU depends only on the two end points, so the "
                    "second path simply required 400 J more heat. The work depends on the "
                    "path; the change in internal energy never does."},

    # ---- 10.6 Heat capacities -------------------------------------------
    {"id": "P32", "category": "Heat capacity", "type": "numeric", "slo": "10.6.1",
     "prompt": "Find the molar heat capacity needed to raise 0.500 mol of a gas through "
               "20.0 K using 4.00 \u00d7 10\u00b3 J of heat. Use C = Q/(n dT). Enter the number "
               "only.",
     "answer": 400.0, "tolerance": 2.0, "unit": "J mol\u207b\u00b9 K\u207b\u00b9",
     "hint": "C = Q / (n \u00b7 dT).",
     "explanation": "C = 4.00 \u00d7 10\u00b3 / (0.500 \u00d7 20.0) = 400 J mol\u207b\u00b9 K\u207b\u00b9. "
                    "That is enormous \u2014 far above any gas \u2014 which is exactly why a "
                    "body needing 4 kJ for half a mole over 20 K must be a metal."},
    {"id": "P33", "category": "Mayer's relation", "type": "numeric", "slo": "10.6.2",
     "prompt": "For a monatomic ideal gas, C_v = 3R/2. Find C_v for one mole. Enter the number "
               "only.",
     "answer": 12.47, "tolerance": 0.05, "unit": "J mol\u207b\u00b9 K\u207b\u00b9",
     "hint": "C_v = (f/2) R with f = 3, so C_v = 1.5 R.",
     "explanation": "C_v = 1.5 \u00d7 8.314 = 12.47 J mol\u207b\u00b9 K\u207b\u00b9. Three "
                    "translational degrees of freedom, each contributing (1/2) R."},
    {"id": "P34", "category": "Mayer's relation", "type": "numeric", "slo": "10.6.3",
     "prompt": "For a diatomic ideal gas, C_p = 7R/2. Find the difference C_p \u2212 C_v for "
               "one mole. Enter the number only.",
     "answer": 8.31, "tolerance": 0.05, "unit": "J mol\u207b\u00b9 K\u207b\u00b9",
     "hint": "This difference is R, whatever the gas.",
     "explanation": "C_p \u2212 C_v = R = 8.314 J mol\u207b\u00b9 K\u207b\u00b9. The extra heat at "
                    "constant pressure is exactly the work of expansion, R dT for one mole."},
    {"id": "P35", "category": "Mayer's relation", "type": "numeric", "slo": "10.6.3",
     "prompt": "A gas has C_p = 29.1 J mol\u207b\u00b9 K\u207b\u00b9 and C_v = 20.8 J mol\u207b\u00b9 "
               "K\u207b\u00b9. Find the ratio gamma = C_p / C_v. Enter the number only.",
     "answer": 1.40, "tolerance": 0.01, "unit": "",
     "hint": "This is the exponent on an adiabat.",
     "explanation": "gamma = 29.1/20.8 = 1.40, the diatomic value. gamma = (f + 2)/f = 7/5 for "
                    "f = 5."},
    {"id": "P36", "category": "Heat capacity", "type": "numeric", "slo": "10.6.4",
     "prompt": "Find the heat needed to raise 2.00 mol of a diatomic ideal gas through "
               "50.0 K at constant pressure. Use C_p = 7R/2 and enter the number only.",
     "answer": 2910.0, "tolerance": 15.0, "unit": "J",
     "hint": "Q = n C_p dT.",
     "explanation": "Q = 2.00 \u00d7 29.10 \u00d7 50.0 = 2910 J. More than at constant volume, "
                    "because at constant pressure some of the heat also pays for the "
                    "expansion."},
    {"id": "P37", "category": "Heat capacity", "type": "mcq", "slo": "10.6.4",
     "prompt": "Why is C_p always greater than C_v?",
     "options": ["Because pressure adds energy to the molecules",
                 "Because at constant pressure the gas also does work as it expands",
                 "because kelvin is bigger than Celsius",
                 "Because C_v is measured in Celsius and C_p in kelvin"],
     "answer": 1,
     "hint": "Think about what the gas must push aside as it warms.",
     "explanation": "At constant pressure the gas expands and does work on the surroundings, "
                    "so more heat is needed for the same rise in temperature. That difference "
                    "is exactly R dT."},

    # ---- 10.7 Second law ------------------------------------------------
    {"id": "P38", "category": "Reversibility", "type": "mcq", "slo": "10.7.1",
     "prompt": "Which of these processes is reversible?",
     "options": ["A gas expanding into a vacuum",
                 "A frictionless piston compressing a gas slowly",
                 "A cup of tea cooling in a room",
                 "A current flowing through a resistor"],
     "answer": 1,
     "hint": "Look for the process with no friction and no temperature or pressure difference.",
     "explanation": "The frictionless slow piston can be undone exactly. The others all "
                    "involve dissipation: spreading heat, mixing, or friction."},
    {"id": "P39", "category": "Second law", "type": "mcq", "slo": "10.7.2",
     "prompt": "The Kelvin-Planck statement of the second law says that...",
     "options": ["heat cannot pass from cold to hot",
                 "no device can take heat from a single reservoir and convert it wholly into "
                 "work",
                 "the entropy of an isolated system can never decrease",
                 "energy is always lost as heat"],
     "answer": 1,
     "hint": "It is the statement about heat engines.",
     "explanation": "That is the Kelvin-Planck statement, and it is why a perfect heat engine "
                    "is impossible. Option 0 is the Clausius statement and option 2 is the "
                    "entropy statement; they are equivalent."},
    {"id": "P40", "category": "Heat engines", "type": "mcq", "slo": "10.7.3",
     "prompt": "A heat engine that took in heat and rejected none would violate...",
     "options": ["the zeroth law", "the first law",
                 "the second law", "none of the laws, it is merely impractical"],
     "answer": 2,
     "hint": "Which law is about the impossibility of something, rather than conservation?",
     "explanation": "The second law. The first law is perfectly happy with 100 % conversion of "
                    "heat to work \u2014 it only forbids creating energy. The second law forbids "
                    "destroying the quality of it."},
    {"id": "P41", "category": "Second law", "type": "mcq", "slo": "10.7.2",
     "prompt": "A refrigerator works because it...",
     "options": ["makes heat flow from cold to hot on its own",
                 "moves heat from cold to hot, but only by using work from an external supply",
                 "creates cold and destroys heat",
                 "reduces the total entropy of the contents"],
     "answer": 1,
     "hint": "Plug it into the socket and think about the Clausius statement.",
     "explanation": "It moves heat from cold to hot, which the second law forbids **on its "
                    "own**, so it must be driven by external work. The total entropy still "
                    "increases, because the electrical energy dissipated more than compensates."},

    # ---- 10.8 Entropy ---------------------------------------------------
    {"id": "P42", "category": "Entropy", "type": "mcq", "slo": "10.8.1",
     "prompt": "The entropy of a gas is best understood as...",
     "options": ["a measure of its temperature",
                 "a measure of the number of microscopic arrangements available to it",
                 "a measure of the disorder visible to the eye",
                 "the heat it contains"],
     "answer": 1,
     "hint": "Count the ways the molecules could be arranged.",
     "explanation": "It counts accessible microscopic arrangements. A gas filling a room has "
                    "enormously more arrangements available than the same gas in a corner."},
    {"id": "P43", "category": "Entropy", "type": "mcq", "slo": "10.8.2",
     "prompt": "Water freezes in a freezer. Which statement is correct?",
     "options": ["this violates the second law",
                 "the entropy of the water decreases, but the entropy of the surroundings "
                 "increases by more, so the total rises",
                 "the total entropy of the universe is unchanged",
                 "entropy only applies to gases"],
     "answer": 1,
     "hint": "The second law is about the total, not about one region.",
     "explanation": "No violation. Local entropy can fall, but the heat removed from the water "
                    "goes into the room, which gains more entropy than the water loses. The "
                    "total never decreases."},
    {"id": "P44", "category": "Entropy", "type": "numeric", "slo": "10.8.2",
     "prompt": "A gas absorbs 2.00 \u00d7 10\u00b3 J of heat reversibly at 400 K. Find the "
               "entropy change, using dS = Q/T. Enter the number only.",
     "answer": 5.00, "tolerance": 0.05, "unit": "J K\u207b\u00b9",
     "hint": "dS = Q_rev / T, with T in kelvin.",
     "explanation": "dS = 2.00 \u00d7 10\u00b3 / 400 = **5.00 J K\u207b\u00b9**. Positive, "
                    "because heat was absorbed at a positive absolute temperature. The units "
                    "J K\u207b\u00b9 are the giveaway that entropy is a capacity for heat, "
                    "not an amount of it."},
    {"id": "P45", "category": "Entropy", "type": "mcq", "slo": "10.8.3",
     "prompt": "Which environmental problem is most directly an entropy problem?",
     "options": ["depletion of concentrated ores that become dispersed when used",
                 "the greenhouse effect", "acid rain", "ozone depletion"],
     "answer": 0,
     "hint": "Which one is about energy quality and dispersal rather than chemistry?",
     "explanation": "Re-concentrating dispersed minerals costs energy, because reversing a "
                    "spontaneous mixing process requires work. The greenhouse effect is real "
                    "and serious, but it is an energy-balance problem more than an entropy "
                    "one."},

    # ---- 10.9 Heat engines ---------------------------------------------
    {"id": "P46", "category": "Heat engines", "type": "numeric", "slo": "10.9.1",
     "prompt": "An engine takes in 1000 J of heat and rejects 600 J. Find its efficiency. "
               "Enter the number only.",
     "answer": 0.40, "tolerance": 0.005, "unit": "",
     "hint": "efficiency = work out / heat in, and W = Q_h \u2212 Q_c.",
     "explanation": "W = 1000 \u2212 600 = 400 J, so eta = 400/1000 = 0.40. Compare it with "
                    "the Carnot limit for the two reservoir temperatures before claiming the "
                    "engine is good."},
    {"id": "P47", "category": "Carnot cycle", "type": "mcq", "slo": "10.9.2",
     "prompt": "The Carnot cycle on a P-V diagram consists of...",
     "options": ["two isobars and two isochores",
                 "two isotherms joined by two adiabats",
                 "one isotherm and three isochores",
                 "two isotherms and two isobars"],
     "answer": 1,
     "hint": "Two curves at constant temperature, joined by two curves where no heat enters.",
     "explanation": "Two isotherms (constant T) joined by two adiabats (Q = 0). The enclosed "
                    "area is the net work done in one cycle."},
    {"id": "P48", "category": "Carnot efficiency", "type": "numeric", "slo": "10.9.3",
     "prompt": "A Carnot engine operates between 600 K and 300 K. Find its efficiency as a "
               "decimal. Enter the number only.",
     "answer": 0.50, "tolerance": 0.005, "unit": "",
     "hint": "eta = 1 \u2212 T_c/T_h, both in kelvin.",
     "explanation": "eta = 1 \u2212 300/600 = 0.50. No engine between these temperatures can "
                    "exceed 50 %."},
    {"id": "P49", "category": "Carnot efficiency", "type": "mcq", "slo": "10.9.3",
     "prompt": "The efficiency of a Carnot engine...",
     "options": ["increases as the hot reservoir gets hotter and the cold one colder",
                 "depends only on the hot reservoir temperature",
                 "is always 100 % for an ideal gas",
                 "is greater than that of any real engine at the same temperatures"],
     "answer": 0,
     "hint": "Look at what happens to the ratio T_c / T_h.",
     "explanation": "It rises as the gap widens. And it is only ever equal to a real engine's "
                    "efficiency in the limit \u2014 a real engine is always worse."},
    {"id": "P50", "category": "Refrigeration", "type": "numeric", "slo": "10.9.4",
     "prompt": "An ideal refrigerator works between a cold space at 250 K and a room at 300 K. "
               "Find its coefficient of performance. Enter the number only.",
     "answer": 5.0, "tolerance": 0.05, "unit": "",
     "hint": "COP = T_c / (T_h \u2212 T_c).",
     "explanation": "COP = 250/(300 \u2212 250) = 5.0. It removes 5 J of heat for every joule "
                    "of electricity. A real refrigerator does worse than this."},
    {"id": "P51", "category": "Refrigeration", "type": "mcq", "slo": "10.9.4",
     "prompt": "A refrigerator's coefficient of performance...",
     "options": ["is the fraction of electrical energy that becomes cooling, so it cannot "
                 "exceed 1",
                 "is the heat removed from the cold space per joule of work supplied",
                 "equals the efficiency of the equivalent heat engine",
                 "is always greater for a refrigerator working in a warm room"],
     "answer": 1,
     "hint": "Work out what is being divided by what.",
     "explanation": "COP = Q_c / W. It is heat **moved**, not energy converted, so it can "
                    "exceed 1 \u2014 a COP of 5 means 5 J of heat moved per joule spent. A warm "
                    "room makes it worse, not better."},
    {"id": "P52", "category": "Heat engines", "type": "numeric", "slo": "10.9.1",
     "prompt": "A power station delivers 400 MJ of electrical energy per second while "
               "rejecting 600 MJ s\u207b\u00b9 of waste heat. Find its efficiency as a decimal. "
               "Enter the number only.",
     "answer": 0.40, "tolerance": 0.005, "unit": "",
     "hint": "Total heat in = useful work out + heat rejected.",
     "explanation": "Heat in = 400 + 600 = 1000 MJ s\u207b\u00b9, so eta = 400/1000 = 0.40. "
                    "Compare that with the Carnot limit for its reservoir temperatures to see "
                    "how much is still on the table."},
]


# --------------------------------------------------------------------------
# References
# --------------------------------------------------------------------------

REFERENCES = [
    {"short": "OpenStax University Physics Vol. 2",
     "title": "Chapter 3: The Kinetic Theory of Gases",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/university-physics-volume-2",
     "used_for": "Molecular theory, pressure, the gas laws, rms speed and the internal energy of a gas."},
    {"short": "OpenStax University Physics Vol. 2",
     "title": "Chapter 4: The First Law of Thermodynamics",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/university-physics-volume-2",
     "used_for": "Work on a P-V diagram, the four processes, heat capacities and Mayer's relation."},
    {"short": "OpenStax University Physics Vol. 2",
     "title": "Chapter 15: The Laws of Thermodynamics",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/university-physics-volume-2",
     "used_for": "Reversible processes, Carnot efficiency, refrigerators and entropy."},
    {"short": "Sears and Salinger",
     "title": "Thermodynamics, Kinetic Theory and Statistical Thermodynamics",
     "org": "Addison-Wesley",
     "url": "https://archive.org/details/thermodynamicskin0000sear",
     "used_for": "The classical, readable treatment of every derivation in this chapter."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 10",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 10.1.1 to 10.9.4."},
]

#: The molar masses the tutor and the worked examples quote.
MOLAR_MASSES = {
    "Hydrogen, H\u2082": 0.002016,
    "Helium, He": 0.004003,
    "Neon, Ne": 0.020180,
    "Nitrogen, N\u2082": 0.028014,
    "Oxygen, O\u2082": 0.031998,
    "Carbon dioxide, CO\u2082": 0.044009,
    "Water vapour, H\u2082O": 0.018015,
    "Ammonia, NH\u2083": 0.017031,
}