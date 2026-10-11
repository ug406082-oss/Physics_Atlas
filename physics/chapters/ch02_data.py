"""Chapter 2 content: Scalars and Vectors.

Four learning outcomes, one per syllabus section, and a small chapter - so the
stations are fewer and deeper than the big chapters later in the book. There is
no "dimensions" station here and no "uncertainty" station: Chapter 2 is about
one idea only, that a quantity either has a direction or it does not, and
everything else follows from that.
"""

from __future__ import annotations

import math

# --------------------------------------------------------------------------
# Learning outcomes
# --------------------------------------------------------------------------

SLOS = [
    {"id": "2.1.1", "text": "Differentiate between scalar and vector quantities.",
     "simple": "A scalar has size only. A vector has size and direction, and needs both to be fully described.", "taught": "Scalars & vectors",
     "activity": "Scalar or vector classifier with a hidden-direction quiz", "check": "Guided practice: name the quantity and say which kind it is, then justify it"},
    {"id": "2.2.1", "text": "Analyse a vector into its rectangular components.",
     "simple": "Break a vector into perpendicular x and y parts, add the parts, and put the answer back together.", "taught": "Rectangular components",
     "activity": "Vector sandpit: drag two vectors, watch the resultant, then read off its components", "check": "Guided practice: resolve, add and re-resolve a pair of vectors"},
    {"id": "2.2.2", "text": "Explain the sum of vectors using perpendicular components.",
     "simple": "Walk the head-to-tail path in x and in y separately; the total change in each axis is the component of the sum.", "taught": "Adding vectors",
     "activity": "Component walk with the path split into an x-row and a y-row", "check": "Guided practice: add two vectors one component at a time"},
    {"id": "2.2.3", "text": "Calculate the resultant of two vectors by rectangular component method.",
     "simple": "Magnitude sqrt(Rx^2 + Ry^2); direction tan^-1(Ry/Rx), measured with the correct quadrant.", "taught": "Resultants",
     "activity": "Two-vector calculator that reports magnitude and direction", "check": "Guided practice: calculate the resultant of two vectors"},
    {"id": "2.3.1", "text": "Define scalar product of two vectors.",
     "simple": "A·B = AB cos θ. It gives a plain number, and it measures how much of B lies along A.", "taught": "Scalar (dot) product",
     "activity": "Shadow dial: rotate one vector and watch the scalar product and the shadow change", "check": "Guided practice: compute and sign-check dot products, and test commutativity"},
    {"id": "2.3.2", "text": "Exemplify scalar product of two vectors in terms of angle between them.",
     "simple": "A dot B = |A||B| cos(theta). Work, power and angle between two lines all use it.", "taught": "Dot product by angle",
     "activity": "Sliders for both magnitudes and the angle, with the projection drawn", "check": "Guided practice: evaluate a scalar product from its angle"},
    {"id": "2.3.3", "text": "Describe properties of scalar product of two vectors.",
     "simple": "Commutative but not associative. A.B = B.A, but A.(B.C) = (A.B).C only for scalars. Zero if perpendicular; -|A||B| if opposite.", "taught": "Properties of the dot product",
     "activity": "Property checklist with a live pass/fail verdict", "check": "Guided practice: test each property of the scalar product"},
    {"id": "2.4.1", "text": "Define vector product of two vectors.",
     "simple": "A×B = AB sin θ, and the answer points perpendicular to both. It measures the 'turn' between them.", "taught": "Vector (cross) product",
     "activity": "Right-hand-rule dial: rotate two vectors and watch the perpendicular direction appear", "check": "Guided practice: compute cross products, decide the sense, and test anti-commutativity"},
    {"id": "2.4.2", "text": "Exemplify vector product of two vectors in terms of angle between them.",
     "simple": "A x B = |A||B| sin(theta), along the right-hand normal. Magnetic force and torque both use it.", "taught": "Cross product by angle",
     "activity": "Right-hand-rule builder showing the axis and sense", "check": "Guided practice: evaluate a vector product from its angle"},
    {"id": "2.4.3", "text": "Describe properties of vector product of two vectors. *.",
     "simple": "Not commutative: A x B = -(B x A). Zero if parallel. Magnitude is area of the parallelogram the two vectors span.", "taught": "Properties of the cross product",
     "activity": "Property checklist with the parallelogram drawn", "check": "Guided practice: test each property of the vector product"},
]

STATIONS = [
    {"key": "overview", "label": "🧭 Where this chapter is going", "slos": []},
    {"key": "kind", "label": "📏 Scalar or vector?", "slos": ["2.1.1"]},
    {"key": "components", "label": "📐 Rectangular components", "slos": ["2.2.1"]},
    {"key": "resultant", "label": "🛰️ Adding by components", "slos": ["2.2.2", "2.2.3"]},
    {"key": "dot", "label": "✖️ Scalar product", "slos": ["2.3.1"]},
    {"key": "dotwork", "label": "💦 Scalar product in use", "slos": ["2.3.2", "2.3.3"]},
    {"key": "cross", "label": "➰ Vector product", "slos": ["2.4.1"]},
    {"key": "crosswork", "label": "🧭 Vector product in use", "slos": ["2.4.2", "2.4.3"]},
    {"key": "worked", "label": "🧮 Worked problems", "slos": []},
    {"key": "practice", "label": "🧠 Practice", "slos": []},
    {"key": "tutor", "label": "🤖 Atlas Tutor (offline AI)", "slos": []},
    {"key": "practical", "label": "\U0001F99E Practical activities", "slos": []},
    {"key": "references", "label": "📚 References", "slos": []},
]

BIG_IDEAS = [
    ("A vector is not a number in disguise.",
     "“5” is not a vector. “5 newtons” is a vector, because 5 N pointing north "
     "and 5 N pointing east are different physical situations, even though the "
     "two numbers are identical."),
    ("Components turn addition into arithmetic.",
     "You cannot add two vectors by adding their sizes. But you can add their x "
     "components and their y components separately, because each of those is "
     "just a signed number."),
    ("There are two ways to multiply.",
     "The scalar product answers “how much do these agree along one line?”. The "
     "vector product answers “how much do these turn away from each other?”. "
     "They use different parts of the angle: cos for one, sin for the other."),
]

TAG = "CHAPTER 2 · OPEN"

INTRO = (
    "Everything in mechanics is built from two kinds of quantity. Some have size "
    "only — mass, time, temperature. Others have size *and* direction — velocity, "
    "force, acceleration. This chapter is short but it is the foundation of the "
    "seven chapters that follow, so it is worth getting exactly right. "
    "Two dials and a vector sandpit are waiting for you."
)

ROUTE = ("Scalar or vector → Rectangular components → Scalar product → Vector product → "
         "Worked problems → Practice.")

HONESTY_PILLS = [
    ("Established scientific definitions", "info"),
    ("Vectors modelled as planar (x, y) pairs", "warn"),
    ("Sandpit values generated by this app", "mute"),
    ("Numbers computed from the formulas shown", "good"),
]

NOTES = [
    ("⚠ WATCH OUT", "“Speed” and “velocity” are not the same word",
     "Speed is a scalar: 60 km/h. Velocity is a vector: 60 km/h due north. "
     "The vector answer is longer on purpose, because the extra direction is "
     "information you cannot throw away. Chapter 3 uses velocity whenever it "
     "means direction."),
    ("🎯 EXAM TIP", "Write the components before you add anything",
     "In every rectangular-component question, draw the axes, draw each arrow "
     "head to tail, then write a small table of x and y before doing any "
     "arithmetic. Marks are given for method, and the table is the method."),
    ("🔬 HONEST LIMIT", "This chapter only handles the xy plane",
     "The cross product of two vectors in one plane always points straight out "
     "of, or straight into, that plane. Real vectors have three components; the "
     "third behaves by exactly the same rule, and it returns in Chapter 4 when "
     "a body rotates about an axis."),
]

# --------------------------------------------------------------------------
# 2.1  Scalars and vectors
# --------------------------------------------------------------------------

SCALARS = [
    {"quantity": "Mass", "symbol": "m", "unit": "kg",
     "why": "10 kg of rice is 10 kg of rice wherever it is.",
     "watch": "If you double the mass you double it, with no question of direction."},
    {"quantity": "Time", "symbol": "t", "unit": "s",
     "why": "An interval of time needs no direction.",
     "watch": "Three seconds is three seconds, forwards or backwards."},
    {"quantity": "Distance", "symbol": "d", "unit": "m",
     "why": "How far, not which way.",
     "watch": "Contrast with displacement, which is a vector."},
    {"quantity": "Speed", "symbol": "v", "unit": "m s⁻¹",
     "why": "The size of the velocity only.",
     "watch": "Contrast with velocity, which also carries direction."},
    {"quantity": "Temperature", "symbol": "T", "unit": "K",
     "why": "20 °C is 20 °C.",
     "watch": "Temperature differences are scalars too."},
    {"quantity": "Work done", "symbol": "W", "unit": "J",
     "why": "Energy is a scalar, and work is a transfer of energy.",
     "watch": "Work is a dot product — Chapter 2.3 shows why the answer is a plain number."},
    {"quantity": "Energy", "symbol": "E", "unit": "J",
     "why": "A joule is a joule.",
     "watch": "Even though it often comes from a force acting through a distance."},
    {"quantity": "Power", "symbol": "P", "unit": "W",
     "why": "The rate of using energy has no direction.",
     "watch": "Careful: P is also used for pressure, which is a scalar too."},
    {"quantity": "Density", "symbol": "ρ", "unit": "kg m⁻³",
     "why": "It is a property of the material itself.",
     "watch": "It rises with temperature, which is why hot air is less dense."},
    {"quantity": "Electric charge", "symbol": "q", "unit": "C",
     "why": "Positive and negative are signs, not directions.",
     "watch": "Do not confuse the sign of charge with a direction of travel."},
]

VECTORS = [
    {"quantity": "Displacement", "symbol": "Δr", "unit": "m",
     "why": "How far and in which direction the body ended up from where it started.",
     "watch": "It does not tell you the route taken — only the net result."},
    {"quantity": "Velocity", "symbol": "v", "unit": "m s⁻¹",
     "why": "Which way the body is going, and how fast.",
     "watch": "A car going round a circle has a velocity that changes even at constant speed."},
    {"quantity": "Acceleration", "symbol": "a", "unit": "m s⁻²",
     "why": "Which way the velocity is changing.",
     "watch": "At the top of a thrown ball the velocity is zero but the "
              "acceleration is not — it is still g downward."},
    {"quantity": "Force", "symbol": "F", "unit": "N",
     "why": "Push or pull, and the direction matters completely.",
     "watch": "This is the vector you meet most often in Chapter 3."},
    {"quantity": "Momentum", "symbol": "p", "unit": "kg m s⁻¹",
     "why": "It is mass times velocity, and velocity is a vector.",
     "watch": "Its direction is always the direction of the velocity."},
    {"quantity": "Weight", "symbol": "W = mg", "unit": "N",
     "why": "The gravitational force points downwards, wherever you stand.",
     "watch": "Weight changes with location; mass does not."},
    {"quantity": "Torque", "symbol": "τ", "unit": "N m",
     "why": "A turning effect needs a sense of rotation.",
     "watch": "It is a cross product — Chapter 2.4."},
    {"quantity": "Magnetic field", "symbol": "B", "unit": "T",
     "why": "The compass needle must point somewhere in particular.",
     "watch": "It has a size and a direction at every point of space."},
    {"quantity": "Angular momentum", "symbol": "L", "unit": "kg m² s⁻¹",
     "why": "It points along the axis of rotation.",
     "watch": "It returns in full in Chapter 4."},
    {"quantity": "Electric field", "symbol": "E", "unit": "N C⁻¹",
     "why": "The direction a positive test charge would be pushed.",
     "watch": "Field lines point the way the force acts on a positive charge."},
]

CLASSIFY_THESE = [
    {"item": "The reading on a pressure gauge", "answer": "scalar",
     "why": "It is a number on a dial; pushing harder simply raises it."},
    {"item": "The direction of the wind", "answer": "vector",
     "why": "A wind from the north is a different weather situation from a wind "
            "of the same strength from the south."},
    {"item": "The mass of a suitcase", "answer": "scalar", "why": "Mass has no direction."},
    {"item": "The kick of a football", "answer": "vector",
     "why": "A 100 N kick high and to the left does something quite different "
            "from 100 N along the ground."},
    {"item": "The mass of the ball", "answer": "scalar", "why": "Mass has no direction."},
    {"item": "The velocity of the wind", "answer": "vector",
     "why": "It has a size and the direction it is blowing towards."},
    {"item": "The temperature of the room", "answer": "scalar", "why": "20 °C is 20 °C."},
    {"item": "The displacement from your desk to the door", "answer": "vector",
     "why": "It says how far and in which direction."},
    {"item": "The energy stored in a stretched spring", "answer": "scalar",
     "why": "Energy is a scalar; the spring does not prefer one direction."},
    {"item": "The torque turning a wheel", "answer": "vector",
     "why": "A turning effect has a sense of rotation — clockwise or anticlockwise."},
    {"item": "The mass of the Earth", "answer": "scalar", "why": "Mass has no direction."},
    {"item": "The acceleration of a freely falling body", "answer": "vector",
     "why": "It points downwards, and down is different from any other direction."},
]

# --------------------------------------------------------------------------
# 2.2  Rectangular components
# --------------------------------------------------------------------------

COMPONENT_RULES = [
    {"rule": "Ax = A cos θ", "meaning": "The component of A along the x axis",
     "note": "θ is the angle between A and the +x axis, measured anticlockwise."},
    {"rule": "Ay = A sin θ", "meaning": "The component of A along the y axis",
     "note": "Sin and cos swap over exactly as you would expect at 0° and 90°."},
    {"rule": "Ax² + Ay² = A²", "meaning": "The components are the legs of a right triangle",
     "note": "Squaring and adding the components always gives back the square of "
             "the magnitude - a free self-check on your arithmetic."},
    {"rule": "tan θ = Ay / Ax", "meaning": "The direction from the components",
     "note": "Use atan2, not atan, in code: the quadrant of a negative component "
             "matters and tan loses that information."},
]

COMPONENT_LAB = [
    {"setup": "A 10 N force acts at 0° to the +x axis",
     "ax": 10, "ay": 0, "magnitude": 10, "angle": 0,
     "explain": "cos 0 = 1 and sin 0 = 0, so the whole force lies along x. "
                "A component of zero is normal, not an error."},
    {"setup": "The same 10 N force acts at 90° to the +x axis",
     "ax": 0, "ay": 10, "magnitude": 10, "angle": 90,
     "explain": "Now cos 90 = 0 and sin 90 = 1, so the whole force has moved to y."},
    {"setup": "The same 10 N force acts at 60°",
     "ax": 5, "ay": 8.660254, "magnitude": 10, "angle": 60,
     "explain": "Ax = 10 cos 60 = 5. Ay = 10 sin 60 = 8.66. The components are "
                "smaller than 10 each, because the arrow is not along either axis."},
    {"setup": "A 6 m displacement is 4 m east and 3 m north",
     "ax": 4, "ay": 3, "magnitude": 5, "angle": 36.86989765,
     "explain": "The 3-4-5 right triangle. The resultant is 5 m, not 4 + 3 = 7 m, "
                "because you cannot add two perpendicular lengths by adding them."},
]

RESULTANT_STEPS = [
    "Choose axes. Standard practice is x to the right and y upwards; write down "
    "which way positive is before you start.",
    "Draw every vector head-to-tail from a common origin, using a ruler and a "
    "protractor. The drawing is not decoration - it is where most sign errors get caught.",
    "Write each vector's x and y component in a table. Keep the signs.",
    "Add the x components together; add the y components together. Those two "
    "numbers are the resultant's components.",
    "Rebuild: draw a single arrow from the origin to the point (sum of x, sum of y).",
    "Check: the resultant's magnitude must be smaller than the arithmetic sum of "
    "the magnitudes, and larger than the largest difference between them.",
]

# --------------------------------------------------------------------------
# 2.3 and 2.4  The two products
# --------------------------------------------------------------------------

PRODUCT_CONTRAST = [
    {"property": "Written as", "dot": "A · B", "cross": "A × B"},
    {"property": "Answer is", "dot": "a scalar (a plain number)",
     "cross": "a vector (with magnitude and direction)"},
    {"property": "Formula", "dot": "A B cos θ", "cross": "A B sin θ"},
    {"property": "Zero when", "dot": "θ = 90° (the vectors are perpendicular)",
     "cross": "θ = 0° or 180° (the vectors are parallel)"},
    {"property": "Largest when", "dot": "θ = 0° (the vectors point the same way)",
     "cross": "θ = 90° (the vectors are at right angles)"},
    {"property": "Direction of the answer", "dot": "none - it is just a number",
     "cross": "perpendicular to both, set by the right-hand rule"},
    {"property": "Order matters?", "dot": "No. A · B = B · A (commutative)",
     "cross": "Yes. A × B = -(B × A) (anti-commutative)"},
    {"property": "Distributive?", "dot": "Yes: A · (B + C) = A·B + A·C",
     "cross": "Yes: A × (B + C) = A×B + A×C"},
    {"property": "A with itself", "dot": "A · A = A², which is never negative",
     "cross": "A × A = 0, which is always zero"},
    {"property": "Physics it appears in", "dot": "work (W = F · d), power, "
                                               "scalar products of angular momentum",
     "cross": "torque (τ = r × F), magnetic force, area of a parallelogram"},
]

DOT_PROPERTIES = [
    {"name": "Commutative", "statement": "A · B = B · A",
     "proof": "A·B = AxBx + AyBy = BxAx + ByAy = B·A. The order of the two "
              "products never changed."},
    {"name": "Distributive", "statement": "A · (B + C) = A·B + A·C",
     "proof": "Expand the bracket: Ax(Bx + Cx) + Ay(By + Cy) = AxBx + AxCx + AyBy + AyCy, "
              "which is A·B + A·C."},
    {"name": "Not associative in a useful way", "statement": "(A · B) · C is not a vector product",
     "proof": "A·B is already a number, so multiplying it by a vector is ordinary "
              "multiplication - which is legal but is not a second product of vectors."},
    {"name": "Positive, negative or zero", "statement": "The sign tells you the geometry",
     "proof": "A·B = AB cos θ. cos is positive below 90°, zero at 90° and negative "
              "above 90°. A negative scalar product means the two vectors pull against "
              "each other."},
    {"name": "A·B = |A||B| only when parallel",
     "statement": "Equal to the product of the sizes only if θ = 0°",
     "proof": "The cos θ factor is exactly the fraction of B that lies along A, so "
              "A·B is the length of B's shadow on A."},
]

CROSS_PROPERTIES = [
    {"name": "Anti-commutative", "statement": "A × B = -(B × A)",
     "proof": "AxBy - AyBx = -(BxAy - ByAx). Swapping the vectors reverses the order "
              "of the products and so reverses the sign. This is the single most "
              "important difference from the scalar product."},
    {"name": "Distributive", "statement": "A × (B + C) = A×B + A×C",
     "proof": "The same expansion works because multiplication distributes over "
              "addition, exactly as it does for ordinary numbers."},
    {"name": "Zero for a vector with itself", "statement": "A × A = 0",
     "proof": "AxAx - AxAx = 0. Two identical vectors are parallel, and there is no "
              "angle to turn through, so there is nothing for the cross product to measure."},
    {"name": "Direction by the right-hand rule",
     "statement": "Curl the fingers of your right hand from A to B; the thumb points along A × B",
     "proof": "The rule is a picture of sin θ. At θ = 90° the fingers are perpendicular "
              "and the thumb sticks out at full length; as θ falls to 0° the thumb lies "
              "along your palm and the magnitude shrinks to zero."},
    {"name": "Magnitude is the area", "statement": "|A × B| = A B sin θ is the area of the parallelogram",
     "proof": "Taking A B sin θ is exactly base × height, where sin θ supplies the "
              "perpendicular height. So the cross product literally measures area."},
]

WORK_APPLICATIONS = [
    {"situation": "A box pushed along a floor",
     "force": "Steady push at 30° above the horizontal",
     "work": "Only the horizontal component does work against friction; the "
             "vertical component is spent pushing the floor's reaction away."},
    {"situation": "A suitcase pulled by its handle",
     "force": "Pull at an upward angle",
     "work": "The upward component makes pushing easier by reducing the normal "
             "force and therefore the friction."},
    {"situation": "A brake on a bicycle",
     "force": "The brake pad pushes backwards while the wheel moves forwards",
     "work": "The angle is 180°, so cos 180° = -1 and the work is negative: "
             "energy is being taken out of the wheel, which is exactly what a brake is for."},
    {"situation": "Gravity on a ball rolling down a slope",
     "force": "Weight straight down",
     "work": "Only the component of the weight along the slope does useful work; "
             "the rest presses the ball into the slope."},
]

TORQUE_APPLICATIONS = [
    {"situation": "A door hinges", "force": "Push near the handle, at right angles",
     "note": "τ = r F sin 90° = rF. Push in the same direction as the door and "
             "sin θ = 0, so nothing turns at all - the classic complaint about "
             "hinge placement."},
    {"situation": "A spanner on a nut", "force": "Pull perpendicular to the handle",
     "note": "sin 90° = 1, the largest possible torque for the same force."},
    {"situation": "A spinning wheel", "force": "Tangential push near the rim",
     "note": "The force is at right angles to the radius, so the whole of it "
             "contributes to the turning."},
    {"situation": "A car's steering wheel", "force": "Both hands on opposite sides",
     "note": "The two torques are in the same rotational sense, so they add - "
             "this is why a steering wheel is held with both hands."},
]

# --------------------------------------------------------------------------
# Worked problems
# --------------------------------------------------------------------------

WORKED_PROBLEMS = [
    {
        "id": "WP1",
        "title": "Classifying quantities, and why",
        "level": "Foundation",
        "slos": ["2.1.1"],
        "question": "State whether each quantity is a scalar or a vector, and justify your answer: "
                    "(a) the mass of a car, (b) the momentum of a car, (c) the temperature of the "
                    "engine, (d) the torque applied to the steering wheel.",
        "known": [
            "Definition: a vector needs a magnitude and a direction; a scalar needs only a magnitude.",
            "Momentum is mass × velocity, and velocity is a vector.",
            "Torque is a turning effect, which has a sense of rotation.",
        ],
        "find": "the classification of each of the four quantities, with reasons",
        "equation": r"\text{vector} \iff \text{the answer depends on direction}",
        "conversions": [
            "No units need converting; this is about the kind of quantity, not its size.",
        ],
        "substitution": r"(a)\; m = 1200\ \text{kg} \qquad (b)\; \mathbf{p} = m\mathbf{v}",
        "calculation": [
            "Step 1 — mass: a mass of 1200 kg is 1200 kg wherever the car is and whichever way it points, so it is a scalar.",
            "Step 2 — momentum: it is mass multiplied by velocity. Because velocity is a vector, momentum is a vector; a car travelling at 20 m/s east and the same speed north have different momenta.",
            "Step 3 — temperature: 90 °C is 90 °C. There is no direction to add, so temperature is a scalar.",
            "Step 4 — torque: it describes a turning effect, which must have a sense (clockwise or anticlockwise) about an axis, so torque is a vector.",
        ],
        "unit_check": r"\mathbf{p}: \mathrm{kg\,m\,s^{-1}} \quad \tau: \mathrm{N\,m} \quad "
                      r"\text{both carry direction; } m: \mathrm{kg},\ T: \mathrm{K} \text{ do not}",
        "answer": "(a) scalar, (b) vector, (c) scalar, (d) vector",
        "sig_fig_note": "The sizes are quoted to three and two significant figures here, but the "
                        "question only asks for a classification, so no rounding is involved.",
        "assumptions": [
            "Temperature means the thermodynamic temperature (or the reading on the gauge), not the direction of heat flow.",
            "Momentum is taken in the Newtonian sense, p = mv.",
        ],
    },
    {
        "id": "WP2",
        "title": "Resolving a force into components",
        "level": "Foundation",
        "slos": ["2.2.1"],
        "question": "A force of 40 N acts on a box at an angle of 37° above the horizontal. "
                    "Resolve the force into its rectangular components, then find the magnitude and "
                    "direction of the force and check your answer.",
        "known": [
            "Force F = 40 N",
            "Angle θ = 37° measured from the +x axis (the horizontal)",
            "Component formula Ax = A cos θ, Ay = A sin θ",
            "sin 37° = 0.602, cos 37° = 0.799",
        ],
        "find": "the x and y components, the magnitude check, and the direction",
        "equation": r"F_x = F\cos\theta, \qquad F_y = F\sin\theta, \qquad "
                    r"\sqrt{F_x^2 + F_y^2} = F",
        "conversions": [
            "No unit conversion is needed; the answer stays in newtons.",
            "Angles are in degrees here, so the trig functions must be evaluated in degrees, not radians.",
        ],
        "substitution": r"F_x = 40(0.799) = 31.96\ \text{N}, \qquad F_y = 40(0.602) = 24.08\ \text{N}",
        "calculation": [
            "Step 1 — x component: Fx = 40 cos 37° = 40 × 0.799 = 31.96 N, to the right.",
            "Step 2 — y component: Fy = 40 sin 37° = 40 × 0.602 = 24.08 N, upwards.",
            "Step 3 — magnitude check: √(31.96² + 24.08²) = √(1021.4 + 579.8) = √1601.2 = 40.0 N. "
            "This comes back to 40 N, which is the free check that the components are right.",
            "Step 4 — direction check: tan θ = 24.08 / 31.96 = 0.7534, so θ = 37.0°. "
            "The angle returns to what it started as, which confirms both the value and the quadrant.",
        ],
        "unit_check": r"\sqrt{\mathrm{N}^2 + \mathrm{N}^2} = \mathrm{N},\ \text{the same unit as the force}",
        "answer": "Fx ≈ 32.0 N horizontally, Fy ≈ 24.1 N vertically; magnitude 40 N at 37° above the horizontal",
        "sig_fig_note": "40 N is given to one significant figure and 37° to two, so the strict answer "
                        "is 3 × 10¹ N and 2 × 10¹ N. These are written out at full precision here so "
                        "the checking steps are visible.",
        "assumptions": [
            "The box is on a horizontal surface, so x is along the floor and y is vertical.",
            "The angle is measured anticlockwise from the +x axis.",
        ],
    },
    {
        "id": "WP3",
        "title": "The resultant of two forces by components",
        "level": "Developing",
        "slos": ["2.2.1"],
        "question": "Two forces act on the same point. The first has magnitude 20 N at 30° to the "
                    "+x axis, and the second has magnitude 15 N at 120° to the +x axis. Find the "
                    "magnitude and direction of the resultant using rectangular components.",
        "known": [
            "A = 20 N at θ₁ = 30°",
            "B = 15 N at θ₂ = 120°",
            "cos 30° = 0.866, sin 30° = 0.500",
            "cos 120° = -0.500, sin 120° = 0.866",
        ],
        "find": "the resultant R and its angle θ_R to the +x axis",
        "equation": r"R_x = A_x + B_x,\quad R_y = A_y + B_y,\quad "
                    r"R = \sqrt{R_x^2 + R_y^2},\quad \theta_R = \tan^{-1}\!\left(\frac{R_y}{R_x}\right)",
        "conversions": ["Both forces are already in newtons; no conversion is needed."],
        "substitution": r"R_x = 17.32 + (-7.50) = 9.82\ \text{N}, \qquad "
                        r"R_y = 10.00 + 12.99 = 22.99\ \text{N}",
        "calculation": [
            "Step 1 — first vector: Ax = 20 cos 30° = 17.32 N, Ay = 20 sin 30° = 10.00 N.",
            "Step 2 — second vector: Bx = 15 cos 120° = -7.50 N (it points backwards), "
            "By = 15 sin 120° = 12.99 N.",
            "Step 3 — add components: Rx = 17.32 - 7.50 = 9.82 N and Ry = 10.00 + 12.99 = 22.99 N. "
            "Notice that adding the two magnitudes, 20 + 15 = 35 N, is NOT allowed: the two "
            "forces are 90° apart, not in the same direction.",
            "Step 4 — magnitude: R = √(9.82² + 22.99²) = √(96.4 + 528.6) = √625.0 = 25.0 N.",
            "Step 5 — direction: θ_R = tan⁻¹(22.99 / 9.82) = tan⁻¹(2.341) = 66.9°. "
            "Because Rx is positive the resultant lies in the first quadrant.",
            "Step 6 — sanity check: the angle between the forces is 120° - 30° = 90°, so the "
            "resultant must be √(20² + 15²) = 25.0 N exactly, and 25.0 < 35. Both agree.",
        ],
        "unit_check": r"R = \sqrt{\mathrm{N}^2+\mathrm{N}^2} = \mathrm{N};\ \theta_R \text{ is an angle, so it carries no unit}",
        "answer": "R ≈ 25.0 N at 66.9° above the +x axis",
        "sig_fig_note": "Both forces are given to two significant figures and the angles to three, so "
                        "the answer is 25 N at 66.9°. The extra digits shown are working, not a claim of accuracy.",
        "assumptions": [
            "Both forces act on the same point and the same particle, so the forces can be added directly.",
            "The angles are measured anticlockwise from the +x axis.",
        ],
    },
    {
        "id": "WP4",
        "title": "Scalar product and the work done by a force",
        "level": "Developing",
        "slos": ["2.3.1"],
        "question": "A force of 25 N acts on a trolley while it moves 8 m in a straight line. "
                    "The force makes an angle of 60° with the displacement. Calculate the work done, "
                    "and say what would happen if the force acted at 180°.",
        "known": [
            "F = 25 N, d = 8 m, θ = 60°",
            "cos 60° = 0.500, cos 120° = -0.500, cos 180° = -1",
            "Scalar product W = F · d = F d cos θ",
        ],
        "find": "the work done at 60°, and at 180°",
        "equation": r"W = \mathbf{F}\cdot\mathbf{d} = F\,d\,\cos\theta",
        "conversions": [
            "Work is measured in joules, so N × m = J. No other conversion is needed.",
        ],
        "substitution": r"W = 25 \times 8 \times 0.500 = 100\ \text{J}",
        "calculation": [
            "Step 1 — write the product as a magnitude, a magnitude and cos θ: W = 25 × 8 × cos 60°.",
            "Step 2 — evaluate: cos 60° = 0.500, so W = 200 × 0.500 = 100 J.",
            "Step 3 — interpret the sign: the force has a component of 25 cos 60° = 12.5 N along "
            "the displacement, and 12.5 N × 8 m = 100 J. Only that component moves the trolley "
            "in its own direction; the rest pushes sideways.",
            "Step 4 — at 180°: cos 180° = -1, so W = 25 × 8 × (-1) = -200 J. The work is negative "
            "because the force acts directly against the motion, which is exactly what happens when "
            "something brakes a trolley.",
        ],
        "unit_check": r"\mathrm{N\,m} = \mathrm{J}",
        "answer": "W = +100 J at 60°; W = -200 J at 180°",
        "sig_fig_note": "25 N and 8 m are each to one significant figure, so the strict answers are "
                        "1 × 10² J and -2 × 10² J.",
        "assumptions": [
            "The force is constant in magnitude and direction while the trolley moves in a straight line.",
            "No other forces are doing work, so this is the net work on the trolley.",
        ],
    },
    {
        "id": "WP5",
        "title": "Vector product and the torque on a wheel",
        "level": "Challenge",
        "slos": ["2.4.1"],
        "question": "A force of 30 N is applied at the end of a 0.40 m spanner, at an angle of "
                    "70° to the handle measured from the axis of rotation. Calculate the magnitude "
                    "of the torque and state its direction using the right-hand rule. Then explain "
                    "what happens to the torque if the angle is halved to 35°.",
        "known": [
            "F = 30 N, r = 0.40 m, θ₁ = 70°, θ₂ = 35°",
            "sin 70° = 0.9397, sin 35° = 0.5736",
            "τ = r F sin θ",
        ],
        "find": "|τ| at 70°, its direction, and the ratio τ(35°)/τ(70°)",
        "equation": r"\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F},\qquad "
                    r"\tau = r\,F\,\sin\theta",
        "conversions": [
            "Torque is measured in N m. Leave it in N m unless you are asked for energy, in which case 1 N m = 1 J.",
        ],
        "substitution": r"\tau_1 = 0.40 \times 30 \times 0.9397 = 11.28\ \text{N m}, \qquad "
                        r"\tau_2 = 0.40 \times 30 \times 0.5736 = 6.88\ \text{N m}",
        "calculation": [
            "Step 1 — only the perpendicular component of the force turns the spanner: F_perp = F sin θ = 30 × 0.9397 = 28.19 N.",
            "Step 2 — magnitude: τ = r F_perp = 0.40 × 28.19 = 11.28 N m.",
            "Step 3 — direction: curl the fingers of your right hand from r to F; the thumb gives the "
            "sense of rotation. Because sin 70° is positive the torque is along the axis in the "
            "sense that turns the spanner the way the force is pushing it, not the opposite way.",
            "Step 4 — halving the angle: τ₂ = 0.40 × 30 × sin 35° = 6.88 N m, so τ₂/τ₁ = 0.61.",
            "Step 5 — the lesson: torque is NOT proportional to the angle. Halving the angle reduced "
            "the torque to about 61 % of its old value, not to 50 %, because the relationship is "
            "sinusoidal, not linear.",
        ],
        "unit_check": r"\mathrm{m\,N} = \mathrm{N\,m};\ \text{the ratio }\tau_2/\tau_1 \text{ is dimensionless}",
        "answer": "|τ| = 11.3 N m at 70°, directed along the axis by the right-hand rule; 6.88 N m at 35°, a ratio of 0.61",
        "sig_fig_note": "30 N and 0.40 m are each to two significant figures, so τ = 11 N m and "
                        "τ₂ = 6.9 N m.",
        "assumptions": [
            "The spanner is straight and pivots about one end.",
            "The force is applied at the far end and is constant while it acts.",
        ],
    },
    {
        "id": "WP6",
        "title": "Choosing the right tool: dot or cross",
        "level": "Developing",
        "slos": ["2.3.1", "2.4.1"],
        "question": "For each situation below, say whether a scalar product or a vector product is "
                    "involved, and write the resulting equation: (a) the work done in moving a body "
                    "3 m along a straight line against a steady 10 N force, (b) the magnetic force on "
                    "a current-carrying wire of length 0.5 m carrying 2 A in a field of 0.3 T at "
                    "right angles to the wire.",
        "known": [
            "Work involves a force and a displacement, both vectors, and the answer is energy (a scalar).",
            "Magnetic force involves a current (a scalar) and a field (a vector), and the answer is a force (a vector).",
        ],
        "find": "the correct product and the numerical answer in each case",
        "equation": r"W = \mathbf{F}\cdot\mathbf{d},\qquad \mathbf{F} = I\,\mathbf{L}\times\mathbf{B}",
        "conversions": [
            "N m and J are the same unit; 1 N m = 1 J.",
            "The current in amperes is a scalar, so I is not part of either product.",
        ],
        "substitution": r"(a)\; W = 10 \times 3 \times \cos 180^\circ = -30\ \text{J}, \qquad "
                        r"(b)\; F = 2 \times 0.5 \times 0.3 \times \sin 90^\circ = 0.30\ \text{N}",
        "calculation": [
            "Step 1 — decide the type from the ANSWER, not from the inputs. Work is measured in "
            "joules, a scalar, so it must come from a scalar product.",
            "Step 2 — the body moves 3 m along the line and the 10 N force acts against that motion, "
            "so θ = 180°: W = 10 × 3 × cos 180° = -30 J. Negative because energy is being put into "
            "the body rather than taken out.",
            "Step 3 — the magnetic force is a vector, so it must come from a vector product.",
            "Step 4 — sin 90° = 1, so the full length counts: F = 2 × 0.5 × 0.3 × 1 = 0.30 N.",
            "Step 5 — check both units: J for work and N for force. If a unit came out as N m for a "
            "force, or J for a torque-per-second, the wrong product had been chosen.",
        ],
        "unit_check": r"(a)\ \mathrm{N\,m} = \mathrm{J};\qquad (b)\ \mathrm{A\,m\,T} = \mathrm{N}",
        "answer": "(a) scalar product, W = -30 J; (b) vector product, F = 0.30 N",
        "sig_fig_note": "All the values are given to one or two significant figures, so -30 J and "
                        "0.30 N are the appropriate rounded answers.",
        "assumptions": [
            "In (b) the wire is perpendicular to the magnetic field, which is the largest-force case.",
            "The force in (a) acts exactly opposite to the displacement.",
        ],
    },
]

# --------------------------------------------------------------------------
# Practice questions
# --------------------------------------------------------------------------

PRACTICE_QUESTIONS = [
    # 2.1.1
    {"id": "P1", "category": "Scalar or vector", "type": "mcq", "slo": "2.1.1",
     "prompt": "Which of these is a vector quantity?",
     "options": ["The mass of a ball", "The temperature of a room",
                 "The velocity of a car", "The energy stored in a battery"],
     "answer": 2,
     "hint": "A vector needs a direction that changes what is being described.",
     "explanation": "Velocity has size and direction: 60 km/h north is a different "
                    "situation from 60 km/h east. Mass, temperature and energy are "
                    "the same number wherever you are."},
    {"id": "P2", "category": "Scalar or vector", "type": "mcq", "slo": "2.1.1",
     "prompt": "A car travels once round a circular track at a steady 20 m/s. Its velocity is...",
     "options": ["constant, because the speed is constant",
                 "constant, because the direction never changes",
                 "changing, because the direction changes even though the speed does not",
                 "zero, because the car returns to its start"],
     "answer": 2,
     "hint": "Velocity = speed + direction. Which of those is changing?",
     "explanation": "The speed is steady but the direction turns through a full circle "
                    "every lap, so the velocity changes continuously. This is exactly "
                    "why a velocity can be a centripetal acceleration even at constant speed."},
    {"id": "P3", "category": "Scalar or vector", "type": "numeric", "slo": "2.1.1",
     "prompt": "How many of the following are vectors: mass, displacement, work, momentum, "
               "temperature, acceleration? Enter just the number.",
     "answer": 3, "tolerance": 0, "unit": "vectors",
     "hint": "Go through the list one at a time and ask whether the direction changes the answer.",
     "explanation": "Displacement, momentum and acceleration are vectors, so the answer is 3. "
                    "Work is the trap: it is written as the scalar product F·d and is "
                    "measured in joules, so it is a scalar even though it is built from two "
                    "vectors. Mass and temperature are scalars for the usual reason."},
    {"id": "P4", "category": "Scalar or vector", "type": "mcq", "slo": "2.1.1",
     "prompt": "Which statement about a vector quantity is correct?",
     "options": ["Adding two vectors means adding their magnitudes",
                 "Two vectors with the same magnitude in different directions are different vectors",
                 "A vector can be described completely by one number and a unit",
                 "Multiplying a vector by zero makes it larger"],
     "answer": 1,
     "hint": "Think about 5 N north versus 5 N south.",
     "explanation": "Direction is part of what a vector is. 5 N north and 5 N south have "
                    "the same magnitude but are different vectors, and their sum is zero."},

    # 2.2.1
    {"id": "P5", "category": "Rectangular components", "type": "numeric", "slo": "2.2.1",
     "prompt": "A vector has magnitude 10 and direction 60° from the +x axis. Enter its x "
               "component (the number only).",
     "answer": 5.0, "tolerance": 0.05, "unit": "",
     "hint": "The x component uses cos, not sin.",
     "explanation": "Ax = A cos 60° = 10 × 0.5 = 5.0. The y component would be "
                    "10 sin 60° = 8.66."},
    {"id": "P6", "category": "Rectangular components", "type": "numeric", "slo": "2.2.1",
     "prompt": "Two vectors are given as A = (3, 4) and B = (-1, 2). Enter the magnitude of "
               "their sum A + B. Enter the number only.",
     "answer": 6.4031242374328485, "tolerance": 0.02, "unit": "",
     "hint": "Add the components first, then take the square root of the sum of their squares.",
     "explanation": "A + B = (3 - 1, 4 + 2) = (2, 6). Its magnitude is √(4 + 36) = √40 = 6.40. "
                    "Note the sum's magnitude is smaller than 5 + √5 = 7.24, as it must be."},
    {"id": "P7", "category": "Rectangular components", "type": "numeric", "slo": "2.2.1",
     "prompt": "A cyclist rides 3.0 km east and then 4.0 km north. Enter the magnitude of "
               "the displacement in km (the number only).",
     "answer": 5.0, "tolerance": 0.05, "unit": "km",
     "hint": "This is a 3-4-5 right triangle. You cannot add 3 + 4.",
     "explanation": "The displacement is the straight line from start to finish: "
                    "√(3² + 4²) = 5.0 km. The distance actually ridden is 7.0 km, which "
                    "is a different quantity."},
    {"id": "P8", "category": "Rectangular components", "type": "mcq", "slo": "2.2.1",
     "prompt": "The vector 3î + 4ĵ has magnitude...",
     "options": ["7", "12", "5", "1"],
     "answer": 2,
     "hint": "Pythagoras on the components.",
     "explanation": "√(3² + 4²) = √25 = 5. Components are the legs of a right triangle, "
                    "so they combine with the square root of the sum of squares, not by "
                    "ordinary addition."},
    {"id": "P9", "category": "Rectangular components", "type": "numeric", "slo": "2.2.1",
     "prompt": "A 12 N force acts at 30° above the horizontal. Enter the horizontal component "
               "of the force in newtons (the number only).",
     "answer": 10.392304845413264, "tolerance": 0.05, "unit": "N",
     "hint": "Horizontal means along x, so use cos 30°.",
     "explanation": "Fx = 12 cos 30° = 12 × 0.866 = 10.4 N. The vertical component is "
                    "12 sin 30° = 6.0 N."},
    {"id": "P10", "category": "Rectangular components", "type": "mcq", "slo": "2.2.1",
     "prompt": "A vector points 150° from the +x axis. What are the signs of its x and y components?",
     "options": ["x positive, y positive", "x negative, y positive",
                 "x positive, y negative", "both negative"],
     "answer": 1,
     "hint": "150° is past vertical. Which side of the y axis are you on?",
     "explanation": "150° is in the second quadrant: cos 150° is negative and sin 150° is "
                    "positive. So the x component points backwards and the y component "
                    "points upwards. Getting the quadrant wrong is the single most common "
                    "error in component questions."},

    # 2.3.1
    {"id": "P11", "category": "Scalar product", "type": "numeric", "slo": "2.3.1",
     "prompt": "Two vectors have magnitudes 5 and 4 with an angle of 60° between them. "
               "Enter their scalar product (the number only).",
     "answer": 10.0, "tolerance": 0.1, "unit": "",
     "hint": "A·B = AB cos θ.",
     "explanation": "5 × 4 × cos 60° = 20 × 0.5 = 10.0. The result is a plain number with "
                    "no direction, which is why this is called the scalar product."},
    {"id": "P12", "category": "Scalar product", "type": "mcq", "slo": "2.3.1",
     "prompt": "When is the scalar product of two vectors zero?",
     "options": ["When they are parallel", "When they are perpendicular",
                 "When one of them is zero in size only",
                 "When they point in opposite directions"],
     "answer": 1,
     "hint": "cos θ is zero at one particular angle.",
     "explanation": "cos 90° = 0, so perpendicular vectors give a scalar product of zero. "
                    "Parallel vectors give ±AB, which is the largest magnitude possible."},
    {"id": "P13", "category": "Scalar product", "type": "numeric", "slo": "2.3.1",
     "prompt": "A force of 12 N acts at 120° to a displacement of 3 m. Enter the work done "
               "(the number only, in joules).",
     "answer": -18.0, "tolerance": 0.2, "unit": "J",
     "hint": "W = F d cos θ, and cos 120° is negative.",
     "explanation": "12 × 3 × cos 120° = 36 × (-0.5) = -18 J. Negative work means the force "
                    "opposes the displacement, so energy is being put into the system."},
    {"id": "P14", "category": "Scalar product", "type": "mcq", "slo": "2.3.1",
     "prompt": "Which statement about the scalar product is true?",
     "options": ["A · B = -B · A",
                 "A · B = B · A, so the order does not matter",
                 "A × A = 0 always",
                 "A · B has a direction perpendicular to A"],
     "answer": 1,
     "hint": "Compare A·B = AxBx + AyBy with B·A = BxAx + ByAy.",
     "explanation": "Multiplication of numbers commutes, so the scalar product is "
                    "commutative: A·B = B·A. The vector product behaves the opposite way, "
                    "which is option A's statement."},
    {"id": "P15", "category": "Scalar product", "type": "numeric", "slo": "2.3.1",
     "prompt": "A vector A = (2, 3). Enter A · A, the scalar product of A with itself.",
     "answer": 13.0, "tolerance": 0.01, "unit": "",
     "hint": "A · A is always the square of the magnitude.",
     "explanation": "2×2 + 3×3 = 13. Equivalently, |A| = √13, so A·A = |A|² = 13. This is "
                    "never negative for any vector."},

    # 2.4.1
    {"id": "P16", "category": "Vector product", "type": "numeric", "slo": "2.4.1",
     "prompt": "Two vectors have magnitudes 6 and 3 with an angle of 30° between them. "
               "Enter the magnitude of their vector product (the number only).",
     "answer": 9.0, "tolerance": 0.1, "unit": "",
     "hint": "|A × B| = AB sin θ.",
     "explanation": "6 × 3 × sin 30° = 18 × 0.5 = 9.0. The magnitude of the vector product "
                    "is also the area of the parallelogram the two vectors enclose."},
    {"id": "P17", "category": "Vector product", "type": "mcq", "slo": "2.4.1",
     "prompt": "Where does A × B point?",
     "options": ["Along A", "Along B", "Perpendicular to both A and B",
                 "At an angle θ to A"],
     "answer": 2,
     "hint": "Use the right-hand rule, or remember what area the product represents.",
     "explanation": "A × B is perpendicular to both vectors, with its sense fixed by the "
                    "right-hand rule. In the xy plane that means straight out of or into "
                    "the page."},
    {"id": "P18", "category": "Vector product", "type": "numeric", "slo": "2.4.1",
     "prompt": "A force of 20 N acts at the end of a 0.50 m spanner, perpendicular to the "
               "spanner. Enter the torque in N m (the number only).",
     "answer": 10.0, "tolerance": 0.1, "unit": "N m",
     "hint": "Perpendicular means sin 90°, which is 1.",
     "explanation": "τ = r F sin 90° = 0.50 × 20 × 1 = 10 N m. A force perpendicular to "
                    "the arm gives the largest torque possible for that force."},
    {"id": "P19", "category": "Vector product", "type": "mcq", "slo": "2.4.1",
     "prompt": "Which is the correct relationship between the two products?",
     "options": ["A · B = A × B", "A · B = -A × B",
                 "A · B = B × A, so A × B = -(A · B)",
                 "A × B = -(B × A), while A · B = B · A"],
     "answer": 3,
     "hint": "Try two simple vectors in each product and compare.",
     "explanation": "The scalar product commutes (A·B = B·A) while the vector product "
                    "anti-commutes (A×B = -(B×A)). Using A = î, B = ĵ: A·B = 0 and A×B = k̂, "
                    "so the two products are clearly different quantities."},
    {"id": "P20", "category": "Vector product", "type": "numeric", "slo": "2.4.1",
     "prompt": "Let A = (2, 0) and B = (0, 3). Enter the z-component of A × B (the number only, "
               "positive means out of the page).",
     "answer": 6.0, "tolerance": 0.01, "unit": "",
     "hint": "The z-component of the cross product is Ax·By - Ay·Bx.",
     "explanation": "Ax·By - Ay·Bx = 2×3 - 0×0 = 6. Positive, so it points out of the page: "
                    "going from A (along x) to B (along y) is anticlockwise, so the right-hand "
                    "thumb points towards you."},
    {"id": "P21", "category": "Vector product", "type": "mcq", "slo": "2.4.1",
     "prompt": "Two vectors point in exactly the same direction. What is their vector product?",
     "options": ["AB, the largest possible value",
                 "A + B", "−AB", "Zero"],
     "answer": 3,
     "hint": "sin 0° is what?",
     "explanation": "sin 0° = 0, so A × A = 0. Parallel vectors have no angle between them, "
                    "so there is nothing for the cross product to measure. The scalar product "
                    "of parallel vectors, by contrast, is AB."},

    # Short numerical
    {"id": "P22", "category": "Short numerical", "type": "numeric", "slo": "2.2.1",
     "prompt": "Vector A has components (6, 8). Enter the magnitude of A (the number only).",
     "answer": 10.0, "tolerance": 0.01, "unit": "",
     "hint": "Pythagoras on the components.",
     "explanation": "√(36 + 64) = √100 = 10. This is the 6-8-10 triangle, and the check "
                    "√(Ax² + Ay²) = A should always hold."},
    {"id": "P23", "category": "Short numerical", "type": "numeric", "slo": "2.3.1",
     "prompt": "Two vectors of magnitude 4 and 6 point in opposite directions. Enter their "
               "scalar product (the number only).",
     "answer": -24.0, "tolerance": 0.1, "unit": "",
     "hint": "Opposite directions means θ = 180°.",
     "explanation": "cos 180° = -1, so A·B = 4 × 6 × (-1) = -24. Opposite vectors give the "
                    "most negative scalar product possible."},
    {"id": "P24", "category": "Short numerical", "type": "numeric", "slo": "2.4.1",
     "prompt": "Two vectors of magnitude 4 and 6 point in opposite directions. Enter the "
               "magnitude of their vector product (the number only).",
     "answer": 0.0, "tolerance": 0.001, "unit": "",
     "hint": "Opposite directions means θ = 180°. What is sin 180°?",
     "explanation": "sin 180° = 0, so |A × B| = 0. This is the mirror image of the previous "
                    "question: opposite vectors minimise the scalar product and kill the "
                    "vector product."},

    {"id": "P25", "category": "Components", "type": "mcq", "slo": "2.2.2",
     "prompt": "Why is a vector resolved into rectangular components before two vectors are added?",
     "options": ["because components are easier to draw",
                 "because x and y are perpendicular, so each can be added on its own and recombined",
                 "because the angle between them becomes 90 degrees",
                 "because the resultant is always larger than either vector"],
     "answer": 1,
     "hint": "Perpendicular axes do not interfere with each other.",
     "explanation": "Because the axes are perpendicular. The total change in x and the total "
                    "change in y can each be found by ordinary addition, and the two are then "
                    "independent. Adding whole vectors before resolving them means adding "
                    "lengths, which is meaningless."},
    {"id": "P26", "category": "Resultants", "type": "numeric", "slo": "2.2.3",
     "prompt": "A vector of magnitude 6 N acts at 0 degrees to the x axis and another of "
               "magnitude 8 N acts at 90 degrees to the x axis. Find the magnitude of the "
               "resultant. Enter the number only.",
     "answer": 10.0, "tolerance": 0.1, "unit": "N",
     "hint": "Rx = 6 cos 0 + 8 cos 90, Ry = 6 sin 0 + 8 sin 90, then |R| = sqrt(Rx^2 + Ry^2).",
     "explanation": "Rx = 6 + 0 = 6 N and Ry = 0 + 8 = 8 N, so |R| = sqrt(36 + 64) = 10 N. "
                    "This is a 6-8-10 triangle: whenever the two vectors are at right "
                    "angles the resultant is the hypotenuse."},
    {"id": "P27", "category": "Scalar product", "type": "numeric", "slo": "2.3.2",
     "prompt": "Two vectors of magnitudes 5 N and 12 N make an angle of 90 degrees. Find "
               "their scalar product. Enter the number only.",
     "answer": 0.0, "tolerance": 0.1, "unit": "N m",
     "hint": "A.B = AB cos(theta), and cos 90 degrees is zero.",
     "explanation": "5 x 12 x cos 90 = 0. Perpendicular vectors have no component along one "
                    "another, so their scalar product is exactly zero however long they are. "
                    "This is why a force perpendicular to a displacement does no work."},
    {"id": "P28", "category": "Scalar product", "type": "mcq", "slo": "2.3.3",
     "prompt": "Which statement about the scalar product is false?",
     "options": ["A.B is a scalar, so it has magnitude but no direction",
                 "A.B = B.A", "A.(B.C) equals (A.B).C",
                 "A.B is negative when the vectors point in opposite directions"],
     "answer": 2,
     "hint": "Check which kind of quantity each side produces.",
     "explanation": "The scalar product is **not associative**. B.C is already a scalar, so "
                    "A.(B.C) is a scalar, while (A.B).C is a vector. They are different kinds "
                    "of quantity and cannot be equal."},
    {"id": "P29", "category": "Vector product", "type": "numeric", "slo": "2.4.2",
     "prompt": "Two vectors of magnitudes 4 m and 6 m make an angle of 30 degrees. Find the "
               "magnitude of their vector product. Enter the number only.",
     "answer": 12.0, "tolerance": 0.2, "unit": "m m",
     "hint": "|A x B| = AB sin(theta).",
     "explanation": "4 x 6 x sin 30 = 24 x 0.5 = 12. Note it is **sin**, not cos: the cross "
                    "product is largest when the vectors are perpendicular, and zero when they "
                    "are parallel. The scalar product behaves the opposite way round."},
    {"id": "P30", "category": "Vector product", "type": "mcq", "slo": "2.4.3",
     "prompt": "The vector product A x B is zero when...",
     "options": ["A and B are perpendicular", "A and B are parallel",
                 "either vector is zero length", "the angle is 90 degrees"],
     "answer": 1,
     "hint": "Ask what the parallelogram looks like.",
     "explanation": "When the vectors are parallel the parallelogram they span collapses to a "
                    "line, so its area - the magnitude of the cross product - is zero. "
                    "Perpendicularity maximises it. This is exactly the opposite of the "
                    "scalar product."},
]

# --------------------------------------------------------------------------
# References
# --------------------------------------------------------------------------

REFERENCES = [
    {"short": "OpenStax University Physics Vol. 1",
     "title": "University Physics Volume 1: Mechanics",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/university-physics-volume-1",
     "used_for": "Chapter 2 on vectors, including the scalar and vector products and their properties."},
    {"short": "Sears and Zemansky solutions",
     "title": "University Physics with Modern Physics, worked examples for vectors",
     "org": "Young & Freedman, Pearson",
     "url": "https://www.pearson.com/en-us/subject-catalog/p/university-physics-with-modern-physics/",
     "used_for": "Worked component-addition problems and the right-hand rule convention."},
    {"short": "HyperPhysics",
     "title": "Vectors and vector products",
     "org": "Georgia State University",
     "url": "https://hyperphysics.phy-astr.gsu.edu/hbase/vector/vector.html",
     "used_for": "Compact reference tables for the scalar and vector product properties."},
    {"short": "NPTEL / IIT course notes",
     "title": "Engineering Mechanics: vector algebra for beginners",
     "org": "Indian Institute of Technology",
     "url": "https://nptel.ac.in/courses",
     "used_for": "The component method taught step by step, matching the sequence used in this station."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 2",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 2.1.1, 2.2.1, 2.3.1 and 2.4.1."},
]
