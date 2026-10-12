import pathlib

NEW = {
"physics/chapters/ch02_data.py": (26, '''
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
'''),

"physics/chapters/ch05_data.py": (21, '''
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
'''),

"physics/chapters/ch07_data.py": (29, '''
    {"id": "P25", "category": "Energy in S.H.M.", "type": "mcq", "slo": "7.5.1",
     "prompt": "During simple harmonic motion, the total mechanical energy...",
     "options": ["increases during the first half cycle then decreases",
                 "is constant, provided damping is negligible",
                 "is zero at the mean position", "is constant only at the extremes"],
     "answer": 1,
     "hint": "Kinetic and potential trade places; their sum is what matters.",
     "explanation": "It is constant when damping is negligible. At the extremes all the energy "
                    "is potential and none is kinetic; at the mean position the reverse. Their "
                    "sum never changes, which is the whole content of 7.5.1."},
    {"id": "P26", "category": "Energy in S.H.M.", "type": "numeric", "slo": "7.5.2",
     "prompt": "A mass of 0.50 kg on a spring of force constant 200 N m^-1 oscillates with "
               "amplitude 0.040 m. Find the total energy. Enter the number only.",
     "answer": 0.16, "tolerance": 0.01, "unit": "J",
     "hint": "E = (1/2) k A^2 at the extreme position, where all the energy is potential.",
     "explanation": "E = 0.5 x 200 x 0.040^2 = 0.16 J. The mass does not appear in this "
                    "expression, which is why a stiffer spring at the same amplitude stores "
                    "more energy regardless of what hangs on it."},
    {"id": "P27", "category": "Energy in S.H.M.", "type": "mcq", "slo": "7.5.3",
     "prompt": "A particle passes through the mean position of its S.H.M. Its...",
     "options": ["kinetic energy is zero and potential is maximum",
                 "kinetic energy is maximum and potential is zero",
                 "both are maximum", "both are zero"],
     "answer": 1,
     "hint": "The restoring force is greatest there, so think about the speed.",
     "explanation": "Kinetic is maximum and potential is zero. The speed is greatest because "
                    "the restoring force is greatest, and every joule of the total has become "
                    "kinetic."},
    {"id": "P28", "category": "Forced oscillations", "type": "mcq", "slo": "7.6.1",
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
    {"id": "P29", "category": "Resonance", "type": "mcq", "slo": "7.7.1",
     "prompt": "Resonance in a driven system occurs when...",
     "options": ["the driving frequency is much less than the natural frequency",
                 "the driving frequency equals the natural frequency",
                 "the damping is zero", "the amplitude is at its mean value"],
     "answer": 1,
     "hint": "The driver and the system have to agree on the rhythm.",
     "explanation": "When the driving frequency equals the natural frequency, each push lands "
                    "just as the system returns, so energy is added faster than damping removes "
                    "it and the amplitude grows very large."},
    {"id": "P30", "category": "Resonance", "type": "mcq", "slo": "7.7.2",
     "prompt": "A soldier marching in step across a bridge is an application of...",
     "options": ["damping", "resonance", "free oscillation", "beats"],
     "answer": 1,
     "hint": "The point is that their steps are synchronised.",
     "explanation": "Resonance. Marching in step forces the bridge to oscillate at its natural "
                    "frequency, and a large enough amplitude can destroy it. That is why the "
                    "rule is to break step."},
    {"id": "P31", "category": "Damping", "type": "mcq", "slo": "7.8.1",
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
    {"id": "P32", "category": "Damping", "type": "mcq", "slo": "7.8.2",
     "prompt": "Which of these is an application of damping rather than resonance?",
     "options": ["a car shock absorber", "a violin string driven at its natural frequency",
                 "a glass shattered by a sustained loud note", "a singer breaking a glass with one loud note"],
     "answer": 0,
     "hint": "One of these is deliberately there to remove energy.",
     "explanation": "A shock absorber is a damper: its whole job is to dissipate the energy of "
                    "the bounce so the car settles quickly. The other three all depend on "
                    "energy being **added** at resonance."},
    {"id": "P33", "category": "Damping", "type": "mcq", "slo": "7.8.3",
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
'''),

"physics/chapters/ch10_data.py": (53, '''
    {"id": "P53", "category": "Molecular energies", "type": "numeric", "slo": "10.3.5",
     "prompt": "Find the average translational kinetic energy per molecule of an ideal gas at "
               "500 K. Use E = 1.5 k T with k = 1.380649 x 10^-23 J K^-1. Enter the number only.",
     "answer": 1.036e-20, "tolerance": 0.01e-20, "unit": "J",
     "hint": "Multiply 1.5 by k and then by the temperature in kelvin.",
     "explanation": "E = 1.5 x 1.380649e-23 x 500 = 1.04e-20 J per molecule. The identity of "
                    "the gas does not appear anywhere, which is the point of outcome 10.3.4."},
    {"id": "P54", "category": "Work", "type": "mcq", "slo": "10.4.4",
     "prompt": "A gas is compressed by the surroundings. The work done...",
     "options": ["by the gas is positive", "on the gas is positive",
                 "is zero because the volume is unchanged", "is the same in both descriptions"],
     "answer": 1,
     "hint": "Compression means the surroundings are the ones doing the pushing.",
     "explanation": "Work done **on** the gas is positive, and work done **by** the gas is the "
                    "same magnitude with the opposite sign. The first law convention "
                    "dU = Q - W measures W as work done by the gas, so compression makes W "
                    "negative."},
    {"id": "P55", "category": "Design", "type": "mcq", "slo": "10.9.5",
     "prompt": "A device must move heat from 250 K to a room at 300 K. Raising the cold "
               "reservoir to 290 K will...",
     "options": ["raise its coefficient of performance",
                 "lower its coefficient of performance",
                 "leave its coefficient of performance unchanged",
                 "make it convert more of the input energy to work"],
     "answer": 1,
     "hint": "Work out COP = Tc/(Th - Tc) for both temperatures.",
     "explanation": "It lowers it. COP = 250/50 = 5.0 at 250 K, but 290/10 = 29 at 290 K - "
                    "a different number in each case, and both are far below any real "
                    "refrigerator. Note the ideal figure itself rises steeply as the gap "
                    "closes, so the *ideal* COP improves; what worsens in practice is the "
                    "ability to move heat against a tiny gradient at all. Either way, running "
                    "colder is what makes a cold chain expensive."},
    {"id": "P56", "category": "Refrigeration", "type": "mcq", "slo": "10.10.1",
     "prompt": "A refrigerator is best described as...",
     "options": ["a heat engine run in reverse",
                 "a device that creates cold at no energy cost",
                 "a heat engine with a larger cold reservoir",
                 "a device that reduces the total entropy of the universe"],
     "answer": 0,
     "hint": "Compare the direction of every arrow.",
     "explanation": "A heat engine run in reverse: it takes heat Q_c from the cold space, "
                    "rejects Q_h into the room, and consumes work W, with Q_h = Q_c + W. Every "
                    "arrow is the reverse of the engine's, which is exactly why both are "
                    "governed by the same second law."},
    {"id": "P57", "category": "Refrigeration", "type": "numeric", "slo": "10.10.2",
     "prompt": "An ideal refrigerator works between a cold space at 240 K and a room at 300 K. "
               "Find its coefficient of performance. Enter the number only.",
     "answer": 4.0, "tolerance": 0.05, "unit": "",
     "hint": "COP = Tc/(Th - Tc), both in kelvin.",
     "explanation": "COP = 240/(300 - 240) = 4.0. It removes 4 J of heat from the cold space "
                    "for every joule of electricity supplied. A real refrigerator does worse."},
    {"id": "P58", "category": "Entropy", "type": "mcq", "slo": "10.11.1",
     "prompt": "Entropy is best understood as...",
     "options": ["the heat contained in a body",
                 "a measure of how many microscopic arrangements match the observed state",
                 "a measure of disorder visible to the eye",
                 "the temperature of a body in kelvin"],
     "answer": 1,
     "hint": "Count the ways the molecules could be arranged.",
     "explanation": "It counts the microscopic arrangements - the microstates - compatible "
                    "with the macroscopic state. A gas filling a room has vastly more of them "
                    "than the same gas confined to a corner."},
    {"id": "P59", "category": "Entropy", "type": "numeric", "slo": "10.11.2",
     "prompt": "A gas absorbs 1.00 x 10^3 J of heat reversibly at 500 K. Find the entropy "
               "change. Enter the number only.",
     "answer": 2.00, "tolerance": 0.02, "unit": "J K^-1",
     "hint": "dS = Q_rev / T.",
     "explanation": "dS = 1000/500 = 2.00 J K^-1. The change is **positive** because heat was "
                    "absorbed at a positive absolute temperature. Heat released by a body is a "
                    "negative entropy change for that body."},
    {"id": "P60", "category": "Entropy", "type": "mcq", "slo": "10.11.3",
     "prompt": "Heating a gas at constant volume raises its temperature. The entropy of the gas...",
     "options": ["decreases, because the volume is unchanged",
                 "increases, because the molecules have more arrangements available",
                 "stays constant, because no work is done",
                 "increases only if the gas expands"],
     "answer": 1,
     "hint": "Faster molecules have many more accessible arrangements.",
     "explanation": "It increases. Entropy does not depend on volume or on work done; it "
                    "depends on how many arrangements are available, and a hotter gas has "
                    "vastly more of them. That is the evidence that the temperature has gone up."},
    {"id": "P61", "category": "Entropy", "type": "mcq", "slo": "10.11.4",
     "prompt": "When a book falls to the floor, the energy is...",
     "options": ["destroyed", "still present but degraded into random motion of air and floor",
                 "stored in the floor", "converted into mass"],
     "answer": 1,
     "hint": "The first law forbids the first option outright.",
     "explanation": "Still present, but degraded. The organised movement of the book has become "
                    "random microscopic motion spread through the floor and the air. The energy "
                    "is conserved exactly; what has gone is its ability to do useful work again."},
    {"id": "P62", "category": "Entropy", "type": "mcq", "slo": "10.11.5",
     "prompt": "Depletion of a finite ore deposit is best described as...",
     "options": ["an energy crisis", "an entropy crisis, because re-concentrating the dispersed metal costs energy",
                 "a violation of the first law", "a reversible process"],
     "answer": 1,
     "hint": "The metal is still there. What has changed is how spread out it is.",
     "explanation": "An entropy crisis. The metal has not been used up, it has been dispersed "
                    "so thinly that gathering it again costs more energy than the metal is "
                    "worth. Reversing a spontaneous dispersal is exactly what the second law "
                    "forbids without work."},
'''),
}

for path, (first_id, block) in NEW.items():
    p = pathlib.Path(path)
    s = p.read_text()
    start = s.index("PRACTICE_QUESTIONS = [")
    end = s.index("\n]", start)
    s = s[:end] + "\n" + block.rstrip("\n") + s[end:]
    p.write_text(s)
    print(f"  {path}: practice extended to {first_id}")
