"""Chapter 8 content: Waves.

Nineteen outcomes across six sections - the widest spread in the book, from a
single sine curve all the way to red and blue shifts. The chapter owns three
instruments of its own: a **two-wave bench** where any pair of sources can be
superposed and the interference pattern watched emerge, a **stationary-wave
bench** for strings and air columns, and a **Doppler explorer** where the four
cases of the syllabus can each be set up and read off in numbers.
"""

from __future__ import annotations

SLOS = [
    {"id": "8.1.1", "text": "Define progressive waves.",
     "simple": "A wave that carries energy from one point to another without carrying matter with it.",
     "taught": "Wave motion", "activity": "Two-wave bench separating the travelling wave from the displacement it leaves behind",
     "check": "Guided practice: define progressive wave and identify crests, troughs, amplitude and wavelength"},
    {"id": "8.1.2", "text": "Explain energy transfer through a progressive wave.",
     "simple": "Energy moves at the wave speed; the medium's particles oscillate about fixed points and do not travel with it.",
     "taught": "Energy transfer", "activity": "Cork-on-a-pond demonstration drawn frame by frame",
     "check": "Guided practice: explain how energy transfers while the medium does not"},
    {"id": "8.1.3", "text": "Solve word problems using intensity = power/area and intensity proportional to (amplitude)^2.",
     "simple": "Intensity is power per unit area, and it goes as the square of the amplitude.",
     "taught": "Intensity", "activity": "Intensity calculator with the amplitude-squared law exposed",
     "check": "Guided practice: solve intensity problems in both forms"},
    {"id": "8.1.4", "text": "Solve word problems using v = f lambda.",
     "simple": "Wave speed equals frequency times wavelength.",
     "taught": "The wave equation", "activity": "Three-variable solver for v, f and lambda",
     "check": "Guided practice: solve v = f lambda problems"},
    {"id": "8.2.1", "text": "Differentiate between transverse and longitudinal waves.",
     "simple": "Transverse: particles move across the direction of travel. Longitudinal: particles move along it.",
     "taught": "Types of wave", "activity": "Particle-motion diagram for each type side by side",
     "check": "Guided practice: classify waves and justify from the particle motion"},
    {"id": "8.2.2", "text": "Analyse graphical representations of transverse and longitudinal waves.",
     "simple": "Crest, trough, compression and rarefaction - and amplitude is half the crest-to-trough height.",
     "taught": "Reading wave graphs", "activity": "Annotated graphs with every feature labelled",
     "check": "Guided practice: read amplitude, wavelength and phase off graphs"},
    {"id": "8.3.1", "text": "State the principle of superposition of two waves.",
     "simple": "The resultant displacement at every point is the sum of the two individual displacements.",
     "taught": "Superposition", "activity": "Two-wave bench with the sum drawn third",
     "check": "Guided practice: apply superposition and confirm it is reversible"},
    {"id": "8.3.2", "text": "Describe the phenomenon of interference of sound waves.",
     "simple": "Overlapping sound is louder where the waves arrive in step and quieter where they arrive out of step.",
     "taught": "Interference", "activity": "Interference explorer over a whole range of path differences",
     "check": "Guided practice: predict loud and quiet positions from the path difference"},
    {"id": "8.3.3", "text": "Calculate the phase difference between two waves.",
     "simple": "Delta phi = (2 pi / lambda) times the path difference, in radians.",
     "taught": "Phase difference", "activity": "Phase-difference calculator with the loud/quiet verdict",
     "check": "Guided practice: compute phase differences from path differences"},
    {"id": "8.3.4", "text": "Explain the formation of beats using diagrams.",
     "simple": "Two close frequencies interfere, and the pattern drifts, so the loudness rises and falls at f1 - f2.",
     "taught": "Beats", "activity": "Beat generator showing the summed wave inside a drifting envelope",
     "check": "Guided practice: calculate beat frequency and period and explain the drifting pattern"},
    {"id": "8.4.1", "text": "Define nodes and antinodes.",
     "simple": "A node never moves; an antinode moves most. They sit lambda/2 apart.",
     "taught": "Stationary waves", "activity": "Stationary-wave bench for any mode, nodes and antinodes marked",
     "check": "Guided practice: locate nodes and antinodes for a given mode"},
    {"id": "8.4.2", "text": "Describe formation of stationary waves in a string and air column.",
     "simple": "Two identical waves travelling in opposite directions superpose into a wave that does not travel.",
     "taught": "Strings and pipes", "activity": "String, open pipe and closed pipe compared on one bench",
     "check": "Guided practice: explain formation and write the boundary conditions"},
    {"id": "8.4.3", "text": "Solve word problems related to stationary waves.",
     "simple": "Numerical problems on harmonics, nodes and antinodes in strings and pipes.",
     "taught": "Stationary-wave problems", "activity": "Harmonic calculator for all three column types",
     "check": "Guided practice: solve stationary-wave word problems"},
    {"id": "8.5.1", "text": "Describe Doppler's effect.",
     "simple": "The observed frequency changes when source and observer move relative to each other.",
     "taught": "Doppler's effect", "activity": "Doppler explorer showing wavelength compression ahead of a source",
     "check": "Guided practice: describe the effect and predict rising or falling pitch"},
    {"id": "8.5.2", "text": "Derive relations for apparent frequency in four cases: (a) source at rest, listener moving; "
                           "(b) listener at rest, source moving; (c) both moving toward each other; "
                           "(d) both moving away.",
     "simple": "f' = f(v plus or minus v_o)/(v minus or plus v_s), with the sign set by the geometry.",
     "taught": "The four Doppler formulas", "activity": "All four cases side by side with the sanity check applied",
     "check": "Guided practice: derive and apply all four relations"},
    {"id": "8.5.3", "text": "Solve word problems using these relations.",
     "simple": "Numerical problems on apparent frequency in all four cases.",
     "taught": "Doppler problems", "activity": "Problem set with the 'if nothing moves, f' = f check on every answer",
     "check": "Guided practice: solve Doppler word problems with a sign check"},
    {"id": "8.5.4", "text": "Explain application of Doppler's effect in electromagnetic waves.",
     "simple": "Red shift when receding, blue shift when approaching - how the expanding universe was found.",
     "taught": "Doppler in light", "activity": "Spectrum-shift panel with the shift drawn as a visible offset",
     "check": "Guided practice: explain red and blue shift in terms of wavelength change"},
    {"id": "8.5.5", "text": "Apply Doppler's effect to radar, sonar, satellites, red and blue shifts.",
     "simple": "Speed detection by radio, sonar, satellite tracking and astronomical redshift.",
     "taught": "Applications of Doppler", "activity": "Round-trip diagram showing the doubled shift",
     "check": "Guided practice: explain each application, including the factor of two in radar"},
    {"id": "8.6.1", "text": "Use of waves for: medical purposes, digital transmission, storage of information, "
                           "monitoring earthquakes and tsunamis.",
     "simple": "Five modern applications, each explained by the wave property it exploits.",
     "taught": "Waves in the modern world", "activity": "Application table with the exploited property named",
     "check": "Guided practice: match each application to the wave property it uses"},
]

STATIONS = [
    {"key": "overview", "label": "\U0001F5FA\uFE0F Your route & outcomes", "slos": []},
    {"key": "progressive", "label": "\U0001F30A Progressive waves & energy", "slos": ["8.1.1", "8.1.2"]},
    {"key": "intensity", "label": "\U0001F4A1 Intensity", "slos": ["8.1.3"]},
    {"key": "waveequation", "label": "\U0001F44E v = f lambda", "slos": ["8.1.4"]},
    {"key": "types", "label": "\u2194\uFE0F Transverse & longitudinal", "slos": ["8.2.1", "8.2.2"]},
    {"key": "superposition", "label": "\u2795 Superposition & interference", "slos": ["8.3.1", "8.3.2", "8.3.3"]},
    {"key": "beats", "label": "\U0001F3B5 Beats", "slos": ["8.3.4"]},
    {"key": "stationary", "label": "\U0001F3BB Stationary waves", "slos": ["8.4.1", "8.4.2", "8.4.3"]},
    {"key": "doppler", "label": "\U0001F697 Doppler effect", "slos": ["8.5.1", "8.5.2", "8.5.3"]},
    {"key": "lightshift", "label": "\U0001F30D Doppler in light & applications", "slos": ["8.5.4", "8.5.5"]},
    {"key": "modern", "label": "\U0001F30F Waves in the modern world", "slos": ["8.6.1"]},
    {"key": "worked", "label": "\U0001F9EE Worked problems", "slos": []},
    {"key": "practice", "label": "\U0001F9E0 Practice", "slos": []},
    {"key": "tutor", "label": "\U0001F916 Atlas Tutor (offline AI)", "slos": []},
    {"key": "references", "label": "\U0001F4DA References", "slos": []},
]

BIG_IDEAS = [
    ("Everything in this chapter is one sine curve.",
     "A wave is y = A sin(kx - ωt). Crests, troughs, wavelength, frequency, amplitude, "
     "interference, beats and stationary waves are all consequences of adding or subtracting "
     "that one expression."),
    ("Superposition is reversible, and that is what makes interference useful.",
     "Two waves pass through each other and reappear unchanged. The interference pattern "
     "exists only where they overlap - which is why you can prove interference with two "
     "tuning forks without either of them being damaged."),
    ("Doppler is a wavelength argument, not a speed argument.",
     "A moving source crams its crests closer together in front and spreads them out behind. "
     "The medium's speed never changes - only the spacing the observer meets."),
]

TAG = "CHAPTER 8 \u00B7 OPEN"
INTRO = (
    "Nineteen outcomes, from a single definition of a progressive wave to the redshift of a "
    "galaxy. The thread running through all of it is one curve, y = A sin(kx - ωt): add two of "
    "them and you get interference; add them travelling opposite ways and you get a stationary "
    "wave; vary the spacing and you get the Doppler effect. There are three benches here - a "
    "two-wave bench, a stationary-wave bench and a Doppler explorer."
)
ROUTE = ("Progressive waves \u2192 Intensity \u2192 v = f lambda \u2192 Types of wave \u2192 "
         "Superposition and interference \u2192 Beats \u2192 Stationary waves \u2192 Doppler \u2192 "
         "Doppler in light \u2192 Waves in the modern world \u2192 Worked problems \u2192 Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("speed of sound taken as 340 m s\u207b\u00b9", "warn"),
                 ("Diagrams schematic, not to scale", "mute"),
                 ("Every trace computed by this app", "good")]

NOTES = [
    ("\u26A0 WATCH OUT", "Amplitude is half the crest-to-trough height",
     "If a graph shows 6 cm from crest to trough, the amplitude is 3 cm. Doubling that error "
     "costs marks in every wave question in the syllabus."),
    ("\U0001F3AF EXAM TIP", "Always test a Doppler formula with nothing moving",
     "Substituting v_o = v_s = 0 must give f' = f. If it does not, the signs are wrong before "
     "you have done any arithmetic - and that check takes five seconds."),
    ("\U0001F52E HONEST LIMIT", "Doppler is not sound getting excited",
     "The pitch of a passing siren drops because each wavefront is emitted from a position "
     "further away, so the crests are spread out behind the source. The wave is not changing "
     "speed or loudness in any way a listener can measure."),
]


# --------------------------------------------------------------------------
# 8.1  Progressive waves
# --------------------------------------------------------------------------

PROGRESSIVE_POINTS = [
    {"point": "A progressive wave carries energy, not matter",
     "detail": "Each particle of the medium oscillates about a fixed position while the "
               "energy passes from particle to particle."},
    {"point": "The demonstration to remember",
     "detail": "A cork on a pond bobs up and down and drifts slowly. A floating boat is "
               "pushed back to the shore after the waves have passed. Matter stays; energy goes."},
    {"point": "Crest, trough, compression, rarefaction",
     "detail": "Crests and troughs belong to transverse waves; compressions and rarefactions "
               "to longitudinal ones. Both are places of maximum and minimum displacement."},
    {"point": "Amplitude and wavelength",
     "detail": "Amplitude is half the crest-to-trough height. Wavelength is measured crest to "
               "crest, or compression to compression."},
]

INTENSITY_CASES = [
    {"situation": "Doubling the amplitude of a sound wave",
     "change": "intensity becomes 4 times larger", "why": "I is proportional to A²."},
    {"situation": "Halving the amplitude", "change": "intensity becomes one quarter",
     "why": "I is proportional to A², so ½² = ¼."},
    {"situation": "Tripling the amplitude", "change": "intensity becomes 9 times larger",
     "why": "3² = 9."},
    {"situation": "Spreading the same power over 4 times the area",
     "change": "intensity becomes one quarter", "why": "I = P/A, and A has quadrupled."},
    {"situation": "A point source, where the area grows as r²",
     "change": "intensity falls as 1/r²", "why": "A = 4πr², so I = P/(4πr²)."},
]

WAVE_EQUATION_NOTES = [
    {"question": "What if the medium changes but the frequency stays the same?",
     "answer": "The speed changes, so the wavelength changes. Sound entering water keeps its "
               "frequency - which is why the pitch does not change - but its wavelength "
               "shrinks from about 0.78 m to about 0.33 m."},
    {"question": "What if you raise the frequency on a fixed string?",
     "answer": "The wavelength shortens: lambda = v/f. That is exactly what pressing a "
               "fret does."},
    {"question": "Why does the speed not change with frequency in air?",
     "answer": "The wave speed is set by the medium - how quickly the air is pushed aside - "
               "not by how often. In air they happen to be nearly independent."},
    {"question": "What if you change both f and lambda?",
     "answer": "The speed cannot change in a fixed medium, so v = f lambda fixes the ratio. "
               "Moving a wave faster at the same frequency is impossible in a given medium."},
]

TRANSVERSE_DETAIL = [
    {"property": "Particle motion", "transverse": "perpendicular to the direction of travel",
     "longitudinal": "along the direction of travel"},
    {"property": "Features on the graph", "transverse": "crests and troughs",
     "longitudinal": "compressions and rarefactions"},
    {"property": "Particles cross the direction of travel?",
     "transverse": "no", "longitudinal": "yes"},
    {"property": "Examples", "transverse": "light, water ripples, S-waves in rock, rope waves",
     "longitudinal": "sound in air and water, P-waves in rock, sound in a solid rod"},
    {"property": "Can it be polarised?", "transverse": "yes", "longitudinal": "no"},
    {"property": "Needs a medium to travel?", "transverse": "not for light; yes for ripples",
     "longitudinal": "always"},
]

SUPERPOSITION_POINTS = [
    {"point": "The principle itself",
     "detail": "When two waves overlap, the resultant displacement at every point is the sum "
               "of the individual displacements."},
    {"point": "It is linear",
     "detail": "Two sounds combined in this way are also distinguishable from one another by "
               "ear. This is the whole basis of binaural recording."},
    {"point": "It is reversible",
     "detail": "After the waves have passed through each other each carries on unchanged. "
               "Neither is consumed, so the interference is only where they overlap."},
    {"point": "The simplest case",
     "detail": "Two pulses meeting head-on pass straight through each other, emerging with "
               "their shapes intact. Watching them pass through each other is the easiest "
               "possible demonstration of superposition."},
]

MODERN_USES_TABLE = [
    {"field": "Medical imaging", "wave": "Ultrasound",
     "property used": "Reflection and time of flight",
     "detail": "A 20 kHz to 1 MHz pulse is sent into the body and timed on echo. The delay "
               "gives the depth, and the strength of the echo tells whether the boundary is "
               "soft tissue or bone. The Doppler shift of the echo gives the blood flow."},
    {"field": "Digital transmission", "wave": "Radio, microwaves, light in fibre",
     "property used": "Amplitude, frequency or phase modulation",
     "detail": "A carrier is switched on and off, or its amplitude, frequency or phase is "
               "changed in step with the signal. The receiver detects the change and turns it "
               "back into data. Nothing physical has to travel between the two ends."},
    {"field": "Storage", "wave": "Light in optical discs",
     "property used": "Focusing and interference-limited spot size",
     "detail": "A laser is focused to a spot a fraction of a micrometre across and burns a pit, "
               "or changes the magnetic orientation of a domain. The limit on how many bits "
               "fit is set by how small the spot can be made."},
    {"field": "Earthquakes", "wave": "Seismic P, S and surface waves",
     "property used": "Speed differences between wave types",
     "detail": "S-waves are slower and cannot travel through liquid, so their behaviour "
               "revealed that the outer core is liquid. Comparing arrival times at many "
               "stations locates the epicentre."},
    {"field": "Tsunamis", "wave": "Long-wavelength shallow-water waves",
     "property used": "Speed depending on depth",
     "detail": "In deep water a tsunami travels at about 700 km/h but is only centimetres "
               "high. As it reaches shallow water it slows to walking pace and piles up into a "
               "wall of water at the coast."},
    {"field": "Astronomy", "wave": "The whole electromagnetic spectrum",
     "property used": "Wavelength determines what can be observed",
     "detail": "Telescopes detect radio, infrared, visible, ultraviolet, X-ray and gamma "
               "emission from the same objects. The universe is not dark: it simply glows at "
               "wavelengths our eyes cannot see."},
]


# --------------------------------------------------------------------------
# 8.3  Interference and beats
# --------------------------------------------------------------------------

INTERFERENCE_NOTES = [
    {"case": "Path difference = n lambda",
     "phase": "2 pi n", "kind": "constructive, loud",
     "why": "The waves arrive exactly in step, so their displacements add."},
    {"case": "Path difference = (n + 1/2) lambda",
     "phase": "(2n + 1) pi", "kind": "destructive, quiet",
     "why": "The waves arrive half a cycle out of step, so each crest lands on a trough."},
    {"case": "Anything between", "phase": "anything between",
     "kind": "partly constructive",
     "why": "The resultant lies between the loud and the quiet value."},
]

BEAT_POINTS = [
    {"point": "Two slightly different frequencies",
     "detail": "Say 440 Hz and 444 Hz. They are close enough that you hear them as one note "
               "with a wobble."},
    {"point": "The interference pattern drifts",
     "detail": "Wherever the two waves happen to be in step is fine and loud. That fine pair "
               "moves steadily along the line joining the sources."},
    {"point": "So the loudness rises and falls",
     "detail": "As the pattern sweeps past you, the sound waxes and wanes. One full rise and "
               "fall is one beat."},
    {"point": "The beat frequency is the difference",
     "detail": "f_beat = |f1 - f2| = 4 Hz here, so the beat repeats every 0.25 s."},
    {"point": "That is a measurement tool",
     "detail": "Beats slow to nothing when two sounds match exactly, so a piano tuner listens "
               "for the beats to disappear rather than trying to compare pitches by ear."},
]

# --------------------------------------------------------------------------
# 8.4  Stationary waves
# --------------------------------------------------------------------------

STANDING_WAVE_POINTS = [
    {"point": "How they are made",
     "detail": "Two identical waves travelling in opposite directions. A wave sent along a "
               "string and reflected back from the far end does exactly this."},
    {"point": "The pattern does not travel",
     "detail": "The shape stays put while the particles oscillate about it. That is why they "
               "are called stationary or standing waves."},
    {"point": "Nodes are always still",
     "detail": "A node is a point whose two component waves are always exactly opposite. "
               "The displacement there is zero at every instant."},
    {"point": "Antinodes swing most",
     "detail": "At an antinode the two displacements always add. The particles pass through "
               "the equilibrium position together, and their speed is largest."},
    {"point": "They are lambda/2 apart",
     "detail": "Node to next antinode is a quarter wavelength; antinode to next antinode is "
               "half a wavelength."},
    {"point": "No energy is carried",
     "detail": "The energy stays put, oscillating between the two stores, exactly as in "
               "simple harmonic motion."},
]

COLUMN_RULES = [
    {"column": "String, both ends fixed", "end condition": "node at both ends",
     "f_n": "f_n = n v / 2L", "allowed": "n = 1, 2, 3, ...",
     "note": "All harmonics are present, so the tone is rich."},
    {"column": "Pipe, both ends open", "end condition": "antinode at both ends",
     "f_n": "f_n = n v / 2L", "allowed": "n = 1, 2, 3, ...",
     "note": "The same frequencies as an open-ended string. An open pipe and a string of the "
             "same length sound at the same note."},
    {"column": "Pipe, one end closed", "end condition": "node at the closed end, antinode at "
                                                    "the open end",
     "f_n": "f_n = (2n - 1) v / 4L", "allowed": "n = 1, 3, 5, ...",
     "note": "Only the odd harmonics exist, so the tone is hollow. A closed pipe sounds an "
             "octave above an open pipe of the same length."},
]

DOPPLER_SUMMARY = [
    {"case": "a", "title": "Source at rest, observer moving",
     "formula": "f' = f (v + v_o) / v", "sign": "+ if approaching, - if receding",
     "picture": "The observer meets the crests faster or slower, but the wavelengths are "
                "untouched."},
    {"case": "b", "title": "Observer at rest, source moving",
     "formula": "f' = f v / (v - v_s)", "sign": "- if approaching, + if receding",
     "picture": "The moving source crams its crests together ahead of it and spreads them out "
                "behind it."},
    {"case": "c", "title": "Both moving towards each other",
     "formula": "f' = f (v + v_o) / (v - v_s)", "sign": "+ and -",
     "picture": "Both effects add, so this is the largest possible shift."},
    {"case": "d", "title": "Both moving away from each other",
     "formula": "f' = f (v - v_o) / (v + v_s)", "sign": "- and +",
     "picture": "Both effects subtract, so this is the smallest possible shift."},
]

DOPPLER_APPLICATIONS = [
    {"application": "Police radar",
     "how": "A microwave pulse is reflected off the moving car and the beat between the "
            "transmitted and returned frequency is measured.",
     "why_it_works": "The pulse is shifted twice, once outbound and once on return, so the "
                     "measured shift is about 2fv/c — the factor of two is what makes the "
                     "small shift measurable at all."},
    {"application": "Weather radar",
     "how": "Short wavelength pulses are reflected off raindrops inside a storm.",
     "why_it_works": "Drops moving towards the radar return a higher frequency, so a map of "
                     "the shift reveals wind speed inside the storm — information ordinary "
                     "radar cannot give."},
    {"application": "Sonar and ultrasound",
     "how": "Sound pulses are reflected off submarines, shoals and moving organs.",
     "why_it_works": "The same Doppler argument applies to sound, so depth sounders can give "
                     "both range and closing speed."},
    {"application": "Medical Doppler",
     "how": "Ultrasound is bounced off flowing blood cells.",
     "why_it_works": "Cells moving towards the probe return a higher frequency, so the "
                     "shift measures the blood velocity and reveals a blockage."},
    {"application": "Satellite tracking",
     "how": "Ground stations track satellites and launchers by the shift of the carrier.",
     "why_it_works": "The apparent range is slightly changed by the radial velocity, which "
                     "allows orbital decay to be measured precisely."},
    {"application": "Astronomy",
     "how": "The spectra of stars and galaxies are compared with laboratory lines.",
     "why_it_works": "Every distant galaxy is red-shifted in proportion to its distance, "
                     "which is the direct evidence that the universe is expanding."},
]


# --------------------------------------------------------------------------
# Worked problems
# --------------------------------------------------------------------------

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "The wave equation in three directions",
     "level": "Foundation", "slos": ["8.1.4"],
     "question": "A sound wave in air has a frequency of 440 Hz and a speed of 340 m s\u207b\u00b9. "
                 "Find its wavelength. Then find the frequency of the same wave after it passes "
                 "into water, where its speed is 1500 m s\u207b\u00b9.",
     "known": ["f\u2081 = 440 Hz", "v\u2081 = 340 m s\u207b\u00b9", "v\u2082 = 1500 m s\u207b\u00b9"],
     "find": "lambda\u2081 in air, f\u2082 in water, and then \u03bb\u2082 in water",
     "equation": r"v = f\lambda",
     "conversions": ["All values are already in SI units. The key point is that the frequency "
                     "does **not** change when a wave enters a new medium."],
     "substitution": r"\lambda_1 = \frac{v_1}{f_1} = \frac{340}{440}"
                     r"\qquad \lambda_2 = \frac{v_2}{f_1} = \frac{1500}{440}",
     "calculation": [
         "Step 1 \u2014 wavelength in air: \u03bb = v/f = 340/440 = 0.773 m.",
         "Step 2 \u2014 what changes at the boundary? The **medium** changes, so the speed "
         "changes. The frequency is set by the source and stays exactly the same.",
         "Step 3 \u2014 the frequency in water is therefore still **440 Hz**. That is the trap "
         "in this question: the speed of a wave has nothing to do with what its source is doing.",
         "Step 4 \u2014 with the frequency known, the new wavelength follows at once: "
         "\u03bb\u2082 = v\u2082/f = 1500/440 = 3.41 m.",
         "Step 5 \u2014 this is the whole lesson of the question: the **pitch** does not change "
         "when sound enters water, but the wavelength more than quadruples (3.41/0.773 = 4.4). "
         "People expecting a pitch change are mixing up frequency with wavelength, and people "
         "who divide the new speed by the old wavelength are ignoring that the frequency "
         "never changed at all.",
     ],
     "unit_check": r"\lambda = \frac{\mathrm{m\,s^{-1}}}{\mathrm{s^{-1}}} = [L] = \mathrm{m}",
     "answer": r"\lambda_1 = 0.773\ \mathrm{m},\quad f_2 = 440\ \mathrm{Hz\ (unchanged)}"
               r"\quad \lambda_2 = 3.41\ \mathrm{m}",
     "sig_fig_note": "Three significant figures throughout, so 0.773 m and 3.41 m. Reporting a "
                     "frequency of 1940 Hz is the classic wrong answer here.",
     "assumptions": ["The frequency is set entirely by the source and is unchanged at a boundary.",
                     "Both speeds are taken as constant over the region considered."]},
    {"id": "WP2", "title": "Intensity and amplitude",
     "level": "Developing", "slos": ["8.1.3"],
     "question": "A loudspeaker radiates 12 W uniformly over a hemisphere of radius 4.0 m. Find the "
                 "intensity at that distance. If the amplitude of the wave is doubled, what happens "
                 "to the power and to the intensity?",
     "known": ["P = 12 W", "hemisphere of radius r = 4.0 m",
               "area of a hemisphere = 2 pi r\u00b2", "I is proportional to A\u00b2"],
     "find": "I at 4.0 m, and the effect of doubling the amplitude",
     "equation": r"I = \frac{P}{A}, \qquad I \propto A^2",
     "conversions": ["No unit conversion needed; watts per square metre is the SI unit of intensity."],
     "substitution": r"I = \frac{12}{2\pi(4.0)^2} = \frac{12}{100.53}",
     "calculation": [
         "Step 1 \u2014 surface area of the hemisphere: A = 2 pi r\u00b2 = 2 pi (16) = 100.53 m\u00b2.",
         "Step 2 \u2014 intensity: I = 12/100.53 = 0.119 W m\u207b\u00b2.",
         "Step 3 \u2014 doubling the amplitude: since I is proportional to A\u00b2, the intensity "
         "becomes **four times** larger, so 0.478 W m\u207b\u00b2.",
         "Step 4 \u2014 the power must then be four times larger too: 48 W, because the same area "
         "is being used. If the power had stayed at 12 W the intensity would not have changed.",
         "Step 5 \u2014 the practical reading: loudness is not linear in amplitude. Doubling the "
         "amplitude is a big step, and the power needed to make it rises just as steeply \u2014 "
         "which is why amplifier power ratings are often quoted in decibels.",
     ],
     "unit_check": r"I = \mathrm{W\,m^{-2}}; \ [\text{intensity}] = [\text{power}] [L]^{-2}",
     "answer": "I = 0.119 W m\u207b\u00b2; doubling the amplitude quadruples both the power "
               "(to 48 W) and the intensity (to 0.478 W m\u207b\u00b2)",
     "sig_fig_note": "The power is to two significant figures and the radius to two, so I = 0.12 W m\u207b\u00b2.",
     "assumptions": ["The radiation is uniform across the hemisphere, which a small loudspeaker "
                     "approximates but a horn does not.",
                     "There is no absorption over 4 m."]},
    {"id": "WP3", "title": "Beats between two forks",
     "level": "Developing", "slos": ["8.3.4"],
     "question": "Two tuning forks of frequencies 400 Hz and 404 Hz are struck together. Find the beat "
                 "frequency and the time between one beat and the next. If a third fork of 408 Hz is "
                 "added, what is the beat frequency between it and the 400 Hz fork?",
     "known": ["f\u2081 = 400 Hz", "f\u2082 = 404 Hz", "f\u2083 = 408 Hz"],
     "find": "the beat frequency, the beat period, and the new beat frequency",
     "equation": r"f_{\text{beat}} = |f_1 - f_2|, \qquad T_{\text{beat}} = \frac{1}{f_{\text{beat}}}",
     "conversions": ["All values are already in hertz; the beat period comes out in seconds."],
     "substitution": r"f_{\text{beat}} = |400 - 404|, \qquad T_{\text{beat}} = \frac{1}{f_{\text{beat}}}",
     "calculation": [
         "Step 1 \u2014 beat frequency: f_beat = |404 \u2212 400| = 4 Hz.",
         "Step 2 \u2014 beat period: T_beat = 1/4 = 0.25 s. So four beats fall in every second.",
         "Step 3 \u2014 adding the third fork: between 408 and 400 the beat is |408 \u2212 400| = 8 Hz.",
         "Step 4 \u2014 the superposed result is more complicated than either answer alone. Three "
         "frequencies give 4 Hz beats between 400 and 404, 4 Hz between 404 and 408, and 8 Hz "
         "between 400 and 408, all interfering with one another.",
         "Step 5 \u2014 the rule is that beats come from **every pair**, and when the differences "
         "are small the ear hears the tone rise and fall at the smallest difference, with a faster "
         "ripple riding on it. This is why a chord can sound unsteady when the notes are close "
         "together but clean when they are far apart.",
     ],
     "unit_check": r"[\text{beat frequency}] = [T^{-1}] = \mathrm{Hz}; \ T_{\text{beat}} = [T] = \mathrm{s}",
     "answer": "f_beat = 4 Hz, beat period = 0.25 s; the 408 Hz fork beats with the 400 Hz one at 8 Hz",
     "sig_fig_note": "The frequencies are given to the nearest hertz, so the differences are exact to that precision.",
     "assumptions": ["The three forks are struck hard enough to sound together but not hard "
                     "enough to shift their frequencies (which loud forks do)."]},
    {"id": "WP4", "title": "Harmonics in a string and a closed pipe",
     "level": "Challenge", "slos": ["8.4.2", "8.4.3"],
     "question": "A string 0.65 m long has a wave speed of 340 m s\u207b\u00b9 and is fixed at both ends. "
                 "An air column of the same length is closed at one end. Find the fundamental and the "
                 "first two overtones of each, and explain why the two instruments differ.",
     "known": ["L = 0.65 m, v = 340 m s\u207b\u00b9",
               "String: f_n = n v / 2L", "Closed pipe: f_n = (2n \u2212 1) v / 4L"],
     "find": "the fundamental and first two overtones of each",
     "equation": r"f_{n,\text{string}} = \frac{nv}{2L}, \qquad f_{n,\text{closed}} = \frac{(2n-1)v}{4L}",
     "conversions": ["No unit conversion is needed; the length is already in metres."],
     "substitution": r"f_{1,\text{string}} = \frac{340}{2(0.65)}, \qquad "
                     r"f_{1,\text{closed}} = \frac{340}{4(0.65)}",
     "calculation": [
         "Step 1 \u2014 string fundamental: 340/1.30 = 261.5 Hz.",
         "Step 2 \u2014 string overtones: 2 f\u2081 = 523.0 Hz and 3 f\u2081 = 784.6 Hz. All harmonics "
         "are present.",
         "Step 3 \u2014 closed pipe fundamental: 340/2.60 = 130.8 Hz.",
         "Step 4 \u2014 closed pipe: only the odd harmonics, so the first two overtones are "
         "3 f\u2081 = 392.3 Hz and 5 f\u2081 = 653.8 Hz. The 2nd harmonic, 261.5 Hz, does not exist.",
         "Step 5 \u2014 why: a node is forced at the closed end, so the column must fit a whole number "
         "of **half** wavelengths. An odd number of quarter wavelengths only. Because quarter "
         "wavelengths fit twice as many modes as half wavelengths, the lowest mode is half as "
         "high \u2014 a closed pipe sounds an octave below a string of the same length.",
         "Step 6 \u2014 the missing even harmonics are why a stopped pipe sounds hollow and a violin "
         "does not. Missing harmonics remove high frequencies, and high frequencies are what give "
         "a note its edge.",
     ],
     "unit_check": r"f = \frac{\mathrm{m\,s^{-1}}}{\mathrm{m}} = [T^{-1}] = \mathrm{Hz}",
     "answer": "String: 261.5, 523.0, 784.6 Hz. Closed pipe: 130.8, 392.3, 653.8 Hz \u2014 an octave "
               "lower, with only odd harmonics",
     "sig_fig_note": "The length is to two significant figures and the speed to three, so the answers are 260 Hz and 523 Hz.",
     "assumptions": ["End corrections for the pipe are neglected; real pipes are slightly longer "
                     "than the geometrical length, which is why the real fundamental is lower."]},
    {"id": "WP5", "title": "Doppler with both moving",
     "level": "Challenge", "slos": ["8.5.2", "8.5.3"],
     "question": "A police car with its siren at 800 Hz travels at 30 m s\u207b\u00b9 towards a "
                 "stationary observer, while the observer runs towards the car at 10 m s\u207b\u00b9. "
                 "Take the speed of sound as 340 m s\u207b\u00b9. Find the frequency heard.",
     "known": ["f = 800 Hz", "v = 340 m s\u207b\u00b9",
               "v_o = 10 m s\u207b\u00b9 (observer approaching)",
               "v_s = 30 m s\u207b\u00b9 (source approaching)"],
     "find": "the observed frequency f'",
     "equation": r"f' = f\frac{v + v_o}{v - v_s}",
     "conversions": ["Both speeds are already in m s\u207b\u00b9 and the frequency in hertz. "
                     "No conversion is needed \u2014 but every speed must be in the same units."],
     "substitution": r"f' = 800 \times \frac{340 + 10}{340 - 30}",
     "calculation": [
         "Step 1 \u2014 identify the case: the observer is approaching and the source is approaching, "
         "so this is case (c).",
         "Step 2 \u2014 sanity check before calculating. Put v_o = v_s = 0 into the formula: it gives "
         "800 × 340/340 = 800 Hz. Correct \u2014 with nobody moving you must hear the original note. "
         "The formula is right.",
         "Step 3 \u2014 substitute: f' = 800 × 350/310 = 800 × 1.129 = 903.2 Hz.",
         "Step 4 \u2014 the pitch rises by about 13 %, which sounds like a lot. That is what "
         "approaching a siren at speed actually sounds like.",
         "Step 5 \u2014 what if they both stopped? The observer would hear 800 Hz. The whole "
         "difference came from the relative motion, and the air itself never changed.",
     ],
     "unit_check": r"f' = f \times \frac{[L T^{-1}]}{[L T^{-1}]} = f,\ \text{dimensionally a pure frequency}",
     "answer": "f' = 903 Hz, a rise of about 13 %",
     "sig_fig_note": "The speeds are to two or three figures, so 903 Hz is appropriate; the percentage is 13 %.",
     "assumptions": ["The observer moves directly towards the source along the line of sight.",
                     "The speed of sound is constant at 340 m s\u207b\u00b9 and the motions are steady."]},
]


# --------------------------------------------------------------------------
# Practice questions
# --------------------------------------------------------------------------

PRACTICE_QUESTIONS = [
    {"id": "P1", "category": "Progressive waves", "type": "mcq", "slo": "8.1.1",
     "prompt": "A progressive wave is one that...",
     "options": ["transfers energy without permanently transferring matter",
                 "transfers both energy and matter along",
                 "stays in one place", "needs no medium"],
     "answer": 0,
     "hint": "Think about a cork floating on a wave.",
     "explanation": "It carries energy forward while the medium's particles oscillate about "
                    "fixed positions. Put a cork on a pond and it bobs up and down but stays "
                    "roughly where it started."},
    {"id": "P2", "category": "Progressive waves", "type": "mcq", "slo": "8.1.2",
     "prompt": "The clearest proof that a wave carries energy and not matter is that...",
     "options": ["the wave slows down in water", "a floating boat is thrown back to the shore",
                 "the crests get further apart", "sound cannot travel through a vacuum"],
     "answer": 1,
     "hint": "Where does the displaced material end up?",
     "explanation": "The boat is pushed outward as the wave arrives and pulled back as it "
                    "leaves, returning to the shore. Energy went out; the boat did not."},
    {"id": "P3", "category": "Progressive waves", "type": "numeric", "slo": "8.1.2",
     "prompt": "A wave has a crest-to-trough distance of 5.0 cm. Enter the amplitude in centimetres.",
     "answer": 2.5, "tolerance": 0.05, "unit": "cm",
     "hint": "Amplitude is measured from the equilibrium line, not from crest to trough.",
     "explanation": "2.5 cm. This is the single most common mark loss in wave questions."},
    {"id": "P4", "category": "Intensity", "type": "numeric", "slo": "8.1.3",
     "prompt": "A wave of intensity 8.0 W m^-2 has its amplitude doubled. Enter the new intensity "
               "in W m^-2.",
     "answer": 32.0, "tolerance": 0.2, "unit": "W m⁻²",
     "hint": "Intensity is proportional to the square of the amplitude.",
     "explanation": "32 W m^-2, because 2² = 4 and 8 × 4 = 32."},
    {"id": "P5", "category": "Intensity", "type": "numeric", "slo": "8.1.3",
     "prompt": "A source radiates 60 W uniformly over a sphere of radius 5.0 m. Enter the intensity "
               "in W m^-2. (Use pi = 3.142.)",
     "answer": 0.1909859317102744, "tolerance": 0.005, "unit": "W m⁻²",
     "hint": "Area of a sphere = 4 pi r squared.",
     "explanation": "A = 4 pi (25) = 314.2 m², so I = 60/314.2 = 0.191 W m⁻²."},
    {"id": "P6", "category": "Intensity", "type": "mcq", "slo": "8.1.3",
     "prompt": "The intensity of a point source falls off with distance r as...",
     "options": ["1/r", "1/r²", "1/r³", "it stays constant"], "answer": 1,
     "hint": "The area a sphere presents grows as the square of the radius.",
     "explanation": "I = P/(4 pi r²), so it falls as 1/r². Doubling the distance quarters the "
                    "intensity."},
    {"id": "P7", "category": "Wave equation", "type": "numeric", "slo": "8.1.4",
     "prompt": "A wave has frequency 250 Hz and speed 20 m s^-1. Enter its wavelength in metres.",
     "answer": 0.08, "tolerance": 0.002, "unit": "m",
     "hint": "lambda = v/f.",
     "explanation": "lambda = 20/250 = 0.080 m, that is 8 cm."},
    {"id": "P8", "category": "Wave equation", "type": "numeric", "slo": "8.1.4",
     "prompt": "Sound of frequency 500 Hz has a speed of 340 m s^-1 in air. Enter its wavelength in "
               "metres.",
     "answer": 0.68, "tolerance": 0.005, "unit": "m",
     "hint": "Divide the speed by the frequency.",
     "explanation": "lambda = 340/500 = 0.680 m."},
    {"id": "P9", "category": "Wave equation", "type": "mcq", "slo": "8.1.4",
     "prompt": "A sound wave passes from air into water. Its frequency...",
     "options": ["increases", "decreases", "stays the same", "halves"], "answer": 2,
     "hint": "The frequency is set by the source, not by the medium.",
     "explanation": "Stays the same. The speed changes (upwards) and so the wavelength changes "
                    "(downwards), but the frequency is set by the source and cannot change at a "
                    "boundary. This is why the pitch does not change."},
    {"id": "P10", "category": "Types of wave", "type": "mcq", "slo": "8.2.1",
     "prompt": "Which of these is a transverse wave?",
     "options": ["Sound in air", "Sound in a solid rod", "Ripples on water",
                 "An S-wave in an earthquake"], "answer": 2,
     "hint": "Look for the one where the particles move across the direction of travel.",
     "explanation": "Water ripples are transverse. Sound is longitudinal in every medium, and "
                    "S-waves are longitudinal too. Light is also transverse, but it needs no "
                    "medium at all."},
    {"id": "P11", "category": "Types of wave", "type": "mcq", "slo": "8.2.1",
     "prompt": "Which of these can be polarised?",
     "options": ["Sound in air", "All transverse waves", "Longitudinal waves",
                 "Water pressure waves"], "answer": 1,
     "hint": "Polarisation needs a transverse wave because it involves a direction of vibration.",
     "explanation": "Only transverse waves can be polarised, because polarisation is about the "
                    "plane of vibration, and a longitudinal wave has no such plane."},
    {"id": "P12", "category": "Types of wave", "type": "mcq", "slo": "8.2.2",
     "prompt": "On a longitudinal wave graph, the regions where the particles are pushed closest "
               "together are called...",
     "options": ["crests", "troughs", "compressions", "antinodes"], "answer": 2,
     "hint": "It is the high-pressure region.",
     "explanation": "Compressions, where the particles bunch up and the pressure is highest. "
                    "The sparse low-pressure regions are rarefactions. Crests and troughs "
                    "belong to transverse waves."},
    {"id": "P13", "category": "Superposition", "type": "mcq", "slo": "8.3.1",
     "prompt": "The principle of superposition states that...",
     "options": ["the total energy is conserved",
                 "the resultant displacement is the sum of the individual displacements",
                 "waves cannot overlap", "the frequency of the sum is higher"],
     "answer": 1,
     "hint": "It is about displacement, point by point.",
     "explanation": "At every point, the displacements simply add. It is linear and reversible, "
                    "which is why two overlapping waves emerge unchanged afterwards."},
    {"id": "P14", "category": "Interference", "type": "numeric", "slo": "8.3.2",
     "prompt": "Two waves of wavelength 2.0 m arrive with a path difference of 3.0 m. Is this "
               "constructive or destructive? Enter 1 for constructive, 2 for destructive.",
     "answer": 2, "tolerance": 0, "unit": "",
     "hint": "Path difference = n lambda for constructive, (n + 1/2) lambda for destructive.",
     "explanation": "Destructive, so enter 2. The path difference of 3.0 m is 1.5 wavelengths, "
                    "which is one whole wavelength plus a half \u2014 and the half is what "
                    "matters, because a whole wavelength changes nothing. So the waves arrive "
                    "a half cycle out of step."},
    {"id": "P15", "category": "Interference", "type": "numeric", "slo": "8.3.2",
     "prompt": "Two equal waves of intensity 4.0 W m^-2 each overlap constructively. Enter the "
               "resultant intensity in W m^-2.",
     "answer": 16.0, "tolerance": 0.2, "unit": "W m⁻²",
     "hint": "Displacements add, so intensities add too, but only when in step.",
     "explanation": "16 W m^-2, because the displacements double and intensity goes as the "
                    "square of amplitude: 4 × 2² = 16. This is why a loud bang from two "
                    "sounds in step is disproportionately loud."},
    {"id": "P16", "category": "Interference", "type": "numeric", "slo": "8.3.3",
     "prompt": "Two waves of wavelength 1.0 m have a path difference of 0.25 m. Enter the phase "
               "difference in radians.",
     "answer": 1.5707963267948966, "tolerance": 0.01, "unit": "rad",
     "hint": "Delta phi = 2 pi delta / lambda.",
     "explanation": "Delta phi = 2 pi (0.25)/1.0 = pi/2 = 1.571 rad, which is a quarter cycle. "
                    "Phase difference is always measured in radians."},
    {"id": "P17", "category": "Beats", "type": "numeric", "slo": "8.3.4",
     "prompt": "Two sound waves of 512 Hz and 524 Hz overlap. Enter the beat frequency in Hz.",
     "answer": 12.0, "tolerance": 0.1, "unit": "Hz",
     "hint": "It is the difference of the two frequencies.",
     "explanation": "12 Hz. The interference pattern drifts at 12 cycles per second, so the "
                    "loudness rises and falls twelve times a second."},
    {"id": "P18", "category": "Beats", "type": "numeric", "slo": "8.3.4",
     "prompt": "Two forks produce 8 beats per second. Enter the time between consecutive beats in "
               "seconds.",
     "answer": 0.125, "tolerance": 0.005, "unit": "s",
     "hint": "One beat period is the reciprocal of the beat frequency.",
     "explanation": "0.125 s. Notice this is the same as the period of an 8 Hz oscillation, "
                    "which is the in-step condition repeating."},
    {"id": "P19", "category": "Stationary waves", "type": "mcq", "slo": "8.4.1",
     "prompt": "A node on a stationary wave is a point that...",
     "options": ["oscillates with the greatest amplitude", "never moves at all",
                 "moves at twice the speed of an antinode", "moves at half the amplitude of an antinode"],
     "answer": 1,
     "hint": "Two waves are passing through it in opposite directions.",
     "explanation": "At a node the two component waves are always exactly opposite, so the "
                    "displacement is zero at every instant. An antinode oscillates at twice the "
                    "amplitude, not at a different speed."},
    {"id": "P20", "category": "Stationary waves", "type": "mcq", "slo": "8.4.2",
     "prompt": "Stationary waves are produced when...",
     "options": ["two waves of different frequencies meet", "two identical waves travel in opposite "
                 "directions and superpose", "a wave is reflected at a free end",
                 "two waves meet at right angles"], "answer": 1,
     "hint": "They must be identical and travelling towards each other.",
     "explanation": "Identical waves travelling in opposite directions. A reflection at a fixed "
                    "end does produce them, because the reflected wave runs back along the "
                    "incident wave; at a free end the reflection is inverted."},
    {"id": "P21", "category": "Stationary waves", "type": "numeric", "slo": "8.4.3",
     "prompt": "A string fixed at both ends is 0.60 m long and waves travel at 300 m s^-1. Enter the "
               "fundamental frequency in Hz.",
     "answer": 250.0, "tolerance": 1.0, "unit": "Hz",
     "hint": "The fundamental fits one half wavelength into the length.",
     "explanation": "lambda = 2L = 1.20 m, so f = v/lambda = 300/1.20 = 250 Hz."},
    {"id": "P22", "category": "Stationary waves", "type": "mcq", "slo": "8.4.3",
     "prompt": "Which harmonics exist in an air column closed at one end?",
     "options": ["All of them", "Only the even ones", "Only the odd ones",
                 "Only the fundamental"], "answer": 2,
     "hint": "The closed end forces a node.",
     "explanation": "Only the odd ones. The column must fit an odd number of quarter "
                    "wavelengths, so f = (2n-1)v/4L and the even harmonics simply do not exist. "
                    "That is why a stopped pipe sounds hollow."},
    {"id": "P23", "category": "Doppler", "type": "mcq", "slo": "8.5.1",
     "prompt": "As an ambulance approaches you, its siren sounds...",
     "options": ["lower in pitch", "higher in pitch", "unchanged", "lower in volume"],
     "answer": 1,
     "hint": "The wavefronts are bunching up in front of it.",
     "explanation": "Higher in pitch. The approaching source packs its crests closer together, "
                    "so the wavelength reaching you is shorter and the frequency higher. As it "
                    "recedes the pitch drops."},
    {"id": "P24", "category": "Doppler", "type": "numeric", "slo": "8.5.2",
     "prompt": "A source of 500 Hz moves at 34 m s^-1 directly towards a stationary observer. Take "
               "the speed of sound as 340 m s^-1. Enter the observed frequency in Hz.",
     "answer": 555.5555555555555, "tolerance": 0.5, "unit": "Hz",
     "hint": "Case (b): f' = f v / (v - v_s).",
     "explanation": "500 × 340/(340-34) = 500 × 340/306 = 555.6 Hz. The pitch has risen by "
                    "about 11 %."},
    {"id": "P25", "category": "Doppler", "type": "numeric", "slo": "8.5.3",
     "prompt": "A stationary source of 400 Hz is observed by an observer moving at 34 m s^-1 towards "
               "it. Take the speed of sound as 340 m s^-1. Enter the observed frequency in Hz.",
     "answer": 440.0, "tolerance": 0.5, "unit": "Hz",
     "hint": "Case (a): f' = f (v + v_o) / v.",
     "explanation": "400 × 374/340 = 440 Hz. Compare with P24: the same closing speed gives a "
                    "bigger shift when the source moves than when the observer does, because "
                    "moving the source also changes the wavelength itself."},
    {"id": "P26", "category": "Doppler", "type": "mcq", "slo": "8.5.3",
     "prompt": "A quick check that a Doppler formula has the signs right is to...",
     "options": ["convert to kilometres per hour", "put v_o = v_s = 0 and confirm f' = f",
                 "square both sides", "check the units are hertz"],
     "answer": 1,
     "hint": "If nothing is moving, nothing should change.",
     "explanation": "Setting both speeds to zero must give back f. It takes five seconds and "
                    "catches the most common error in Doppler questions."},
    {"id": "P27", "category": "Doppler in light", "type": "mcq", "slo": "8.5.4",
     "prompt": "A distant galaxy shows a red shift. This means its spectrum...",
     "options": ["is shifted towards shorter wavelengths", "is shifted towards longer wavelengths",
                 "is brighter", "shows no Doppler effect"], "answer": 1,
     "hint": "Red is at the long-wavelength end of the visible spectrum.",
     "explanation": "Longer wavelengths. The galaxy is receding, so the light is stretched. The "
                    "degree of red shift is proportional to distance, which is how the expansion "
                    "of the universe was discovered."},
    {"id": "P28", "category": "Applications", "type": "mcq", "slo": "8.5.5",
     "prompt": "Police radar measures speed because the returned signal has been shifted...",
     "options": ["once", "twice, because the pulse makes a round trip", "not at all",
                 "by half, because of reflection"], "answer": 1,
     "hint": "Count how many times the pulse is Doppler shifted.",
     "explanation": "Twice: once as the pulse reaches the moving car and again as the reflection "
                    "returns. That factor of two is what makes the tiny shift measurable."},
    {"id": "P29", "category": "Modern uses", "type": "mcq", "slo": "8.6.1",
     "prompt": "Ultrasound is used in medicine because sound...",
     "options": ["travels faster than light", "reflects at boundaries between tissues",
                 "cannot be reflected", "travels only in a vacuum"], "answer": 1,
     "hint": "What produces the echo?",
     "explanation": "It reflects at boundaries between tissues of different density. The time "
                    "delay gives the depth, and the strength of the echo tells what the boundary "
                    "is made of."},
    {"id": "P30", "category": "Modern uses", "type": "mcq", "slo": "8.6.1",
     "prompt": "The fact that S-waves do not travel through liquid helped prove that...",
     "options": ["the Earth's core is liquid", "the Earth's core is solid",
                 "the oceans are salty", "earthquakes are predictable"], "answer": 0,
     "hint": "S-waves are transverse and cannot travel through a liquid.",
     "explanation": "The liquid outer core. Since seismic stations everywhere continued to receive "
                    "S-waves, whatever they were travelling through must support transverse waves "
                    "- so it cannot be liquid."},
]


REFERENCES = [
    {"short": "OpenStax College Physics 2e",
     "title": "Chapter 16: Periodic Motion and Chapter 17: Sound",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/college-physics-2e",
     "used_for": "Progressive waves, intensity, interference, beats and the Doppler effect for sound."},
    {"short": "OpenStax University Physics Vol. 1",
     "title": "Chapter 15: Waves and Chapter 16: Sound",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/university-physics-volume-1",
     "used_for": "The mathematical description y = A sin(kx - omega t) and superposition."},
    {"short": "NASA",
     "title": "Doppler effect and the expansion of the universe",
     "org": "NASA",
     "url": "https://www.nasa.gov/",
     "used_for": "Red and blue shift applied to galaxies, and the radial-velocity method."},
    {"short": "NOAA",
     "title": "Doppler weather radar",
     "org": "National Oceanic and Atmospheric Administration",
     "url": "https://www.noaa.gov/",
     "used_for": "How the Doppler shift is used to measure wind speed inside storms."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 8",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 8.1.1 to 8.6.1."},
]
