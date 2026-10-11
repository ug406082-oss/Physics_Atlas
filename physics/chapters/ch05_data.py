"""Chapter 5 content: Deformation in Solids.

Five outcomes — the shortest chapter in the book — so the stations are few and
deep. The centrepiece is an **interactive stress–strain tester**: choose a
material, load a sample of adjustable cross-section, and watch the real curve
respond to your controls. Nothing about that curve is a picture of a textbook
figure; it is recomputed each time you move a slider.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Learning outcomes
# --------------------------------------------------------------------------

SLOS = [
    {"id": "5.1.1", "text": "Distinguish between the structures of crystalline, amorphous and polymeric solids.",
     "simple": "Crystalline: a regular repeating lattice. Amorphous: no long-range order. Polymeric: very long chains.", "taught": "Types of solids",
     "activity": "Solid classifier with ordering, melting behaviour and examples", "check": "Guided practice: classify real substances and justify from their structure"},
    {"id": "5.2.1", "text": "Describe the deformation of solids in one dimension.",
     "simple": "A solid changes length when a force is applied — stretching it or squashing it.", "taught": "Deformation in one dimension",
     "activity": "Stretching simulator with a live extension readout", "check": "Guided practice: compute and explain the change in length of loaded wires and bars"},
    {"id": "5.3.1", "text": "Describe terms elastic deformation, plastic deformation and elastic limit.",
     "simple": "Elastic: springs back completely. Plastic: stays deformed. The elastic limit is where plastic starts.", "taught": "Elastic and plastic deformation",
     "activity": "Load–unload tracer that shows the permanent set", "check": "Guided practice: identify the region of a curve and predict whether a body will return"},
    {"id": "5.4.1", "text": "Define stress, strain and Young modulus.",
     "simple": "Stress = F/A, strain = ΔL/L, Y = stress/strain — and the slope of the early straight line is Y.", "taught": "Stress, strain and Young's modulus",
     "activity": "Stress–strain tester with a real curve and the slope measured live", "check": "Guided practice: read slopes off curves and solve numerical problems"},
    {"id": "5.4.2", "text": "Interpret force extension graph for a deformed material.",
     "simple": "A straight line means extension is proportional to load, so the wire obeys Hooke's law.", "taught": "Reading the curve",
     "activity": "Force-extension graph with the elastic limit and yield point marked", "check": "Guided practice: identify the elastic region and the limit of proportionality"},
    {"id": "5.4.3", "text": "Solve word problems related to Young modulus.",
     "simple": "Y = stress/strain = (F/A)/(extension/length).", "taught": "Young's modulus problems",
     "activity": "Sliders for load, area and length with Y computed live", "check": "Guided practice: solve Young's modulus word problems"},
    {"id": "5.4.4", "text": "Use daily life objects to explain stress, strain and Young modulus.",
     "simple": "Steel bars in concrete are stiff and strong; rubber is stretchy; both are stress and strain.", "taught": "Stress in daily objects",
     "activity": "Everyday-object table naming the property exploited", "check": "Guided practice: explain stress and strain in everyday objects"},
    {"id": "5.5.1", "text": "Determine the elastic potential energy of a material by using E = Fx = (1/2) k x^2.",
     "simple": "The energy stored is the area under the force–extension line, which is a triangle.", "taught": "Elastic potential energy",
     "activity": "Energy integrator with a bounce simulation", "check": "Guided practice: compute stored energy from F, x, k or from a graph"},
]

STATIONS = [
    {"key": "overview", "label": "🗺️ Your route & outcomes", "slos": []},
    {"key": "types", "label": "💎 Types of solids", "slos": ["5.1.1"]},
    {"key": "deformation", "label": "📏 Deformation in one dimension", "slos": ["5.2.1"]},
    {"key": "elastic", "label": "🔁 Elastic and plastic deformation", "slos": ["5.3.1"]},
    {"key": "curve", "label": "📈 Reading the force-extension graph", "slos": ["5.4.2", "5.4.3"]},
    {"key": "objects", "label": "🛠️ Stress and strain around you", "slos": ["5.4.4"]},    {"key": "stress", "label": "📐 Stress, strain and Young's modulus", "slos": ["5.4.1"]},
    {"key": "energy", "label": "🔋 Elastic potential energy", "slos": ["5.5.1"]},
    {"key": "worked", "label": "🧮 Worked problems", "slos": []},
    {"key": "practice", "label": "🧠 Practice", "slos": []},
    {"key": "tutor", "label": "🤖 Atlas Tutor (offline AI)", "slos": []},
    {"key": "practical", "label": "\uD83E\uDD9E Practical activities", "slos": []},
    {"key": "references", "label": "📚 References", "slos": []},
]

BIG_IDEAS = [
    ("How much a solid stretches is set by a ratio, not a force.",
     "A 1 N load stretches a thin wire a lot and a thick one barely at all. What matters "
     "is force spread over area (stress) compared with change in length spread over "
     "original length (strain)."),
    ("Every solid has a limit beyond which it does not spring back.",
     "Pull gently and it returns; pull hard and it stays bent. The elastic limit is the "
     "boundary, and it is a property of the material, not of how carefully you pull."),
    ("The area under the curve is the answer, whatever the curve looks like.",
     "Stiff materials store very little; stretchable ones store a lot. That single fact "
     "explains why a steel spring is strong but stores little energy, and a rubber band "
     "stores a great deal."),
]

TAG = "CHAPTER 5 · OPEN"
INTRO = (
    "Five outcomes, and they build directly on Chapter 1: once you know that "
    "stress, strain and Young's modulus are quantities with defined units and "
    "dimensions, the whole mechanics of stretching becomes arithmetic. There is a "
    "stress–strain tester in this chapter that recomputes a real curve from your "
    "controls — try steel against rubber and see how little they have in common."
)
ROUTE = ("Types of solids → Deformation → Elastic and plastic → Stress, strain and Young's "
         "modulus → Elastic energy → Worked problems → Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("Modulus values are typical room-temperature figures", "warn"),
                 ("Curves generated from a model, not measured data", "mute"),
                 ("Your inputs, your results, computed live", "good")]

NOTES = [
    ("⚠ WATCH OUT", "Stress is not the same as force",
     "Stress divides force by the area that resists it. Double the cross-section of a "
     "wire and the same load produces half the stress. That is why thick cables carry "
     "more load, and why the stress — not the load — is what appears on a material's "
     "specification."),
    ("🎯 EXAM TIP", "The slope of the straight part *is* Young's modulus",
     "On a stress–strain graph, the gradient of the initial straight region is Y. Pick "
     "two well-separated points on that line, not the origin and one nearby point, or "
     "the reading will be dominated by rounding."),
    ("🔬 HONEST LIMIT", "Steel in this app is a model curve, not a test certificate",
     "The curves are generated from each material's modulus and yield stress using a "
     "simple hardening model. Real steel has inclusions, welds and grain structure that "
     "scatter the results; use these curves to learn the shape, not to certify a component."),
]

# --------------------------------------------------------------------------
# 5.2 and 5.3  Deformation
# --------------------------------------------------------------------------

SYMBOL_TABLE = [
    {"symbol": "F", "means": "the applied force", "unit": "N"},
    {"symbol": "A", "means": "the cross-sectional area resisting it", "unit": "m²"},
    {"symbol": "σ = F/A", "means": "stress", "unit": "Pa (N m⁻²)"},
    {"symbol": "L", "means": "the original length", "unit": "m"},
    {"symbol": "ΔL", "means": "the change in length", "unit": "m"},
    {"symbol": "ε = ΔL/L", "means": "strain", "unit": "dimensionless"},
    {"symbol": "Y = σ/ε", "means": "Young's modulus", "unit": "Pa"},
    {"symbol": "k", "means": "force constant of the material", "unit": "N m⁻¹"},
]

DEFORMATION_TYPES = [
    {"kind": "Tensile (stretching)", "load": "The two ends are pulled apart.",
     "change": "The length increases.", "daily": "Stretching a rubber band, drawing a wire",
     "diagram": "F →  ← ← ← ← F"},
    {"kind": "Compressive (squashing)", "load": "The two ends are pushed towards each other.",
     "change": "The length decreases.", "daily": "A column carrying a roof, a foot on a stair",
     "diagram": "→ → → → F  F ← ← ← ←"},
    {"kind": "Shear", "load": "A force parallel to the surface.",
     "change": "One layer slides past another.", "daily": "Sliding one sheet of paper over another",
     "diagram": "⇒⇒⇒ over ⇒⇒⇒"},
    {"kind": "Torsion", "load": "A turning force about an axis.",
     "change": "The body twists.", "daily": "Wringing a wet towel, turning a screwdriver",
     "diagram": "↻ about ↻"},
]

REGIONS = [
    {"name": "Linear elastic", "behaviour": "Strain is exactly proportional to stress.",
     "on_returning": "Returns exactly to its original length.",
     "slopes": "This is the straight part, and its slope is Young's modulus.",
     "micro": "The atoms are stretched elastically from their equilibrium spacing; "
              "every change is reversible."},
    {"name": "Elastic limit", "behaviour": "The last point on the straight line.",
     "on_returning": "Still returns completely, but only just.",
     "slopes": "Beyond it the slope drops: the material is softening.",
     "micro": "Some atomic bonds are at the point of slipping past one another."},
    {"name": "Yield point", "behaviour": "The curve bends sharply.",
     "on_returning": "No longer returns completely.",
     "slopes": "Almost flat for a little while — the material 'gives'.",
     "micro": "Layers of atoms start sliding past each other without breaking."},
    {"name": "Plastic region", "behaviour": "Large permanent deformation for little extra stress.",
     "on_returning": "Stays deformed for good.",
     "slopes": "Rising slowly: strain hardening, as the material resists more.",
     "micro": "Dislocations move and multiply, and block one another."},
    {"name": "Ultimate stress", "behaviour": "The highest stress the curve reaches.",
     "on_returning": "It has been permanently deformed for a long time by now.",
     "slopes": "After this point the curve turns down.",
     "micro": "The neck begins to form."},
    {"name": "Necking and fracture", "behaviour": "Stress falls while the body breaks up.",
     "on_returning": "It is in pieces.",
     "slopes": "The falling stress does not mean it is getting stronger — the "
               "cross-section carrying the load is shrinking rapidly.",
     "micro": "Hollows grow in the material and join into a crack."},
]

DAILY_LIFE = [
    {"object": "Steel spring in a car suspension",
     "explanation": "A steel spring is strong enough to carry the car, and its length "
                    "changes with the load. That change tells the driver and the "
                    "computer how heavily the car is loaded."},
    {"object": "Rubber soles on a running shoe",
     "explanation": "Rubber has a Young's modulus about forty thousand times smaller "
                    "than steel's, so the same stress gives it a far larger strain. "
                    "That is exactly why it cushions."},
    {"object": "A ceramic cup",
     "explanation": "Ceramics are stiff but brittle: their curve is straight right up "
                    "to fracture. A sharp knock puts a tiny region into tension while "
                    "the rest holds it in compression, and a crack starts there."},
    {"object": "Bridge cables",
     "explanation": "A cable is stiff and enormously strong in tension, so it stretches "
                    "very little. Steel's strain at working load is around one part in a "
                    "thousand, which is why a suspension bridge visibly moves in a gale."},
    {"object": "A plastic ruler",
     "explanation": "Polymers have low stiffness and a long plastic region. Bend one "
                    "too far and it stays bent — the chains have slid past each other "
                    "and will not line up again."},
    {"object": "Glass and ceramics in a cookware pan",
     "explanation": "These materials do not conduct heat or electricity at all, and they "
                    "do not expand much when heated, so they can go straight from a "
                    "fridge to a hot hob."},
]

# --------------------------------------------------------------------------
# Worked problems
# --------------------------------------------------------------------------

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "The extension of a stretched wire",
     "level": "Foundation", "slos": ["5.2.1", "5.4.1"],
     "question": "A copper wire 2.0 m long and 0.50 mm in diameter is stretched by a force of 25 N. "
                 "Taking Young's modulus for copper as 1.1 × 10¹¹ Pa, find the extension.",
     "known": ["L = 2.0 m", "diameter = 0.50 mm, so radius = 2.5 × 10⁻⁴ m",
               "A = π r² = π (2.5 × 10⁻⁴)² = 1.963 × 10⁻⁷ m²",
               "Y = 1.1 × 10¹¹ Pa, F = 25 N"],
     "find": "the extension ΔL of the wire",
     "equation": r"Y = \frac{F L}{A\,\Delta L} \quad\Rightarrow\quad \Delta L = \frac{F L}{A\,Y}",
     "conversions": ["The diameter is in millimetres; 0.50 mm = 0.50 × 10⁻³ m = 5.0 × 10⁻⁴ m. "
                     "Cross-section in m², stress in Pa."],
     "substitution": r"\Delta L = \frac{25 \times 2.0}{(1.963\times10^{-7})(1.1\times10^{11})}",
     "calculation": [
         "Step 1 — area: A = π r² = π (2.5 × 10⁻⁴)² = 1.963 × 10⁻⁷ m². Getting this wrong by a factor of four (using the diameter as the radius) is the single most common error in this type of question.",
         "Step 2 — numerator: F L = 25 × 2.0 = 50 N m.",
         "Step 3 — denominator: A Y = (1.963 × 10⁻⁷)(1.1 × 10¹¹) = 2.16 × 10⁴ N.",
         "Step 4 — extension: ΔL = 50 / 2.16 × 10⁴ = 2.31 × 10⁻³ m = 2.3 mm.",
         "Step 5 — sanity check: 2.3 mm over 2000 mm is a strain of 1.2 × 10⁻³, which is just under copper's elastic limit strain of about 6 × 10⁻⁴... it is slightly above it, so the wire has just passed its elastic limit and will not quite return to its original length. A good thing to notice: the formula still gives a valid answer, but the material is no longer behaving elastically.",
     ],
     "unit_check": r"Y = \frac{[M L T^{-2}][L]}{[L^2][L]} = [M L^{-1} T^{-2}] = \text{pascals};\ "
                   r"\Delta L = \frac{\mathrm{N\,m}}{\mathrm{m^2\,Pa}} = [L]",
     "answer": "ΔL ≈ 2.3 × 10⁻³ m, that is 2.3 mm",
     "sig_fig_note": "The diameter of 0.50 mm is to two significant figures and the area goes as its square, so the area is really only good to two figures. The final answer is quoted to two significant figures.",
     "assumptions": ["The wire is uniform and obeys Hooke's law over this range.",
                     "The elastic limit is not exceeded, so the deformation is reversible."]},
    {"id": "WP2", "title": "Reading Young's modulus off a graph",
     "level": "Developing", "slos": ["5.4.1"],
     "question": "On a stress–strain graph for a metal, the straight elastic region passes through the point "
                 "(strain = 0.002, stress = 4.0 × 10⁸ Pa) and the origin. Calculate Young's modulus, and "
                 "explain why the origin is not a good second point to use.",
     "known": ["The straight line passes through the origin: (0, 0)",
               "and through (0.002, 4.0 × 10⁸ Pa)",
               "Young's modulus is the gradient of this line"],
     "find": "Y, and the reason the origin is a poor choice of point",
     "equation": r"Y = \frac{\text{stress}}{\text{strain}} = \frac{4.0\times10^{8}}{0.002}",
     "conversions": ["Strain is dimensionless, so Y carries the same unit as stress: pascals."],
     "substitution": r"Y = \frac{4.0\times10^{8}\ \mathrm{Pa}}{0.002} = 2.0\times10^{11}\ \mathrm{Pa}",
     "calculation": [
         "Step 1 — Young's modulus is the gradient of the stress–strain curve, and on the straight elastic branch that gradient is constant.",
         "Step 2 — using the two points: Y = (4.0 × 10⁸ − 0) / (0.002 − 0) = 2.0 × 10¹¹ Pa. This is a value typical of steel.",
         "Step 3 — why not use the origin? On any real graph, the point (0, 0) is drawn to a rounding of the pen width and is usually the first point of an instrument trace rather than a measurement. Its coordinates are known far less accurately than a pair of readings further along the line.",
         "Step 4 — the practical rule: take two points as far apart as possible while staying on the straight section. A large separation means the percentage error in each reading makes a small difference to the gradient.",
         "Step 5 — cross-check: 2.0 × 10¹¹ Pa means a stress of 1 Pa stretches the material by 1/(2 × 10¹¹) of its length. A copper wire carrying 1 kg per square millimetre stretches by about 0.1 % of its length.",
     ],
     "unit_check": r"[\text{stress}]/[\text{strain}] = [M L^{-1} T^{-2}] = \text{Pa}",
     "answer": "Y = 2.0 × 10¹¹ Pa; the origin is unreliable because its coordinates are fixed by drawing rather than measured",
     "sig_fig_note": "The strain of 0.002 has one significant figure as written, but the answer is normally quoted as 2 × 10¹¹ Pa.",
     "assumptions": ["The straight region really is straight over the range used.",
                     "The stress and strain axes are linear, not logarithmic."]},
    {"id": "WP3", "title": "Elastic energy stored in a spring",
     "level": "Developing", "slos": ["5.5.1"],
     "question": "A spring of force constant 400 N/m is compressed by 5.0 cm. Find the elastic potential "
                 "energy stored, and the average force during compression.",
     "known": ["k = 400 N/m", "x = 5.0 cm = 0.050 m", "Force rises linearly from 0 to kx"],
     "find": "the stored energy and the average force",
     "equation": r"E = \tfrac{1}{2} k x^2 = \tfrac{1}{2} F_{\max}\, x",
     "conversions": ["5.0 cm = 0.050 m. Leaving it in centimetres and getting 200 000 instead of "
                     "20 J is the standard trap."],
     "substitution": r"E = \tfrac{1}{2}(400)(0.050)^2 = \tfrac{1}{2}(400)(0.0025)",
     "calculation": [
         "Step 1 — the maximum force: F = kx = 400 × 0.050 = 20 N.",
         "Step 2 — stored energy: E = ½ × 400 × (0.050)² = ½ × 400 × 0.0025 = 0.50 J.",
         "Step 3 — check with the triangle: ½ × base × height = ½ × 0.050 × 20 = 0.50 J. ✓",
         "Step 4 — the average force is half the maximum, because the triangle's height is at its midpoint: F_avg = 20/2 = 10 N.",
         "Step 5 — a useful scaling fact: E goes as x², so compressing a spring twice as far stores four times the energy. This is why a hard squash in a diving board or a trampoline feels so different from a gentle one.",
     ],
     "unit_check": r"E = \mathrm{N\,m^{-1}} \times \mathrm{m^2} = \mathrm{N\,m} = \mathrm{J}",
     "answer": "E = 0.50 J stored; average force during compression = 10 N",
     "sig_fig_note": "k = 400 N/m is ambiguous in sig figs but is conventionally taken as three; x = 5.0 cm is two, so E = 0.50 J.",
     "assumptions": ["The spring obeys Hooke's law over this compression, so the force is proportional to x.",
                     "No energy is lost to internal friction during the compression."]},
    {"id": "WP4", "title": "Energy stored in a stretched wire",
     "level": "Challenge", "slos": ["5.4.1", "5.5.1"],
     "question": "A steel wire of length 3.0 m and cross-sectional area 2.0 × 10⁻⁶ m² is stretched by a "
                 "force of 4000 N. Find its extension and the energy stored in it. (Y for steel is 2.0 × 10¹¹ Pa.)",
     "known": ["L = 3.0 m", "A = 2.0 × 10⁻⁶ m²", "F = 4000 N", "Y = 2.0 × 10¹¹ Pa"],
     "find": "the extension ΔL and the stored energy E",
     "equation": r"\Delta L = \frac{F L}{A Y}, \qquad E = \tfrac{1}{2} F\,\Delta L",
     "conversions": ["All values are already in SI units."],
     "substitution": r"\Delta L = \frac{4000 \times 3.0}{(2.0\times10^{-6})(2.0\times10^{11})}, "
                     r"\quad E = \tfrac{1}{2}(4000)\Delta L",
     "calculation": [
         "Step 1 — extension: A Y = (2.0 × 10⁻⁶)(2.0 × 10¹¹) = 4.0 × 10⁵ N. So ΔL = 12000 / 4.0 × 10⁵ = 3.0 × 10⁻² m = 3.0 cm.",
         "Step 2 — check the strain: ΔL/L = 0.030/3.0 = 0.010, which is 1 %. Steel yields at about 0.15 %, so the wire is still comfortably elastic. The formula is being used legitimately.",
         "Step 3 — energy: E = ½ × 4000 × 0.030 = 60 J.",
         "Step 4 — cross-check with the spring form. For a wire, k = YA/L = (2.0 × 10¹¹)(2.0 × 10⁻⁶)/3.0 = 1.33 × 10⁵ N/m, so E = ½kx² = ½(1.33 × 10⁵)(0.030)² = 60 J. ✓",
         "Step 5 — the two routes agree because they are the same physics: a stretched wire behaves exactly like a spring with a force constant set by its geometry.",
     ],
     "unit_check": r"\Delta L: \mathrm{N\,m\,m^{-3}\,m} \to \mathrm{m};\qquad "
                   r"E: \mathrm{N\,m} = \mathrm{J}",
     "answer": "Extension = 3.0 × 10⁻² m (3.0 cm); energy stored = 60 J",
     "sig_fig_note": "All values are to two significant figures, so both answers are quoted to two figures.",
     "assumptions": ["The wire is uniform and its length is unchanged in the area term.",
                     "The strain stays inside the elastic region throughout."]},
    {"id": "WP5", "title": "Predicting whether a body will return",
     "level": "Developing", "slos": ["5.3.1", "5.4.1"],
     "question": "A copper wire is loaded until its stress reaches 7.0 × 10⁷ Pa and then the load is removed. "
                 "Will it return to its original length? Copper has Y = 1.1 × 10¹¹ Pa and a yield stress of "
                 "about 7.0 × 10⁷ Pa.",
     "known": ["Y = 1.1 × 10¹¹ Pa", "Elastic limit = yield_stress / Y",
               "Applied stress = 7.0 × 10⁷ Pa"],
     "find": "whether the deformation is reversible",
     "equation": r"\varepsilon_{\text{elastic}} = \frac{\sigma}{Y}",
     "conversions": ["Stress and modulus are both in pascals, so the strain they produce is dimensionless."],
     "substitution": r"\varepsilon = \frac{7.0\times10^{7}}{1.1\times10^{11}} = 6.4\times10^{-4}",
     "calculation": [
         "Step 1 — the elastic strain at the elastic limit: ε = σ/Y = 7.0 × 10⁷ / 1.1 × 10¹¹ = 6.4 × 10⁻⁴, that is 0.064 %.",
         "Step 2 — compare. The applied stress of 7.0 × 10⁷ Pa is exactly at copper's yield stress, so the strain has exactly reached the elastic limit.",
         "Step 3 — at the limit the wire will still return, but only just. Any further loading and it begins to deform permanently.",
         "Step 4 — the practical reading: copper is being used right at the edge of its elastic region. In engineering, the working stress is always set to a fraction of the yield stress precisely to avoid this ambiguity.",
         "Step 5 — a striking comparison: glass has a much higher yield stress than copper, but its fracture strain is only about 0.001. It is stronger and stiffer and yet it breaks almost immediately once it stops being elastic, because it never develops a plastic region at all.",
     ],
     "unit_check": r"[M L^{-1} T^{-2}] / [M L^{-1} T^{-2}] = \text{dimensionless}",
     "answer": "The strain reached is 6.4 × 10⁻⁴, exactly the elastic limit strain, so the wire just returns — with no safety margin",
     "sig_fig_note": "The elastic strain is about 0.06 %, which is small enough that the numbers must be kept carefully.",
     "assumptions": ["The load is applied slowly and the temperature is constant.",
                     "The wire is free to contract equally along its whole length on unloading."]},
]

# --------------------------------------------------------------------------
# Practice questions
# --------------------------------------------------------------------------

PRACTICE_QUESTIONS = [
    {"id": "P1", "category": "Types of solids", "type": "mcq", "slo": "5.1.1",
     "prompt": "Which of these is a crystalline solid?",
     "options": ["Glass", "Quartz", "Rubber", "Wax"], "answer": 1,
     "hint": "Crystalline solids have a long-range repeating pattern.",
     "explanation": "Quartz has a regular lattice of silicon and oxygen atoms repeating in space. "
                    "Glass, wax and rubber have no long-range order, which is why they soften "
                    "gradually rather than melting at a sharp temperature."},
    {"id": "P2", "category": "Types of solids", "type": "mcq", "slo": "5.1.1",
     "prompt": "Old window panes of medieval buildings are thicker at the bottom than at the top. "
               "This is best explained by the fact that glass...",
     "options": ["is crystalline, so its layers settle over centuries",
                 "is amorphous and has flowed slowly over centuries under gravity",
                 "is a polymer whose chains have stretched under pressure",
                 "is denser than the surrounding air"], "answer": 1,
     "hint": "What does the uneven thickness tell you about the material's structure?",
     "explanation": "Glass is amorphous. Over centuries gravity has let the very viscous glass "
                    "flow downwards, thickening the bottom. A crystalline material would not "
                    "have done this."},
    {"id": "P3", "category": "Types of solids", "type": "mcq", "slo": "5.1.1",
     "prompt": "Which class of solid contains very long chains of repeating units?",
     "options": ["Crystalline", "Amorphous", "Polymeric", "None of these"], "answer": 2,
     "hint": "Poly-ethene, rubber and nylon all belong to this class.",
     "explanation": "Polymeric solids are built from very long chains, often cross-linked. When "
                    "you stretch rubber the chains uncoil and line up, which is why it can be "
                    "stretched to many times its resting length and still spring back."},
    {"id": "P4", "category": "Types of solids", "type": "numeric", "slo": "5.1.1",
     "prompt": "How many of these are amorphous solids: diamond, glass, rubber, sodium chloride, wax, "
               "polyethene? Enter just the number.",
     "answer": 4, "tolerance": 0, "unit": "solids",
     "hint": "Crystalline solids melt sharply; amorphous ones do not.",
     "explanation": "Glass, rubber, wax and polyethene are amorphous, so 4. Diamond and sodium "
                    "chloride are crystalline, with regular lattices and sharp melting points."},

    {"id": "P5", "category": "Deformation", "type": "mcq", "slo": "5.2.1",
     "prompt": "A wire is stretched by a force F. Which change makes it stretch MORE?",
     "options": ["Increasing its cross-sectional area",
                 "Increasing its length", "Using a stiffer material",
                 "Reducing the force"], "answer": 1,
     "hint": "Look at the formula ΔL = FL/(AY).",
     "explanation": "ΔL is proportional to L and F but inversely proportional to A and Y. So "
                    "doubling the length doubles the extension, doubling the area halves it, and "
                    "a stiffer material stretches less."},
    {"id": "P6", "category": "Deformation", "type": "numeric", "slo": "5.2.1",
     "prompt": "A wire stretches 4 mm under a load. Under twice the load, the same wire stretches how "
               "many millimetres? Enter the number only.",
     "answer": 8.0, "tolerance": 0.1, "unit": "mm",
     "hint": "Within the elastic region, extension is proportional to force.",
     "explanation": "8 mm, because ΔL = FL/(AY) is linear in F. This only holds while the wire "
                    "stays elastic; past the limit the relationship breaks down and the extension "
                    "runs away."},
    {"id": "P7", "category": "Deformation", "type": "mcq", "slo": "5.2.1",
     "prompt": "Deformation caused by a force parallel to the surface of a body is called...",
     "options": ["tensile deformation", "compressive deformation", "shear deformation",
                 "torsional deformation"], "answer": 2,
     "hint": "This is what happens when one sheet slides over another.",
     "explanation": "Shear deformation slides one layer past another. Tensile stretches, "
                    "compressive squashes, and torsional is twisting."},

    {"id": "P8", "category": "Elastic and plastic", "type": "mcq", "slo": "5.3.1",
     "prompt": "The elastic limit of a material is the point...",
     "options": ["beyond which the material breaks",
                 "beyond which the material no longer returns to its original shape",
                 "at which the material begins to stretch at all",
                 "beyond which the material stretches forever"], "answer": 1,
     "hint": "Try loading a rubber band a little and then a lot.",
     "explanation": "Up to the elastic limit the deformation is fully reversible. Past it, "
                    "permanent plastic deformation begins, and only much later does the material "
                    "actually break."},
    {"id": "P9", "category": "Elastic and plastic", "type": "mcq", "slo": "5.3.1",
     "prompt": "You stretch a metal wire and it snaps. What must have been true?",
     "options": ["The wire was always within its elastic limit",
                 "The wire was taken beyond its elastic limit, into the plastic region",
                 "Elastic and plastic deformation are the same thing",
                 "The force must have been zero"], "answer": 1,
     "hint": "A wire that returns to its original length cannot snap.",
     "explanation": "A snap requires the stress to have risen far past the elastic limit, so "
                    "large permanent deformation accumulated until fracture. Any wire that has "
                    "recovered fully was never beyond its elastic limit."},
    {"id": "P10", "category": "Elastic and plastic", "type": "numeric", "slo": "5.3.1",
     "prompt": "A spring is stretched 10 cm and released, and it returns exactly to its original length. "
               "How many centimetres of the 10 cm are elastic? Enter the number only.",
     "answer": 10, "tolerance": 0, "unit": "cm",
     "hint": "If it returns completely, all of the deformation was elastic.",
     "explanation": "All 10 cm. Any part of a deformation that is recovered on release is elastic "
                    "by definition; the part that remains behind is the plastic part."},

    {"id": "P11", "category": "Stress and strain", "type": "numeric", "slo": "5.4.1",
     "prompt": "A force of 200 N acts on a circular cross-section of radius 0.010 m. Calculate the stress "
               "in pascals. Enter the number only.",
     "answer": 636619.7723675814, "tolerance": 500.0, "unit": "Pa",
     "hint": "σ = F/A and A = πr².",
     "explanation": "A = π(0.010)² = 3.1416 × 10⁻⁴ m², so σ = 200 / 3.1416 × 10⁻⁴ = 6.37 × 10⁵ Pa, "
                    "which is about 6.4 atmospheres."},
    {"id": "P12", "category": "Stress and strain", "type": "numeric", "slo": "5.4.1",
     "prompt": "A wire stretches 0.5 mm over its original length of 2 m. Calculate the strain. "
               "Enter the number only.",
     "answer": 0.00025, "tolerance": 1e-6, "unit": "",
     "hint": "Strain = change in length ÷ original length, and both lengths must be in the same unit.",
     "explanation": "0.5 mm = 0.0005 m, so ε = 0.0005 / 2 = 2.5 × 10⁻⁴. Strain has no unit. "
                    "Mixing millimetres with metres here gives a wildly wrong answer."},
    {"id": "P13", "category": "Stress and strain", "type": "numeric", "slo": "5.4.1",
     "prompt": "A material has a stress of 2.0 × 10⁸ Pa at a strain of 0.001. Calculate Young's modulus in "
               "pascals. Enter the number only.",
     "answer": 2.0e11, "tolerance": 1e8, "unit": "Pa",
     "hint": "Y = stress / strain.",
     "explanation": "Y = 2.0 × 10⁸ / 0.001 = 2.0 × 10¹¹ Pa, a value typical of steel."},
    {"id": "P14", "category": "Stress and strain", "type": "mcq", "slo": "5.4.1",
     "prompt": "On a stress–strain graph, the gradient of the initial straight portion is...",
     "options": ["the tensile strength", "Young's modulus",
                 "the elastic limit stress", "the strain at fracture"], "answer": 1,
     "hint": "Y = stress / strain = the slope when strain is on the horizontal axis.",
     "explanation": "With strain across the bottom and stress up the side, the slope of the "
                    "straight elastic region is stress divided by strain, which is Young's modulus."},
    {"id": "P15", "category": "Stress and strain", "type": "mcq", "slo": "5.4.1",
     "prompt": "Two wires of the same material carry the same force, but one has twice the cross-sectional "
               "area. The stress in the thicker wire is...",
     "options": ["twice as large", "the same", "half as large", "one quarter as large"], "answer": 2,
     "hint": "σ = F/A.",
     "explanation": "Half as large. The stress is halved, which is exactly why thick cables can "
                    "carry larger loads at the same safe stress."},
    {"id": "P16", "category": "Stress and strain", "type": "mcq", "slo": "5.4.1",
     "prompt": "On a stress–strain curve, the stress falls after reaching the ultimate stress because...",
     "options": ["the material has suddenly become weaker",
                 "the cross-section carrying the load is shrinking rapidly as a neck forms",
                 "the force is being reduced", "the strain is decreasing"], "answer": 1,
     "hint": "Stress is force divided by area.",
     "explanation": "The load is still rising, but it is being carried by a rapidly thinning neck, "
                    "so the stress over the remaining cross-section falls. The material has not "
                    "become weaker; less of it is doing the work."},

    {"id": "P17", "category": "Elastic energy", "type": "numeric", "slo": "5.5.1",
     "prompt": "A spring of force constant 200 N/m is stretched by 0.10 m. Calculate the elastic potential "
               "energy in joules. Enter the number only.",
     "answer": 1.0, "tolerance": 0.02, "unit": "J",
     "hint": "E = ½kx².",
     "explanation": "E = ½ × 200 × 0.01 = 1.0 J."},
    {"id": "P18", "category": "Elastic energy", "type": "numeric", "slo": "5.5.1",
     "prompt": "A force rises linearly from 0 N to 60 N while a body moves 0.20 m. How much work is done? "
               "Enter the number only, in joules.",
     "answer": 6.0, "tolerance": 0.1, "unit": "J",
     "hint": "The area under the line is a triangle.",
     "explanation": "½ × 0.20 × 60 = 6.0 J. This is also ½Fx, and since F = kx for a spring it is "
                    "the same as ½kx²."},
    {"id": "P19", "category": "Elastic energy", "type": "numeric", "slo": "5.5.1",
     "prompt": "A spring stores 8 J when stretched 0.20 m. What energy does it store when stretched "
               "0.40 m? Enter the number only, in joules.",
     "answer": 32.0, "tolerance": 0.5, "unit": "J",
     "hint": "E goes as x², not as x.",
     "explanation": "Doubling the extension quadruples the energy: 8 × 4 = 32 J. This is why a "
                    "trampoline or a diving board feels so different when pushed twice as far."},
    {"id": "P20", "category": "Elastic energy", "type": "mcq", "slo": "5.5.1",
     "prompt": "Which materials store the most elastic energy for a given stress?",
     "options": ["Stiff metals such as steel", "Very stiff materials such as tungsten",
                 "Flexible materials such as rubber", "Brittle materials such as glass"],
     "answer": 2,
     "hint": "Energy density is ½ × stress × strain, and strain depends on the modulus.",
     "explanation": "Energy density = ½σε = σ²/(2Y), so for the same stress it is inversely "
                    "proportional to Young's modulus. Rubber's modulus is some forty thousand "
                    "times smaller than steel's, so it stores vastly more energy per unit volume."},

    {"id": "P21", "category": "Force-extension graphs", "type": "mcq", "slo": "5.4.2",
     "prompt": "On a force-extension graph for a metal wire, the straight part of the curve is the region where the wire is...",
     "options": ["permanently deformed", "in the elastic region",
                 "already broken", "being stretched past its elastic limit"],
     "answer": 1,
     "hint": "Hooke's law holds over one region only.",
     "explanation": "The straight region is where extension is proportional to load, so the "
                    "wire obeys Hooke's law and returns to its original length when the load "
                    "is removed. Past the elastic limit the curve bends and the extension does "
                    "not return."},
    {"id": "P22", "category": "Young modulus", "type": "numeric", "slo": "5.4.3",
     "prompt": "A wire of length 2.0 m and cross-sectional area 4.0 x 10^-6 m^2 stretches by "
               "0.50 mm under a load of 120 N. Find the Young modulus. Enter the number only.",
     "answer": 1.2e11, "tolerance": 0.06e11, "unit": "Pa",
     "hint": "Y = (F/A) / (extension/original length). Convert the extension to metres.",
     "explanation": "stress = 120 / 4.0e-6 = 3.0e7 Pa; strain = 0.50e-3 / 2.0 = 2.5e-4; "
                    "Y = 3.0e7 / 2.5e-4 = 1.2e11 Pa. Always convert the millimetres before "
                    "dividing."},
    {"id": "P23", "category": "Stress and strain", "type": "mcq", "slo": "5.4.4",
     "prompt": "A steel wire is stretched until it breaks. Which everyday object relies on the "
               "same combination of high stress and high strain?",
     "options": ["a glass fibre optic cable", "a steel reinforcing rod in concrete",
                 "a rubber eraser", "a paperclip"],
     "answer": 1,
     "hint": "Look for the object that must be both very strong and able to deform a little "
             "without snapping.",
     "explanation": "A reinforcing rod works because steel has a high stress at fracture but "
                    "also stretches slightly before breaking, so it absorbs load instead of "
                    "snapping. A fibre optic cable and an eraser both fail long before their "
                    "breaking stress."},
]

REFERENCES = [
    {"short": "OpenStax College Physics 2e",
     "title": "Chapter 9: Statics and Elasticity",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/college-physics-2e",
     "used_for": "Stress, strain, Young's modulus and the elastic potential energy of a spring."},
    {"short": "DoITPoMS teaching package",
     "title": "The elastic properties of materials",
     "org": "University of Cambridge, Department of Materials Science",
     "url": "https://www.doitpoms.ac.uk/tlplib/elasticity/",
     "used_for": "Stress–strain curves for real materials, and how to read the regions of the curve."},
    {"short": "Engineering Toolbox",
     "title": "Elastic properties of materials: modulus reference table",
     "org": "Engineering Toolbox",
     "url": "https://www.engineeringtoolbox.com/young-modulus-d_417.html",
     "used_for": "Cross-checking the typical Young's modulus values used in this chapter."},
    {"short": "Britannica",
     "title": "Crystal, amorphous and polymeric solids",
     "org": "Encyclopaedia Britannica",
     "url": "https://www.britannica.com/science/solid-state-physics",
     "used_for": "The structural distinction between the three classes of solid."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 5",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 5.1.1 to 5.5.1."},
]

# --------------------------------------------------------------------------
# 5.4.2 and 5.4.3  Reading a force-extension graph
# --------------------------------------------------------------------------

CURVE_REGIONS = [
    {"region": "Origin to the limit of proportionality",
     "meaning": "A straight line. Extension is proportional to load, so the wire obeys "
                "Hooke's law and the gradient here **is** Young's modulus."},
    {"region": "Limit of proportionality to elastic limit",
     "meaning": "The curve begins to bend but the wire still returns to its original "
                "length when the load is removed. The gradient is changing, so the simple "
                "gradient is no longer Young's modulus."},
    {"region": "Elastic limit",
     "meaning": "The last point at which the wire is still perfectly elastic. Beyond it "
                "any permanent deformation begins."},
    {"region": "Yield point",
     "meaning": "The load now increases very little while the extension grows quickly. This "
                "is where a ductile metal such as copper or mild steel starts to deform "
                "permanently."},
    {"region": "Beyond yield, up to fracture",
     "meaning": "The wire keeps stretching with rising load until it breaks. The area under "
                "this part of the curve is the energy needed to break it, which is a measure "
                "of toughness."},
    {"region": "For a brittle solid such as glass or cast iron",
     "meaning": "There is **no** elastic limit, yield point or plastic region. The curve "
                "stays straight right up to a sudden break, which is why brittle materials "
                "give no warning before failing."},
]

DAILY_OBJECTS = [
    {"object": "Steel reinforcing bars in concrete",
     "what": "Carry tension in a beam that would otherwise sag or crack.",
     "property": "High stress at fracture combined with enough strain to absorb load.",
     "explain": "Concrete is excellent in compression and poor in tension. The steel does the "
                "tension. A bar is allowed to be stressed well below fracture but to strain "
                "measurably, so a warning crack appears in the concrete before the steel "
                "yields. Designing with that margin is what keeps a building standing."},
    {"object": "A glass fibre optic cable",
     "what": "Carries light for kilometres without it leaking out of the sides.",
     "property": "A very high refractive index difference between core and cladding.",
     "explain": "Light is trapped by total internal reflection, which is a geometric effect "
                "rather than a mechanical one, but the same failure logic applies: glass is "
                "brittle, with no warning before it breaks, so the cable is handled with the "
                "gentleness that implies."},
    {"object": "A rubber tyre",
     "what": "Absorbs bumps and keeps contact with the road.",
     "property": "A very low Young's modulus, so a large strain for a small stress.",
     "explain": "Rubber sits far down the stiffness scale. It deforms enormously and "
                "recovers, which is exactly what a suspension component must do. Raise its "
                "stiffness and the ride suffers."},
    {"object": "A paperclip",
     "what": "Holds paper together through thousands of open and close cycles.",
     "property": "Moderate stiffness with a high elastic limit.",
     "explain": "If the elastic limit were lower, the clip would take a permanent set after a "
                "few dozen uses and stop springing back. The point is not the peak stress but "
                "the limit of the elastic region."},
    {"object": "A steel guitar string",
     "what": "Stays in tune while being bent and released.",
     "property": "A high elastic limit combined with low internal damping.",
     "explain": "A string that took a permanent set would go out of tune permanently. Low "
                "damping keeps it ringing rather than dying away, which is the same quantity "
                "the oscillation chapters call the quality factor."},
]

DAILY_CONCEPTS = [
    {"concept": "Stiffness is not strength",
     "meaning": "Young's modulus says how hard a material resists deformation; the stress at "
                "fracture says how much it can take. Diamond is extremely stiff and also "
                "extremely strong; a stiff steel wire is easily bent by a small force because "
                "being hard to stretch is not the same as being hard to break."},
    {"concept": "Toughness is not strength",
     "meaning": "Strength is the peak stress; toughness is the area under the whole curve, "
                "the energy absorbed before fracture. Glass is strong and brittle, so it has "
                "almost no toughness. Mild steel is strong and ductile, so it absorbs a great "
                "deal of energy before it fails."},
    {"concept": "Why design allows some strain",
     "meaning": "A structure that takes a small permanent strain has absorbed energy rather "
                "than snapping. The strain is evidence that the load was carried, not evidence "
                "that the material failed."},
]
