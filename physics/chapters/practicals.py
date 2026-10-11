"""The topic-wise practical activities of the AKU-EB Grade XI syllabus.

The board lists twelve experiments with their apparatus. They are examinable
content, so they belong in the book rather than in a separate lab manual. Each
one carries what it measures, how to do it, the formula that turns the
measurement into an answer, and the columns a data table needs.

Nothing here simulates a reading. The tables are for real measurements; the
worked analysis underneath is there to show what to do with what you get.
"""

from __future__ import annotations

__all__ = ["PRACTICALS", "for_chapter", "for_topic"]

#: topic number -> experiment number, taken from the syllabus table.
PRACTICALS = [
    {"no": 1, "topic": 1, "title": "Determine the capacity and thickness of a test tube by "
                                    "using Vernier callipers.",
     "apparatus": ["Vernier callipers", "test tube"],
     "measures": "Two lengths: the outside diameter and the depth of the tube.",
     "how": ["Zero the callipers and check they slide smoothly before starting.",
             "Measure the outside diameter at three positions along the tube and average.",
             "Measure the internal depth from the rim to the bottom of the curved part.",
             "Repeat each reading. Vernier callipers have no zero error once checked, so "
             "any disagreement is your own."],
     "formula": "capacity = pi r^2 h, with r the internal radius",
     "columns": ["reading 1", "reading 2", "reading 3", "mean"],
     "theory": ["The vernier scale carries ten divisions over nine of the main scale, so "
                "one main division is split into ten parts. That gives a least count of "
                "0.01 cm rather than 0.1 cm.",
                "Report the mean to one decimal place, because the instrument itself is only "
                "good to about 0.05 cm.",
                "A test tube is not a cylinder: the curved bottom has to be allowed for, "
                "which is why the depth is measured to the start of the curve."]},

    {"no": 2, "topic": 1, "title": "Measure the diameter of ball bearings of different sizes "
                                    "using a screw gauge and estimate their volumes.",
     "apparatus": ["screw gauges", "steel ball bearings of several sizes"],
     "measures": "The diameter of each bearing, to 0.01 mm.",
     "how": ["Use the flat anvil against the ball for a diameter, or between the anvil and "
             "the spindle if the ball is small enough to sit in the recess.",
             "Close the spindle gently until it just touches. Do not force it: the spindle "
             "can be bent, and a bent spindle reads low for the rest of the session.",
             "Take at least three readings at different orientations of the same ball.",
             "Do the same for a second and third bearing of a different size."],
     "formula": "volume = (4/3) pi r^3",
     "columns": ["reading 1", "reading 2", "reading 3", "mean diameter", "volume"],
     "theory": ["A screw gauge has a pitch of 0.5 mm with fifty divisions, so one division "
                "is 0.01 mm. That is a hundred times finer than the callipers.",
                "Zero the gauge with the anvil and spindle in contact before starting.",
                "The volume of a sphere goes as the cube of the radius, so a bearing twice "
                "the diameter has eight times the volume. That is why accurate diameters "
                "matter so much here."]},

    {"no": 3, "topic": 1, "title": "Determine the radius of curvature of a spherical surface "
                                    "by using a spherometer.",
     "apparatus": ["spherometer", "convex or concave lens or mirror"],
     "measures": "The depth of a shallow spherical cap.",
     "how": ["Place the spherometer on a flat glass surface and find the zero reading with "
             "all three legs touching.",
             "Stand it on the spherical surface you are measuring.",
             "Read the dial gauge for the sagitta h, and note the distance L between the "
             "three legs (the chord of the circle they stand on)."],
     "formula": "R = (L^2 + 4h^2) / (8h)",
     "columns": ["zero reading", "reading on the surface", "sagitta h", "L", "radius R"],
     "theory": ["Three legs on a sphere mark out a circle. The centre of that circle is h "
                "below the top of the sphere, and the geometry of the cap gives "
                "R = (L^2 + 4h^2)/(8h).",
                "The formula was derived by Bishop in 1874 from the Indian astronomical "
                "system of spherical mensuration, centuries before the instrument existed.",
                "A large radius means a shallow sagitta, so h is small and the relative "
                "error in it is large. Measure h as carefully as you can."]},

    {"no": 4, "topic": 2, "title": "Determine the weight of a body by vector addition of "
                                    "forces.",
     "apparatus": ["parallelogram method strip"],
     "measures": "Two forces and their resultant, geometrically.",
     "how": ["Fix one end of the strip and mark the direction of the first force to scale.",
             "From that point mark the second force to scale.",
             "Complete the parallelogram and measure the diagonal: that is the resultant.",
             "Repeat for a second pair of forces, and for the pair and its reversed "
             "version."],
     "formula": "|R| = |A + B|, measured with a ruler along the diagonal",
     "columns": ["A (N)", "B (N)", "measured R (N)", "calculated R (N)", "difference"],
     "theory": ["A parallelogram method strip is printed with the grid already on it, so "
                "the only judgement is where you put the points.",
                "Check your measurement against the components: resolve both forces, add "
                "the numbers, and compare. The two must agree.",
                "When the forces are equal and opposite the parallelogram collapses and the "
                "resultant is zero. That single case is worth doing, because it shows the "
                "method handles the degenerate case too."]},

    {"no": 5, "topic": 3, "title": "Measure the free fall time of a ball using a ticker-timer "
                                    "and hence find the acceleration due to gravity.",
     "apparatus": ["ticker-tape vibrator", "roll of ticker-tape", "steel ball",
                   "transformer", "sellotape"],
     "measures": "The spacing of the dots on the tape as the ball falls.",
     "how": ["Pass the tape through the timer and let the ball fall while the timer marks it.",
             "The dots get further apart as the ball speeds up. That spacing **is** the "
             "measurement; you never need to time anything.",
             "Mark the positions of a run of dots and measure the successive intervals.",
             "Plot interval against the interval number. The pattern is linear, and twice "
             "the gradient is g."],
     "formula": "u = (s_n + s_n+1)/T, then a = (s_n+1 - s_n)/T^2",
     "columns": ["dot group", "position (m)", "interval s (m)", "T (s)", "mean velocity"],
     "theory": ["The timer marks at a fixed frequency, so every T seconds the ball covers "
                "further than the last. The difference in successive intervals is aT^2.",
                "This is the whole of the uniformly-accelerated motion chapter, used to "
                "measure g without a stopwatch at all.",
                "Use the timer frequency, not your own timing. Any error in T is squared in "
                "the final answer, so an uncertain mains frequency is the main systematic "
                "error here."]},

    {"no": 6, "topic": 3, "title": "Investigate the value of acceleration due to gravity by "
                                    "the free-fall method using an electronic timer.",
     "apparatus": ["free fall apparatus", "steel ball", "electronic timer with power supply",
                   "plumb line", "meter rod"],
     "measures": "The fall time for two known heights.",
     "how": ["Set the apparatus so the ball falls vertically and the timer triggers on "
             "release.",
             "Measure the drop height h with the meter rod and the plumb line.",
             "Record the time t for the ball to fall that height.",
             "Repeat for several heights and plot t^2 against 2h."],
     "formula": "h = (1/2) g t^2, so a plot of t^2 against h has gradient 2/g",
     "columns": ["h (m)", "t1", "t2", "t3", "mean t", "t^2"],
     "theory": ["Free fall is the special case of uniform acceleration with u = 0. Nothing "
                "else in the experiment depends on any assumption you cannot check.",
                "A straight line through the origin confirms the model. A parallel line "
                "that misses the origin points at a systematic error, usually a delay in "
                "the trigger.",
                "Take the gradient of the graph rather than calculating g from a single "
                "reading. Every point then contributes."]},

    {"no": 7, "topic": 7, "title": "Verify that the time period of the simple pendulum is "
                                    "directly proportional to the square root of its length, "
                                    "and hence find g from the graph.",
     "apparatus": ["simple pendulum", "stopwatch", "stand with clamp", "thread", "cork",
                   "Vernier callipers"],
     "measures": "The period T for a range of pendulum lengths.",
     "how": ["Measure the length from the point of suspension to the centre of the bob, not "
             "to its bottom edge.",
             "Keep the amplitude small, under about 10 degrees. Larger amplitudes make the "
             "period longer than the small-angle formula predicts.",
             "Time twenty complete oscillations and divide by twenty. A single oscillation "
             "cannot be timed accurately by hand.",
             "Repeat for at least five lengths and plot T^2 against L."],
     "formula": "T = 2 pi sqrt(L/g), so a plot of T^2 against L has gradient 4 pi^2 / g",
     "columns": ["L (m)", "20 oscillations (s)", "T (s)", "T^2 (s^2)"],
     "theory": ["Squaring the equation removes the square root and turns a curve into a "
                "straight line. That is the trick: plot T^2 against L, not T against L.",
                "The gradient is 4 pi^2/g, so g = 4 pi^2 / gradient. Using the gradient "
                "rather than one point uses every measurement you made.",
                "The graph also settles the amplitude question: if the large-amplitude "
                "points sit high, you have allowed the swing to grow."]},

    {"no": 8, "topic": 8, "title": "Determine the frequency of a sonometer.",
     "apparatus": ["AC vibrator", "step-down transformer 6 V", "connecting wires", "thread",
                   "pulley", "scale", "planer"],
     "measures": "The length of a stretched string that vibrates at a known frequency.",
     "how": ["Fix the string between the bridge and the pulley and hang known masses from it.",
             "Set the vibrator driving frequency and adjust the vibrating length until you "
             "get a clear standing wave with a node at the midpoint.",
             "Measure the vibrating length between the nodes.",
             "Repeat for several frequencies."],
     "formula": "f = (1/2L) sqrt(T/mu), and T = mg for a mass m hung on the string",
     "columns": ["frequency (Hz)", "mass (kg)", "vibrating length L (m)", "frequency found"],
     "theory": ["A string fixed at both ends vibrates in its fundamental with half a "
                "wavelength along the vibrating length.",
                "The wave speed on a string depends on the tension and the mass per unit "
                "length, so changing the hanging mass changes the pitch.",
                "The formula connects two chapters at once: waves for the standing wave, "
                "and rotation for nothing at all, but mechanics for the tension."]},

    {"no": 9, "topic": 8, "title": "Investigate the laws of vibration of stretched strings "
                                    "by sonometer or electromagnetic method.",
     "apparatus": ["sonometer", "tuning forks of different frequencies", "hanger",
                   "1/2 kg weights", "wires of different diameter",
                   "physical, digital or spring balance", "weight box", "meter rod"],
     "measures": "The vibrating length for each of two different wires.",
     "how": ["Set up one wire and find the vibrating length for several tuning forks.",
             "Plot length against 1/f. A straight line through the origin is the law.",
             "Swap to a wire of different diameter and repeat, keeping the tension the same.",
             "The two gradients differ by the square root of the mass per unit length."],
     "formula": "L proportional to 1/f at fixed tension, and L proportional to 1/sqrt(mu)",
     "columns": ["f (Hz)", "1/f", "L for wire 1 (m)", "L for wire 2 (m)"],
     "theory": ["Two laws are being tested at once: the inverse relation between length and "
                "frequency, and the effect of the string's mass per unit length.",
                "Use copper rather than iron for the second wire, as the syllabus notes, "
                "because iron stretches enough under the same load to change the tension.",
                "Measure the wire diameters too, so mu can be compared with the gradients "
                "rather than just asserted."]},

    {"no": 10, "topic": 8, "title": "Determine the wavelength of sound in air using "
                                     "stationary waves and calculate the speed of sound using "
                                     "a resonance tube.",
     "apparatus": ["resonance apparatus", "different tuning forks of known frequencies",
                   "thermometer", "Vernier callipers", "rubber pad", "two set squares",
                   "beaker"],
     "measures": "The length of the air column at resonance.",
     "how": ["Set the tuning fork vibrating on the rim of the tube, held with a rubber pad "
             "so it does not touch the glass.",
             "Vary the air column by moving the water reservoir until the note is loudest.",
             "That is resonance. Measure the air column and note the end correction.",
             "Repeat for several forks of known frequency."],
     "formula": "L + e = lambda/4 at first resonance, so v = f lambda",
     "columns": ["f (Hz)", "air column L (m)", "corrected length", "lambda (m)",
                 "speed v (m/s)"],
     "theory": ["A tube closed at one end supports a quarter-wavelength at its first "
                "resonance, with a node at the closed end and an antinode at the open one.",
                "The measured column is always slightly shorter than a quarter wavelength, "
                "by an end correction of about 0.6 times the tube radius for each open end.",
                "Plot corrected length against 1/f. The gradient is the wavelength for unit "
                "frequency, and v = f lambda follows."]},

    {"no": 11, "topic": 10, "title": "Determine the specific heat capacity of a solid using "
                                     "the method of mixture (Regnault's method).",
     "apparatus": ["Regnault's apparatus for specific heat", "thermometer", "solid ball",
                   "calorimeter"],
     "measures": "The temperature of water, water plus the hot solid, and their masses.",
     "how": ["Heat the solid ball in steam for about ten minutes so it is at 100 °C.",
             "Measure the mass of the calorimeter and the mass of the water in it, and note "
             "the initial temperature.",
             "Transfer the ball quickly into the water and stir.",
             "Note the highest temperature reached. Work fast: the steam time and the "
             "transfer are the two places heat is lost."],
     "formula": "m_s c_s (100 - T) = (m_w c_w + C_cal)(T - T_0)",
     "columns": ["mass of solid (g)", "mass of water (g)", "T initial (°C)",
                 "T final (°C)"],
     "theory": ["Heat lost by the ball equals heat gained by the water and the calorimeter. "
                "That single equation is the first law of thermodynamics with no gas in "
                "sight.",
                "The calorimeter's own heat capacity C_cal is not negligible and must be "
                "included, or the answer comes out far too large.",
                "This is the practical counterpart of outcome 10.5.3: the same balance of "
                "heat in against heat out."]},

    {"no": 12, "topic": 10, "title": "Determine the specific heat capacity of water by the "
                                     "electrical method.",
     "apparatus": ["electrical calorimeter", "1/5 °C thermometer", "battery", "rheostat",
                   "key", "ammeter", "volmeter", "connecting wires", "stopwatch",
                   "physical, digital or spring balance", "weight box"],
     "measures": "Current, potential difference, mass of water and the time taken.",
     "how": ["Set the circuit and use the rheostat to pass a modest current.",
             "Measure the current and the potential difference across the calorimeter.",
             "Record the temperature and start the stopwatch together.",
             "Stop after the temperature has risen by about 20 °C, stirring throughout."],
     "formula": "c = V I t / (m (T_2 - T_1))",
     "columns": ["I (A)", "V (V)", "t (s)", "m (kg)", "T1 (°C)", "T2 (°C)", "c"],
     "theory": ["The electrical energy VI t goes into raising the temperature of the water, "
                "so c falls straight out of the measurement.",
                "Stir constantly. Convection currents inside the calorimeter are the main "
                "practical source of error, and they bias the result low.",
                "Plot temperature against time first. If it is not a straight line, the "
                "heating was not steady and no single c should be quoted."]},
]

_BY_CHAPTER = {n: [p for p in PRACTICALS if p["topic"] == n] for n in range(1, 11)}


def for_chapter(number):
    """The experiments the syllabus lists for one chapter, in order."""
    return _BY_CHAPTER.get(number, [])


def for_topic(topic):
    """The experiments for one sub-topic number, e.g. ``for_topic(7)``."""
    return [p for p in PRACTICALS if p["topic"] == topic]
