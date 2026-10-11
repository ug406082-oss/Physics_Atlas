"""Chapter 6 content: Fluids Dynamics.

Eighteen outcomes across five sections. The chapter carries two benches of its
own: an **Archimedes bench** where you choose an object and a fluid and watch
whether it floats, and a **pipe simulator** that draws a tapering pipe and
tracks continuity, pressure and speed down its whole length at once.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Learning outcomes
# --------------------------------------------------------------------------

SLOS = [
    {"id": "6.1.1", "text": "Describe upthrust.",
     "simple": "A fluid pushes upwards on anything immersed in it.", "taught": "Upthrust",
     "activity": "Archimedes bench with a force-balance readout", "check": "Guided practice: compute upthrust and explain its direction"},
    {"id": "6.1.2", "text": "Solve word problems using Upthrust = rho g V.",
     "simple": "Upthrust is the weight of the fluid displaced.", "taught": "Upthrust calculations",
     "activity": "Upthrust calculator with a live displaced-weight column", "check": "Guided practice: numerical problems on upthrust"},
    {"id": "6.1.3", "text": "State the principle of floatation in terms of upthrust.",
     "simple": "A body floats when its weight is no more than the maximum upthrust.", "taught": "Principle of floatation",
     "activity": "Floating-fraction calculator with a submerged bar", "check": "Guided practice: find the submerged fraction of a floating body"},
    {"id": "6.1.4", "text": "State Archimedes' principle of floatation.",
     "simple": "Upthrust equals exactly the weight of the fluid displaced.", "taught": "Archimedes' principle",
     "activity": "Displaced-volume comparison against measured weight", "check": "Guided practice: apply the principle to explain floating, sinking and hovering"},
    {"id": "6.1.5", "text": "Justify that ships are engineered to float in the sea.",
     "simple": "A hollow hull displaces enough water for the upthrust to equal the whole weight.", "taught": "Why ships float",
     "activity": "Hull designer with a cargo slider and a waterline indicator", "check": "Guided practice: compute the displacement needed for a given load"},
    {"id": "6.2.1", "text": "Define the following terms: a. streamline flow (laminar flow), b. turbulent flow, c. incompressible flow.",
     "simple": "Streamline: smooth layers that never mix. Turbulent: chaotic swirls. Incompressible: constant density.", "taught": "Types of flow",
     "activity": "Flow-regime explorer driven by the Reynolds number", "check": "Guided practice: classify real flows and define each term"},
    {"id": "6.2.2", "text": "State the conditions required for turbulent flow.",
     "simple": "High speed, large diameter and low viscosity all promote turbulence.", "taught": "Conditions for turbulence",
     "activity": "Reynolds number calculator with a regime verdict", "check": "Guided practice: judge whether given conditions will flow smoothly or turbulently"},
    {"id": "6.3.1", "text": "Derive the equation of continuity.",
     "simple": "For an incompressible fluid, A₁v₁ = A₂v₂.", "taught": "The equation of continuity",
     "activity": "Tapering pipe simulator with the volume flow rate tracked everywhere", "check": "Guided practice: apply continuity to tapering pipes and hose jets"},
    {"id": "6.3.2", "text": "Explain that squeezing one end of a rubber pipe results in increase in flow velocity at the other end.",
     "simple": "Squeeze the narrow end and the fluid speeds up there, because the same volume must pass through less area.", "taught": "Squeezing a pipe",
     "activity": "Side-by-side wide and narrow sections with speed readouts", "check": "Guided practice: explain and calculate the speed change on squeezing"},
    {"id": "6.3.3", "text": "Solve word problems related to the equation of continuity.",
     "simple": "Numerical problems on flow rate and velocity.", "taught": "Continuity problems",
     "activity": "Flow-rate solver with the conservation check displayed", "check": "Guided practice: solve continuity problems and check the flow rate is unchanged"},
    {"id": "6.4.1", "text": "Derive Bernoulli's equation.",
     "simple": "P + ½ρv² + ρgh is the same everywhere along a streamline.", "taught": "Bernoulli's equation",
     "activity": "Bernoulli solver with a four-quantity energy budget", "check": "Guided practice: derive and apply Bernoulli to find a missing quantity"},
    {"id": "6.4.2", "text": "Justify that the difference in pressure can arise from different rates of flow of a fluid.",
     "simple": "Where the flow is faster, the pressure is lower.", "taught": "Pressure and flow rate",
     "activity": "Venturi meter with a live pressure profile along the throat", "check": "Guided practice: relate pressure difference to flow speed"},
    {"id": "6.4.3", "text": "Explain Bernoulli effect in the following cases: a. atomizer, b. swing of ball, c. the lift of golf ball the magnus effect, d. venturi duct.",
     "simple": "Four places where a speed difference becomes a push.", "taught": "Applications of Bernoulli",
     "activity": "Four-device explorer with the speed and pressure at each point", "check": "Guided practice: explain each application in terms of a pressure difference"},
    {"id": "6.5.1", "text": "Define the following terms: a. viscous fluids, b. non-viscous fluids.",
     "simple": "Viscous fluids resist internal shear; non-viscous (ideal) fluids do not.", "taught": "Viscosity",
     "activity": "Viscosity comparison table with settling times", "check": "Guided practice: classify fluids as viscous or non-viscous and justify"},
    {"id": "6.5.2", "text": "Describe that viscous force in a fluid causes a retarding force on an object moving through it.",
     "simple": "A viscous fluid exerts a drag force that opposes motion.", "taught": "Fluid friction",
     "activity": "Drag explorer showing how force grows with speed", "check": "Guided practice: describe the retarding force and its dependence on speed"},
    {"id": "6.5.3", "text": "Explain that real fluids are viscous fluids.",
     "simple": "There is no perfectly non-viscous fluid in nature — only idealisations.", "taught": "Real fluids are viscous",
     "activity": "Settling-time comparison across everyday liquids", "check": "Guided practice: explain why the ideal fluid is a model rather than a substance"},
    {"id": "6.5.4", "text": "Describe the following terms: a. fluid friction, b. super fluidity.",
     "simple": "Fluid friction dissipates energy; superfluidity is the limit case of zero viscosity.", "taught": "Superfluidity",
     "activity": "Four superfluidity demonstrations described and compared", "check": "Guided practice: describe superfluidity and contrast it with ordinary liquids"},
    {"id": "6.5.5", "text": "Use different liquids in the surroundings to explain fluid friction and super fluidity.",
     "simple": "Honey, water and superfluid helium span the whole range from very viscous to frictionless.", "taught": "Comparing real liquids",
     "activity": "Range explorer from air to superfluid helium", "check": "Guided practice: compare liquids quantitatively using their viscosities"},
]

STATIONS = [
    {"key": "overview", "label": "🗺️ Your route & outcomes", "slos": []},
    {"key": "upthrust", "label": "🎈 Upthrust & floatation", "slos": ["6.1.1", "6.1.2", "6.1.3", "6.1.4"]},
    {"key": "ships", "label": "🚢 Why ships float", "slos": ["6.1.5"]},
    {"key": "flow", "label": "🌊 Streamline & turbulent flow", "slos": ["6.2.1", "6.2.2"]},
    {"key": "continuity", "label": "🔧 The equation of continuity", "slos": ["6.3.1", "6.3.2", "6.3.3"]},
    {"key": "bernoulli", "label": "🌀 Bernoulli's equation", "slos": ["6.4.1", "6.4.2"]},
    {"key": "applications", "label": "💨 Applications of Bernoulli", "slos": ["6.4.3"]},
    {"key": "viscosity", "label": "🍯 Viscosity & fluid friction", "slos": ["6.5.1", "6.5.2", "6.5.3"]},
    {"key": "superfluidity", "label": "❄ Superfluidity", "slos": ["6.5.4", "6.5.5"]},
    {"key": "worked", "label": "🧮 Worked problems", "slos": []},
    {"key": "practice", "label": "🧠 Practice", "slos": []},
    {"key": "tutor", "label": "🤖 Atlas Tutor (offline AI)", "slos": []},
    {"key": "practical", "label": "\uD83E\uDD9E Practical activities", "slos": []},
    {"key": "references", "label": "📚 References", "slos": []},
]

BIG_IDEAS = [
    ("Fluid forces are forces about displaced fluid.",
     "Once you learn that the upthrust equals the weight of the fluid you have pushed "
     "aside, floating stops being mysterious. A ship floats because its hollow hull "
     "displaces a huge mass of water."),
    ("Fluids do not stretch, so they must move faster where the space is smaller.",
     "That one idea is the whole of the equation of continuity. Squeeze the pipe and "
     "the fluid has nowhere to go but faster."),
    ("Speed and pressure trade off against each other.",
     "Bernoulli's equation says that where a fluid speeds up it loses pressure. That "
     "single trade is why a sprayer works and why a curve ball curves."),
]

TAG = "CHAPTER 6 · OPEN"
INTRO = (
    "Water is not a substance in this chapter so much as a substance that obeys rules. "
    "Eighteen outcomes cover what happens when bodies float, how flow behaves in steady "
    "and chaotic regimes, and the two equations — continuity and Bernoulli — that "
    "govern almost every practical flow problem. There is an Archimedes bench and a "
    "tapering-pipe simulator to try them on."
)
ROUTE = ("Upthrust and floatation → Why ships float → Flow regimes → Continuity → "
         "Bernoulli → Applications → Viscosity → Superfluidity → Worked problems → Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("g taken as 9.8 m s⁻², ρ of water as 1000 kg m⁻³", "warn"),
                 ("Ideal-flow models, not measured pipe data", "mute"),
                 ("Results computed live from your inputs", "good")]

NOTES = [
    ("⚠ WATCH OUT", "Archimedes' principle is about displaced fluid, not submerged fraction",
     "Archimedes says upthrust = weight of fluid displaced. The *principle of floatation* "
     "is the separate statement that a body floats only if its weight does not exceed the "
     "upthrust. Mixing the two is the most common slip in this chapter."),
    ("🎯 EXAM TIP", "Draw the pipe before you do any arithmetic",
     "Continuity problems go wrong when the areas are confused. Sketch the pipe, label "
     "every diameter, compute every area as πd²/4, and only then substitute. The sketch "
     "takes thirty seconds and catches almost every error."),
    ("🔬 HONEST LIMIT", "Bernoulli assumes steady, incompressible, non-viscous flow",
     "Real pipe flow loses energy to friction, so the pressure along a real pipe falls "
     "faster than Bernoulli alone predicts. Bernoulli gives the ideal answer and the "
     "direction of the effect; it does not predict the losses."),
]

# --------------------------------------------------------------------------
# Reference tables
# --------------------------------------------------------------------------

UPTHRUST_SETUP = [
    {"symbol": "ρ_f", "means": "density of the fluid", "unit": "kg m⁻³"},
    {"symbol": "V_d", "means": "volume of fluid displaced", "unit": "m³"},
    {"symbol": "W", "means": "weight of the body", "unit": "N"},
    {"symbol": "U", "means": "upthrust = ρ_f g V_d", "unit": "N"},
]

FLOATATION_CASES = [
    {"case": "ρ_body < ρ_fluid", "verdict": "Floats",
     "submerged": "A fraction ρ_body / ρ_fluid of the volume is submerged.",
     "reason": "The body is less dense than the fluid, so it needs only a fraction of its "
               "own volume of fluid beneath it before the upthrust balances its weight."},
    {"case": "ρ_body = ρ_fluid", "verdict": "Fully submerged, in equilibrium",
     "submerged": "The whole volume.",
     "reason": "It displaces its own volume of fluid, whose weight equals its own weight, so "
               "it hangs motionless at any depth."},
    {"case": "ρ_body > ρ_fluid", "verdict": "Sinks",
     "submerged": "The whole volume, then it accelerates downward.",
     "reason": "Even the maximum upthrust, equal to the weight of its whole volume of fluid, "
               "is less than its weight."},
]

TURBULENCE_FACTORS = [
    {"factor": "Flow speed", "direction": "increases turbulence",
     "why": "Inertia relative to viscosity grows as v² grows, so the fluid keeps going "
            "straight past obstacles instead of being smoothed out."},
    {"factor": "Pipe diameter", "direction": "increases turbulence",
     "why": "A wider pipe has larger eddies relative to its own size, and Re ∝ L."},
    {"factor": "Viscosity", "direction": "decreases turbulence",
     "why": "Thicker fluids damp out small swirls. Re is inversely proportional to η."},
    {"factor": "Fluid density", "direction": "increases turbulence",
     "why": "Denser fluid carries more inertia for the same speed, so Re ∝ ρ."},
    {"factor": "Roughness and obstructions", "direction": "increase turbulence",
     "why": "Sharp edges shed eddies that then grow as they travel downstream."},
]

BERNOULLI_QUANTITIES = [
    {"term": r"P", "name": "Pressure", "meaning": "the push of the fluid, per unit area",
     "note": "Higher when the fluid is slow, low or deep."},
    {"term": r"\tfrac{1}{2}\rho v^2", "name": "Kinetic energy per unit volume",
     "meaning": "the energy of the fluid's motion", "note": "Higher when the fluid is fast."},
    {"term": r"\rho g h", "name": "Gravitational energy per unit volume",
     "meaning": "the energy stored by height", "note": "Higher when the fluid is high."},
]

BERNOULLI_APPLICATIONS = [
    {"device": "Perfume atomizer",
     "mechanism": "Squeezing the bulb forces air through a narrow jet. The jet moves fast, "
                  "so its pressure falls below atmospheric.",
     "effect": "The fall in pressure pulls liquid up the tube, and the air stream carries it "
               "out as a fine spray.",
     "without_it": "Without the narrow jet there is no speed, so no pressure drop, so the "
                   "liquid would simply sit in the tube."},
    {"device": "Swing of a struck ball",
     "mechanism": "The ball's seams or spin drag the air round with it, so the air on one side "
                  "moves faster than on the other.",
     "effect": "The faster side has lower pressure, so the ball is pushed towards the slow "
               "side — the direction of the spin.",
     "without_it": "Without spin the pressure would be equal on both sides and the ball would "
                   "travel in a straight line."},
    {"device": "Magnus effect",
     "mechanism": "The general form of the same idea: a spinning body creates an asymmetric "
                  "flow, and therefore an unbalanced pressure force.",
     "effect": "The force curves the path. Golf balls are dimpled precisely to make the "
               "boundary layer turbulent and the effect strong and predictable.",
     "without_it": "A smooth ball sees less spin-induced deflection, which is why a smooth "
                   "ball travels much further in the same conditions."},
    {"device": "Venturi duct",
     "mechanism": "A deliberately narrowed section forces the flow to speed up, and by "
                  "Bernoulli its pressure falls.",
     "effect": "The pressure difference between the wide and narrow ends is what actually "
               "measures the flow rate. This is exactly how a carburettor meters fuel.",
     "without_it": "A wide constant pipe gives no pressure difference to measure, so the flow "
                   "rate cannot be inferred."},
]

# --------------------------------------------------------------------------
# Worked problems
# --------------------------------------------------------------------------

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "Does a block float or sink?",
     "level": "Foundation", "slos": ["6.1.1", "6.1.3", "6.1.4"],
     "question": "A wooden block of volume 2.0 × 10⁻³ m³ has a density of 600 kg/m³. It is placed in water "
                 "(density 1000 kg/m³, g = 9.8 m/s²). Does it float, and what fraction of it is submerged?",
     "known": ["V = 2.0 × 10⁻³ m³", "ρ_body = 600 kg/m³", "ρ_water = 1000 kg/m³",
               "Weight W = ρVg = 600 × 2.0 × 10⁻³ × 9.8 = 11.76 N"],
     "find": "whether it floats, and the submerged fraction",
     "equation": r"U = \rho_f\,g\,V_d \qquad\text{and}\qquad W = \rho_{body}\,g\,V",
     "conversions": ["No unit conversion is needed; everything is already in SI units."],
     "substitution": r"\frac{\rho_{body}}{\rho_f} = \frac{600}{1000} = 0.60",
     "calculation": [
         "Step 1 — compare the densities: 600 is less than 1000, so the block floats. This is quicker than computing forces, and the force calculation below confirms it.",
         "Step 2 — for a floating body, the upthrust equals the whole weight: ρ_f g V_d = ρ_body g V.",
         "Step 3 — cancel g and solve for the fraction: V_d / V = ρ_body / ρ_f = 600/1000 = 0.60.",
         "Step 4 — so 60 % of the block is underwater. The submerged volume is 1.2 × 10⁻³ m³ and the upthrust is 1000 × 9.8 × 1.2 × 10⁻³ = 11.76 N, exactly matching the weight. ✓",
         "Step 5 — the g cancels entirely, which is worth noticing: the submerged fraction depends only on the ratio of the densities, not on g or on the size of the block.",
     ],
     "unit_check": r"U = \mathrm{kg\,m^{-3}}\ \mathrm{m\,s^{-2}}\ \mathrm{m^3} = \mathrm{kg\,m\,s^{-2}} = \mathrm{N}",
     "answer": "It floats with 60 % of its volume submerged",
     "sig_fig_note": "The densities are given to one or two significant figures, so the answer is 0.6 or 60 %.",
     "assumptions": ["The block's density is that of the wood itself, not of the wood plus any water it has absorbed.",
                     "The block floats freely without touching the bottom or a side."]},
    {"id": "WP2", "title": "Why a ship floats at all",
     "level": "Developing", "slos": ["6.1.5"],
     "question": "A cargo ship of mass 2.0 × 10⁷ kg floats in sea water of density 1025 kg/m³. Find the volume of "
                 "water it must displace, and explain how a hull made mostly of steel achieves this.",
     "known": ["m = 2.0 × 10⁷ kg", "ρ_sea = 1025 kg/m³", "g = 9.8 m/s²",
               "Floating requires ρ_sea g V_d = mg"],
     "find": "the displaced volume",
     "equation": r"V_d = \frac{m}{\rho_f} = \frac{mg}{\rho_f g}",
     "conversions": ["Density is given in kg/m³ already, so no conversion is needed."],
     "substitution": r"V_d = \frac{2.0\times10^{7}}{1025} = 1.951\times10^{4}\ \mathrm{m^3}",
     "calculation": [
         "Step 1 — for flotation, upthrust equals weight: ρ_sea g V_d = mg.",
         "Step 2 — cancel g: V_d = m / ρ_sea = 2.0 × 10⁷ / 1025 = 1.95 × 10⁴ m³, about 19 500 tonnes of seawater.",
         "Step 3 — steel has a density of about 7850 kg/m³. If the hull were a solid block of that volume it would weigh 1.53 × 10⁸ kg — far more than the ship.",
         "Step 4 — but it is not solid. It is a hollow box, mostly air. The mass of steel is small, but the hull encloses a great volume, and that whole volume is excluded from the water.",
         "Step 5 — this is why the *shape* is the engineering: the hull spreads a modest mass over an enormous waterplane so that a manageable amount of water is displaced. A crumpled paper ball floats; the same paper rolled into a tight ball sinks.",
     ],
     "unit_check": r"V_d = [M][M^{-1}L^3] = [L^3] = \mathrm{m^3}",
     "answer": "The ship displaces about 1.95 × 10⁴ m³ of seawater, achieved by making the hull hollow",
     "sig_fig_note": "The mass is to two significant figures and the density to four, so V_d ≈ 2.0 × 10⁴ m³.",
     "assumptions": ["The ship floats freely and is not attached to a mooring that carries part of its weight.",
                     "The displaced volume is measured from the waterline to the lowest point of the hull."]},
    {"id": "WP3", "title": "The equation of continuity in a tapering pipe",
     "level": "Developing", "slos": ["6.3.1", "6.3.2", "6.3.3"],
     "question": "Water flows through a horizontal pipe that narrows from a diameter of 20 mm to 10 mm. "
                 "If the speed in the wide section is 1.5 m/s, find the speed in the narrow section and the "
                 "volume flow rate.",
     "known": ["D₁ = 20 mm, D₂ = 10 mm", "v₁ = 1.5 m/s",
               "A = πd²/4, so A₁ = π(0.020)²/4 = 3.142 × 10⁻⁴ m² and A₂ = 7.854 × 10⁻⁵ m²",
               "The area ratio is A₁/A₂ = 4, because area goes as the square of the diameter"],
     "find": "v₂ and the volume flow rate",
     "equation": r"A_1 v_1 = A_2 v_2",
     "conversions": ["The diameters are in millimetres; 20 mm = 0.020 m and 10 mm = 0.010 m. "
                     "Halving the diameter quarters the area."],
     "substitution": r"v_2 = \frac{A_1 v_1}{A_2} = \frac{(3.142\times10^{-4})(1.5)}{7.854\times10^{-5}}",
     "calculation": [
         "Step 1 — area of the wide section: A₁ = π(0.020)²/4 = 3.142 × 10⁻⁴ m².",
         "Step 2 — area of the narrow section: A₂ = π(0.010)²/4 = 7.854 × 10⁻⁵ m². That is exactly one quarter of A₁.",
         "Step 3 — continuity: v₂ = A₁v₁/A₂ = (3.142 × 10⁻⁴)(1.5)/(7.854 × 10⁻⁵) = 4.714 × 10⁻⁴ / 7.854 × 10⁻⁵ = 6.0 m/s.",
         "Step 4 — flow rate: Q = A₁v₁ = 3.142 × 10⁻⁴ × 1.5 = 4.71 × 10⁻⁴ m³/s, which is 0.47 litres per second.",
         "Step 5 — the answer is 6.0 m/s and not 3.0 m/s. Halving the diameter quarters the area, so the speed must quadruple. This is the single most common error in continuity problems: people halve the diameter and think the speed halves too.",
     ],
     "unit_check": r"Q = A v = [L^2][L T^{-1}] = [L^3 T^{-1}] = \mathrm{m^3\,s^{-1}}",
     "answer": "v₂ = 6.0 m/s; volume flow rate Q = 4.71 × 10⁻⁴ m³/s",
     "sig_fig_note": "The diameter ratio 2:1 is exact, so the speed ratio 4:1 is exact. With v₁ = 1.5 m/s to two figures, v₂ = 6.0 m/s.",
     "assumptions": ["The water is incompressible and the flow is steady, so the same volume passes every section each second.",
                     "The pipe is horizontal, so no gravitational term is needed."]},
    {"id": "WP4", "title": "Bernoulli across a venturi throat",
     "level": "Challenge", "slos": ["6.4.1", "6.4.2"],
     "question": "Water flows through a horizontal pipe whose diameter halves from 40 mm to 20 mm. At the wide "
                 "part the pressure is 2.0 × 10⁵ Pa and the speed is 1.0 m/s. Find the pressure at the narrow "
                 "part. (ρ = 1000 kg/m³.)",
     "known": ["P₁ = 2.0 × 10⁵ Pa, v₁ = 1.0 m/s, h₁ = h₂ (horizontal)",
               "A₂ = A₁/4, so v₂ = 4v₁ = 4.0 m/s from continuity"],
     "find": "P₂ at the throat",
     "equation": r"P_1 + \tfrac{1}{2}\rho v_1^2 + \rho g h_1 = P_2 + \tfrac{1}{2}\rho v_2^2 + \rho g h_2",
     "conversions": ["All quantities are already in SI units. Pressures are absolute here; gauge "
                     "pressures give the same difference."],
     "substitution": r"P_2 = 2.0\times10^{5} + \tfrac{1}{2}(1000)(1.0)^2 - \tfrac{1}{2}(1000)(4.0)^2",
     "calculation": [
         "Step 1 — continuity first: the diameter halves so the area quarters, giving v₂ = 4 × 1.0 = 4.0 m/s.",
         "Step 2 — the heights are equal, so ρgh drops out of the equation entirely.",
         "Step 3 — substitute: P₂ = 2.0 × 10⁵ + ½(1000)(1) − ½(1000)(16) = 2.0 × 10⁵ + 500 − 8000.",
         "Step 4 — P₂ = 2.0 × 10⁵ − 7500 = 1.925 × 10⁵ Pa, about 1.93 × 10⁵ Pa.",
         "Step 5 — the pressure has fallen by 7500 Pa. The energy per unit volume that was in the slow bulk flow has moved into the fast flow at the throat. That difference is exactly what a venturi flow meter measures.",
     ],
     "unit_check": r"P = [M L^{-1} T^{-2}] = \mathrm{Pa};\quad \tfrac{1}{2}\rho v^2 = "
                   r"\mathrm{kg\,m^{-3}}\ \mathrm{m^2\,s^{-2}} = \mathrm{Pa}",
     "answer": "P₂ ≈ 1.93 × 10⁵ Pa, a fall of 7.5 × 10³ Pa across the throat",
     "sig_fig_note": "v₁ = 1.0 m/s to two figures makes v₂ = 4.0 m/s, so the ½ρv² term is good to two figures.",
     "assumptions": ["Steady, incompressible and non-viscous flow, with negligible height change.",
                     "The flow is along a single streamline through the pipe."]},
    {"id": "WP5", "title": "Comparing viscosity across everyday liquids",
     "level": "Developing", "slos": ["6.5.1", "6.5.3", "6.5.5"],
     "question": "The dynamic viscosities of air, water, glycerine and honey at about 20 °C are 1.8 × 10⁻⁵, "
                 "1.0 × 10⁻³, 1.5 and 2.0 × 10¹ Pa·s respectively. Compare them, and describe what changes "
                 "when a small steel ball is dropped into each.",
     "known": ["Air: 1.8 × 10⁻⁵ Pa·s", "Water: 1.0 × 10⁻³ Pa·s",
               "Glycerine: 1.5 Pa·s", "Honey: 2.0 × 10¹ Pa·s"],
     "find": "the ratios, and the effect on a falling ball",
     "equation": r"F_{\text{drag}} = 6\pi\eta\,r\,v \quad\text{(low Reynolds number)}",
     "conversions": ["All viscosities are already in Pa·s."],
     "substitution": r"\frac{\eta_{\text{honey}}}{\eta_{\text{water}}} = \frac{2.0\times10^{1}}{1.0\times10^{-3}} = 2\times10^{4}",
     "calculation": [
         "Step 1 — honey is about 20 000 times more viscous than water, and a million times more viscous than air.",
         "Step 2 — the drag on the same ball at the same speed is proportional to η, so it is 20 000 times larger in honey than in water.",
         "Step 3 — in air the drag is negligible and the ball reaches its terminal velocity within a few centimetres, falling almost at 9.8 m/s². In water it falls slowly and visibly slows. In glycerine and honey it falls at a fraction of that, or does not appear to fall at all.",
         "Step 4 — there is a second effect as well as viscosity: the upthrust. Honey is 1.4 times denser than water, so for a ball denser than water the upthrust is larger too, and the two effects reinforce each other.",
         "Step 5 — the contrast with superfluidity: helium, cooled below about 2.2 K, has a viscosity that is not merely small but exactly zero, and it climbs the walls of its container. Honey is at the far end of the scale and helium at the other.",
     ],
     "unit_check": r"\eta = \mathrm{Pa\,s} = [M L^{-1} T^{-1}];\ \text{the ratios are dimensionless}",
     "answer": "Honey is roughly 2 × 10⁴ times more viscous than water and 10⁶ times more viscous than air; the drag force on a falling ball scales in the same proportion",
     "sig_fig_note": "Viscosities are quoted to two significant figures, so the ratios are also to two figures.",
     "assumptions": ["All viscosities are at the same temperature, since viscosity of liquids falls sharply as they warm.",
                     "The ball is the same in each liquid and the comparison is made at the same speed."]},
]

# --------------------------------------------------------------------------
# Practice questions
# --------------------------------------------------------------------------

PRACTICE_QUESTIONS = [
    {"id": "P1", "category": "Upthrust", "type": "numeric", "slo": "6.1.2",
     "prompt": "An object displaces 0.002 m³ of water. Taking ρ = 1000 kg/m³ and g = 9.8 m/s², calculate the "
               "upthrust. Enter the number only, in newtons.",
     "answer": 19.6, "tolerance": 0.2, "unit": "N",
     "hint": "U = ρgV.",
     "explanation": "U = 1000 × 9.8 × 0.002 = 19.6 N. This is the weight of 2 litres of water, "
                    "which is what Archimedes' principle states."},
    {"id": "P2", "category": "Upthrust", "type": "mcq", "slo": "6.1.1",
     "prompt": "The direction of the upthrust on an immersed object is...",
     "options": ["downwards, following gravity", "upwards, opposite to gravity",
                 "along the direction of flow", "sideways"], "answer": 1,
     "hint": "The fluid presses on the underside of the object more than on the top, because the pressure rises with depth.",
     "explanation": "Pressure increases with depth, so the underside of a submerged object is "
                    "pushed harder than the top. The net force is upwards."},
    {"id": "P3", "category": "Upthrust", "type": "numeric", "slo": "6.1.4",
     "prompt": "A block floats with exactly half its volume submerged in water of density 1000 kg/m³. "
               "What is the density of the block? Enter the number only.",
     "answer": 500.0, "tolerance": 1.0, "unit": "kg m⁻³",
     "hint": "For a floating body, ρ_f g V_submerged = ρ_body g V.",
     "explanation": "ρ_body = ρ_f × 0.5 = 500 kg/m³. Note that g cancels, so the answer does "
                    "not depend on where on Earth the block is floating."},
    {"id": "P4", "category": "Upthrust", "type": "mcq", "slo": "6.1.3",
     "prompt": "The principle of floatation states that a body will float only if...",
     "options": ["its density is less than the fluid's",
                 "its weight does not exceed the maximum upthrust",
                 "it is completely submerged", "the fluid is denser than air"], "answer": 1,
     "hint": "Think in terms of forces, not densities.",
     "explanation": "It floats if its weight can be balanced by upthrust, i.e. if W does not "
                    "exceed ρ_f g V. The density condition is a consequence of that, not the "
                    "statement itself."},
    {"id": "P5", "category": "Upthrust", "type": "mcq", "slo": "6.1.4",
     "prompt": "Archimedes' principle states that the upthrust on a body is equal to...",
     "options": ["the weight of the body", "the weight of the fluid displaced",
                 "the body's volume", "the pressure at the surface"], "answer": 1,
     "hint": "The principle is named after the man who ran into a bath shouting 'Eureka'.",
     "explanation": "The upthrust equals the weight of the fluid displaced. It is why a body "
                    "feels lighter in water and why nothing at all happens to a body of the "
                    "same density as the fluid."},
    {"id": "P6", "category": "Why ships float", "type": "numeric", "slo": "6.1.5",
     "prompt": "A raft of mass 600 kg floats on water of density 1000 kg/m³. How many cubic metres of water "
               "does it displace? Enter the number only.",
     "answer": 0.6, "tolerance": 0.01, "unit": "m³",
     "hint": "For flotation, mg = ρ g V_d, and g cancels.",
     "explanation": "V_d = m/ρ = 600/1000 = 0.6 m³, which is 600 litres. A ship of the same mass "
                    "displaces the same volume of water; what makes a ship possible is spreading "
                    "that mass over a huge waterline so the depth needed stays small."},
    {"id": "P7", "category": "Why ships float", "type": "mcq", "slo": "6.1.5",
     "prompt": "A crumpled ball of paper floats but the same sheet rolled into a tight ball sinks. Why?",
     "options": ["The rolled ball is heavier", "The rolled ball excludes less water, so its upthrust is smaller",
                 "Paper absorbs water when rolled", "The water is colder deeper down"], "answer": 1,
     "hint": "Same mass, different shape. What does the shape change?",
     "explanation": "Upthrust depends on the volume of water displaced, which depends on the "
                    "shape. A crumpled ball traps air and encloses a large volume; a tight ball "
                    "does not. Mass is identical in both cases."},

    {"id": "P8", "category": "Flow regimes", "type": "mcq", "slo": "6.2.1",
     "prompt": "Streamline (laminar) flow is characterised by...",
     "options": ["fluid particles moving in smooth layers that do not mix",
                 "fluid particles moving in chaotic swirls",
                 "a change in the density of the fluid",
                 "flow that only occurs at very low speed"], "answer": 0,
     "hint": "Imagine layers of different-coloured water in a glass tube.",
     "explanation": "In streamline flow the layers slide smoothly past one another and never "
                    "mix, so the boundary between colours stays sharp for a long distance. "
                    "Turbulent flow mixes them almost immediately."},
    {"id": "P9", "category": "Flow regimes", "type": "mcq", "slo": "6.2.1",
     "prompt": "A fluid is said to be incompressible when...",
     "options": ["it cannot be poured", "its density remains essentially constant under pressure",
                 "it has no viscosity", "it flows in streamline layers"], "answer": 1,
     "hint": "Liquids resist compression almost completely; gases do not.",
     "explanation": "Liquids change volume by only a tiny fraction under enormous pressure, so "
                    "their density is treated as constant. That is what lets continuity reduce "
                    "to A₁v₁ = A₂v₂."},
    {"id": "P10", "category": "Flow regimes", "type": "numeric", "slo": "6.2.2",
     "prompt": "Water flows through a pipe of diameter 0.02 m at 0.5 m/s. Its viscosity is 1.0 × 10⁻³ Pa·s "
               "and its density is 1000 kg/m³. Taking the characteristic length as the diameter, calculate "
               "the Reynolds number. Enter the number only.",
     "answer": 10000.0, "tolerance": 50.0, "unit": "",
     "hint": "Re = ρvL/η.",
     "explanation": "Re = 1000 × 0.5 × 0.02 / 1.0 × 10⁻³ = 10 000. Since this is above about 2000, "
                    "the flow would be turbulent despite the modest speed — the small diameter and "
                    "the low viscosity of water are enough."},
    {"id": "P11", "category": "Flow regimes", "type": "mcq", "slo": "6.2.2",
     "prompt": "Which change would tend to make a flow LESS turbulent?",
     "options": ["Increasing the pipe diameter", "Increasing the speed",
                 "Using a more viscous liquid", "Roughening the pipe walls"], "answer": 2,
     "hint": "Reynolds number = ρvL/η.",
     "explanation": "A more viscous liquid has a larger η and so a smaller Reynolds number, which "
                    "means viscosity wins over inertia and the layers stay ordered. The other "
                    "three changes all increase Re."},

    {"id": "P12", "category": "Continuity", "type": "numeric", "slo": "6.3.1",
     "prompt": "A pipe of cross-sectional area 0.01 m² carries water at 2 m/s. It narrows to an area of "
               "0.0025 m². What is the speed in the narrow section? Enter the number only.",
     "answer": 8.0, "tolerance": 0.05, "unit": "m/s",
     "hint": "A₁v₁ = A₂v₂.",
     "explanation": "v₂ = (0.01 × 2)/0.0025 = 8 m/s. The area has been quartered, so the speed "
                    "has quadrupled."},
    {"id": "P13", "category": "Continuity", "type": "mcq", "slo": "6.3.2",
     "prompt": "You squeeze one end of a soft rubber pipe carrying water. What happens at the other end?",
     "options": ["The flow slows down because the pipe is bent",
                 "The flow speeds up because less area is available",
                 "The flow rate increases overall", "Nothing changes"], "answer": 1,
     "hint": "The same volume per second must pass through a smaller opening.",
     "explanation": "Squeezing reduces the cross-sectional area, and by continuity the same "
                    "volume per second must pass through less area, so the speed rises. The "
                    "overall flow rate out of the pipe is unchanged."},
    {"id": "P14", "category": "Continuity", "type": "mcq", "slo": "6.3.1",
     "prompt": "A hose of area A₁ squirts a jet of area A₂. Ignoring air resistance, the ratio of speeds is...",
     "options": ["A₁ : A₂", "A₂ : A₁", "the square root of A₁ : A₂", "the square root of A₂ : A₁"],
     "answer": 0,
     "hint": "A₁v₁ = A₂v₂, so v₁ : v₂ = A₂ : A₁.",
     "explanation": "v₁/v₂ = A₂/A₁. Because area goes as the square of diameter, halving the "
                    "diameter quarters the area and quadruples the speed — this is the principle "
                    "of a fire hose nozzle."},
    {"id": "P15", "category": "Continuity", "type": "numeric", "slo": "6.3.3",
     "prompt": "How many cubic metres of water pass through a pipe of area 0.02 m² in 5 s if the speed is "
               "3 m/s? Enter the number only.",
     "answer": 0.3, "tolerance": 0.005, "unit": "m³",
     "hint": "Volume = area × speed × time.",
     "explanation": "Q = Av = 0.02 × 3 = 0.06 m³/s, and over 5 s that is 0.3 m³, or 300 litres."},

    {"id": "P16", "category": "Bernoulli", "type": "mcq", "slo": "6.4.1",
     "prompt": "Bernoulli's equation for a fluid along a streamline is...",
     "options": ["P + ρv² + ρgh = constant", "P + ½ρv² + ρgh = constant",
                 "P − ½ρv² + ρgh = constant", "Pv + ρgh = constant"], "answer": 1,
     "hint": "The kinetic term is the energy of the fluid's motion per unit volume.",
     "explanation": "P + ½ρv² + ρgh is constant along a streamline of steady, incompressible, "
                    "non-viscous flow. It is energy conservation written for a fluid."},
    {"id": "P17", "category": "Bernoulli", "type": "mcq", "slo": "6.4.2",
     "prompt": "In a horizontal pipe, where the water flows fastest...",
     "options": ["the pressure is highest", "the pressure is lowest",
                 "the pressure is the same everywhere", "the pressure is zero"], "answer": 1,
     "hint": "With height fixed, the pressure and the kinetic term must trade against each other.",
     "explanation": "The fastest part is the narrowest part, and that is where the pressure is "
                    "lowest. This is why a Venturi meter can measure flow rate at all."},
    {"id": "P18", "category": "Bernoulli", "type": "numeric", "slo": "6.4.1",
     "prompt": "Water flows horizontally at 10 m/s where the pressure is 1.0 × 10⁵ Pa. At a point where the "
               "speed is 5 m/s, what is the pressure? Take ρ = 1000 kg/m³. Enter the number only.",
     "answer": 137500.0, "tolerance": 500.0, "unit": "Pa",
     "hint": "Bernoulli with equal heights: P₁ + ½ρv₁² = P₂ + ½ρv₂².",
     "explanation": "P₂ = 1.0 × 10⁵ + ½(1000)(100 − 25) = 1.0 × 10⁵ + 37 500 = 1.375 × 10⁵ Pa. "
                    "Slowing down raises the pressure — energy stored as motion has gone back "
                    "into pressure."},
    {"id": "P19", "category": "Bernoulli applications", "type": "mcq", "slo": "6.4.3",
     "prompt": "In a perfume atomizer, the liquid rises up the tube because...",
     "options": ["the tube is narrow and so the liquid is squeezed upward",
                 "the air jet is fast and its pressure is below atmospheric",
                 "the liquid is lighter than the air", "the bottle is upside down"], "answer": 1,
     "hint": "Which part of Bernoulli is at work here?",
     "explanation": "The fast air jet has a pressure below atmospheric, so the higher pressure "
                    "of the surrounding air pushes the liquid up into the low-pressure region, "
                    "where the jet then atomises it."},
    {"id": "P20", "category": "Bernoulli applications", "type": "mcq", "slo": "6.4.3",
     "prompt": "A spinning cricket ball swings in the air because...",
     "options": ["spin makes the ball lighter on one side",
                 "the spin makes air move faster on one side, lowering the pressure there",
                 "the seams are heavier than the ball",
                 "gravity is weaker over the swing"], "answer": 1,
     "hint": "This is the Magnus effect.",
     "explanation": "The spin drags air round with it, so the flow is faster on one side. By "
                    "Bernoulli that side is at lower pressure, so the ball is pushed towards it."},
    {"id": "P21", "category": "Bernoulli applications", "type": "mcq", "slo": "6.4.3",
     "prompt": "Golf balls are covered in dimples mainly to...",
     "options": ["make the ball heavier", "reduce the pressure inside the ball",
                 "increase the Magnus effect by making the boundary layer turbulent",
                 "make the ball more elastic"], "answer": 2,
     "hint": "It has nothing to do with the ball's weight.",
     "explanation": "Dimpling trips the boundary layer into turbulence, which delays the "
                    "separation of flow and makes the pressure difference across the ball both "
                    "larger and more consistent, so the ball flies further and more accurately."},

    {"id": "P22", "category": "Viscosity", "type": "mcq", "slo": "6.5.1",
     "prompt": "A viscous fluid is one that...",
     "options": ["resists internal friction or shear between its layers",
                 "flows very fast", "has a high density", "is a gas"], "answer": 0,
     "hint": "Think about what happens when you stir honey.",
     "explanation": "Viscosity is the resistance of a fluid to internal shear. Honey resists it "
                    "strongly, air barely at all."},
    {"id": "P23", "category": "Viscosity", "type": "numeric", "slo": "6.5.1",
     "prompt": "The viscosity of water is 1.0 × 10⁻³ Pa·s and that of honey is 2.0 × 10¹ Pa·s. How many "
               "times more viscous is the honey? Enter the number only.",
     "answer": 20000.0, "tolerance": 100.0, "unit": "times",
     "hint": "Divide the two viscosities.",
     "explanation": "2.0 × 10¹ / 1.0 × 10⁻³ = 2 × 10⁴ = 20 000 times. This is why a spoon of "
                    "honey barely moves in a spoon of water but a drop of water vanishes in honey."},
    {"id": "P24", "category": "Viscosity", "type": "mcq", "slo": "6.5.2",
     "prompt": "The retarding force of a viscous fluid on a moving object...",
     "options": ["acts in the direction of motion", "acts opposite to motion and grows with speed",
                 "is constant whatever the speed", "acts only when the object stops"], "answer": 1,
     "hint": "Which way does friction act, and does a faster object feel more of it?",
     "explanation": "Drag always opposes the motion, and for a small sphere moving slowly it is "
                    "proportional to speed: F = 6πηrv. At higher speeds it grows even faster."},
    {"id": "P25", "category": "Viscosity", "type": "mcq", "slo": "6.5.3",
     "prompt": "Why do textbooks describe an ideal fluid as 'non-viscous' even though no such fluid exists?",
     "options": ["Because viscosity is zero in every fluid at low temperature",
                 "Because it is a simplification that makes the equations solvable",
                 "Because gases have no viscosity", "Because viscosity only acts in solids"], "answer": 1,
     "hint": "It is a model, not a substance.",
     "explanation": "An ideal fluid is an idealisation: perfectly incompressible and perfectly "
                    "frictionless. Every real fluid has some viscosity, and the chapter returns to "
                    "that in the final section."},
    {"id": "P26", "category": "Superfluidity", "type": "mcq", "slo": "6.5.4",
     "prompt": "Superfluid helium is unusual because...",
     "options": ["it freezes at a very high temperature",
                 "its viscosity falls to zero and it can creep up the walls of its container",
                 "it becomes a gas below 2 K", "it has a negative density"], "answer": 1,
     "hint": "It is the limit case of zero viscosity.",
     "explanation": "Below about 2.2 K liquid helium enters a superfluid phase with zero "
                    "viscosity: it flows without resistance, climbs the container walls and "
                    "keeps spinning forever once started."},
    {"id": "P27", "category": "Superfluidity", "type": "numeric", "slo": "6.5.5",
     "prompt": "Glycerine has a viscosity of 1.5 Pa·s and water 1.0 × 10⁻³ Pa·s. How many times more viscous "
               "is glycerine than water? Enter the number only.",
     "answer": 1500.0, "tolerance": 20.0, "unit": "times",
     "hint": "1.5 divided by 1.0 × 10⁻³.",
     "explanation": "1500 times. Small air bubbles trapped in glycerine rise so slowly that you "
                    "can watch them; the same bubbles in water shoot to the top."},
    {"id": "P28", "category": "Superfluidity", "type": "mcq", "slo": "6.5.5",
     "prompt": "Compared with ordinary liquids, superfluid helium behaves as though it has...",
     "options": ["a very high viscosity", "exactly zero viscosity",
                 "a viscosity that increases with speed", "no density at all"], "answer": 1,
     "hint": "The word 'super' refers to the behaviour, not the amount.",
     "explanation": "Exactly zero viscosity, which is why a stirred bath of superfluid helium "
                    "never slows down and a bucket of it can spin indefinitely."},
]

REFERENCES = [
    {"short": "OpenStax College Physics 2e",
     "title": "Chapter 12: Fluid Dynamics and Its Biological and Medical Applications",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/college-physics-2e",
     "used_for": "Archimedes' principle, the equation of continuity and Bernoulli's equation."},
    {"short": "MIT OpenCourseWare",
     "title": "2.25 Advanced Fluid Mechanics: Reynolds number and pipe flow",
     "org": "Massachusetts Institute of Technology",
     "url": "https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/",
     "used_for": "The Reynolds number and what determines whether a flow is laminar or turbulent."},
    {"short": "Nobel Prize in Physics 1996",
     "title": "Discovery of superfluidity in helium-3 and helium-4",
     "org": "The Royal Swedish Academy of Sciences",
     "url": "https://www.nobelprize.org/prizes/physics/1996/summary/",
     "used_for": "The experimental facts of superfluidity and the Nobel lecture's accessible account."},
    {"short": "APS Physics",
     "title": "Focus: The fountain effect in superfluid helium",
     "org": "American Physical Society",
     "url": "https://physics.aps.org/",
     "used_for": "An accessible description of the fountain effect and the creeping film."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 6",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 6.1.1 to 6.5.5."},
]
