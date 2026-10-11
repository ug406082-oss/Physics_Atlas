"""Chapter 7 content: Oscillations.

Thirteen outcomes across four sections. The chapter owns two linked instruments:
an **S.H.M. scope** that draws displacement, velocity and acceleration on one
time axis so the quarter-period offsets are visible rather than asserted, and a
**pendulum rig** that integrates the full nonlinear equation when the swing is
large, so the small-angle approximation can be compared against the truth.
"""

from __future__ import annotations

SLOS = [
    {"id": "7.1.1", "text": "Define periodic and non-periodic oscillation.",
     "simple": "Periodic motion repeats to within a fraction of a percent. Non-periodic motion does not repeat at all.", "taught": "Periodic and non-periodic motion",
     "activity": "Classifier with a self-test on recorded samples", "check": "Guided practice: classify systems and justify from the repeat behaviour"},
    {"id": "7.1.2", "text": "Describe Simple Harmonic Motion S.H.M.",
     "simple": "Acceleration proportional to displacement and directed towards the mean position: a = -ω²x.", "taught": "Simple harmonic motion",
     "activity": "Scope showing a = -ω²x holding at every point", "check": "Guided practice: verify a = -ω²x and identify what makes motion 'simple harmonic'"},
    {"id": "7.2.1", "text": "Define the following terms in the context of oscillations: a. displacement, b. amplitude, c. period, d. frequency, e. angular frequency, f. phase difference.",
     "simple": "The vocabulary of oscillation: how far, how big, how often, how fast, and where in the cycle you are.", "taught": "Terms of oscillation",
     "activity": "Definitions table with the units and dimensions of each", "check": "Guided practice: define each term with its unit and dimension"},
    {"id": "7.2.2", "text": "Relate S.H.M. with uniform circular motion.",
     "simple": "S.H.M. is the shadow of a point moving round a circle at constant speed.", "taught": "S.H.M. and circular motion",
     "activity": "The wheel and its projection drawn together", "check": "Guided practice: explain the connection and identify amplitude and speed"},
    {"id": "7.2.3", "text": "Derive expression for instantaneous displacement, velocity and acceleration in terms of angular velocity (omega).",
     "simple": "x = A sin ωt, v = Aω cos ωt, a = -Aω² sin ωt.", "taught": "The three S.H.M. expressions",
     "activity": "Scope with all three quantities traced together", "check": "Guided practice: derive and use the three expressions"},
    {"id": "7.2.4", "text": "Solve word problems related to the SLO #.",
     "simple": "Numerical problems on the three expressions, including phase.", "taught": "S.H.M. problems",
     "activity": "Problem set with a phase diagram on every answer", "check": "Guided practice: solve S.H.M. word problems"},
    {"id": "7.2.5", "text": "Analyse graphical representations of the variations of displacement, velocity and acceleration with time for simple harmonic motion.",
     "simple": "Velocity leads displacement by T/4, and acceleration is a further T/4 behind, so a is opposite to x.", "taught": "Reading S.H.M. graphs",
     "activity": "Three graphs on one axis with the quarter-period offsets marked", "check": "Guided practice: read amplitudes, periods and phase from graphs"},
    {"id": "7.3.1", "text": "Explain that the motion of a body under elastic restoring force is S.H.M.",
     "simple": "F = -kx gives a = -(k/m)x, which is exactly the S.H.M. condition.", "taught": "The mass-spring oscillator",
     "activity": "Spring rig with the force and acceleration traced", "check": "Guided practice: show a spring obeys a = -ω²x"},
    {"id": "7.3.2", "text": "Derive an expression for the time period of a mass-spring system.",
     "simple": "T = 2π√(m/k).", "taught": "Mass-spring period",
     "activity": "Period calculator with every dependency shown", "check": "Guided practice: derive T = 2π√(m/k) and state what it does not depend on"},
    {"id": "7.3.3", "text": "Solve word problems using the expression for the time period of a mass-spring system.",
     "simple": "Numerical problems on the mass-spring oscillator.", "taught": "Mass-spring problems",
     "activity": "Problem set with T, f and ω computed together", "check": "Guided practice: solve mass-spring word problems"},
    {"id": "7.4.1", "text": "Explain that the motion of a simple pendulum is S.H.M.",
     "simple": "For small angles the restoring force is proportional to displacement, which is the S.H.M. condition.", "taught": "The simple pendulum",
     "activity": "Pendulum rig with small-angle and large-angle traces overlaid", "check": "Guided practice: explain when the pendulum is S.H.M. and when it is not"},
    {"id": "7.4.2", "text": "Derive an expression for the time period of a simple pendulum.",
     "simple": "T = 2π√(L/g), for small oscillations only.", "taught": "Pendulum period",
     "activity": "Period calculator with the large-angle correction applied", "check": "Guided practice: derive T = 2π√(L/g) and state the limitation"},
    {"id": "7.4.3", "text": "Solve word problems using the expression for the time period of a simple pendulum.",
     "simple": "Numerical problems on the pendulum, including timing experiments.", "taught": "Pendulum problems",
     "activity": "Period table with timing error included", "check": "Guided practice: solve pendulum word problems"},
    {"id": "7.5.1", "text": "Derive an expression to show that energy is conserved in mass-spring system executing S.H.M.",
     "simple": "1/2 kA^2 = 1/2 m v^2 + 1/2 k x^2, so the sum never changes.", "taught": "Energy in S.H.M.",
     "activity": "Kinetic and potential traces on one time axis, crossing", "check": "Guided practice: derive the energy expression for a mass-spring system"},
    {"id": "7.5.2", "text": "Solve word problems related to given expression.",
     "simple": "E = (1/2) k A^2 at the extreme; the mass does not appear.", "taught": "Energy problems",
     "activity": "Calculator with amplitude and k, showing E at several positions", "check": "Guided practice: solve energy word problems"},
    {"id": "7.5.3", "text": "Analyse the interchange between kinetic and potential energy during simple harmonic motion.",
     "simple": "Energy swaps between kinetic and potential twice per cycle.", "taught": "The energy exchange",
     "activity": "Two curves, one rising as the other falls, over one period", "check": "Guided practice: analyse the kinetic-potential interchange"},
    {"id": "7.6.1", "text": "Exemplify free and forced oscillation.",
     "simple": "Free oscillations run on stored energy; forced ones are driven at a chosen frequency.", "taught": "Free and forced",
     "activity": "Two traces side by side, one decaying and one driven", "check": "Guided practice: distinguish free from forced oscillation"},
    {"id": "7.7.1", "text": "Define resonance.",
     "simple": "A large amplitude when the driving frequency matches the natural frequency.", "taught": "Resonance",
     "activity": "Amplitude against driving frequency with a spike at resonance", "check": "Guided practice: define resonance and locate it on a curve"},
    {"id": "7.7.2", "text": "Describe applications and consequences of resonance in real life.",
     "simple": "Bridges, glass, pushers, tuning forks - all useful and all destructive.", "taught": "Resonance in life",
     "activity": "Applications and hazards listed together", "check": "Guided practice: describe applications and consequences of resonance"},
    {"id": "7.8.1", "text": "Explain damped oscillation.",
     "simple": "Energy leaks away, so amplitude falls while frequency barely changes.", "taught": "Damping",
     "activity": "Amplitude envelope falling over time", "check": "Guided practice: explain damped oscillation"},
    {"id": "7.8.2", "text": "List different applications of damped oscillation.",
     "simple": "Shock absorbers, door closers, bicycle dampers, compasses in water.", "taught": "Uses of damping",
     "activity": "Application table with the damping mechanism named", "check": "Guided practice: list applications of damped oscillation"},
    {"id": "7.8.3", "text": "Illustrate displacement-time graphs to show light, critical and heavy damping.",
     "simple": "Light oscillates many times; critical returns fastest without overshoot; heavy does not oscillate.", "taught": "Degrees of damping",
     "activity": "Three displacement-time graphs drawn together", "check": "Guided practice: illustrate light, critical and heavy damping"},
]

STATIONS = [
    {"key": "overview", "label": "🗺️ Your route & outcomes", "slos": []},
    {"key": "periodic", "label": "🔄 Periodic & non-periodic", "slos": ["7.1.1"]},
    {"key": "shm", "label": "🌀 Simple harmonic motion", "slos": ["7.1.2"]},
    {"key": "terms", "label": "📖 The terms of oscillation", "slos": ["7.2.1"]},
    {"key": "circular", "label": "🎡 S.H.M. as circular motion", "slos": ["7.2.2"]},
    {"key": "expressions", "label": "📈 x, v and a", "slos": ["7.2.3", "7.2.4", "7.2.5"]},
    {"key": "spring", "label": "🧷 The mass-spring system", "slos": ["7.3.1", "7.3.2", "7.3.3"]},
    {"key": "pendulum", "label": "⏱ The simple pendulum", "slos": ["7.4.1", "7.4.2", "7.4.3"]},
    {"key": "energy", "label": "⚙️ Energy in S.H.M.", "slos": ["7.5.1", "7.5.2", "7.5.3"]},
    {"key": "driven", "label": "🔊 Free & forced, resonance, damping", "slos": ["7.6.1", "7.7.1", "7.7.2", "7.8.1", "7.8.2", "7.8.3"]},
    {"key": "worked", "label": "🧮 Worked problems", "slos": []},
    {"key": "practice", "label": "🧠 Practice", "slos": []},
    {"key": "tutor", "label": "🤖 Atlas Tutor (offline AI)", "slos": []},
    {"key": "practical", "label": "\uD83E\uDD9E Practical activities", "slos": []},
    {"key": "references", "label": "📚 References", "slos": []},
]

BIG_IDEAS = [
    ("S.H.M. has one defining feature, and everything follows from it.",
     "a = −ω²x. Acceleration proportional to displacement, and towards the centre. Get "
     "that and the graphs, the energy, the period formulas and the connection to a "
     "circle are all consequences rather than separate facts."),
    ("The three quantities are one-quarter cycle apart.",
     "Velocity leads displacement by T/4, and acceleration lags velocity by T/4 — which "
     "means acceleration is exactly half a cycle out of step with displacement, and so is "
     "always opposite in sign to it."),
    ("Every period formula has a hidden assumption.",
     "T = 2π√(m/k) needs a spring that obeys Hooke's law. T = 2π√(L/g) needs a small "
     "swing. Outside those conditions the motion is still periodic, but the simple "
     "formula is only an approximation — and the size of the error is worth knowing."),
]

TAG = "CHAPTER 7 · OPEN"
INTRO = (
    "Everything that repeats has the same vocabulary, whether it is a swing, a spring, "
    "a tuning fork or the current in a circuit. This chapter takes thirteen outcomes and "
    "builds them from a single relation, a = -ω²x. There is an S.H.M. scope for the three "
    "graphs and a pendulum rig that integrates the full nonlinear equation, so you can see "
    "exactly where the small-angle approximation stops being good enough."
)
ROUTE = ("Periodic motion → S.H.M. → The terms → S.H.M. as circular motion → x, v and a → "
         "The mass-spring system → The simple pendulum → Worked problems → Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("g taken as 9.8 m s⁻²", "warn"),
                 ("Large-angle pendulum integrated numerically", "mute"),
                 ("Every trace computed by this app", "good")]

NOTES = [
    ("⚠ WATCH OUT", "Small angles means about 10 degrees or less",
     "T = 2π√(L/g) is a small-angle approximation. At 10° the period is already about "
     "0.2 % long, at 30° about 1.7 %, and at 90° about 18 %. In an experiment this shows "
     "up as a systematic error that grows with the amplitude of the swing you chose."),
    ("🎯 EXAM TIP", "The period does not depend on the amplitude",
     "For ideal S.H.M. — a spring, or a pendulum swinging gently — doubling the amplitude "
     "changes nothing about the period. Real amplitudes change it, but only through the "
     "breakdown of the ideal assumptions. Questions that try to make the period depend on "
     "amplitude are testing whether you know this."),
    ("🔬 HONEST LIMIT", "Real oscillations damp and eventually stop",
     "Friction at a pivot and drag in the air remove energy steadily, so the amplitude "
     "decays even though the period barely changes. Every graph in this chapter is an "
     "undamped ideal, which is why a real pendulum eventually stops swinging rather than "
     "settling into a smaller and smaller endless arc."),
]

PERIODIC_EXAMPLES = [
    {"system": "A simple pendulum on a long string", "periodic": True,
     "reason": "Repeats to within a fraction of a percent. Only damping, which is slow, changes it."},
    {"system": "A tuning fork struck once", "periodic": True,
     "reason": "Vibrates at a very steady frequency, decaying only slowly in amplitude."},
    {"system": "The suspension of a car over a bump", "periodic": True,
     "reason": "The up-and-down motion repeats each time a wheel crosses the bump."},
    {"system": "A beating heart", "periodic": True,
     "reason": "Regular, though the rate is not constant across a lifetime."},
    {"system": "The rise and fall of a country's GDP", "periodic": True,
     "reason": "Business cycles repeat, but not on a fixed timetable."},
    {"system": "A seismograph trace during an earthquake", "periodic": False,
     "reason": "Each tremor has a different amplitude and duration, so the pattern never repeats."},
    {"system": "A leaf tumbling in the wind", "periodic": False,
     "reason": "Air currents push it differently every time."},
    {"system": "Sea level at one beach", "periodic": False,
     "reason": "Wind and atmospheric pressure add slow irregular changes on top of the tide."},
]

TERMS = [
    {"term": "displacement", "symbol": "x", "meaning": "Position measured from the mean position.",
     "unit": "m", "dimension": "[L]", "range": "−A to +A"},
    {"term": "amplitude", "symbol": "A", "meaning": "The greatest displacement from the mean.",
     "unit": "m", "dimension": "[L]", "range": "always positive"},
    {"term": "period", "symbol": "T", "meaning": "The time for one complete cycle.",
     "unit": "s", "dimension": "[T]", "range": "T = 1/f"},
    {"term": "frequency", "symbol": "f", "meaning": "Cycles per second.",
     "unit": "Hz", "dimension": "[T⁻¹]", "range": "f = 1/T"},
    {"term": "angular frequency", "symbol": "ω", "meaning": "How fast the phase advances.",
     "unit": "rad s⁻¹", "dimension": "[T⁻¹]", "range": "ω = 2π/T = 2πf"},
    {"term": "phase difference", "symbol": "Δφ", "meaning": "How far one oscillator is ahead of another.",
     "unit": "rad", "dimension": "[1]", "range": "0 to 2π"},
    {"term": "mechanical energy", "symbol": "E", "meaning": "Kinetic plus potential, constant for ideal S.H.M.",
     "unit": "J", "dimension": "[ML²T⁻²]", "range": "½kA² = ½mω²A²"},
]

SHM_CONDITION = [
    {"requirement": "Acceleration proportional to displacement",
     "expression": "a ∝ x", "note": "Without this there is no oscillation at all."},
    {"requirement": "Acceleration directed towards the mean position",
     "expression": "a = -ω²x", "note": "The minus sign is what makes it turn round rather than run away."},
    {"requirement": "The constant ω² is the same for every displacement",
     "expression": "a/x = constant", "note": "If the restoring force is not linear, the motion is periodic but not simple harmonic."},
]

CIRCULAR_CONNECTION = [
    {"step": "Take a point moving round a circle at constant speed",
     "detail": "Its speed and its angular velocity are both constant, so there is no tangential acceleration."},
    {"step": "The only acceleration is the centripetal one, a = ω²R, always towards the centre",
     "detail": "This is exactly the S.H.M. condition: acceleration proportional to displacement, directed to a fixed point."},
    {"step": "Now measure only the horizontal coordinate",
     "detail": "That coordinate oscillates between −R and +R, following R sin ωt."},
    {"step": "That single horizontal coordinate IS simple harmonic motion",
     "detail": "The amplitude is the circle's radius, the angular frequency is the circular speed, and the period is the time for one lap."},
    {"step": "Why this is so useful",
     "detail": "Circular motion is easier to picture and to solve. S.H.M. can always be "
               "replaced by a point on a circle, and any circular motion can be reduced "
               "to one S.H.M. by looking at a single coordinate."},
]

SPRING_POINTS = [
    {"point": "Hooke's law is already the S.H.M. condition",
     "detail": "F = −kx says the restoring force is proportional to displacement and "
               "always points back towards the equilibrium. That is the definition of "
               "simple harmonic motion."},
    {"point": "Divide by the mass and ω² appears",
     "detail": "a = F/m = −(k/m)x, and comparing with a = −ω²x gives ω² = k/m, so "
               "ω = √(k/m)."},
    {"point": "The period follows immediately",
     "detail": "T = 2π/ω = 2π√(m/k). Heavier mass means a slower oscillation; stiffer "
               "spring means a faster one."},
    {"point": "The period does not depend on the amplitude",
     "detail": "Neither m nor k changes with how far you pull it, so T is the same "
               "however hard you start. Push a spring too far and Hooke's law fails, and "
               "then the motion stops being exactly periodic."},
    {"point": "The energy is shared between two stores",
     "detail": "All potential at maximum extension, all kinetic as it passes through the "
               "equilibrium position, and back again. The total ½kA² never changes."},
]

PENDULUM_POINTS = [
    {"point": "The restoring force is NOT proportional to displacement — not exactly",
     "detail": "The restoring force is mg sin θ. For small θ, sin θ ≈ θ in radians, and "
               "the arc displacement is x = Lθ, so the force becomes proportional to x. "
               "That approximation is the whole source of the simple formula."},
    {"point": "The mass cancels",
     "detail": "Both the restoring force and the inertia scale with m, so T does not "
               "depend on the mass of the bob at all — a fact you can test with a heavy "
               "and a light bob on the same string."},
    {"point": "The length is the only geometric variable",
     "detail": "T = 2π√(L/g). Doubling the length makes the period 1.41 times longer, "
               "not twice as long."},
    {"point": "Small angles really are required",
     "detail": "The exact period grows with amplitude: about 0.2 % at 10°, 1.7 % at 30°, "
               "18 % at 90°. A laboratory pendulum is deliberately kept to a few degrees."},
    {"point": "So why do timing experiments work so well?",
     "detail": "Because the error stays well under 1 % if the swing is small and the time "
               "over many oscillations is long, so the random error in the stopwatch is "
               "divided down by the number of swings counted."},
]

SPRING_PENDULUM_COMPARISON = [
    {"question": "Period", "spring": "T = 2π√(m/k)", "pendulum": "T = 2π√(L/g)"},
    {"question": "Depends on the mass of the bob?",
     "spring": "Yes, as √m", "pendulum": "No — m cancels"},
    {"question": "Depends on the amplitude?",
     "spring": "No, within the elastic limit",
     "pendulum": "Only because large angles break the small-angle approximation"},
    {"question": "Valid range",
     "spring": "Up to the elastic limit, then Hooke's law fails",
     "pendulum": "Angles up to about 10°; beyond that the formula is only approximate"},
    {"question": "Where the energy goes",
     "spring": "Between kinetic and elastic potential",
     "pendulum": "Between kinetic and gravitational potential"},
    {"question": "The real trap",
     "spring": "Over-stretching makes the period drift as the spring warms and settles",
     "pendulum": "Amplitude creep makes the period look longer than T = 2π√(L/g)"},
]

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "Reading a pendulum to find g",
     "level": "Foundation", "slos": ["7.4.2", "7.4.3"],
     "question": "A pendulum 1.00 m long completes 20 oscillations in 39.2 s. Calculate the "
                 "acceleration due to gravity at that location.",
     "known": ["L = 1.00 m", "20 oscillations in 39.2 s", "g = 4π²L / T²"],
     "find": "g",
     "equation": r"T = 2\pi\sqrt{\frac{L}{g}} \quad\Rightarrow\quad g = \frac{4\pi^2 L}{T^2}",
     "conversions": ["The time per oscillation, not the total, must be used: T = 39.2/20 = 1.96 s."],
     "substitution": r"g = \frac{4(3.1416)^2(1.00)}{(1.96)^2}",
     "calculation": [
         "Step 1 — period: T = 39.2 s / 20 = 1.96 s. Using 39.2 s as the period is the standard mistake here.",
         "Step 2 — rearrange: g = 4π²L/T².",
         "Step 3 — substitute: g = 4 × 9.8696 × 1.00 / 3.8416 = 39.478 / 3.8416 = 10.28 m s⁻².",
         "Step 4 — compare with the standard 9.81. The measurement gives about 5 % too high, and the "
         "most likely reason is that the swing was larger than 10°, which makes the real period longer "
         "than the small-angle formula predicts and so the computed g come out too large.",
         "Step 5 — that is the experimental lesson: amplitude is the systematic error that timing "
         "experiments must control.",
     ],
     "unit_check": r"g = \frac{[T^{-2}][L]}{[T^2]} = [L T^{-2}] = \mathrm{m\,s^{-2}}",
     "answer": "g ≈ 10.3 m s⁻² by this measurement, against a true 9.81",
     "sig_fig_note": "The time is to three significant figures and the count of oscillations is exact, so the answer is 10.3 m s⁻².",
     "assumptions": ["The swing is small enough for T = 2π√(L/g) to hold.",
                     "The pendulum length is measured to the pivot, not to the centre of the bob."]},
    {"id": "WP2", "title": "A mass on a spring",
     "level": "Developing", "slos": ["7.3.1", "7.3.2", "7.3.3"],
     "question": "A 0.50 kg mass hangs on a spring of force constant 200 N/m and is displaced 0.050 m "
                 "from equilibrium and released. Find the period, the maximum speed and the energy of "
                 "the oscillation.",
     "known": ["m = 0.50 kg", "k = 200 N/m", "A = 0.050 m", "g is not needed — it only moves the equilibrium"],
     "find": "T, v_max and E",
     "equation": r"T = 2\pi\sqrt{\frac{m}{k}}, \qquad v_{\max} = \omega A, \qquad E = \tfrac{1}{2}kA^2",
     "conversions": ["A = 0.050 m = 5.0 cm. No other conversion is needed."],
     "substitution": r"T = 2\pi\sqrt{\frac{0.50}{200}}, \quad \omega = \sqrt{\frac{200}{0.50}}, \quad "
                     r"E = \tfrac{1}{2}(200)(0.050)^2",
     "calculation": [
         "Step 1 — angular frequency: ω = √(k/m) = √(200/0.50) = √400 = 20 rad s⁻¹.",
         "Step 2 — period: T = 2π/ω = 6.283/20 = 0.314 s.",
         "Step 3 — maximum speed: the speed is greatest as the mass passes through equilibrium, where all "
         "the energy is kinetic: v_max = ωA = 20 × 0.050 = 1.0 m s⁻¹.",
         "Step 4 — energy: E = ½kA² = ½ × 200 × 0.0025 = 0.25 J. Check: E = ½m v_max² = ½ × 0.50 × 1 = 0.25 J. ✓",
         "Step 5 — note what does not appear: g is nowhere. Adding gravity simply shifts the equilibrium "
         "position down by mg/k = 0.0245 m; it does not change the period.",
     ],
     "unit_check": r"T = \sqrt{[M]/([M T^{-2}])} = [T]; \ v = [T^{-1}][L] = [L T^{-1}]; \ E = [M L^2 T^{-2}] = \mathrm{J}",
     "answer": "T = 0.314 s, v_max = 1.0 m s⁻¹, E = 0.25 J",
     "sig_fig_note": "m = 0.50 kg and k = 200 N/m are each to two or three figures, so T = 0.31 s.",
     "assumptions": ["The spring obeys Hooke's law over the whole displacement.",
                     "There is no damping, so the amplitude stays at 0.050 m."]},
    {"id": "WP3", "title": "The three expressions at one instant",
     "level": "Developing", "slos": ["7.2.3", "7.2.4", "7.2.5"],
     "question": "An oscillator has amplitude 0.20 m and period 0.50 s, starting from the mean position "
                 "moving in the positive direction. Find x, v and a at t = 0.125 s, and state which of "
                 "the three is at its maximum.",
     "known": ["A = 0.20 m", "T = 0.50 s, so ω = 2π/T = 12.566 rad s⁻¹",
               "At t = 0.125 s the phase is ωt = 12.566 × 0.125 = 1.5708 rad = π/2"],
     "find": "x, v and a at t = 0.125 s",
     "equation": r"x = A\sin\omega t, \quad v = A\omega\cos\omega t, \quad a = -A\omega^2\sin\omega t",
     "conversions": ["Nothing to convert; the phase is what matters here."],
     "substitution": r"x = 0.20\sin\frac{\pi}{2}, \quad v = 0.20(12.566)\cos\frac{\pi}{2}, \quad "
                     r"a = -0.20(12.566)^2\sin\frac{\pi}{2}",
     "calculation": [
         "Step 1 — t = 0.125 s is exactly T/4, so the phase is π/2.",
         "Step 2 — x = A sin(π/2) = 0.20 × 1 = +0.20 m. This is the amplitude, so the oscillator is at the extreme of its travel.",
         "Step 3 — v = Aω cos(π/2) = 2.513 × 0 = 0. At the extreme the body momentarily stops.",
         "Step 4 — a = −Aω² sin(π/2) = −0.20 × 158.0 = −31.6 m s⁻². This is the maximum acceleration, and it points back towards the mean position.",
         "Step 5 — the pattern: at T/4 the displacement is maximum, the velocity is zero and the acceleration is maximum in magnitude. All three are always a quarter cycle apart.",
     ],
     "unit_check": r"a = [L][T^{-2}] = [L T^{-2}] = \mathrm{m\,s^{-2}}",
     "answer": "x = +0.20 m, v = 0, a = −31.6 m s⁻²; the acceleration is at its maximum",
     "sig_fig_note": "A = 0.20 m is to two significant figures, so a = −32 m s⁻².",
     "assumptions": ["The oscillator starts from the mean position with phase constant φ = 0.",
                     "There is no damping."]},
    {"id": "WP4", "title": "How far the small-angle formula can be trusted",
     "level": "Challenge", "slos": ["7.4.1", "7.4.2"],
     "question": "A pendulum has a period T = 2π√(L/g) for small swings. By what percentage does the "
                 "true period exceed this value for swings of 10°, 30° and 60°?",
     "known": ["L = 1.00 m, g = 9.8 m s⁻², so T₀ = 2π√(1/9.8) = 2.007 s",
               "The exact period is larger by the factor 1 + θ²/16 + 11θ⁴/3072 with θ in radians"],
     "find": "the percentage error at each amplitude",
     "equation": r"\frac{T - T_0}{T_0} \times 100\%, \qquad T = T_0\left(1 + \frac{\theta^2}{16} + \frac{11\theta^4}{3072}\right)",
     "conversions": ["Angles must be in radians: 10° = 0.1745 rad, 30° = 0.5236 rad, 60° = 1.0472 rad."],
     "substitution": r"\%\text{ error} = \left(\frac{\theta^2}{16} + \frac{11\theta^4}{3072}\right)\times 100",
     "calculation": [
         "Step 1 — 10°: θ = 0.1745 rad, θ² = 0.03046, θ⁴ = 0.000928. Error = (0.03046/16 + 11×0.000928/3072) × 100 = (0.001904 + 0.00000332) × 100 = 0.19 %.",
         "Step 2 — 30°: θ = 0.5236 rad, θ² = 0.2742, θ⁴ = 0.07517. Error = (0.2742/16 + 11×0.07517/3072) × 100 = (0.017139 + 0.000269) × 100 = 1.74 %.",
         "Step 3 — 60°: θ = 1.0472 rad, θ² = 1.0966, θ⁴ = 1.2026. Error = (1.0966/16 + 11×1.2026/3072) × 100 = (0.068538 + 0.004306) × 100 = 7.28 %.",
         "Step 4 — the pattern: the error grows roughly as the square of the angle. Doubling the angle "
         "quadruples the error to first order.",
         "Step 5 — the practical conclusion: a laboratory pendulum kept below about 10° has a systematic "
         "error under 0.2 %, which is smaller than the random error in most stopwatch timing. Push the "
         "swing to 30° and the systematic error alone exceeds the precision of the experiment.",
     ],
     "unit_check": r"\theta \text{ is dimensionless, so the error is a pure percentage}",
     "answer": "0.19 % at 10°, 1.74 % at 30°, 7.3 % at 60°",
     "sig_fig_note": "The percentage errors are given to two significant figures.",
     "assumptions": ["The correction series is used in the regime where it converges well, which is fine up to about 60°.",
                     "Damping is neglected."]},
]

PRACTICE_QUESTIONS = [
    {"id": "P1", "category": "Periodic motion", "type": "mcq", "slo": "7.1.1",
     "prompt": "Which of these is NOT periodic?",
     "options": ["A tuning fork", "A simple pendulum", "A seismograph trace during an earthquake",
                 "The suspension of a car over a bump"], "answer": 2,
     "hint": "Periodic means it repeats to within a fraction of a percent.",
     "explanation": "Each earthquake tremor has a different amplitude and duration, so the "
                    "pattern never repeats. A tuning fork, a gentle pendulum swing and a car's "
                    "suspension all repeat closely."},
    {"id": "P2", "category": "Periodic motion", "type": "numeric", "slo": "7.1.1",
     "prompt": "A body completes 12 oscillations in 6.0 s. What is the period? Enter the number only, "
               "in seconds.",
     "answer": 0.5, "tolerance": 0.01, "unit": "s",
     "hint": "Period is the time for ONE complete cycle.",
     "explanation": "T = 6.0/12 = 0.50 s. The most common error is to divide the other way round."},
    {"id": "P3", "category": "Periodic motion", "type": "mcq", "slo": "7.1.1",
     "prompt": "Oscillations that repeat exactly are called...",
     "options": ["random", "periodic", "damped", "isotropic"], "answer": 1,
     "hint": "Same word as in 'periodic table'.",
     "explanation": "Periodic oscillations repeat on a fixed pattern. Non-periodic ones — an "
                    "earthquake trace, a tumbling leaf — never repeat exactly."},
    {"id": "P4", "category": "Simple harmonic motion", "type": "mcq", "slo": "7.1.2",
     "prompt": "The defining condition of simple harmonic motion is...",
     "options": ["the force is constant", "the acceleration is proportional to displacement and "
                 "directed towards the mean position", "the speed is constant",
                 "the amplitude decreases steadily"], "answer": 1,
     "hint": "One equation: a = -ω²x.",
     "explanation": "a = −ω²x. The minus sign is what turns the motion round; without it the "
                    "body would accelerate away from equilibrium rather than return."},
    {"id": "P5", "category": "Simple harmonic motion", "type": "numeric", "slo": "7.1.2",
     "prompt": "In S.H.M. with ω = 4.0 rad s⁻¹, what is the acceleration when the displacement is "
               "0.050 m? Enter the number only, in m s⁻².",
     "answer": -0.8, "tolerance": 0.02, "unit": "m s⁻²",
     "hint": "a = -ω²x.",
     "explanation": "a = -(4.0)²(0.050) = -0.80 m s⁻². The negative sign shows the acceleration "
                    "points back towards the mean position."},
    {"id": "P6", "category": "Simple harmonic motion", "type": "mcq", "slo": "7.1.2",
     "prompt": "Which statement about S.H.M. is correct?",
     "options": ["The speed is constant", "The acceleration is constant",
                 "The energy is constant", "The period depends on the amplitude"], "answer": 2,
     "hint": "Energy is exchanged between two stores, but the total does not change.",
     "explanation": "The total energy is constant in ideal S.H.M., alternating between kinetic "
                    "and potential. Speed and acceleration both vary, and the period does not "
                    "depend on amplitude."},

    {"id": "P7", "category": "Terms", "type": "mcq", "slo": "7.2.1",
     "prompt": "The SI unit of angular frequency is...",
     "options": ["Hz", "rad s⁻¹", "s", "m"], "answer": 1,
     "hint": "Frequency is in hertz; angular frequency is different.",
     "explanation": "rad s⁻¹. Note that hertz and rad s⁻¹ have the same dimension [T⁻¹] and the "
                    "same SI dimension, differing only in how they describe the quantity; ω = 2πf."},
    {"id": "P8", "category": "Terms", "type": "numeric", "slo": "7.2.1",
     "prompt": "An oscillator has a period of 0.40 s. Calculate its angular frequency. Enter the number "
               "only, in rad s⁻¹.",
     "answer": 15.707963267948966, "tolerance": 0.05, "unit": "rad s⁻¹",
     "hint": "ω = 2π/T.",
     "explanation": "ω = 2π/0.40 = 15.7 rad s⁻¹, and the frequency is 1/0.40 = 2.5 Hz."},
    {"id": "P9", "category": "Terms", "type": "mcq", "slo": "7.2.1",
     "prompt": "The amplitude of an oscillation is...",
     "options": ["the total distance travelled in one cycle",
                 "the greatest displacement from the mean position",
                 "the time for one cycle", "the distance from the mean position at t = 0"], "answer": 1,
     "hint": "It is always a positive quantity.",
     "explanation": "The greatest displacement from the mean position, always taken as positive. "
                    "The total distance in one cycle would be 4A."},
    {"id": "P10", "category": "Terms", "type": "mcq", "slo": "7.2.1",
     "prompt": "Phase difference between two oscillators is measured in...",
     "options": ["seconds", "hertz", "radians", "metres"], "answer": 2,
     "hint": "The same unit as ωt.",
     "explanation": "Radians. Phase difference is an angle, so it is dimensionless like the "
                    "radian itself."},

    {"id": "P11", "category": "S.H.M. expressions", "type": "numeric", "slo": "7.2.3",
     "prompt": "An oscillator has A = 0.15 m and ω = 8.0 rad s⁻¹, starting from the mean position. "
               "Find its displacement at t = π/16 s. Enter the number only, in metres.",
     "answer": 0.15, "tolerance": 0.005, "unit": "m",
     "hint": "x = A sin ωt, and ωt = 8 × π/16 = π/2.",
     "explanation": "ωt = 8.0 × π/16 = π/2, so x = 0.15 × sin(π/2) = 0.150 m. Whenever the "
                    "phase is a quarter cycle the oscillator is at its extreme, so the "
                    "displacement equals the amplitude."},
    {"id": "P12", "category": "S.H.M. expressions", "type": "numeric", "slo": "7.2.3",
     "prompt": "An oscillator has A = 0.10 m and ω = 5.0 rad s⁻¹, starting from the mean position. "
               "Find its velocity at t = 0 s. Enter the number only, in m s⁻¹.",
     "answer": 0.5, "tolerance": 0.01, "unit": "m s⁻¹",
     "hint": "v = Aω cos ωt, and cos 0 = 1.",
     "explanation": "v = 0.10 × 5.0 × 1 = 0.50 m s⁻¹. At t = 0 the body passes through the mean "
                    "position at its greatest speed, so v = Aω = v_max."},
    {"id": "P13", "category": "S.H.M. graphs", "type": "mcq", "slo": "7.2.5",
     "prompt": "On displacement–time and velocity–time graphs drawn on the same axis, the velocity "
               "graph...",
     "options": ["lags the displacement by T/4", "leads the displacement by T/4",
                 "is in phase with the displacement", "leads by T/2"], "answer": 1,
     "hint": "Consider where each is at its extreme.",
     "explanation": "Velocity leads displacement by T/4. When displacement is at its extreme the "
                    "velocity is zero, and the velocity reaches its maximum a quarter cycle "
                    "before displacement does."},
    {"id": "P14", "category": "S.H.M. graphs", "type": "mcq", "slo": "7.2.5",
     "prompt": "On an x–t graph and an a–t graph drawn on the same axis, the two curves are...",
     "options": ["in phase", "a quarter cycle apart", "half a cycle apart", "inverted versions of each other"],
     "answer": 2,
     "hint": "Add up the offsets: T/4 from x to v, then another T/4 from v to a.",
     "explanation": "Half a cycle apart, which for a sine means a is always the negative of ω²x — "
                    "exactly the S.H.M. condition. That is why the acceleration is opposite in "
                    "sign to the displacement at every instant."},
    {"id": "P15", "category": "S.H.M. graphs", "type": "numeric", "slo": "7.2.5",
     "prompt": "An oscillator has period 0.80 s. How far ahead of the displacement is the velocity, in "
               "seconds? Enter the number only.",
     "answer": 0.2, "tolerance": 0.005, "unit": "s",
     "hint": "A quarter of the period.",
     "explanation": "T/4 = 0.80/4 = 0.20 s. The acceleration is a further T/4 behind the velocity."},

    {"id": "P16", "category": "Mass-spring", "type": "numeric", "slo": "7.3.2",
     "prompt": "Find the period of a 0.20 kg mass on a spring of force constant 50 N/m. Enter the "
               "number only, in seconds.",
     "answer": 0.397383530631844, "tolerance": 0.005, "unit": "s",
     "hint": "T = 2π√(m/k).",
     "explanation": "T = 2π√(0.20/50) = 2π√0.004 = 2π(0.06325) = 0.397 s."},
    {"id": "P17", "category": "Mass-spring", "type": "mcq", "slo": "7.3.1",
     "prompt": "A mass on a spring performs S.H.M. because Hooke's law gives...",
     "options": ["a constant restoring force", "a force proportional to displacement and towards "
                 "equilibrium", "zero net force", "a force proportional to speed"], "answer": 1,
     "hint": "That is exactly the S.H.M. condition.",
     "explanation": "F = −kx. Proportional to displacement, always towards the equilibrium "
                    "position, with a constant ratio — which is the definition of simple "
                    "harmonic motion."},
    {"id": "P18", "category": "Mass-spring", "type": "numeric", "slo": "7.3.2",
     "prompt": "The mass on a spring in the last question is quadrupled. By what factor does the period "
               "change? Enter the number only.",
     "answer": 2.0, "tolerance": 0.01, "unit": "times",
     "hint": "T ∝ √m, not ∝ m.",
     "explanation": "Doubled, because T = 2π√(m/k) and √4 = 2. A mass four times heavier oscillates "
                    "only twice as slowly."},
    {"id": "P19", "category": "Mass-spring", "type": "mcq", "slo": "7.3.3",
     "prompt": "Which quantity does NOT appear in the period of a mass-spring system?",
     "options": ["The mass", "The force constant", "The amplitude", "None — all three appear"], "answer": 2,
     "hint": "Neither m nor k changes with how far you stretch the spring.",
     "explanation": "The amplitude. T = 2π√(m/k) contains only m and k, so pulling the spring "
                    "harder does not change the period at all — provided the spring stays "
                    "within its elastic limit."},

    {"id": "P20", "category": "Pendulum", "type": "numeric", "slo": "7.4.2",
     "prompt": "Find the period of a simple pendulum 0.81 m long. Take g = 9.8 m s⁻². Enter the number "
               "only, in seconds.",
     "answer": 1.8063809308390442, "tolerance": 0.01, "unit": "s",
     "hint": "T = 2π√(L/g).",
     "explanation": "T = 2π√(0.81/9.8) = 2π√0.08265 = 2π(0.28750) = 1.808 s. This is the classic "
                    "laboratory result: a 0.81 m pendulum ticks at about 2 Hz."},
    {"id": "P21", "category": "Pendulum", "type": "mcq", "slo": "7.4.1",
     "prompt": "The period of a simple pendulum does NOT depend on...",
     "options": ["its length", "the acceleration due to gravity", "the mass of the bob",
                 "the amplitude, for small swings"], "answer": 2,
     "hint": "Both the restoring force and the inertia scale with mass.",
     "explanation": "The mass cancels out of T = 2π√(L/g) entirely. That is easily verified "
                    "experimentally with a light and a heavy bob on the same string."},
    {"id": "P22", "category": "Pendulum", "type": "mcq", "slo": "7.4.2",
     "prompt": "T = 2π√(L/g) is an accurate approximation only when...",
     "options": ["the bob is heavy", "the length is short", "the swing angle is small",
                 "the string is inextensible"], "answer": 2,
     "hint": "It comes from sin θ ≈ θ in radians.",
     "explanation": "For small angles. The error grows as θ²: about 0.2 % at 10°, 1.7 % at 30° and "
                    "18 % at 90°."},
    {"id": "P23", "category": "Pendulum", "type": "numeric", "slo": "7.4.3",
     "prompt": "A pendulum is 2.0 m long and makes 50 oscillations in 63.4 s. Calculate its period. "
               "Enter the number only, in seconds.",
     "answer": 1.268, "tolerance": 0.01, "unit": "s",
     "hint": "Divide the total time by the number of oscillations.",
     "explanation": "T = 63.4/50 = 1.268 s. Compare with the formula: 2π√(2.0/9.8) = 1.268 s, "
                    "which is why timing many oscillations is how g is measured accurately."},
    {"id": "P24", "category": "Pendulum", "type": "numeric", "slo": "7.4.2",
     "prompt": "The length of a pendulum is quadrupled. By what factor does its period change? "
               "Enter the number only.",
     "answer": 2.0, "tolerance": 0.01, "unit": "times",
     "hint": "T ∝ √L.",
     "explanation": "Doubled, because T = 2π√(L/g). The period grows with the square root of the "
                    "length, not in proportion to it."},

    {"id": "P25", "category": "SHM and circular motion", "type": "mcq", "slo": "7.2.2",
     "prompt": "Which statement connects S.H.M. with uniform circular motion correctly?",
     "options": ["The projection of a point moving in a circle performs S.H.M.",
                 "Any object moving in a circle performs S.H.M.",
                 "S.H.M. is caused by circular motion",
                 "They describe the same motion at all times"],
     "answer": 0,
     "hint": "Think of the shadow of a point on the rim of a wheel.",
     "explanation": "It is the **projection** \u2014 the shadow \u2014 of a point moving round "
                    "a circle that performs S.H.M., not the circular motion itself. The shadow "
                    "runs at constant angular speed, yet its restoring force is still linear in "
                    "displacement, so its acceleration stays proportional to -x."},
    {"id": "P26", "category": "SHM and circular motion", "type": "numeric", "slo": "7.2.2",
     "prompt": "A point moves round a circle of radius 0.20 m at a steady 3.0 rad s\u207b\u00b9. "
               "Find the period of the S.H.M. made by its shadow. Enter the number only, in "
               "seconds.",
     "answer": 2.09, "tolerance": 0.03, "unit": "s",
     "hint": "The shadow completes one cycle for each turn, so T = 2\u03c0/\u03c9.",
     "explanation": "T = 2\u03c0/3.0 = 2.09 s. The radius does not affect the period, which is "
                    "why the shadow obeys T = 2\u03c0\u221a(L/g) exactly for this arrangement."},
    {"id": "P27", "category": "Phase", "type": "numeric", "slo": "7.2.4",
     "prompt": "A particle performs S.H.M. of amplitude 5.0 cm with angular frequency "
               "4.00 rad s\u207b\u00b9 and phase \u03c6 = \u03c0/2 at t = 0. Find its "
               "displacement at t = 0. Enter the number in cm; use -5 for a negative answer.",
     "answer": 5.0, "tolerance": 0.3, "unit": "cm",
     "hint": "x = A sin(\u03c9t + \u03c6). At t = 0 this becomes A sin \u03c6.",
     "explanation": "x = 5.0 \u00d7 sin(\u03c0/2) = +5.0 cm, the maximum displacement. A phase of "
                    "\u03c0/2 puts the particle at the extreme of its motion, not at the mean "
                    "position \u2014 which is what \u03c6 = 0 would give."},
    {"id": "P28", "category": "Phase", "type": "numeric", "slo": "7.2.4",
     "prompt": "The same particle is released from rest at the positive extreme, so "
               "x = 5.0 cos(4.00t) cm. Find its velocity at t = 0.150 s. Enter the number in "
               "cm s\u207b\u00b9; use a negative number if it is moving back towards the "
               "equilibrium position.",
     "answer": -15.6, "tolerance": 0.8, "unit": "cm s\u207b\u00b9",
     "hint": "v = dx/dt = -A\u03c9 sin(\u03c9t) for the cosine form.",
     "explanation": "v = -(5.0 \u00d7 4.00) sin(4.00 \u00d7 0.150) = -20.0 \u00d7 0.613 = "
                    "-15.6 cm s\u207b\u00b9. The negative sign shows it has passed the "
                    "equilibrium position and is heading back to the starting extreme."},

    {"id": "P38", "category": "Energy in S.H.M.", "type": "mcq", "slo": "7.5.1",
     "prompt": "During simple harmonic motion, the total mechanical energy...",
     "options": ["increases during the first half cycle then decreases",
                 "is constant, provided damping is negligible",
                 "is zero at the mean position", "is constant only at the extremes"],
     "answer": 1,
     "hint": "Kinetic and potential trade places; their sum is what matters.",
     "explanation": "It is constant when damping is negligible. At the extremes all the energy "
                    "is potential and none is kinetic; at the mean position the reverse. Their "
                    "sum never changes, which is the whole content of 7.5.1."},
    {"id": "P39", "category": "Energy in S.H.M.", "type": "numeric", "slo": "7.5.2",
     "prompt": "A mass of 0.50 kg on a spring of force constant 200 N m^-1 oscillates with "
               "amplitude 0.040 m. Find the total energy. Enter the number only.",
     "answer": 0.16, "tolerance": 0.01, "unit": "J",
     "hint": "E = (1/2) k A^2 at the extreme position, where all the energy is potential.",
     "explanation": "E = 0.5 x 200 x 0.040^2 = 0.16 J. The mass does not appear in this "
                    "expression, which is why a stiffer spring at the same amplitude stores "
                    "more energy regardless of what hangs on it."},
    {"id": "P40", "category": "Energy in S.H.M.", "type": "mcq", "slo": "7.5.3",
     "prompt": "A particle passes through the mean position of its S.H.M. Its...",
     "options": ["kinetic energy is zero and potential is maximum",
                 "kinetic energy is maximum and potential is zero",
                 "both are maximum", "both are zero"],
     "answer": 1,
     "hint": "The restoring force is greatest there, so think about the speed.",
     "explanation": "Kinetic is maximum and potential is zero. The speed is greatest because "
                    "the restoring force is greatest, and every joule of the total has become "
                    "kinetic."},
    {"id": "P41", "category": "Forced oscillations", "type": "mcq", "slo": "7.6.1",
     "prompt": "A free oscillation differs from a forced oscillation in that...",
     "options": ["a free oscillation needs no driving force",
                 "a free oscillation always decays",
                 "a forced oscillation always grows",
                 "free oscillations only occur in gases"],
     "answer": 0,
     "hint": "Think about what supplies the energy in each case.",
     "explanation": "A free oscillation runs on its own stored energy with no external driver. "
                    "A forced one is driven at some frequency, and the motion that results is "
                    "a mixture of the natural frequency and the driving frequency."},
    {"id": "P42", "category": "Resonance", "type": "mcq", "slo": "7.7.1",
     "prompt": "Resonance in a driven system occurs when...",
     "options": ["the driving frequency is much less than the natural frequency",
                 "the driving frequency equals the natural frequency",
                 "the damping is zero", "the amplitude is at its mean value"],
     "answer": 1,
     "hint": "The driver and the system have to agree on the rhythm.",
     "explanation": "When the driving frequency equals the natural frequency, each push lands "
                    "just as the system returns, so energy is added faster than damping removes "
                    "it and the amplitude grows very large."},
    {"id": "P43", "category": "Resonance", "type": "mcq", "slo": "7.7.2",
     "prompt": "A soldier marching in step across a bridge is an application of...",
     "options": ["damping", "resonance", "free oscillation", "beats"],
     "answer": 1,
     "hint": "The point is that their steps are synchronised.",
     "explanation": "Resonance. Marching in step forces the bridge to oscillate at its natural "
                    "frequency, and a large enough amplitude can destroy it. That is why the "
                    "rule is to break step."},
    {"id": "P44", "category": "Damping", "type": "mcq", "slo": "7.8.1",
     "prompt": "A damped oscillator...",
     "options": ["gains energy steadily from the surroundings",
                 "loses energy steadily to friction and the surroundings",
                 "keeps a constant amplitude forever",
                 "stops oscillating immediately"],
     "answer": 1,
     "hint": "Real systems always lose something.",
     "explanation": "It loses energy steadily, through friction, air resistance and sound "
                    "radiation, so its amplitude falls exponentially with time while the "
                    "frequency stays almost unchanged."},
    {"id": "P45", "category": "Damping", "type": "mcq", "slo": "7.8.2",
     "prompt": "Which of these is an application of damping rather than resonance?",
     "options": ["a car shock absorber", "a violin string driven at its natural frequency",
                 "a glass shattered by a sustained loud note", "a singer breaking a glass with one loud note"],
     "answer": 0,
     "hint": "One of these is deliberately there to remove energy.",
     "explanation": "A shock absorber is a damper: its whole job is to dissipate the energy of "
                    "the bounce so the car settles quickly. The other three all depend on "
                    "energy being **added** at resonance."},
    {"id": "P46", "category": "Damping", "type": "mcq", "slo": "7.8.3",
     "prompt": "In heavy damping, the displacement-time graph shows...",
     "options": ["many oscillations before returning to equilibrium",
                 "rapid oscillations that die away slowly",
                 "a quick return to equilibrium with little or no overshoot",
                 "continuous oscillation at constant amplitude"],
     "answer": 2,
     "hint": "Compare with light damping, which oscillates many times.",
     "explanation": "Heavy damping returns the system to equilibrium quickly, usually without "
                    "overshooting at all. Light damping oscillates many times before settling; "
                    "critical damping is the fastest return without overshoot."},
]

REFERENCES = [
    {"short": "OpenStax College Physics 2e",
     "title": "Chapter 16: Periodic Motion",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/college-physics-2e",
     "used_for": "Simple harmonic motion, the mass-spring oscillator and the simple pendulum."},
    {"short": "MIT OpenCourseWare",
     "title": "8.02 Physics II: Electricity and Magnetism, oscillations",
     "org": "Massachusetts Institute of Technology",
     "url": "https://ocw.mit.edu/courses/8-02t-electricity-and-magnetism-spring-2009/",
     "used_for": "The derivation of both period formulas and the energy argument."},
    {"short": "Khan Academy",
     "title": "Simple harmonic motion: the master equation",
     "org": "Khan Academy",
     "url": "https://www.khanacademy.org/physics/oscillations-and-waves/simple-harmonic-motion",
     "used_for": "How the three expressions come from one another and how to read the graphs."},
    {"short": "APS Physics",
     "title": "Focus: the pendulum and the measurement of g",
     "org": "American Physical Society",
     "url": "https://physics.aps.org/",
     "used_for": "Why small amplitudes and many counted oscillations matter experimentally."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 7",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 7.1.1 to 7.4.3."},
]
# --------------------------------------------------------------------------
# 7.5 - 7.8  Energy, forcing, resonance and damping
# --------------------------------------------------------------------------

ENERGY_SPLIT_NOTES = [
    {"position": "at the extreme position x = A",
     "kinetic": "0", "potential": "(1/2) k A^2",
     "note": "The turning point. All the energy is potential and the speed is zero, which is "
             "why the acceleration is greatest here."},
    {"position": "at the mean position x = 0",
     "kinetic": "(1/2) k A^2", "potential": "0",
     "note": "Every joule is kinetic. The speed and therefore the kinetic energy are at their "
             "greatest, and the acceleration is zero."},
    {"position": "half way, x = A/2",
     "kinetic": "(3/8) k A^2", "potential": "(1/8) k A^2",
     "note": "The ratio is fixed at every point of the motion: K : U = A^2 - x^2 : x^2. "
             "Energy moves smoothly from one form to the other rather than jumping."},
    {"position": "the turning point, going back",
     "kinetic": "0", "potential": "(1/2) k A^2",
     "note": "Exactly as at the start. That the motion repeats is the statement that energy is "
             "conserved; nothing is lost on the way round."},
]

RESONANCE_NOTES = [
    {"title": "The beat of the driving force",
     "detail": "When the driving frequency passes through the natural frequency the system "
               "absorbs far more energy per cycle than it loses to damping, so the amplitude "
               "climbs. The resonance curve is peaked, not a step."},
    {"title": "Quality factor",
     "detail": "Q = amplitude at resonance divided by the half-power bandwidth. A high Q means "
               "a sharp, selective resonance; a heavily damped system has a low Q and "
               "responds to a wide range of frequencies."},
    {"title": "Phase at resonance",
     "detail": "At resonance the displacement lags the driving force by a quarter of a cycle, "
               "and the velocity is in step with the force \u2014 which is why energy is being "
               "transferred most efficiently at exactly that point."},
    {"title": "Resonance is not a mystery",
     "detail": "Push a swing at the right moment on every return and it builds. Drive a car "
               "wheel at the right rate and the axle oscillates. The mathematics is identical."},
]

RESONANCE_CASES = [
    {"case": "A glass shattered by one loud sustained note",
     "effect": "The note's frequency matched a natural frequency of the glass, so the "
               "amplitude built until the glass broke.", "kind": "hazard"},
    {"case": "Soldiers marching in step across a bridge",
     "effect": "Identical steps drive the bridge at its natural frequency. Breaking step "
               "randomises the forcing and stops the build-up.", "kind": "hazard"},
    {"case": "A cello string pressed against the fingerboard",
     "effect": "Shortening the string raises its natural frequency to match the bow, so the "
               "note becomes much louder.", "kind": "application"},
    {"case": "A radio tuned to a station",
     "effect": "The aerial is driven at many frequencies; only the one matching the tuned "
               "circuit's natural frequency is amplified.", "kind": "application"},
    {"case": "A bridge or building in a strong wind",
     "effect": "Periodic vortex shedding can drive the structure at its natural frequency. "
               "Tall flexible buildings are often tuned to avoid this.", "kind": "hazard"},
    {"case": "A singer breaking a champagne glass",
     "effect": "The singer matches the glass's natural frequency. Much of the popular account "
               "is exaggerated, but the principle is sound.", "kind": "application"},
]

DAMPING_NOTES = [
    {"term": "Light damping",
     "meaning": "The system oscillates many times, losing amplitude slowly and exponentially. "
                "Common when damping is small, for example a swinging pendulum in air."},
    {"term": "Critical damping",
     "meaning": "The system returns to equilibrium as fast as possible **without "
                "overshooting**. This is what a well-designed car suspension aims for."},
    {"term": "Heavy damping",
     "meaning": "The system does not oscillate at all; it creeps back to equilibrium. A "
                "closed door with a heavy damper behaves this way."},
    {"term": "What causes damping",
     "meaning": "Friction between the moving parts, air resistance, and energy carried away "
                "as sound. All three remove energy from the motion without removing it from "
                "the universe."},
    {"term": "Frequency is barely affected",
     "meaning": "Damping mainly reduces amplitude. The frequency of a damped oscillator is "
                "very slightly below the natural frequency, and the difference becomes "
                "significant only for heavy damping."},
]

DAMPING_USES = [
    {"application": "Car shock absorber",
     "mechanism": "Oil forced through a narrow valve dissipates the energy of the bounce.",
     "effect": "The car settles in one or two oscillations instead of bouncing."},
    {"application": "Door closer",
     "mechanism": "A piston and cylinder with an adjustable valve.",
     "effect": "The door closes without slamming, and without the handle being damaged."},
    {"application": "Bicycle and motorcycle suspension",
     "mechanism": "Elastomer or oil dampers in the fork.",
     "effect": "Controls rebound so the wheel keeps contact with uneven ground."},
    {"application": "Compass in a bowl of water",
     "mechanism": "The water applies a viscous drag to the needle.",
     "effect": "The needle settles quickly instead of oscillating about north forever."},
    {"application": "Clouds and the atmosphere",
     "mechanism": "Air resistance and turbulent drag on air parcels.",
     "effect": "Buoyant oscillations are damped out, which helps the atmosphere settle."},
]
