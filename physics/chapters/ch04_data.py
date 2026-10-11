"""Chapter 4 content: Motion in Two Dimensions.

Twenty outcomes - the first chapter where the station count exceeds the outcome
count. The chapter owns two simulations of its own: a **trajectory studio** where
launch speed and angle sweep a whole family of paths at once, and a **rotation
bench** where every moment of inertia in the syllabus is spun on the same wheel
so their differences are visible rather than tabulated.
"""

from __future__ import annotations

import math

SLOS = [
    {"id": "4.1.1", "text": "Explain projectile motion.",
     "simple": "A projectile is anything thrown; its motion splits into a steady horizontal part and a falling vertical part.", "taught": "Projectile motion",
     "activity": "Trajectory studio with the two component motions drawn separately", "check": "Guided practice: identify horizontal and vertical motion and state what stays constant"},
    {"id": "4.1.2", "text": "Derive the relation for: a. time of flight, b. maximum height, c. horizontal range of a projectile, d. maximum horizontal range of a projectile.",
     "simple": "T = 2u sin θ/g, H = u² sin²θ/2g, R = u² sin 2θ/g, and R is greatest at 45°.", "taught": "Projectile relations",
     "activity": "Relation solver with the derivation steps exposed", "check": "Guided practice: derive and use all four relations"},
    {"id": "4.1.3", "text": "Solve word problems related to the given relations a, b, c and d.",
     "simple": "Numerical problems on time of flight, height, range and the 45° optimum.", "taught": "Projectile problems",
     "activity": "Worked numerical problems with a check on every answer", "check": "Guided practice: solve projectile word problems"},
    {"id": "4.1.4", "text": "Predict qualitatively the effect of air resistance on the motion of a projectile.",
     "simple": "Air resistance shortens the range, lowers the peak, and makes the fall steeper than the rise.", "taught": "Air resistance",
     "activity": "Side-by-side comparison of vacuum and resisted trajectories", "check": "Guided practice: predict and explain the effect of drag"},
    {"id": "4.2.1", "text": "Describe angular displacement, angular velocity and angular acceleration.",
     "simple": "θ in radians, ω = dθ/dt in rad s⁻¹, α = dω/dt in rad s⁻².", "taught": "Angular quantities",
     "activity": "Angle, speed and acceleration dials driven by one wheel", "check": "Guided practice: define and compute the three angular quantities"},
    {"id": "4.2.2", "text": "Derive the relationship between linear and angular displacement, velocity and acceleration.",
     "simple": "s = rθ, v = rω, a = rα — every point on a rigid body obeys these.", "taught": "Linear and angular relations",
     "activity": "Rotating disc with five marked radii", "check": "Guided practice: convert between linear and angular quantities"},
    {"id": "4.2.3", "text": "Solve word problems related to the rotational motion.",
     "simple": "Numerical problems using the angular equations of motion.", "taught": "Rotational problems",
     "activity": "Angular motion solver with the linear equivalents shown", "check": "Guided practice: solve rotational word problems"},
    {"id": "4.3.1", "text": "Define centripetal force and centripetal acceleration.",
     "simple": "Any force turning a body towards a centre, with a = v²/r and F = mv²/r.", "taught": "Centripetal force",
     "activity": "Circular motion explorer with the inward arrow always on show", "check": "Guided practice: compute centripetal acceleration and force"},
    {"id": "4.3.2", "text": "Derive centripetal acceleration when speed is uniform.",
     "simple": "Even at constant speed, the direction of the velocity changes, so there is an acceleration.", "taught": "Deriving a = v²/r",
     "activity": "Velocity-vector diagram showing the change over a small time", "check": "Guided practice: derive a = v²/r from the velocity triangle"},
    {"id": "4.3.3", "text": "Justify that a centrifuge is used to separate materials using centripetal force.",
     "simple": "Denser particles need a larger radius to get the same centripetal acceleration, so they move outward.", "taught": "The centrifuge",
     "activity": "Centrifuge simulator with particles sorting by density", "check": "Guided practice: explain how a centrifuge separates a mixture"},
    {"id": "4.3.4", "text": "Explain that the objects in orbiting satellites appear to be weightless.",
     "simple": "Satellite and astronaut fall together at the same rate, so the floor never pushes up on them.", "taught": "Weightlessness in orbit",
     "activity": "Apparent weight against altitude, including the ISS", "check": "Guided practice: explain apparent weightlessness and why it is not the same as zero gravity"},
    {"id": "4.3.5", "text": "Describe that artificial gravity is created to counter weightlessness.",
     "simple": "Rotating a spacecraft makes the floor push on the crew with a = ω²r.", "taught": "Artificial gravity",
     "activity": "Rotating habitat with the required rotation rate computed", "check": "Guided practice: calculate the rotation rate that gives Earth-like gravity"},
    {"id": "4.4.1", "text": "Explain moment of inertia and its SI unit with dimension.",
     "simple": "I = Σmr², the rotational analogue of mass. Unit kg m², dimension [ML²].", "taught": "Moment of inertia",
     "activity": "Moment of inertia builder with mass moved further from the axis", "check": "Guided practice: state the unit and dimension and compute I for a simple case"},
    {"id": "4.4.2", "text": "Compare the moment of inertia in rod, ring, disc and sphere.",
     "simple": "For the same m and R, ring > shell > disc > sphere > semi-disc: mass further out means larger I.", "taught": "Comparing shapes",
     "activity": "Rotation bench spinning every shape on one axle", "check": "Guided practice: rank shapes by I and justify from the mass distribution"},
    {"id": "4.4.3", "text": "Derive relationship between torque, moment of inertia and angular acceleration.",
     "simple": "τ = Iα, the rotational form of F = ma.", "taught": "τ = Iα",
     "activity": "Torque bench with τ, I and α shown as a live equation", "check": "Guided practice: use τ = Iα and contrast it with F = ma"},
    {"id": "4.4.4", "text": "Solve word problems related to the given relationships.",
     "simple": "Numerical problems on rotational dynamics.", "taught": "Rotational problems",
     "activity": "Problem set with both the linear and rotational routes", "check": "Guided practice: solve rotational word problems"},
    {"id": "4.5.1", "text": "Explain angular momentum and its SI unit with dimension.",
     "simple": "L = Iω. Unit kg m² s⁻¹, dimension [ML²T⁻¹].", "taught": "Angular momentum",
     "activity": "Momentum gauge reading Iω with the unit and dimension shown", "check": "Guided practice: compute angular momentum and state its unit and dimension"},
    {"id": "4.5.2", "text": "Solve word problems related to angular momentum.",
     "simple": "Numerical problems on L = Iω.", "taught": "Angular momentum problems",
     "activity": "Problem set with dimensional checks on every answer", "check": "Guided practice: solve angular momentum word problems"},
    {"id": "4.5.3", "text": "Explain the law of conservation of angular momentum.",
     "simple": "With no external torque, total L is constant — so lowering I raises ω.", "taught": "Conservation of angular momentum",
     "activity": "Skater simulator where pulling in the arms speeds up the spin", "check": "Guided practice: apply conservation and explain the change in spin"},
    {"id": "4.5.4", "text": "Illustrate the applications of conservation of angular momentum in: a. flywheels to store rotational energy, b. gyroscopes in navigation system, c. ice skaters to adjust their angular velocity.",
     "simple": "Flywheels smooth speed, gyroscopes hold a direction, skaters spin faster by shrinking I.", "taught": "Applications of angular momentum",
     "activity": "Four applications compared side by side", "check": "Guided practice: explain each application in terms of conserved L"},
]

STATIONS = [
    {"key": "overview", "label": "🗺️ Your route & outcomes", "slos": []},
    {"key": "projectile", "label": "🎯 Projectile motion", "slos": ["4.1.1"]},
    {"key": "relations", "label": "📐 The four relations", "slos": ["4.1.2", "4.1.3"]},
    {"key": "drag", "label": "🍃 Air resistance", "slos": ["4.1.4"]},
    {"key": "angular", "label": "🌀 Angular motion", "slos": ["4.2.1", "4.2.2", "4.2.3"]},
    {"key": "centripetal", "label": "🎡 Centripetal force", "slos": ["4.3.1", "4.3.2"]},
    {"key": "centrifuge", "label": "🧪 The centrifuge", "slos": ["4.3.3"]},
    {"key": "orbit", "label": "🛰️ Orbit and weightlessness", "slos": ["4.3.4", "4.3.5"]},
    {"key": "inertia", "label": "⚙️ Moment of inertia", "slos": ["4.4.1", "4.4.2"]},
    {"key": "torque", "label": "🔧 Torque and α", "slos": ["4.4.3", "4.4.4"]},
    {"key": "angularmomentum", "label": "🌀 Angular momentum", "slos": ["4.5.1", "4.5.2", "4.5.3", "4.5.4"]},
    {"key": "worked", "label": "🧮 Worked problems", "slos": []},
    {"key": "practice", "label": "🧠 Practice", "slos": []},
    {"key": "tutor", "label": "🤖 Atlas Tutor (offline AI)", "slos": []},
    {"key": "references", "label": "📚 References", "slos": []},
]

BIG_IDEAS = [
    ("Projectile motion is really two motions wearing a coat.",
     "Horizontal, the acceleration is zero so the speed never changes. Vertical, gravity "
     "takes over and the speed changes constantly. They are the same motion only because "
     "we insist on describing it with one pair of coordinates."),
    ("Rotation has its own version of every linear idea.",
     "Displacement becomes angle, velocity becomes ω, acceleration becomes α, mass becomes "
     "moment of inertia, and F = ma becomes τ = Iα. The two sets of equations are the same "
     "equations wearing different names."),
    ("What is conserved decides what you can predict.",
     "Linear momentum for collisions, angular momentum for spinning. Neither needs a force "
     "to be explained; conservation does the work."),
]

TAG = "CHAPTER 4 · OPEN"
INTRO = (
    "The busiest chapter in the first half of the book, and the one where the ideas of "
    "Chapters 2 and 3 come together. A projectile is a vector split into two perpendicular "
    "parts; a rotating body is linear motion repeated at many radii. There is a trajectory "
    "studio and a rotation bench waiting, and the chapter ends with the reason flying "
    "machines can lift their own weight."
)
ROUTE = ("Projectile motion → The four relations → Air resistance → Angular motion → "
         "Centripetal force → The centrifuge → Orbit and weightlessness → Moment of inertia → "
         "Torque → Angular momentum → Worked problems → Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("g taken as 9.8 m s⁻², planets as idealised spheres", "warn"),
                 ("Air resistance modelled qualitatively", "mute"),
                 ("Every number computed by this app", "good")]

NOTES = [
    ("⚠ WATCH OUT", "There are two independent motions, not one curved motion",
     "The horizontal and vertical velocities change completely independently. The "
     "horizontal velocity is constant throughout the flight; the vertical velocity grows "
     "linearly. Adding them to get a resultant speed is fine, but do not let one part "
     "change the rules of the other."),
    ("🎯 EXAM TIP", "R = u² sin 2θ / g, not u² sin θ / g",
     "The range uses sin **2θ**, while the height uses sin²θ. Writing R = 2u² sin θ cos θ / g "
     "first makes the doubling obvious and the 45° maximum falls straight out of it."),
    ("🔬 HONEST LIMIT", "Circular motion is an idealisation",
     "A body in circular motion at constant speed is a thought experiment; real objects "
     "always lose a little speed to drag. More importantly, treating ω as constant is the "
     "assumption that lets you use the rigid-body relations at all."),
]

PROJECTILE_RELATIONS = [
    {"symbol": "T", "name": "time of flight", "formula": r"T = \frac{2u\sin\theta}{g}",
     "from": "The time to rise equals the time to fall, because the vertical speed goes up then comes back to the same height.",
     "depends_on": "u and θ — not on the height of launch, provided it lands at the same level."},
    {"symbol": "H", "name": "maximum height", "formula": r"H = \frac{u^2\sin^2\theta}{2g}",
     "from": "At the top the vertical velocity is zero, so v² = u² + 2as gives 0 = u² sin²θ − 2gH.",
     "depends_on": "u² sin²θ — the height ignores the horizontal component entirely."},
    {"symbol": "R", "name": "horizontal range", "formula": r"R = \frac{u^2\sin 2\theta}{g}",
     "from": "Multiply the horizontal speed u cos θ by the time of flight 2u sin θ / g, and use 2 sin θ cos θ = sin 2θ.",
     "depends_on": "sin 2θ, which is 1 at θ = 45° — so 45° gives the longest range."},
    {"symbol": "R_max", "name": "maximum range", "formula": r"R_{\max} = \frac{u^2}{g}\ \text{at}\ \theta = 45^\circ",
     "from": "sin 2θ cannot exceed 1, and it reaches 1 when 2θ = 90°.",
     "depends_on": "only on u and g. At 45° the height is half the maximum: R_max = u²/g and H = u²/4g."},
]

PROJECTILE_DERIVATION = [
    "Split the launch velocity: uₓ = u cos θ stays constant, and u_y = u sin θ is acted on by g.",
    "Vertical motion with a = −g: u_y = u sin θ − gt. The ball rises while this is positive.",
    "Time of flight: put u_y = 0 to get t_top = u sin θ / g, then double it, because the "
    "fall back to the same level takes exactly as long as the rise.",
    "Maximum height: with u_y = 0, v² = u_y² + 2aH gives 0 = u² sin²θ − 2gH, so "
    "H = u² sin²θ / 2g.",
    "Range: the horizontal speed never changed, so R = u cos θ × T = u cos θ × 2u sin θ / g, "
    "which is u² sin 2θ / g using the double-angle identity.",
    "Maximum: sin 2θ is largest at 2θ = 90°, so θ = 45° and R_max = u²/g.",
]

AIR_RESISTANCE = [
    {"quantity": "Time of flight", "without": "2u sin θ / g",
     "with": "longer than the vacuum value",
     "why": "The descent is slowed by drag, so the projectile stays in the air longer on the way down."},
    {"quantity": "Horizontal range", "without": "u² sin 2θ / g", "with": "less",
     "why": "Drag opposes the horizontal velocity throughout, so it covers less ground in the same time."},
    {"quantity": "Maximum height", "without": "u² sin²θ / 2g", "with": "less",
     "why": "Part of the upward kinetic energy is spent working against drag before the apex."},
    {"quantity": "Shape of the path", "without": "a symmetric parabola",
     "with": "asymmetric, steeper on the way down",
     "why": "Near the apex the vertical speed is small, so drag is relatively stronger there and "
            "shortens the rise more than it shortens the fall."},
    {"quantity": "Angle for maximum range", "without": "45°", "with": "less than 45°",
     "why": "A flatter launch suits the extra time drag adds to the descent."},
]

ANGULAR_QUANTITIES = [
    {"quantity": "displacement", "linear": "s (m)", "angular": "θ (rad)",
     "relation": "s = rθ", "note": "θ must be in radians for this to hold exactly."},
    {"quantity": "velocity", "linear": "v (m s⁻¹)", "angular": "ω (rad s⁻¹)",
     "relation": "v = rω", "note": "The outermost point of a wheel moves fastest."},
    {"quantity": "acceleration", "linear": "a (m s⁻²)", "angular": "α (rad s⁻²)",
     "relation": "a = rα", "note": "This one is tangential; circular motion adds a_c = ω²r."},
    {"quantity": "force", "linear": "F (N)", "angular": "τ (N m)", "relation": "τ = F r sin θ",
     "note": "Only the component perpendicular to the lever turns the body."},
    {"quantity": "mass", "linear": "m (kg)", "angular": "I (kg m²)", "relation": "I = Σmr²",
     "note": "Moment of inertia is the rotational analogue of mass."},
    {"quantity": "newton's law", "linear": "F = ma", "angular": "τ = Iα",
     "relation": "the same law", "note": "The whole of rotational dynamics is this one line."},
    {"quantity": "momentum", "linear": "p = mv", "angular": "L = Iω",
     "relation": "same form", "note": "Unit kg m² s⁻¹, dimension [ML²T⁻¹]."},
]

ANGULAR_CONVERSION = [
    {"topic": "Why radians are special",
     "note": "One radian is the angle subtended by an arc equal to the radius itself. That is "
             "why a 60° sweep is exactly 1.047 rad, and why 2π rad is one full turn."},
    {"topic": "Revolutions and radians",
     "note": "One revolution = 2π rad. The number of revolutions is θ × 180/(360π)."},
    {"topic": "The rigid-body condition",
     "note": "s = rθ, v = rω and a = rα hold exactly for a rigid body rotating about a fixed "
             "axis — which is why every point keeps the same ω and α."},
    {"topic": "Total linear acceleration",
     "note": "A point on a spinning body has a tangential part rα and a centripetal part "
             "ω²r at right angles, so its total acceleration is √((rα)² + (ω²r)²)."},
]

CENTRIPETAL_DERIVATION = [
    "In uniform circular motion the speed v is constant but the direction of the velocity "
    "changes every instant.",
    "Acceleration is defined as the rate of change of velocity — and velocity is a vector, so "
    "changing only its direction is still an acceleration.",
    "Take two points a short time Δt apart. The velocity vectors have the same length v but "
    "different directions, so their tips lie on a circle of radius v.",
    "The chord joining the two tips has length vΔθ, and it subtends the angle Δθ at the centre.",
    "The change in velocity Δv therefore equals vΔθ, so a = Δv/Δt = vΔθ/Δt.",
    "But Δθ/Δt is the angular velocity ω, and v = rω, so a = vω = v(v/r) = **v²/r**.",
    "This acceleration always points to the centre — which is exactly why the name "
    "'centripetal' means 'towards the centre'.",
]

CENTRIFUGE_POINTS = [
    {"point": "Every particle needs the same centripetal acceleration",
     "detail": "In a rotating sample all particles share one ω, so a = ω²r. The particles with "
               "the greatest density have the largest mass and need the largest force."},
    {"point": "But the force available is the same for all",
     "detail": "The outward centrifugal effect competes with the same inward impulse for every "
               "particle, whatever its mass."},
    {"point": "So heavy particles must sit further out",
     "detail": "A larger r gives a larger ω²r, which is what the heavy particle needs. The dense "
               "material ends up packed against the wall of the tube."},
    {"point": "Which is why you never open a centrifuge while it is running",
     "detail": "The sediment is sitting hard against the outside of the tube at several times "
               "the force of gravity."},
]

ORBIT_FACTS = [
    {"fact": "g falls off, but not much",
     "detail": "g = GM/r², so at the International Space Station's altitude of about 400 km it "
               "is still about 90 % of the value at the surface."},
    {"fact": "Yet astronauts report weightlessness",
     "detail": "Because the spacecraft and everything inside it are all falling together at "
               "the same rate. The floor never has to push up on them."},
    {"fact": "So it is free fall, not an absence of gravity",
     "detail": "Gravity at that altitude is nearly as strong as at the ground. What is missing "
               "is the supporting force, which on Earth is what your legs push against."},
    {"fact": "This is why the ISS keeps re-raising itself",
     "detail": "It is continuously dragged into a lower orbit by the thin upper atmosphere. "
               "Without thrust it would slowly spiral back to Earth."},
]

MOMENT_OF_INERTIA_NOTES = [
    {"idea": "It depends on where the axis is",
     "detail": "A rod has I = 1/12 ML² about its centre and 1/3 ML² about one end — four times "
               "larger for the same rod, purely because of where the pivot is."},
    {"idea": "It depends on where the mass is",
     "detail": "Since I = Σmr², moving mass outwards always increases I. That is why a ring is "
               "harder to spin than a disc of the same mass and radius."},
    {"idea": "The unit and dimension",
     "detail": "kg m², dimension [ML²] — the same as mass × length². Multiply by rad s⁻¹ and "
               "you get the unit of angular momentum."},
    {"idea": "It is not 'weight of the body'",
     "detail": "Every point mass, however tiny, contributes mr². A swarm of flies in a wide "
               "basket has a much larger I than a lump of lead of the same total mass."},
]

L_APPLICATIONS = [
    {"application": "Flywheel",
     "how": "A heavy wheel is spun up and coupled to a shaft.",
     "why": "A large I means that a small change in torque produces only a small change in ω, "
            "so the shaft speed is smoothed against the jerky torque of a single cylinder "
            "engine."},
    {"application": "Gyroscope",
     "how": "A fast-spinning wheel mounted so its axis can turn freely.",
     "why": "With no external torque, L — and so the direction of the axis — cannot change. "
            "This stabilises a spacecraft and a bicycle."},
    {"application": "Ice skater",
     "how": "Pulling the arms in while spinning.",
     "why": "L is constant and I falls, so ω must rise. The classic demonstration, and the "
            "same trick a diver uses for a tuck."},
    {"application": "Diver",
     "how": "Tucks for somersaults, extends for entry.",
     "why": "A smaller I means more revolutions per second; a larger I means a slower, "
            "straighter entry."},
    {"application": "Helicopter tail rotor",
     "how": "A small rotor at the end of a long tail.",
     "why": "Torque = rF, so a long moment arm converts a small tail force into enough torque "
            "to counter the main rotor."},
]

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "A cricket lofted for maximum range",
     "level": "Foundation", "slos": ["4.1.2", "4.1.3"],
     "question": "A cricket ball is hit at 30 m/s at an angle of 30° above the horizontal. Taking "
                 "g = 9.8 m/s² and neglecting air resistance, find the time of flight, the maximum "
                 "height and the horizontal range.",
     "known": ["u = 30 m/s", "θ = 30°", "sin 30° = 0.5, cos 30° = 0.866, sin 60° = 0.866",
               "g = 9.8 m/s²"],
     "find": "T, H and R",
     "equation": r"T = \frac{2u\sin\theta}{g}, \quad H = \frac{u^2\sin^2\theta}{2g}, \quad "
                 r"R = \frac{u^2\sin 2\theta}{g}",
     "conversions": ["Angles must be in degrees for the sine and cosine. No unit conversion is "
                     "otherwise needed."],
     "substitution": r"T = \frac{2(30)(0.5)}{9.8}, \quad H = \frac{900(0.25)}{2(9.8)}, \quad "
                     r"R = \frac{900(0.866)}{9.8}",
     "calculation": [
         "Step 1 — components: uₓ = 30 × 0.866 = 25.98 m/s, u_y = 30 × 0.5 = 15.0 m/s.",
         "Step 2 — time of flight: T = 2 × 30 × 0.5 / 9.8 = 30/9.8 = 3.06 s. The rise alone is "
         "1.53 s.",
         "Step 3 — maximum height: H = 900 × 0.25 / 19.6 = 225/19.6 = 11.5 m.",
         "Step 4 — range: R = 900 × sin 60° / 9.8 = 900 × 0.866 / 9.8 = 79.5 m.",
         "Step 5 — check: R should also be uₓ × T = 25.98 × 3.06 = 79.5 m. ✓",
         "Step 6 — for comparison, at 45° the range would be u²/g = 900/9.8 = 91.8 m, larger. "
         "So 30° is not the angle for longest range; it was chosen here for the numbers.",
     ],
     "unit_check": r"T: [L T^{-1}][T]/[L T^{-2}] = [T];\ H: [L^2 T^{-2}]/[L T^{-2}] = [L];\ "
                   r"R: [L^2 T^{-2}]/[L T^{-2}] = [L]",
     "answer": "T = 3.06 s, H = 11.5 m, R = 79.5 m",
     "sig_fig_note": "30 m/s and the angle are each to two significant figures, so T = 3.1 s, H = 12 m and R = 80 m. "
                     "The values above are kept unrounded so the arithmetic can be followed.",
     "assumptions": ["Air resistance is neglected.",
                     "The ball is launched and lands at the same height."]},
    {"id": "WP2", "title": "The angle for maximum range",
     "level": "Developing", "slos": ["4.1.2"],
     "question": "A ball is thrown at 25 m/s. Show that the range is greatest at 45°, and find that "
                 "maximum range together with the maximum height at that angle.",
     "known": ["u = 25 m/s", "R = u² sin 2θ / g", "sin 2θ is greatest when 2θ = 90°",
               "g = 9.8 m/s²"],
     "find": "the optimal angle, R_max and the height at that angle",
     "equation": r"R = \frac{u^2\sin 2\theta}{g}, \qquad R_{\max} = \frac{u^2}{g}",
     "conversions": ["None needed."],
     "substitution": r"R_{\max} = \frac{25^2}{9.8} = \frac{625}{9.8}",
     "calculation": [
         "Step 1 — write the range as R = 2u² sin θ cos θ / g.",
         "Step 2 — 2 sin θ cos θ = sin 2θ, and sin 2θ ≤ 1 for every angle.",
         "Step 3 — sin 2θ = 1 when 2θ = 90°, that is θ = 45°. So 45° is the optimum, and the "
         "maximum range is R_max = u²/g.",
         "Step 4 — value: R_max = 625/9.8 = 63.8 m.",
         "Step 5 — the height at 45°: H = u² sin²45°/2g = 625 × 0.5 / 19.6 = 312.5/19.6 = 15.9 m.",
         "Step 6 — worth noticing: the height at the range-optimal angle is only half the "
         "greatest height the ball could reach (which would be u²/2g = 31.9 m at 90°). "
         "Maximum range and maximum height cannot both be achieved at once.",
     ],
     "unit_check": r"R_{\max} = [L^2 T^{-2}]/[L T^{-2}] = [L]",
     "answer": "θ = 45°, R_max = 63.8 m, and the height at that angle is 15.9 m",
     "sig_fig_note": "u = 25 m/s to two significant figures gives R_max = 64 m.",
     "assumptions": ["Launch and landing heights are equal and air resistance is neglected."]},
    {"id": "WP3", "title": "Centripetal acceleration of a satellite",
     "level": "Developing", "slos": ["4.3.1", "4.3.2"],
     "question": "A satellite moves in a circular orbit of radius 6.8 × 10⁶ m at 7.8 km s⁻¹. Find its "
                 "centripetal acceleration, the force this requires on a 1000 kg satellite, and "
                 "explain why the astronaut inside feels weightless.",
     "known": ["r = 6.8 × 10⁶ m", "v = 7.8 × 10³ m s⁻¹", "m = 1000 kg",
               "a_c = v²/r"],
     "find": "a_c, the force, and the explanation of weightlessness",
     "equation": r"a_c = \frac{v^2}{r}, \qquad F_c = m a_c",
     "conversions": ["7.8 km s⁻¹ = 7.8 × 10³ m s⁻¹. Using 7.8 instead gives an answer a "
                     "million times too small."],
     "substitution": r"a_c = \frac{(7.8\times10^{3})^2}{6.8\times10^{6}}, \qquad "
                     r"F_c = 1000\,a_c",
     "calculation": [
         "Step 1 — a_c = (7.8 × 10³)² / (6.8 × 10⁶) = 6.084 × 10⁷ / 6.8 × 10⁶ = 8.95 m s⁻².",
         "Step 2 — F_c = 1000 × 8.95 = 8950 N, about 9000 N.",
         "Step 3 — this is less than the 9800 N weight the satellite would have on the ground, "
         "because the orbit is above the surface where g is slightly weaker. That is why the "
         "orbit speed at the surface would be √(gR) = 7.9 km s⁻¹ — almost exactly the value given.",
         "Step 4 — why the astronaut feels weightless: the only force on the astronaut is "
         "gravity, 9000 N downwards, and that is exactly what is needed for the circular path. "
         "So the floor of the spacecraft exerts no force at all.",
         "Step 5 — 'weight' means the support force from the floor. It is zero, even though "
         "gravity itself is nearly as strong as at the surface. Weightlessness is free fall, "
         "not an absence of gravity.",
     ],
     "unit_check": r"a_c = [L^2 T^{-2}]/[L] = [L T^{-2}]; \ F_c = [M][L T^{-2}] = \mathrm{N}",
     "answer": "a_c ≈ 8.95 m s⁻², F_c ≈ 8950 N; the astronaut feels weightless because the satellite and everything in it fall together",
     "sig_fig_note": "The radius and speed are both to two significant figures, so a_c = 9.0 m s⁻² and F = 9000 N.",
     "assumptions": ["The orbit is circular and the height is small compared with Earth's radius.",
                     "The satellite is acted on by gravity alone."]},
    {"id": "WP4", "title": "Comparing moments of inertia",
     "level": "Developing", "slos": ["4.4.1", "4.4.2"],
     "question": "Find the moment of inertia of (a) a uniform ring of mass 2 kg and radius 0.20 m, "
                 "(b) a uniform disc of the same mass and radius, (c) a uniform rod of length 0.80 m "
                 "and mass 2 kg about an axis through its centre.",
     "known": ["m = 2 kg", "ring radius R = 0.20 m", "rod length L = 0.80 m",
               "ring I = MR², disc I = ½MR², rod (centre) I = 1/12 ML²"],
     "find": "I for each, in kg m²",
     "equation": r"I = \sum m r^2",
     "conversions": ["Lengths are already in metres."],
     "substitution": r"I_{\text{ring}} = 2(0.20)^2, \quad I_{\text{disc}} = \tfrac{1}{2}(2)(0.20)^2, "
                     r"\quad I_{\text{rod}} = \tfrac{1}{12}(2)(0.80)^2",
     "calculation": [
         "Step 1 — ring: I = 2 × 0.04 = 0.080 kg m². Every gram of the ring is at the full "
         "radius, so this is the largest possible I for this mass and radius.",
         "Step 2 — disc: I = ½ × 2 × 0.04 = 0.040 kg m². Exactly half the ring, because much of "
         "the disc's mass sits closer to the axis.",
         "Step 3 — rod about its centre: I = (1/12) × 2 × 0.64 = 0.107 kg m². This is larger than "
         "the ring, because a 0.80 m rod has parts further than 0.20 m from the axis — its ends "
         "are 0.40 m away.",
         "Step 4 — ranking so far: rod (0.107) > ring (0.080) > disc (0.040). Comparing shapes "
         "only means something if m and the outermost radius are the same, so the rod is not "
         "really comparable with the others.",
         "Step 5 — the rod about one end: I = (1/3) × 2 × 0.64 = 0.427 kg m², four times the value "
         "about its centre. The choice of axis matters as much as the shape.",
     ],
     "unit_check": r"I = [M][L^2] = [ML^2] = \mathrm{kg\,m^2}",
     "answer": "Ring 0.080 kg m², disc 0.040 kg m², rod about its centre 0.107 kg m²",
     "sig_fig_note": "All values are to two significant figures.",
     "assumptions": ["Each body is uniform, so its mass is evenly distributed.",
                     "All axes pass through the centre of mass."]},
    {"id": "WP5", "title": "A skater pulling in her arms",
     "level": "Challenge", "slos": ["4.5.1", "4.5.3", "4.5.4"],
     "question": "A skater spinning at 2.0 rev s⁻¹ pulls her arms in and her moment of inertia falls "
                 "from 1.60 to 0.40 kg m². Find her spin rate afterwards, and by what factor her "
                 "rotational kinetic energy changes.",
     "known": ["I₁ = 1.60 kg m², ω₁ = 2.0 rev s⁻¹",
               "I₂ = 0.40 kg m²", "No external torque, so I₁ω₁ = I₂ω₂"],
     "find": "ω₂ and the kinetic energy ratio",
     "equation": r"I_1\omega_1 = I_2\omega_2, \qquad K = \tfrac{1}{2} I\omega^2",
     "conversions": ["Revolutions per second are already angular rates; the ratio works in any "
                     "units as long as both are the same."],
     "substitution": r"\omega_2 = \frac{I_1\omega_1}{I_2} = \frac{1.60(2.0)}{0.40}",
     "calculation": [
         "Step 1 — conservation of angular momentum: 1.60 × 2.0 = 0.40 ω₂, so ω₂ = 3.20/0.40 = "
         "8.0 rev s⁻¹.",
         "Step 2 — her spin rate has quadrupled. It must: I fell by a factor of 4, so ω rose by "
         "the same factor to keep Iω unchanged.",
         "Step 3 — kinetic energy: K = ½Iω². Before: ½ × 1.60 × 4 = 3.2 J. After: "
         "½ × 0.40 × 64 = 12.8 J.",
         "Step 4 — the energy has quadrupled, and that energy came from her muscles. This is the "
         "one case in the chapter where angular momentum is conserved but energy is not.",
         "Step 5 — this is why the move is useful: 12.8 J of rotational energy is available to "
         "slow down a landing, and the quadruple spin rate makes the pirouette look fast.",
     ],
     "unit_check": r"K = [ML^2][T^{-2}] = \mathrm{J}; \ \text{the ratio is dimensionless}",
     "answer": "ω₂ = 8.0 rev s⁻¹, and the rotational kinetic energy rises by a factor of 4",
     "sig_fig_note": "All values are to two significant figures.",
     "assumptions": ["No external torque acts on the skater, so angular momentum is conserved.",
                     "The limbs are the only part of the body whose moment of inertia changes."]},
    {"id": "WP6", "title": "Artificial gravity in a rotating habitat",
     "level": "Challenge", "slos": ["4.3.5", "4.4.3"],
     "question": "A spacecraft 60 m in diameter is rotated so that the crew feel Earth's gravity, "
                 "9.8 m s⁻², at the rim. Find the rotation period, and state the angular velocity.",
     "known": ["radius R = 30 m", "a = ω²R = 9.8 m s⁻²"],
     "find": "ω and the rotation period T",
     "equation": r"a = \omega^2 R \quad\Rightarrow\quad \omega = \sqrt{\frac{a}{R}}, \qquad "
                 r"T = \frac{2\pi}{\omega}",
     "conversions": ["Diameter in metres, so the radius is 30 m."],
     "substitution": r"\omega = \sqrt{\frac{9.8}{30}} = \sqrt{0.3267}, \qquad T = \frac{2\pi}{0.5716}",
     "calculation": [
         "Step 1 — the floor must push the crew up with 9.8 N per kilogram. That push is a "
         "centripetal acceleration: a = ω²R.",
         "Step 2 — ω = √(9.8/30) = √0.3267 = 0.5716 rad s⁻¹.",
         "Step 3 — period: T = 2π/ω = 6.283/0.5716 = 11.0 s.",
         "Step 4 — that is about 5.5 revolutions per minute, a deliberately gentle rate.",
         "Step 5 — the reason for the gentle rate is Coriolis force. At much higher rotation "
         "rates a person walking would be pushed sideways, and at more than about 2 rpm "
         "astronauts find it impossible to walk normally. Bigger habitats need slower spins for "
         "the same gravity, which is why the design maximises the radius.",
     ],
     "unit_check": r"\omega = [T^{-1}] = \mathrm{rad\,s^{-1}};\ a = [T^{-1}][L] = [L T^{-2}] = \mathrm{m\,s^{-2}}",
     "answer": "ω = 0.572 rad s⁻¹, rotation period T = 11.0 s",
     "sig_fig_note": "The diameter 60 m is to one or two significant figures, so T ≈ 11 s.",
     "assumptions": ["The crew stand on the rim at R = 30 m.",
                     "The rotation rate is slow enough that Coriolis effects are tolerable."]},
]

PRACTICE_QUESTIONS = [
    {"id": "P1", "category": "Projectile motion", "type": "mcq", "slo": "4.1.1",
     "prompt": "During a projectile's flight, which statement is always true (no air resistance)?",
     "options": ["The vertical velocity is constant", "The horizontal velocity is constant",
                 "The speed is constant", "The acceleration is zero"], "answer": 1,
     "hint": "Gravity acts vertically only.",
     "explanation": "Only gravity acts, and gravity is vertical, so the horizontal velocity is "
                    "unaffected. The vertical velocity changes steadily, so neither the speed nor "
                    "the total acceleration is constant."},
    {"id": "P2", "category": "Projectile relations", "type": "numeric", "slo": "4.1.2",
     "prompt": "A ball is thrown at 20 m/s at 30° above the horizontal. Taking g = 10 m/s², find the "
               "time of flight. Enter the number only, in seconds.",
     "answer": 2.0, "tolerance": 0.05, "unit": "s",
     "hint": "T = 2u sin θ / g.",
     "explanation": "T = 2 × 20 × 0.5 / 10 = 2.0 s. The time to the top is half that, 1.0 s."},
    {"id": "P3", "category": "Projectile relations", "type": "numeric", "slo": "4.1.2",
     "prompt": "At what angle is the horizontal range greatest? Enter the number only, in degrees.",
     "answer": 45.0, "tolerance": 0.5, "unit": "°",
     "hint": "R = u² sin 2θ / g, and sin 2θ is greatest at 2θ = 90°.",
     "explanation": "45°. sin 2θ cannot exceed 1, and it reaches 1 when 2θ = 90°. The height at "
                    "that angle is only half the greatest height the ball could reach."},
    {"id": "P4", "category": "Projectile relations", "type": "numeric", "slo": "4.1.2",
     "prompt": "A ball is thrown at 40 m/s. Taking g = 10 m/s², find its maximum horizontal range. "
               "Enter the number only, in metres.",
     "answer": 160.0, "tolerance": 0.5, "unit": "m",
     "hint": "R_max = u² / g.",
     "explanation": "160 m. R_max = 40² / 10 = 160 m, reached at 45°."},
    {"id": "P5", "category": "Projectile relations", "type": "numeric", "slo": "4.1.3",
     "prompt": "A ball is launched at 25 m/s at 60° above the horizontal with g = 9.8 m/s². Find the "
               "maximum height. Enter the number only, in metres.",
     "answer": 23.915816326530607, "tolerance": 0.1, "unit": "m",
     "hint": "H = u² sin²θ / 2g.",
     "explanation": "H = 625 × 0.75 / 19.6 = 468.75/19.6 = 19.9 m. The 60° launch therefore "
                    "reaches a greater height than the 45° launch, which reaches u²/4g = "
                    "15.9 m — yet both have exactly the same range, because sin 60° = sin 120°."},
    {"id": "P6", "category": "Projectile relations", "type": "mcq", "slo": "4.1.3",
     "prompt": "A ball is launched at 30° and then at 60° with the same speed. What happens to the "
               "range?",

     "hint": "Compare sin 60° with sin 120°.",
     "options": ["The 30° launch goes further", "The 60° launch goes further",
                 "They travel the same distance", "It depends on the launch height"], "answer": 2,
     "hint": "Compare sin 60° with sin 120°.",
     "explanation": "The same distance. R ∝ sin 2θ, and sin 60° = sin 120° = 0.866. Any two "
                    "angles that add to 90° give the same range, so 30° and 60° are equally good "
                    "for distance — though 60° stays in the air longer and peaks higher."},
    {"id": "P7", "category": "Projectile relations", "type": "numeric", "slo": "4.1.3",
     "prompt": "A football is kicked at 25 m/s at 40° above the horizontal. Taking g = 9.8 m/s², find "
               "the horizontal range. Enter the number only, in metres.",
     "answer": 62.80661690128877, "tolerance": 0.2, "unit": "m",
     "hint": "R = u² sin 2θ / g, with 2θ = 80°.",
     "explanation": "R = 625 × sin 80° / 9.8 = 625 × 0.9848 / 9.8 = 62.81 m."},
    {"id": "P8", "category": "Air resistance", "type": "mcq", "slo": "4.1.4",
     "prompt": "Compared with the same projectile in a vacuum, air resistance makes the landing point...",
     "options": ["further away", "closer", "at the same place", "higher"], "answer": 1,
     "hint": "Drag acts against the horizontal motion throughout the flight.",
     "explanation": "Closer. Drag removes horizontal speed continuously, so less ground is "
                    "covered. The peak is also lower and the descent takes longer."},
    {"id": "P9", "category": "Air resistance", "type": "mcq", "slo": "4.1.4",
     "prompt": "With air resistance, the best angle for maximum range is...",
     "options": ["45°, unchanged", "greater than 45°", "less than 45°", "90°"], "answer": 2,
     "hint": "Drag lengthens the descent, and a flatter launch suits a longer descent.",
     "explanation": "Less than 45°. The extra time drag adds to the descent is used more "
                    "efficiently by a flatter launch."},
    {"id": "P10", "category": "Air resistance", "type": "mcq", "slo": "4.1.4",
     "prompt": "Why is the path of a projectile under air resistance not symmetric?",
     "options": ["Gravity is weaker on the way down",
                 "Drag is relatively stronger near the apex where the vertical speed is small",
                 "The launch force is stronger", "The horizontal speed increases"], "answer": 1,
     "hint": "Compare the vertical speed near the top with the speed at launch.",
     "explanation": "Near the apex the total speed is smallest, so drag is relatively most "
                    "effective there, shortening the rise more than the fall. The path becomes "
                    "steeper on the descending limb."},

    {"id": "P11", "category": "Angular quantities", "type": "mcq", "slo": "4.2.1",
     "prompt": "The SI unit of angular displacement is...",
     "options": ["the degree", "the revolution", "the radian", "the newton metre"], "answer": 2,
     "hint": "Degrees and revolutions are both non-SI.",
     "explanation": "The radian. One radian is the angle subtended by an arc whose length "
                    "equals the radius; 2π rad is one full turn."},
    {"id": "P12", "category": "Angular quantities", "type": "numeric", "slo": "4.2.1",
     "prompt": "Convert 180 degrees to radians. Enter the number only.",
     "answer": 3.141592653589793, "tolerance": 0.01, "unit": "rad",
     "hint": "Multiply by π/180.",
     "explanation": "180° = π rad. The relation θ(rad) = θ(deg) × π/180 is worth memorising; "
                    "missing it is the commonest error in this chapter."},
    {"id": "P13", "category": "Linear and angular", "type": "numeric", "slo": "4.2.2",
     "prompt": "A wheel of radius 0.50 m rotates at 4.0 rad s⁻¹. Find the speed of a point on the rim. "
               "Enter the number only, in m s⁻¹.",
     "answer": 2.0, "tolerance": 0.02, "unit": "m s⁻¹",
     "hint": "v = rω.",
     "explanation": "v = 0.50 × 4.0 = 2.0 m s⁻¹. Every point on the rim is at the same radius, "
                    "so they all move at the same speed."},
    {"id": "P14", "category": "Linear and angular", "type": "numeric", "slo": "4.2.2",
     "prompt": "A point 0.30 m from an axis sweeps 90°. How far does it travel? Enter the number "
               "only, in metres.",
     "answer": 0.47123889803846897, "tolerance": 0.005, "unit": "m",
     "hint": "s = rθ, and θ must be in radians.",
     "explanation": "θ = 90° = 1.5708 rad, so s = 0.30 × 1.5708 = 0.471 m. Using 90 directly "
                    "instead of 1.5708 gives 27 m, which is a factor of 2π out."},
    {"id": "P15", "category": "Linear and angular", "type": "mcq", "slo": "4.2.3",
     "prompt": "A wheel of radius 1 m turns at 2 rad s⁻¹. What is the tangential acceleration of a rim "
               "point if the wheel slows at 1 rad s⁻²?",
     "options": ["1 m s⁻²", "2 m s⁻²", "4 m s⁻²", "0 m s⁻²"], "answer": 1,
     "hint": "a_t = rα.",
     "explanation": "a_t = rα = 1 × 1 = 1 m s⁻², opposing the motion. This is the tangential "
                    "part; the point also has a centripetal acceleration ω²r = 4 m s⁻² towards "
                    "the centre, and the two are at right angles."},

    {"id": "P16", "category": "Centripetal force", "type": "numeric", "slo": "4.3.1",
     "prompt": "A car travels at 20 m/s round a bend of radius 50 m. Find the centripetal "
               "acceleration. Enter the number only, in m s⁻².",
     "answer": 8.0, "tolerance": 0.05, "unit": "m s⁻²",
     "hint": "a_c = v²/r.",
     "explanation": "a_c = 400/50 = 8.0 m s⁻². This is the sideways acceleration the tyres must "
                    "supply through friction — which is why icy bends are dangerous."},
    {"id": "P17", "category": "Centripetal force", "type": "numeric", "slo": "4.3.1",
     "prompt": "A 1200 kg car goes round a 60 m bend at 15 m/s. Find the centripetal force. Enter "
               "the number only, in newtons.",
     "answer": 4500.0, "tolerance": 20.0, "unit": "N",
     "hint": "F_c = mv²/r.",
     "explanation": "F = 1200 × 225/60 = 4500 N. A sideways force of this size comes entirely "
                    "from friction at the tyres."},
    {"id": "P18", "category": "Centripetal force", "type": "mcq", "slo": "4.3.2",
     "prompt": "A body moves at constant speed around a circle. Its acceleration is...",
     "options": ["zero, because the speed is constant", "non-zero, towards the centre",
                 "non-zero, because the velocity changes direction", "tangential only"],
     "answer": 1,
     "hint": "Acceleration is the rate of change of velocity, and velocity is a vector.",
     "explanation": "Non-zero. Speed constant means |v| is constant, but the direction of v is "
                    "turning every instant, and that change is an acceleration directed to the "
                    "centre."},
    {"id": "P19", "category": "Centripetal force", "type": "mcq", "slo": "4.3.2",
     "prompt": "In uniform circular motion, the centripetal force...",
     "options": ["does work, and increases the body's kinetic energy",
                 "does no work, because it is always perpendicular to the velocity",
                 "does negative work, because it opposes the motion"],
     "answer": 1,
     "hint": "The force is perpendicular to the velocity — what does cos 90° give?",
     "explanation": "It does no work. The centripetal force is perpendicular to the velocity at "
                    "every instant, so W = Fd cos 90° = 0. It changes direction but never "
                    "speed. This is why a satellite in circular orbit needs no engine at all, "
                    "and why a ball on a string keeps whirling at a constant speed with no "
                    "energy input."},
    {"id": "P20", "category": "The centrifuge", "type": "mcq", "slo": "4.3.3",
     "prompt": "In a centrifuge, dense particles end up...",
     "options": ["near the axis", "further from the axis", "at random", "at the top only"],
     "answer": 1,
     "hint": "Every particle needs the same centripetal acceleration ω²r, which grows with r.",
     "explanation": "Further from the axis. The heavy particle needs more centripetal force, and "
                    "the only way to get more is to sit at a larger radius, where ω²r is bigger."},
    {"id": "P21", "category": "The centrifuge", "type": "mcq", "slo": "4.3.3",
     "prompt": "The separation in a centrifuge relies on the same effect as...",
     "options": ["a ball thrown upward", "an artificial satellite in circular orbit",
                 "a car braking", "a spring compressing"], "answer": 1,
     "hint": "Both involve particles needing a centripetal acceleration.",
     "explanation": "A satellite needs a centripetal acceleration to stay in orbit, and a "
                    "centrifuge creates the same requirement in a liquid sample. Both are the "
                    "same physics at different scales."},
    {"id": "P22", "category": "Orbit", "type": "mcq", "slo": "4.3.4",
     "prompt": "An astronaut in the International Space Station is weightless because...",
     "options": ["there is no gravity in orbit", "gravity is very weak at that height",
                 "both the astronaut and the station are falling together",
                 "the station moves faster than light"], "answer": 2,
     "hint": "What would happen if the station did not fall as well?",
     "explanation": "Both fall together at the same rate, so the floor never has to push up on the "
                    "astronaut. Gravity at 400 km is still about 90 % of its surface value — this "
                    "is free fall, not an absence of gravity."},
    {"id": "P23", "category": "Orbit", "type": "numeric", "slo": "4.3.4",
     "prompt": "What fraction of Earth's surface gravity remains at an altitude of 6400 km? Earth's "
               "radius is 6371 km. Enter the ratio only.",
     "answer": 0.49613266649978045, "tolerance": 0.01, "unit": "",
     "hint": "g_h = g (R/(R+h))².",
     "explanation": "(6371/12771)² = 0.249... so about 0.25 of surface gravity. Wait — R + h = "
                    "12771 km, so (6371/12771)² = 0.2489, meaning roughly a quarter of surface "
                    "gravity remains at that height."},
    {"id": "P24", "category": "Orbit", "type": "numeric", "slo": "4.3.5",
     "prompt": "A rotating habitat of radius 40 m is spun so the crew feel 9.8 m s⁻². Find the "
               "rotation period. Enter the number only, in seconds.",
     "answer": 12.693951251881046, "tolerance": 0.1, "unit": "s",
     "hint": "ω = √(a/R), then T = 2π/ω.",
     "explanation": "ω = √(9.8/40) = 0.4950 rad s⁻¹, so T = 2π/0.4950 = 12.7 s, about 4.7 rpm. "
                    "Larger habitats need gentler spins for the same felt gravity."},
    {"id": "P25", "category": "Moment of inertia", "type": "mcq", "slo": "4.4.1",
     "prompt": "The SI unit and dimension of moment of inertia are...",
     "options": ["kg m, [ML]", "kg m² s⁻¹, [ML²T⁻¹]", "kg m², [ML²]", "rad s⁻¹, [T⁻¹]"], "answer": 2,
     "hint": "I = Σmr².",
     "explanation": "kg m² and [ML²]. Multiply by rad s⁻¹ and you get the unit of angular momentum."},
    {"id": "P26", "category": "Moment of inertia", "type": "mcq", "slo": "4.4.2",
     "prompt": "For the same mass and radius, which has the greatest moment of inertia?",
     "options": ["A solid disc", "A solid sphere", "A thin ring", "A semi-disc"], "answer": 2,
     "hint": "Which puts all its mass at the full radius?",
     "explanation": "The ring, with I = MR². Order is ring (1) > hollow sphere (2/3) > disc "
                    "(1/2) > solid sphere (2/5) > semi-disc (1/8), all times MR²."},
    {"id": "P27", "category": "Moment of inertia", "type": "numeric", "slo": "4.4.2",
     "prompt": "Find the moment of inertia of a uniform ring of mass 3 kg and radius 0.20 m about its "
               "central axis. Enter the number only, in kg m².",
     "answer": 0.12, "tolerance": 0.002, "unit": "kg m²",
     "hint": "I = MR² for a thin ring.",
     "explanation": "I = 3 × 0.04 = 0.12 kg m². Every element is at the full radius, so there is "
                    "no averaging-down."},
    {"id": "P28", "category": "Moment of inertia", "type": "numeric", "slo": "4.4.2",
     "prompt": "Find the moment of inertia of a uniform rod of mass 2 kg and length 0.60 m about an "
               "axis through its centre. Enter the number only, in kg m².",
     "answer": 0.06, "tolerance": 0.001, "unit": "kg m²",
     "hint": "I = ML²/12 about the centre.",
     "explanation": "I = (1/12) × 2 × 0.36 = 0.060 kg m²."},
    {"id": "P29", "category": "Torque", "type": "numeric", "slo": "4.4.3",
     "prompt": "A torque of 12 N m acts on a wheel of moment of inertia 3.0 kg m². Find the angular "
               "acceleration. Enter the number only, in rad s⁻².",
     "answer": 4.0, "tolerance": 0.05, "unit": "rad s⁻²",
     "hint": "α = τ/I.",
     "explanation": "α = 12/3.0 = 4.0 rad s⁻². The rotational form of a = F/m."},
    {"id": "P30", "category": "Torque", "type": "numeric", "slo": "4.4.3",
     "prompt": "A 20 N force acts at the end of a 0.80 m spanner at 90° to the spanner. Find the "
               "torque. Enter the number only, in N m.",
     "answer": 16.0, "tolerance": 0.1, "unit": "N m",
     "hint": "τ = rF sin θ, and sin 90° = 1.",
     "explanation": "τ = 0.80 × 20 × 1 = 16 N m, the largest torque that force can give."},
    {"id": "P31", "category": "Torque", "type": "mcq", "slo": "4.4.3",
     "prompt": "The rotational analogue of Newton's second law F = ma is...",
     "options": ["τ = Iα", "L = Iω", "I = mr²", "τ = Fd"], "answer": 0,
     "hint": "Force becomes torque, mass becomes moment of inertia.",
     "explanation": "τ = Iα. The whole of rotational dynamics follows from this one line, exactly "
                    "as Newton's second law governs linear dynamics."},
    {"id": "P32", "category": "Angular momentum", "type": "numeric", "slo": "4.5.1",
     "prompt": "A body has moment of inertia 4.0 kg m² and rotates at 6.0 rad s⁻¹. Find its angular "
               "momentum. Enter the number only, in kg m² s⁻¹.",
     "answer": 24.0, "tolerance": 0.1, "unit": "kg m² s⁻¹",
     "hint": "L = Iω.",
     "explanation": "L = 4.0 × 6.0 = 24 kg m² s⁻¹."},
    {"id": "P33", "category": "Angular momentum", "type": "numeric", "slo": "4.5.3",
     "prompt": "A spinning body has I = 2.0 kg m² at 5.0 rad s⁻¹. Its moment of inertia suddenly "
               "becomes 0.50 kg m². Find the new angular velocity. Enter the number only.",
     "answer": 20.0, "tolerance": 0.1, "unit": "rad s⁻¹",
     "hint": "With no external torque, Iω is unchanged.",
     "explanation": "ω₂ = (2.0 × 5.0)/0.50 = 20 rad s⁻¹. Quartering I quadruples ω — which is "
                    "exactly what a spinning skater does when she pulls her arms in."},
    {"id": "P34", "category": "Angular momentum", "type": "mcq", "slo": "4.5.3",
     "prompt": "Angular momentum is conserved when...",
     "options": ["the kinetic energy is also conserved",
                 "no external torque acts on the system",
                 "the body is spinning slowly", "there is friction present"], "answer": 1,
     "hint": "What is the rotational counterpart of a zero resultant force?",
     "explanation": "When no external torque acts. Friction and a steady applied torque both "
                    "change L, which is why a skater's spin slows slowly once she extends her arms."},
    {"id": "P35", "category": "Applications", "type": "mcq", "slo": "4.5.4",
     "prompt": "A gyroscope keeps its axis pointing the same way in space because...",
     "options": ["its weight balances it", "with no external torque, its angular momentum cannot change",
                 "it is spinning very fast so friction vanishes", "it is made of heavy metal"], "answer": 1,
     "hint": "Direction of L is fixed direction of the spin axis.",
     "explanation": "L points along the axis and cannot change without a torque, so the axis stays "
                    "fixed. This is what stabilises spacecraft attitude control."},

    {"id": "P36", "category": "Rotational dynamics", "type": "numeric", "slo": "4.4.4",
     "prompt": "A 25 kg grinding wheel turns at 60 rad s\u207b\u00b9. A tangential force of 6.0 N "
               "acts on its rim at a radius of 0.20 m. Find the torque. Enter the number only, "
               "in N m.",
     "answer": 1.2, "tolerance": 0.05, "unit": "N m",
     "hint": "\u03c4 = rF sin \u03b8 with \u03b8 = 90\u00b0, so \u03c4 = rF.",
     "explanation": "\u03c4 = 0.20 \u00d7 6.0 = 1.2 N m. A force at 90\u00b0 to the radius gives "
                    "the greatest possible torque for that force."},
    {"id": "P37", "category": "Rotational dynamics", "type": "numeric", "slo": "4.4.4",
     "prompt": "The same 1.2 N m torque acts on that 25 kg wheel while it keeps a steady "
               "60 rad s\u207b\u00b9. Find the angular deceleration. Enter the number only, "
               "in rad s\u207b\u00b2.",
     "answer": -0.048, "tolerance": 0.005, "unit": "rad s\u207b\u00b2",
     "hint": "\u03b1 = \u03c4/I. Find I first, then divide \u03c4 by it and keep the sign.",
     "explanation": "I = \u00bdmr\u00b2 = 0.5 \u00d7 25 \u00d7 0.20\u00b2 = 0.50 kg m\u00b2, so "
                    "\u03b1 = -1.2/0.50 = -0.048 rad s\u207b\u00b2. The negative sign is what slows "
                    "the wheel down; it is not speeding up."},
    {"id": "P38", "category": "Angular momentum", "type": "numeric", "slo": "4.5.2",
     "prompt": "A 2.0 kg disc of radius 0.15 m spins at 8.0 rad s\u207b\u00b9 about its central "
               "axis. Find its angular momentum. Enter the number only, in kg m\u00b2 s\u207b\u00b9.",
     "answer": 0.18, "tolerance": 0.01, "unit": "kg m\u00b2 s\u207b\u00b9",
     "hint": "L = I\u03c9, and a solid disc about its central axis has I = \u00bdmr\u00b2.",
     "explanation": "I = 0.5 \u00d7 2.0 \u00d7 0.15\u00b2 = 0.0225 kg m\u00b2, then "
                    "L = 0.0225 \u00d7 8.0 = 0.18 kg m\u00b2 s\u207b\u00b9."},
    {"id": "P39", "category": "Angular momentum", "type": "numeric", "slo": "4.5.2",
     "prompt": "An ice skater of mass 50 kg spins at 2.5 rev s\u207b\u00b9 with her arms out. "
               "She pulls them in and her angular speed rises to 5.0 rev s\u207b\u00b9. Find "
               "her final moment of inertia. Enter the number only, in kg m\u00b2.",
     "answer": 5.0, "tolerance": 0.2, "unit": "kg m\u00b2",
     "hint": "With no external torque, I\u03c9 stays constant, so I\u2081\u03c9\u2081 = "
             "I\u2082\u03c9\u2082. rev s\u207b\u00b9 is fine; the units cancel.",
     "explanation": "I\u2082 = 50 \u00d7 2.5 / 5.0 = 5.0 kg m\u00b2. She is far harder to spin "
                    "with her arms tucked in, because her mass then sits closer to the axis."},
]

REFERENCES = [
    {"short": "OpenStax University Physics Vol. 1",
     "title": "Chapters 10-11: Rotational Motion and Static Equilibrium",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/university-physics-volume-1",
     "used_for": "Projectile relations, angular quantities and the derivation of a = v²/r."},
    {"short": "OpenStax College Physics 2e",
     "title": "Chapter 10: Rotational Motion and Angular Momentum",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/college-physics-2e",
     "used_for": "Moments of inertia for standard shapes and the conservation of angular momentum."},
    {"short": "NASA",
     "title": "Why do astronauts float in the International Space Station?",
     "org": "NASA",
     "url": "https://www.nasa.gov/",
     "used_for": "Weightlessness as free fall, and the centripetal acceleration that keeps a station in orbit."},
    {"short": "Khan Academy",
     "title": "Projectile motion and the range formula",
     "org": "Khan Academy",
     "url": "https://www.khanacademy.org/physics/two-dimensional-motion/projectile-motion",
     "used_for": "Step-by-step derivations of T, H and R, and the 45° optimum."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 4",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 4.1.1 to 4.5.4."},
]