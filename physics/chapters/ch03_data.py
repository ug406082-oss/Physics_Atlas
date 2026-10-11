"""Chapter 3 content: Motion in One Dimension.

Twelve outcomes across five syllabus sections. The chapter carries three
interactive tools that belong to it alone: a **motion lab** where you set u and a
and watch position, velocity and acceleration graphs together; a **collision
bench** where two bodies are launched and momentum and kinetic energy are tracked
on both sides; and a **force–displacement work bench** where the area under the
curve is integrated for you.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Learning outcomes
# --------------------------------------------------------------------------

SLOS = [
    {"id": "3.1.1", "text": "Derive equations of motion for a body moving with uniform acceleration in a straight line.",
     "simple": "Get v = u + at, s = ut + ½at² and v² = u² + 2as — and know why each one only works when the acceleration is constant.",
     "taught": "Equations of motion", "activity": "Motion lab with linked position, velocity and acceleration graphs",
     "check": "Guided practice: solve for each missing quantity and verify with the third equation"},
    {"id": "3.1.2", "text": "Solve word problems related to uniformly accelerated motion including free fall.",
     "simple": "Apply the equations to real problems, including falling bodies where a = g = 9.8 m/s².",
     "taught": "Free fall and word problems", "activity": "Free-fall calculator with orbit and escape-speed comparison",
     "check": "Guided practice: numerical problems on thrown, dropped and freely falling bodies"},
    {"id": "3.2.1", "text": "Describe law of conservation of linear momentum.",
     "simple": "In a closed system with no external force, total momentum stays exactly the same.",
     "taught": "Conservation of momentum", "activity": "Momentum ledger that must balance before and after",
     "check": "Guided practice: compute total momentum before and after and show it is unchanged"},
    {"id": "3.2.2", "text": "Exemplify the law in: karate chops, car crashes, ball and bat, rocket motion.",
     "simple": "See momentum being handed over in four everyday collisions.",
     "taught": "Momentum in the real world", "activity": "Four worked real-world examples with the momentum ledger",
     "check": "Guided practice: identify the system, the impulse and the momentum change in each case"},
    {"id": "3.2.3", "text": "Define elastic and inelastic collision.",
     "simple": "Elastic: momentum and kinetic energy both conserved. Inelastic: only momentum; the rest becomes heat, sound and deformation.",
     "taught": "Elastic and inelastic collisions", "activity": "Energy bars that visibly drop on an inelastic hit",
     "check": "Guided practice: classify collisions and justify with momentum and kinetic energy"},
    {"id": "3.2.4", "text": "Apply law of conservation of momentum to study elastic collision between two bodies in one dimension.",
     "simple": "Derive and use the final velocities after a one-dimensional elastic collision.",
     "taught": "Elastic collisions in one dimension", "activity": "Collision bench restricted to elastic hits",
     "check": "Guided practice: apply the elastic-collision formulas and confirm both conservations"},
    {"id": "3.2.5", "text": "Apply law of conservation of momentum in one and two dimensions in solving word problems.",
     "simple": "Handle oblique collisions by keeping momentum in x and y separately.",
     "taught": "Two-dimensional collisions", "activity": "Oblique collision bench with the line of centres drawn",
     "check": "Guided practice: two-dimensional collision problems solved component by component"},
    {"id": "3.3.1", "text": "Describe work as the dot product of force and displacement.",
     "simple": "W = F·d = Fd cos θ. Positive, negative or zero depending on the angle.",
     "taught": "Work as a dot product", "activity": "Work bench with a live force–displacement diagram",
     "check": "Guided practice: sign-check work problems at 0°, 90° and 180°"},
    {"id": "3.3.2", "text": "Deduce the work done from force-displacement graphs.",
     "simple": "The work done is the area under a force–displacement curve, found by the trapezium rule.",
     "taught": "Area under F–d graphs", "activity": "Trapezium-rule integrator with a draggable force profile",
     "check": "Guided practice: integrate F–d graphs and interpret negative area"},
    {"id": "3.4.1", "text": "Differentiate between conservative and non-conservative fields.",
     "simple": "Conservative forces store energy in a potential and give path-independent work; non-conservative ones dissipate it.",
     "taught": "Conservative and non-conservative fields", "activity": "Two-route test: work along a direct path and a detour",
     "check": "Guided practice: classify fields and state why the work is or is not path-dependent"},
    {"id": "3.5.1", "text": "Deduce the work-energy theorem in non-resistive and resistive medium.",
     "simple": "Net work done on a body equals its change in kinetic energy, whether or not friction is present.",
     "taught": "The work-energy theorem", "activity": "Theorem checker that compares measured work with the change in kinetic energy",
     "check": "Guided practice: separate the work into each force and confirm the sum equals ΔK"},
    {"id": "3.5.2", "text": "Solve word problems related to the work-energy theorem.",
     "simple": "Use W = ΔK to solve numerical problems, including ones where friction removes energy.",
     "taught": "Work–energy problems", "activity": "Problem generator with friction as a settable parameter",
     "check": "Guided practice: numerical work–energy problems with and without friction"},
]

STATIONS = [
    {"key": "overview", "label": "🗺️ Your route & outcomes", "slos": []},
    {"key": "equations", "label": "📈 Equations of motion", "slos": ["3.1.1"]},
    {"key": "freefall", "label": "🍎 Free fall", "slos": ["3.1.2"]},
    {"key": "momentum", "label": "💥 Conservation of momentum", "slos": ["3.2.1", "3.2.2"]},
    {"key": "collisions", "label": "⚔️ Elastic & inelastic collisions", "slos": ["3.2.3", "3.2.4"]},
    {"key": "oblique", "label": "🎯 Collisions in two dimensions", "slos": ["3.2.5"]},
    {"key": "work", "label": "🛠️ Work and F–d graphs", "slos": ["3.3.1", "3.3.2"]},
    {"key": "fields", "label": "🧭 Conservative & non-conservative fields", "slos": ["3.4.1"]},
    {"key": "energy", "label": "⚡ The work-energy theorem", "slos": ["3.5.1", "3.5.2"]},
    {"key": "worked", "label": "🧮 Worked problems", "slos": []},
    {"key": "practice", "label": "🧠 Practice", "slos": []},
    {"key": "tutor", "label": "🤖 Atlas Tutor (offline AI)", "slos": []},
    {"key": "references", "label": "📚 References", "slos": []},
]

BIG_IDEAS = [
    ("Uniform acceleration is a special promise.",
     "These equations only hold when the acceleration is constant. Drop a stone and "
     "they hold to high accuracy; throw a ball against a wall and they do not apply "
     "at all."),
    ("Momentum is conserved; energy is not, by law.",
     "In every collision the momentum ledger balances exactly. Whether the kinetic "
     "energy also balances is a separate question, and the answer is usually no."),
    ("Work is the area, not the force.",
     "How much work a force does depends on both its size and how far it acts "
     "through. The picture of the area under the F–d graph makes that automatic."),
]

TAG = "CHAPTER 3 · OPEN"
INTRO = (
    "One dimension, but twelve outcomes — and the busiest chapter in the first half "
    "of the book. Motion under a constant acceleration, the conservation of momentum, "
    "collisions in one and two dimensions, work from force–displacement graphs, "
    "conservative fields and the work–energy theorem all live here. Three benches are "
    "waiting: a motion lab, a collision bench and a work bench."
)
ROUTE = ("Equations of motion → Free fall → Momentum → Collisions → 2-D collisions → "
         "Work → Fields → Work-energy theorem → Worked problems → Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("g taken as 9.8 m s⁻²", "warn"),
                 ("Simulated measurement data", "mute"),
                 ("Answers computed by this app", "good")]

NOTES = [
    ("⚠ WATCH OUT", "Choosing the wrong equation is the most common error",
     "You have three equations and three unknowns in {u, v, a, s, t}. Find which "
     "quantity is *missing* and pick the equation that does not contain it. No v? "
     "Use s = ut + ½at². No t? Use v² = u² + 2as. Write the unknown down before "
     "you open the formula."),
    ("🎯 EXAM TIP", "Always say which body you are following",
     "In a collision, u₁ and u₂ are both measured *before* the collision and v₁ "
     "and v₂ *after*. Mixing them up silently changes the sign of your answer. "
     "Writing “before:” and “after:” beside each set costs one line and removes "
     "the whole class of error."),
    ("🔬 HONEST LIMIT", "The collision formulas assume smooth spheres and a single impulse",
     "Real collisions last for a finite time and the force varies through it, so "
     "the velocities are averages over that contact. The impulse–momentum theorem "
     "is the honest statement; the closed-form velocities are its solution for a "
     "clean idealised contact."),
]

# --------------------------------------------------------------------------
# 3.1  Equations of motion
# --------------------------------------------------------------------------

KINEMATIC_EQUATIONS = [
    {"name": "First equation", "formula": r"v = u + a\,t", "uses": "u, a, t → v",
     "says": "Velocity changes by a × t. If a is zero, velocity is constant.",
     "check": r"[L T^{-1}] = [L T^{-1}]"},
    {"name": "Second equation", "formula": r"s = u\,t + \tfrac{1}{2} a\,t^2", "uses": "u, a, t → s",
     "says": "Displacement is the area under the velocity–time graph: a rectangle "
             "of height u and width t, plus a triangle of height at and width t.",
     "check": r"[L] = [L T^{-1}][T] + [L T^{-2}][T^2]"},
    {"name": "Third equation", "formula": r"v^2 = u^2 + 2 a\,s", "uses": "u, a, s → v",
     "says": "Time has been eliminated. This is the one to reach for when the "
             "problem never mentions time.",
     "check": r"[L^2 T^{-2}] = [L^2 T^{-2}] + [L T^{-2}][L]"},
]

KINEMATIC_LIMITS = [
    {"situation": "A ball rolling at a steady 5 m/s",
     "a": 0.0, "note": "With a = 0 the first equation gives v = u and the second "
                      "gives s = ut, which is just 'distance = speed × time'."},
    {"situation": "A stone dropped from a windowsill",
     "a": 9.8, "note": "Taking downwards as positive, u = 0 and a = g = +9.8 m/s². "
                      "The stone is in free fall the moment it leaves the sill."},
    {"situation": "A ball thrown straight up",
     "a": -9.8, "note": "If up is positive, gravity is negative. The velocity goes "
                        "positive, then zero at the top, then negative — all with "
                        "the same acceleration."},
    {"situation": "A train slowing from 20 m/s at 2 m/s²",
     "a": -2.0, "note": "Negative acceleration along the direction of motion means "
                        "the train slows down. Deceleration is just negative "
                        "acceleration; it is not a separate thing."},
]

# --------------------------------------------------------------------------
# 3.2  Momentum
# --------------------------------------------------------------------------

MOMENTUM_DEF = (
    "<p><b>Momentum</b> is mass multiplied by velocity: <b>p = m v</b>. Because "
    "velocity is a vector, so is momentum. Its unit is kg m s⁻¹, and in one "
    "dimension it is signed: positive one way, negative the other.</p>"
    "<p><b>The law:</b> if no resultant external force acts on a system, the total "
    "momentum of that system is constant. No force, no change — not a tendency, "
    "an exact statement.</p>"
)

MOMENTUM_EXAMPLES = [
    {"situation": "A karate chop breaking a board",
     "system": "The hand and the board together",
     "before": "The hand has a large momentum concentrated in a small mass.",
     "after": "The hand has slowed, so its momentum has dropped. The difference went "
              "into the board, and the board's fragments carry the rest.",
     "lesson": "A slow hand with a large mass and a small hand moving fast can carry "
               "the same momentum. What breaks the board is the rate of change of "
               "momentum — the force — not the momentum alone."},
    {"situation": "A car crash",
     "system": "Both vehicles",
     "before": "The two cars have separate momenta, one of them large.",
     "after": "They move away together, at a shared, much lower speed.",
     "lesson": "The total momentum is unchanged, so the combined body moves more "
               "slowly than either did. The missing kinetic energy has become heat, "
               "noise, and bent metal. Crash barriers increase the time of the "
               "collision so that the same impulse spreads over far more seconds, "
               "giving a much smaller force."},
    {"situation": "Ball struck by a bat",
     "system": "Ball and bat together",
     "before": "The bat moves slowly but is heavy; the ball moves fast but is light.",
     "after": "The ball leaves faster than it arrived, and the bat slows a little.",
     "lesson": "The bat does not add energy out of nothing. It transfers momentum "
               "from the bat to the ball, and the kinetic energy rises because the "
               "bat is much heavier than the ball."},
    {"situation": "A rocket",
     "system": "The rocket and all its exhaust",
     "before": "Everything is at rest, so the total momentum is zero.",
     "after": "The gases go backwards fast; the rocket goes forwards, slowly.",
     "lesson": "This is conservation of momentum creating order out of nothing — "
               "but only because the system includes the exhaust. If you take the "
               "rocket alone you have not closed the system, and the law does not "
               "apply."},
]

COLLISION_TYPES = [
    {"kind": "Perfectly elastic",
     "momentum": "conserved", "kinetic_energy": "conserved",
     "sound": "a clear note", "deformation": "none that remains",
     "example": "Two polished steel balls on a smooth surface; billiard-ball "
                "collisions near enough",
     "rule": "The total momentum and the total kinetic energy are both exactly "
             "the same before and after."},
    {"kind": "Inelastic",
     "momentum": "conserved", "kinetic_energy": "not conserved",
     "sound": "a thud", "deformation": "permanent",
     "example": "A ball of clay hitting the floor; two cars meeting",
     "rule": "Momentum still balances exactly, but kinetic energy falls and becomes "
             "heat, sound and deformation. The energy is not destroyed — it has "
             "been converted into a form that cannot be recovered."},
    {"kind": "Perfectly inelastic",
     "momentum": "conserved", "kinetic_energy": "not conserved",
     "sound": "a flat bang", "deformation": "they stick together",
     "example": "A bullet embedded in a block of wood; two lumps of clay colliding",
     "rule": "The bodies move off together at a single shared velocity, found by "
             "putting every mass into one momentum balance."},
]

ELASTIC_FORMULAS = [
    {"result": "v₁", "formula": r"v_1 = \frac{(m_1 - m_2)u_1 + 2 m_2 u_2}{m_1 + m_2}",
     "note": "The final velocity of the first body."},
    {"result": "v₂", "formula": r"v_2 = \frac{2 m_1 u_1 + (m_2 - m_1)u_2}{m_1 + m_2}",
     "note": "The final velocity of the second body."},
    {"result": "Special case", "formula": r"m_1 = m_2 \;\Rightarrow\; v_1 = u_2,\; v_2 = u_1",
     "note": "Equal masses simply swap velocities, whatever they were doing "
             "before. This is why a head-on collision of two identical pool balls "
             "looks like the balls passed through each other."},
]

OBLIQUE_METHOD = [
    "Take the second body as the target and draw the line of centres joining the "
    "two centres at the moment of contact.",
    "Along that line, momentum is conserved and the impulse acts. Call the "
    "component of the first ball's velocity along the line uₙ.",
    "Perpendicular to the line, there is no impulse, so the tangential component "
    "of each ball is completely unchanged. That is why a ball can be struck so it "
    "both speeds up and changes direction.",
    "Split both velocities into along-line and across-line parts before you do "
    "anything else.",
    "Apply the one-dimensional result to the along-line parts, and carry the "
    "across-line parts through untouched.",
    "Recombine at the end. Resist the urge to combine earlier — that is exactly "
    "what causes the classic wrong answer.",
]

# --------------------------------------------------------------------------
# 3.3 to 3.5  Work, fields and energy
# --------------------------------------------------------------------------

WORK_ANGLE_CASES = [
    {"theta": "0°", "cos": 1, "sign": "positive", "meaning": "The force acts along the motion. "
     "Maximum positive work; the body speeds up as much as possible.",
     "example": "A push that helps a cyclist up a hill."},
    {"theta": "60°", "cos": 0.5, "sign": "positive", "meaning": "Half the force does useful "
     "work; the rest pushes sideways.",
     "example": "Pulling a suitcase by its handle at an upward angle."},
    {"theta": "90°", "cos": 0, "sign": "zero", "meaning": "The force is perpendicular to the "
     "motion, so it changes the direction of travel but not the speed.",
     "example": "The centripetal force holding a satellite in orbit does exactly zero work."},
    {"theta": "120°", "cos": -0.5, "sign": "negative", "meaning": "The force partly opposes "
     "the motion, so energy is taken away.",
     "example": "A trolley being pushed steadily backwards along its path."},
    {"theta": "180°", "cos": -1, "sign": "negative", "meaning": "The force acts directly "
     "against the motion. Maximum energy removal.",
     "example": "A brake, or a force decelerating a car."},
]

FD_CASES = [
    {"shape": "Constant force", "area": "rectangle F × d",
     "meaning": "W = Fd. A flat F–d line.",
     "diagram": "A horizontal line at height F out to displacement d."},
    {"shape": "Linearly increasing force", "area": "triangle ½Fd",
     "meaning": "A spring obeying Hooke's law: the force grows from zero, so the "
                "area is a triangle, not a rectangle.",
     "diagram": "A straight rising line from the origin."},
    {"shape": "Below the axis", "area": "negative",
     "meaning": "A resistive force opposes the motion, so the area is negative and "
                "energy is removed from the body.",
     "diagram": "A line at negative F over positive displacement."},
    {"shape": "Above then below the axis", "area": "algebraic sum",
     "meaning": "Energy is stored first and then returned, or the reverse. Only the "
                "signed sum is the net work.",
     "diagram": "A curve crossing the axis partway along."},
]

FIELD_EXAMPLES = [
    {"field": "Gravity near the Earth's surface", "conservative": True,
     "work": "mgh depends only on the height lost.",
     "test": "Drop an object by the direct route or along a spiral path — the work "
             "is identical.",
     "potential": "U = mgh, and the energy is recoverable."},
    {"field": "Electrostatic force", "conservative": True,
     "work": "Depends only on the potential difference between two points.",
     "test": "Walk a test charge round any closed loop and the net work is zero.",
     "potential": "U = qV; the field stores its energy in the space around the charge."},
    {"field": "A stretched spring", "conservative": True,
     "work": "½kx², depending only on the extension.",
     "test": "Stretch it by a long route or a short one — same energy stored.",
     "potential": "U = ½kx², returned when the spring is released."},
    {"field": "Kinetic friction", "conservative": False,
     "work": "−Fd, and it depends on the length of the path.",
     "test": "Slide a box across the table along the edge or along the diagonal: "
             "the longer route costs more work, always in the same direction.",
     "potential": "There is no potential energy to store it — it leaves as heat."},
    {"field": "Air resistance (drag)", "conservative": False,
     "work": "Always opposes motion, so it can only remove energy.",
     "test": "A falling object reaches a terminal speed where drag exactly balances "
             "weight, and then energy input equals energy removed.",
     "potential": "None. The lost mechanical energy becomes heat in the air."},
]

WORK_ENERGY_WORKED = [
    {"case": "A 2 kg trolley pushed by 10 N over 3 m on a frictionless floor",
     "work": 30.0, "delta_k": 30.0,
     "explanation": "W = 10 × 3 = 30 J, and the kinetic energy rises from zero to "
                    "30 J. The theorem is satisfied exactly."},
    {"case": "The same trolley, but 4 N of friction, over 3 m",
     "work": 18.0, "delta_k": 18.0,
     "explanation": "The push does 30 J and friction does −12 J, so the net work is "
                    "18 J. The kinetic energy rises by 18 J and 12 J has become "
                    "heat in the wheels."},
    {"case": "A 5 kg ball dropped 3 m onto the floor and stopping",
     "work": -147.0, "delta_k": -147.0,
     "explanation": "Gravity does +147 J during the fall; the floor does −147 J to "
                    "stop it. The net change in kinetic energy is −147 J, going from "
                    "147 J to zero."},
]

# --------------------------------------------------------------------------
# Worked problems
# --------------------------------------------------------------------------

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "A thrown ball — finding time and range",
     "level": "Foundation", "slos": ["3.1.1"],
     "question": "A ball is thrown vertically upwards at 20 m/s from the ground. Taking g = 9.8 m/s², "
                 "find how long it takes to reach its highest point and how high it goes.",
     "known": ["u = 20 m/s (upwards positive)", "a = −g = −9.8 m/s²", "v = 0 at the highest point"],
     "find": "the time to the highest point and the height reached",
     "equation": r"v = u + at \qquad s = u\,t + \tfrac{1}{2} a\,t^2",
     "conversions": ["No unit conversion needed; everything is already in SI units and seconds."],
     "substitution": r"0 = 20 - 9.8\,t",
     "calculation": [
         "Step 1 — choose the sign convention first: up is positive, so gravity is a = −9.8 m/s². This single decision removes almost every sign error in this chapter.",
         "Step 2 — time: 0 = 20 + (−9.8)t, so t = 20 / 9.8 = 2.04 s.",
         "Step 3 — height: s = 20(2.04) + ½(−9.8)(2.04)² = 40.8 − 20.4 = 20.4 m.",
         "Step 4 — check with the third equation: v² = u² + 2as gives 0 = 400 − 2(9.8)(20.4) = 400 − 400 = 0. ✓",
     ],
     "unit_check": r"s = [L T^{-1}][T] + [L T^{-2}][T^2] = [L],\ \text{metres}",
     "answer": "t = 2.04 s, s = 20.4 m",
     "sig_fig_note": "20 m/s and 9.8 m/s² are each to two significant figures, so the answer is 2.0 s and 20 m.",
     "assumptions": ["Air resistance is neglected, so this is a true free-flight parabola.",
                     "g is treated as constant over the 20 m rise."]},
    {"id": "WP2", "title": "Two equations and the right one to use",
     "level": "Developing", "slos": ["3.1.1"],
     "question": "A car travelling at 15 m/s brakes at a constant 5 m/s². How far does it travel before stopping?",
     "known": ["u = 15 m/s", "a = −5 m/s² (opposite to the motion)", "v = 0 when it stops"],
     "find": "the stopping distance s",
     "equation": r"v^2 = u^2 + 2 a\,s",
     "conversions": ["None required."],
     "substitution": r"0 = 225 - 2(5)s",
     "calculation": [
         "Step 1 — ask which quantity is missing. Time is not mentioned and not asked for, so the third equation v² = u² + 2as is the right one. Using the first equation here would mean solving for t first and then going back for s — two operations where one is enough.",
         "Step 2 — substitute: 0 = 15² + 2(−5)s = 225 − 10s.",
         "Step 3 — solve: 10s = 225, so s = 22.5 m.",
         "Step 4 — sanity check on the size. At 15 m/s (54 km/h) a stopping distance of 22.5 m is about right for a hard stop on dry tarmac, and roughly double that on wet roads.",
     ],
     "unit_check": r"[L^2 T^{-2}] = [L^2 T^{-2}] + [L T^{-2}][L]",
     "answer": "s = 22.5 m",
     "sig_fig_note": "15 m/s is to two significant figures and 5 m/s² to one, so the strict answer is 20 m (one significant figure). 22.5 m is shown in full so the working can be followed.",
     "assumptions": ["The deceleration is constant over the whole stop, which is roughly true for a car braking hard.",
                     "Reaction time before the brakes are applied is not included."]},
    {"id": "WP3", "title": "Momentum in a karate chop",
     "level": "Foundation", "slos": ["3.2.1", "3.2.2"],
     "question": "A 0.60 kg hand moving at 8.0 m/s strikes a 1.5 kg board held rigidly and comes to rest. "
                 "Find the momentum of the hand before and after, the impulse delivered, and the "
                 "average force if the contact lasts 0.020 s.",
     "known": ["m_hand = 0.60 kg, u = 8.0 m/s, v = 0",
               "The board is held rigidly, so it does not move — the hand is the only moving part of a closed system.",
               "Contact time t = 0.020 s"],
     "find": "the impulse and the average force",
     "equation": r"F\Delta t = m\,v - m\,u \qquad\text{(impulse–momentum)}",
     "conversions": ["Momentum in kg m s⁻¹; impulse is the same unit; divide by seconds for newtons."],
     "substitution": r"J = 0.60(0) - 0.60(8.0) = -4.8\ \text{kg m s}^{-1}",
     "calculation": [
         "Step 1 — momentum before: p = mu = 0.60 × 8.0 = +4.8 kg m s⁻¹.",
         "Step 2 — momentum after: p = mv = 0.60 × 0 = 0.",
         "Step 3 — impulse equals the change in momentum: J = 0 − 4.8 = −4.8 kg m s⁻¹. The negative sign says the hand's momentum decreased; the board received the +4.8.",
         "Step 4 — average force: F = J / t = −4.8 / 0.020 = −240 N, a magnitude of 240 N, which is about the weight of a 24 kg mass.",
         "Step 5 — the important point: the impulse of 4.8 N s is small, but spread over only 0.02 s it becomes a very large force. Force is a rate of change of momentum, not an amount of momentum.",
     ],
     "unit_check": r"[M L T^{-1}]/[T] = [M L T^{-2}] = \text{newtons}",
     "answer": "p before = +4.8 kg m s⁻¹, after = 0; impulse = −4.8 N s; average force ≈ 240 N",
     "sig_fig_note": "The contact time of 0.020 s is the least precise value and sets the precision of the force.",
     "assumptions": ["The board is held rigidly by an external agent, so the hand plus board is not a closed system — only the momentum of the hand is tracked.",
                     "The force is treated as constant during the 0.020 s contact, so the answer is an average."]},
    {"id": "WP4", "title": "A perfectly inelastic collision",
     "level": "Developing", "slos": ["3.2.3", "3.2.4"],
     "question": "A 2.0 kg trolley moving at 3.0 m/s runs into a stationary 4.0 kg trolley and the two "
                 "stay joined. Find their common velocity, and state how much kinetic energy was lost.",
     "known": ["m₁ = 2.0 kg, u₁ = +3.0 m/s", "m₂ = 4.0 kg, u₂ = 0",
               "They stick together, so v₁ = v₂ = v"],
     "find": "the shared velocity and the kinetic energy lost",
     "equation": r"m_1u_1 + m_2u_2 = (m_1 + m_2)v",
     "conversions": ["Momentum in kg m s⁻¹; kinetic energy in joules."],
     "substitution": r"2.0(3.0) + 4.0(0) = (2.0 + 4.0)v",
     "calculation": [
         "Step 1 — momentum before: 2.0 × 3.0 + 4.0 × 0 = +6.0 kg m s⁻¹.",
         "Step 2 — momentum after: (2.0 + 4.0)v = 6.0v.",
         "Step 3 — conservation gives 6.0 = 6.0v, so v = +1.0 m/s.",
         "Step 4 — kinetic energy before: ½(2.0)(3.0)² = 9.0 J.",
         "Step 5 — kinetic energy after: ½(6.0)(1.0)² = 3.0 J.",
         "Step 6 — lost: 9.0 − 3.0 = 6.0 J. Two thirds of the kinetic energy has become heat in the hinges, sound, and the energy of bending the trolley ends.",
     ],
     "unit_check": r"[M L T^{-1}] = [M][L T^{-1}]; \ [M L^2 T^{-2}] = \text{joules}",
     "answer": "Common velocity = 1.0 m/s in the original direction; 6.0 J of kinetic energy lost",
     "sig_fig_note": "All values are to two significant figures, so the answers are 1.0 m/s and 6.0 J.",
     "assumptions": ["No external horizontal force acts on the two trolleys.",
                     "The collision is treated as instantaneous, so momentum is conserved but energy is not."]},
    {"id": "WP5", "title": "An elastic collision with unequal masses",
     "level": "Challenge", "slos": ["3.2.4"],
     "question": "A 0.10 kg ball moving at 20 m/s strikes a stationary 1.0 kg block of wood on a frictionless "
                 "surface and bounces back. Find the velocity of each body afterwards, and confirm that "
                 "kinetic energy really is conserved.",
     "known": ["m₁ = 0.10 kg, u₁ = +20 m/s", "m₂ = 1.0 kg, u₂ = 0",
               "The collision is elastic, so both momentum and kinetic energy are conserved."],
     "find": "v₁ and v₂",
     "equation": r"v_1 = \frac{(m_1-m_2)u_1 + 2m_2u_2}{m_1+m_2}, \qquad "
                 r"v_2 = \frac{2m_1u_1 + (m_2-m_1)u_2}{m_1+m_2}",
     "conversions": ["All values are already in SI units."],
     "substitution": r"v_1 = \frac{(0.10-1.0)(20) + 0}{1.10},\qquad "
                     r"v_2 = \frac{2(0.10)(20) + 0}{1.10}",
     "calculation": [
         "Step 1 — final velocity of the ball: v₁ = (−0.9 × 20)/1.10 = −18/1.10 = −16.36 m/s. Negative means it bounced back.",
         "Step 2 — final velocity of the block: v₂ = (2 × 0.10 × 20)/1.10 = 4.0/1.10 = +3.64 m/s.",
         "Step 3 — momentum check: before, 0.10 × 20 = +2.0. After, 0.10(−16.36) + 1.0(3.64) = −1.636 + 3.636 = +2.00. ✓",
         "Step 4 — kinetic energy check: before, ½(0.10)(20)² = 20.0 J. After, ½(0.10)(16.36)² + ½(1.0)(3.64)² = 13.38 + 6.62 = 20.0 J. ✓",
         "Step 5 — the lesson: a light body hitting a heavy one bounces back almost at its original speed, transferring only a small fraction of its momentum. That is why a tennis racket squash shot sends the ball the other way.",
     ],
     "unit_check": r"v = [L T^{-1}]; \text{both momenta in } [M L T^{-1}]",
     "answer": "v₁ = −16.4 m/s (rebounding), v₂ = +3.64 m/s; both momentum and kinetic energy conserved",
     "sig_fig_note": "m₁ = 0.10 kg is to two significant figures and the speeds to two, so the answers are −16 m/s and +3.6 m/s.",
     "assumptions": ["The surface is frictionless, so there is no external horizontal impulse.",
                     "The ball is treated as a smooth sphere and the contact as instantaneous."]},
    {"id": "WP6", "title": "Work done and the area under the F–d graph",
     "level": "Developing", "slos": ["3.3.1", "3.3.2"],
     "question": "A force of 40 N acts on a body moving 2.0 m in a straight line at an angle of 60° to the "
                 "displacement. Find the work done, then find it again from a force–displacement graph built "
                 "from the components, and confirm they agree.",
     "known": ["F = 40 N, d = 2.0 m, θ = 60°",
               "Fx = F cos 60° = 20 N is the only component that does work",
               "Fy = F sin 60° = 34.6 N does no work at all"],
     "find": "the work done, by two independent routes",
     "equation": r"W = \mathbf{F}\cdot\mathbf{d} = Fd\cos\theta",
     "conversions": ["Work in newton-metres, which are joules: 1 N m = 1 J."],
     "substitution": r"W = 40 \times 2.0 \times \cos 60^\circ = 40\ \text{J}",
     "calculation": [
         "Step 1 — by the formula: W = 40 × 2.0 × 0.5 = 40 J.",
         "Step 2 — build the graph. The useful force is 20 N, constant, so the F–d line is horizontal at 20 N out to 2.0 m.",
         "Step 3 — the area under that line is a rectangle: W = 20 × 2.0 = 40 J. ✓",
         "Step 4 — the two agree, which is not a coincidence: the rectangle's height F cos θ is exactly the projection of the force onto the displacement.",
         "Step 5 — note what the graph shows that the formula hides: the 34.6 N upward component produced no work at all, because the body never moved in that direction.",
     ],
     "unit_check": r"\mathrm{N\,m} = \mathrm{J}",
     "answer": "W = 40 J by both methods",
     "sig_fig_note": "F = 40 N to one significant figure and d = 2.0 m to two, so the strict answer is 4 × 10¹ J.",
     "assumptions": ["The force is constant in size and direction while the body moves.",
                     "The displacement is a straight line."]},
    {"id": "WP7", "title": "Work–energy theorem with friction",
     "level": "Developing", "slos": ["3.5.1", "3.5.2"],
     "question": "A 5.0 kg trolley moving at 4.0 m/s on a rough floor is brought to rest by a constant "
                 "frictional force of 10 N. How far does it travel before stopping, and how much energy "
                 "has been dissipated?",
     "known": ["m = 5.0 kg, u = 4.0 m/s, v = 0", "friction f = 10 N, opposing the motion",
               "Only friction does work once the push is released"],
     "find": "the stopping distance and the energy dissipated",
     "equation": r"W = \Delta K = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2",
     "conversions": ["Kinetic energy in joules."],
     "substitution": r"(-10)d = 0 - \tfrac{1}{2}(5.0)(4.0)^2 = -40\ \text{J}",
     "calculation": [
         "Step 1 — initial kinetic energy: K₁ = ½(5.0)(4.0)² = 40 J.",
         "Step 2 — final kinetic energy: K₂ = ½(5.0)(0)² = 0 J.",
         "Step 3 — the theorem: the net work equals the change, so W = 0 − 40 = −40 J.",
         "Step 4 — that work comes entirely from friction: W = −fd, so −10d = −40, giving d = 4.0 m.",
         "Step 5 — the dissipated energy is 40 J, and it has not vanished: it is heat in the wheels, the floor, and the air between them, plus a very quiet sound.",
     ],
     "unit_check": r"\mathrm{N\,m} = \mathrm{J}; \ [M L^2 T^{-2}] = \text{joules}",
     "answer": "Stopping distance = 4.0 m; 40 J dissipated as heat and sound",
     "sig_fig_note": "All values are to two significant figures, so d = 4.0 m and E = 40 J.",
     "assumptions": ["The frictional force is constant until the trolley stops.",
                     "No other horizontal force acts."]},
    {"id": "WP8", "title": "Testing whether a field is conservative",
     "level": "Challenge", "slos": ["3.4.1"],
     "question": "A box of mass 4.0 kg is pushed at constant speed 3.0 m across a rough table against a "
                 "frictional force of 5.0 N. Compare the work done over a direct path with the work done "
                 "over a path that detours 1.0 m along the table before continuing. Is the field conservative?",
     "known": ["f = 5.0 N, constant, always opposing motion",
               "Direct path: 3.0 m", "Detour path: 1.0 m + 3.0 m = 4.0 m of total travel"],
     "find": "the work along each path, and the verdict",
     "equation": r"W = \mathbf{F}\cdot\mathbf{d} = Fd\cos 180^\circ = -Fd",
     "conversions": ["Work in joules."],
     "substitution": r"W_{\text{direct}} = -5.0(3.0) = -15\ \text{J}, \qquad "
                     r"W_{\text{detour}} = -5.0(4.0) = -20\ \text{J}",
     "calculation": [
         "Step 1 — friction always opposes motion, so the angle is 180° in both cases and cos 180° = −1.",
         "Step 2 — direct path: W = −5.0 × 3.0 = −15 J.",
         "Step 3 — detour path: the box travels 4.0 m in total, so W = −5.0 × 4.0 = −20 J.",
         "Step 4 — the two differ by 5.0 J, and they end at the same place. The work depends on the route, so the field is non-conservative.",
         "Step 5 — a conservative field would give exactly the same answer both ways, because the energy would be stored in a potential rather than dissipated along the way. Gravity is the contrast: climbing 3 m up costs the same however you route the climb.",
     ],
     "unit_check": r"\mathrm{N\,m} = \mathrm{J}",
     "answer": "W_direct = −15 J, W_detour = −20 J; the field is non-conservative because the work is path-dependent",
     "sig_fig_note": "All values are to two significant figures.",
     "assumptions": ["The frictional force is constant and independent of speed.",
                     "The box is pushed at constant speed, so the net work is zero and the push exactly cancels friction."]},
]

# --------------------------------------------------------------------------
# Practice questions
# --------------------------------------------------------------------------

PRACTICE_QUESTIONS = [
    {"id": "P1", "category": "Equations of motion", "type": "mcq", "slo": "3.1.1",
     "prompt": "A body starts from rest with an acceleration of 4 m/s². How far does it travel in 3 s?",
     "options": ["12 m", "18 m", "36 m", "6 m"], "answer": 1,
     "hint": "u = 0, so the first term of s = ut + ½at² vanishes.",
     "explanation": "s = 0 + ½(4)(9) = 18 m. Note that ½ × 4 × 9 = 18, which is where the "
                    "common answer of 36 comes from if the ½ is dropped."},
    {"id": "P2", "category": "Equations of motion", "type": "numeric", "slo": "3.1.1",
     "prompt": "A car accelerates from 10 m/s to 30 m/s at 4 m/s². How long does it take? Enter the number only.",
     "answer": 5.0, "tolerance": 0.05, "unit": "s",
     "hint": "Use v = u + at and rearrange.",
     "explanation": "t = (v − u)/a = (30 − 10)/4 = 5.0 s."},
    {"id": "P3", "category": "Equations of motion", "type": "numeric", "slo": "3.1.1",
     "prompt": "A ball is thrown upward at 30 m/s. Ignoring air resistance and taking g = 10 m/s², how high "
               "does it rise? Enter the number only, in metres.",
     "answer": 45.0, "tolerance": 0.2, "unit": "m",
     "hint": "At the top v = 0, and time is not needed.",
     "explanation": "v² = u² + 2as gives 0 = 900 − 2(10)s, so s = 45 m. Using the third equation "
                    "avoided working out the time at all."},
    {"id": "P4", "category": "Equations of motion", "type": "mcq", "slo": "3.1.1",
     "prompt": "Which set of values makes the third equation v² = u² + 2as the right one to use?",
     "options": ["u, a and t are given, v is unknown",
                 "u, a and s are given, v is unknown",
                 "u, v and s are given, a is unknown",
                 "a, s and t are given, v is unknown"], "answer": 1,
     "hint": "An equation is only useful if it does not contain the quantity you do not know.",
     "explanation": "v² = u² + 2as contains no t, so it is the right choice when u, a and s are "
                    "known. Option A needs the first equation, option C the first, and option D the second."},
    {"id": "P5", "category": "Free fall", "type": "numeric", "slo": "3.1.2",
     "prompt": "A stone is dropped from rest from a height of 45 m. Taking g = 9.8 m/s², how long does it "
               "take to reach the ground? Enter the number only, in seconds.",
     "answer": 3.0304576336566322, "tolerance": 0.05, "unit": "s",
     "hint": "u = 0, s = 45, a = 9.8. Use s = ut + ½at² and remember that ½at² means at²/2.",
     "explanation": "45 = ½(9.8)t², so t² = 90/9.8 = 9.184 and t = 3.03 s. This is the same as "
                    "t = √(2L/g) = √(2 × 45/9.8), which is worth remembering as a separate formula "
                    "for anything dropped from rest."},
    {"id": "P6", "category": "Free fall", "type": "numeric", "slo": "3.1.2",
     "prompt": "A ball is thrown straight downward at 10.0 m/s from a height of 20 m. Taking g = 9.8 m/s², "
               "how fast is it moving when it reaches the ground? Enter the number only, in m/s.",
     "answer": 22.181073012818835, "tolerance": 0.1, "unit": "m/s",
     "hint": "Take downwards as positive, so both u and a are positive, and use v² = u² + 2as.",
     "explanation": "v² = 10.0² + 2(9.8)(20) = 100 + 392 = 492, so v = 22.2 m/s. Compare this with "
                    "the same ball dropped from rest, which would arrive at √(2 × 9.8 × 20) = "
                    "19.8 m/s. Throwing it down at 10 m/s adds more than 10 m/s to the impact "
                    "speed, because speeds add as squares in this relation, not directly."},
    {"id": "P7", "category": "Free fall", "type": "mcq", "slo": "3.1.2",
     "prompt": "At the highest point of its flight, a thrown ball has...",
     "options": ["zero velocity and zero acceleration",
                 "zero velocity but an acceleration of g downwards",
                 "zero acceleration but a maximum velocity",
                 "zero velocity and a maximum kinetic energy"], "answer": 1,
     "hint": "What makes it stop, and what keeps trying to bring it down?",
     "explanation": "The velocity is zero for an instant, but gravity is still acting, so the "
                    "acceleration is g downwards. This is the clearest demonstration that zero "
                    "velocity is not the same as 'not moving under gravity'."},
    {"id": "P8", "category": "Free fall", "type": "numeric", "slo": "3.1.2",
     "prompt": "On a planet where g = 5.0 m/s², a ball falls from rest for 4.0 s. How far has it fallen? "
               "Enter the number only, in metres.",
     "answer": 40.0, "tolerance": 0.2, "unit": "m",
     "hint": "s = ½at² with u = 0.",
     "explanation": "s = ½(5.0)(16) = 40 m. Note that the time scales as √(L/g), so halving g "
                    "roughly doubles the time of fall for a given height."},

    {"id": "P9", "category": "Momentum", "type": "numeric", "slo": "3.2.1",
     "prompt": "A 1500 kg car moves at 20 m/s. What is its momentum? Enter the number only.",
     "answer": 30000.0, "tolerance": 10.0, "unit": "kg m s⁻¹",
     "hint": "p = m v.",
     "explanation": "p = 1500 × 20 = 3.0 × 10⁴ kg m s⁻¹. The unit is kg m s⁻¹, never N or J."},
    {"id": "P10", "category": "Momentum", "type": "numeric", "slo": "3.2.1",
     "prompt": "A 2 kg body moving at 3 m/s has a perfectly inelastic collision with a stationary 5 kg "
               "body and they stick together. What is their shared velocity? Enter the number only.",
     "answer": 6.0 / 7.0, "tolerance": 0.02, "unit": "m/s",
     "hint": "Total momentum before = total momentum after, and the final mass is 7 kg.",
     "explanation": "6.0 = 7v, so v = 0.857 m/s. Notice how much slower the joined pair moves than "
                    "the 2 kg body did: the heavy body has absorbed most of the momentum."},
    {"id": "P11", "category": "Momentum", "type": "mcq", "slo": "3.2.1",
     "prompt": "The law of conservation of linear momentum applies to a system when...",
     "options": ["no external resultant force acts on it",
                 "the forces inside the system are zero",
                 "the bodies move at constant speed",
                 "kinetic energy is also conserved"], "answer": 0,
     "hint": "Think about what would have to act from outside to change the total.",
     "explanation": "Momentum is conserved when the resultant external force is zero. Internal "
                    "forces do not matter — they are already accounted for by being equal and "
                    "opposite. Kinetic energy is a separate question entirely."},
    {"id": "P12", "category": "Momentum in the real world", "type": "mcq", "slo": "3.2.2",
     "prompt": "A rocket accelerates in deep space. Why can it gain speed when nothing pushes it?",
     "options": ["Rocket motors create momentum from fuel energy",
                 "The exhaust gases are pushed backwards, so the rocket goes forwards",
                 "It pulls itself forwards using gravity",
                 "The air behind it pushes it"], "answer": 1,
     "hint": "Include the exhaust in the system.",
     "explanation": "The rocket plus its exhaust is a closed system with zero initial momentum, "
                    "so the total stays zero: gases go one way, rocket the other. Option A "
                    "confuses energy with momentum — energy is supplied by the fuel, but the "
                    "momentum is balanced by the exhaust."},
    {"id": "P13", "category": "Momentum in the real world", "type": "numeric", "slo": "3.2.2",
     "prompt": "A 60 kg person jumps horizontally off a 2.0 m/s trolley moving at 5.0 m/s, landing on it "
               "with a horizontal speed of 5.4 m/s. How fast does the trolley now move? Enter the number only.",
     "answer": 4.4, "tolerance": 0.03, "unit": "m/s",
     "hint": "The trolley is 40 kg. Write one momentum equation with everything on each side.",
     "explanation": "Before: (60 + 40)(5.0) = 500 kg m s⁻¹. After: 60(5.4) + 40v = 324 + 40v. "
                    "Setting 500 = 324 + 40v gives v = 4.4 m/s. The trolley has slowed because it "
                    "handed 60 × 0.6 = 36 kg m s⁻¹ of momentum to the person. No external "
                    "horizontal force acted, so the total is unchanged."},

    {"id": "P14", "category": "Collisions", "type": "mcq", "slo": "3.2.3",
     "prompt": "Which statement is true for a perfectly inelastic collision?",
     "options": ["Kinetic energy is conserved",
                 "Kinetic energy increases",
                 "Momentum is conserved and kinetic energy is not",
                 "Neither momentum nor kinetic energy is conserved"], "answer": 2,
     "hint": "One of the two is always conserved. Which?",
     "explanation": "Momentum is always conserved in a closed system, whatever happens. Kinetic "
                    "energy is only conserved if the collision is elastic."},
    {"id": "P15", "category": "Collisions", "type": "numeric", "slo": "3.2.4",
     "prompt": "A 2 kg ball moving at 6 m/s hits a stationary 1 kg ball elastically. What is the final "
               "velocity of the 2 kg ball? Enter the number only, in m/s.",
     "answer": 2.0, "tolerance": 0.05, "unit": "m/s",
     "hint": "v₁ = ((m₁−m₂)u₁ + 2m₂u₂)/(m₁+m₂).",
     "explanation": "v₁ = ((2−1)(6) + 0)/(3) = 6/3 = 2 m/s. The heavy ball continues forward but "
                    "much more slowly; the light ball is sent off at 8 m/s."},
    {"id": "P16", "category": "Collisions", "type": "numeric", "slo": "3.2.4",
     "prompt": "Two identical balls collide head-on. One moves at 3 m/s and the other at rest. After an "
               "elastic collision, what is the velocity of the stationary ball? Enter the number only.",
     "answer": 3.0, "tolerance": 0.05, "unit": "m/s",
     "hint": "Equal masses swap velocities.",
     "explanation": "With m₁ = m₂ the formulas reduce to v₁ = u₂ and v₂ = u₁, so the moving ball "
                    "stops and the resting ball leaves at 3 m/s. This is why identical pool balls "
                    "appear to pass through one another."},
    {"id": "P17", "category": "Collisions", "type": "mcq", "slo": "3.2.4",
     "prompt": "A light ball strikes a heavy stationary block elastically. The light ball...",
     "options": ["continues forward at nearly its original speed",
                 "stops dead", "rebounds at nearly its original speed",
                 "rebounds at twice its original speed"], "answer": 2,
     "hint": "Try m₁ much smaller than m₂ in the elastic formula.",
     "explanation": "v₁ = ((m₁−m₂)u₁ + 2m₂u₂)/(m₁+m₂) tends to −u₁ as m₂ grows, so the light "
                    "ball rebounds at nearly its original speed. This is exactly the principle "
                    "behind the squash shot in a tennis racket."},
    {"id": "P18", "category": "Two-dimensional collisions", "type": "mcq", "slo": "3.2.5",
     "prompt": "In an oblique collision between smooth balls, the component of velocity perpendicular to "
               "the line of centres is...",
     "options": ["reduced to zero", "unchanged for both balls", "doubled", "reversed"], "answer": 1,
     "hint": "No impulse acts in that direction.",
     "explanation": "The contact force acts only along the line of centres, so the tangential "
                    "components are untouched. This is what allows a struck ball to change both "
                    "speed and direction."},
    {"id": "P19", "category": "Two-dimensional collisions", "type": "mcq", "slo": "3.2.5",
     "prompt": "When solving an oblique collision, you should...",
     "options": ["resolve both velocities along and across the line of centres first",
                 "add the two speeds to get the resultant",
                 "use the elastic formula directly with the angles",
                 "ignore the tangential components"], "answer": 0,
     "hint": "There is a direction in which the problem becomes one-dimensional.",
     "explanation": "Resolving along the line of centres turns it into the one-dimensional case "
                    "you already know, while the tangential parts simply carry through unchanged."},

    {"id": "P20", "category": "Work", "type": "numeric", "slo": "3.3.1",
     "prompt": "A 100 N force acts through 5 m at 60° to the displacement. How much work is done? "
               "Enter the number only, in joules.",
     "answer": 250.0, "tolerance": 2.0, "unit": "J",
     "hint": "W = Fd cos θ.",
     "explanation": "W = 100 × 5 × 0.5 = 250 J."},
    {"id": "P21", "category": "Work", "type": "mcq", "slo": "3.3.1",
     "prompt": "The work done by a centripetal force on a satellite in circular orbit is...",
     "options": ["positive, because the satellite is moving",
                 "zero, because the force is perpendicular to the velocity",
                 "negative, because the satellite is being held in",
                 "equal to its kinetic energy"], "answer": 1,
     "hint": "What angle does the force make with the velocity?",
     "explanation": "The force points at the centre while the velocity points along the tangent, "
                    "so the angle is 90° and cos 90° = 0. The satellite changes direction every "
                    "instant but never speed, and does no work at all."},
    {"id": "P22", "category": "Work from graphs", "type": "numeric", "slo": "3.3.2",
     "prompt": "A force rises linearly from 0 N to 20 N over 4 m, then stays constant at 20 N for a further "
               "2 m. Find the total work done. Enter the number only, in joules.",
     "answer": 80.0, "tolerance": 1.0, "unit": "J",
     "hint": "Area of a triangle plus area of a rectangle.",
     "explanation": "Triangle: ½ × 4 × 20 = 40 J. Rectangle: 20 × 2 = 40 J. Total 80 J. The spring "
                    "case is the triangle alone."},
    {"id": "P23", "category": "Work from graphs", "type": "mcq", "slo": "3.3.2",
     "prompt": "A force–displacement graph dips below the axis for part of its length. This means...",
     "options": ["the work done is zero overall",
                 "the body is gaining energy over that section",
                 "energy is being removed from the body over that section",
                 "the force is negative but the work is positive"], "answer": 2,
     "hint": "Negative area means negative work.",
     "explanation": "Area below the axis is negative work — a resistive force removing energy from "
                    "the body. The total work is the algebraic sum of all the signed areas."},
    {"id": "P24", "category": "Fields", "type": "mcq", "slo": "3.4.1",
     "prompt": "Which of these is a conservative force?",
     "options": ["Friction", "Air resistance", "Gravity", "Drag"], "answer": 2,
     "hint": "Which one can store energy in a potential instead of dissipating it?",
     "explanation": "Gravity stores mgh and its work depends only on the height lost, not the route. "
                    "The other three all dissipate energy and depend on the path taken."},
    {"id": "P25", "category": "Fields", "type": "mcq", "slo": "3.4.1",
     "prompt": "A conservative field is one in which...",
     "options": ["the force is always small",
                 "the work done round any closed loop is zero, and the work between two points is path-independent",
                 "the force depends on the speed of the body",
                 "energy can never be recovered"], "answer": 1,
     "hint": "Imagine going round a loop and coming back to where you started.",
     "explanation": "Path-independence and zero net work round any closed loop are equivalent "
                    "statements. Both mean the energy is stored in a potential that can be recovered."},
    {"id": "P26", "category": "Work-energy theorem", "type": "numeric", "slo": "3.5.1",
     "prompt": "A net force of 12 N acts on a 4 kg body over a displacement of 3 m. By how much does its "
               "kinetic energy change? Enter the number only, in joules.",
     "answer": 36.0, "tolerance": 0.5, "unit": "J",
     "hint": "Work-energy theorem: W = ΔK.",
     "explanation": "W = 12 × 3 = 36 J, so ΔK = +36 J. The mass was not needed for this part of the "
                    "calculation — which is a hint about when the theorem is the quickest route."},
    {"id": "P27", "category": "Work-energy theorem", "type": "numeric", "slo": "3.5.2",
     "prompt": "A 3 kg body is accelerated from 2 m/s to 8 m/s. What net force acted on it over a "
               "displacement of 10 m? Enter the number only, in newtons.",
     "answer": 9.0, "tolerance": 0.1, "unit": "N",
     "hint": "Find ΔK first, then use W = Fd.",
     "explanation": "ΔK = ½(3)(8² ) − ½(3)(2²) = 96 − 6 = 90 J. The net work is 90 J, so "
                    "F d = 90 and F = 90/10 = 9.0 N. The alternative route gives the same thing: "
                    "a = (v² − u²)/(2s) = (64 − 4)/20 = 3 m/s², so F = ma = 3 × 3 = 9 N."},
    {"id": "P28", "category": "Work-energy theorem", "type": "mcq", "slo": "3.5.1",
     "prompt": "The work-energy theorem is valid in a resistive medium because...",
     "options": ["friction does no work",
                 "the work done against friction simply becomes part of the change in internal energy",
                 "the theorem only applies without friction",
                 "friction conserves momentum"], "answer": 1,
     "hint": "The theorem is about all forces, not only helpful ones.",
     "explanation": "The theorem says the *net* work done on a body equals its change in kinetic "
                    "energy, whatever forces are present. Friction contributes a negative term, "
                    "which is why a sliding body ends up with less kinetic energy."},
]

REFERENCES = [
    {"short": "OpenStax College Physics 2e",
     "title": "Chapter 7 and 8: Linear Momentum and Collisions",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/college-physics-2e",
     "used_for": "Equations of motion, momentum conservation and the elastic-collision derivation."},
    {"short": "MIT OpenCourseWare",
     "title": "8.01 Physics I: Classical Mechanics, Week 4",
     "org": "Massachusetts Institute of Technology",
     "url": "https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/",
     "used_for": "The impulse–momentum theorem and why conservation of momentum follows from Newton's third law."},
    {"short": "NPTEL",
     "title": "Engineering Mechanics: Work and Energy",
     "org": "Indian Institute of Technology",
     "url": "https://nptel.ac.in/courses",
     "used_for": "Area-under-curve work and the conservative/non-conservative field distinction."},
    {"short": "NASA Glenn Research Center",
     "title": "Free fall and the equations of motion",
     "org": "NASA",
     "url": "https://www.grc.nasa.gov/www/k-12/airplane/newton.html",
     "used_for": "Elementary treatment of free fall and the constant-acceleration equations."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 3",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 3.1.1 to 3.5.2."},
]
