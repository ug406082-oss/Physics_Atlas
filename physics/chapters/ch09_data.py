"""Chapter 9 content: Physical Optics.

Twenty-eight outcomes across six sections - the widest chapter in the book. Its
instruments are built around a single idea: interference is the same mathematics
every time, so one **interference explorer** serves Young's double slit, the
single slit, the grating and Michelson at once, with the interference path
differences shown explicitly rather than assumed.
"""

from __future__ import annotations

SLOS = [
    {"id": "9.1.1", "text": "Discuss different points of view about nature of light.",
     "simple": "Corpuscular, wave, electromagnetic, quantum - each explained evidence the earlier one could not.",
     "taught": "Theories of light", "activity": "Timeline of theories with what each one fixed",
     "check": "Guided practice: match each theory to the evidence that supported it"},
    {"id": "9.1.2", "text": "Discuss the concept of wave-front.",
     "simple": "A surface joining all the points reached by the wave at the same instant.",
     "taught": "Wavefronts", "activity": "Wavefront construction drawn at successive times",
     "check": "Guided practice: define a wavefront and identify its normal direction"},
    {"id": "9.1.3", "text": "Describe Huygens' principle.",
     "simple": "Every point on a wavefront is itself a source of secondary wavelets.",
     "taught": "Huygens' principle", "activity": "Step-by-step construction with the envelope drawn",
     "check": "Guided practice: apply Huygens' principle to reflection and refraction"},
    {"id": "9.2.1", "text": "Define coherent and monochromatic sources.",
     "simple": "Coherent: constant phase difference. Monochromatic: one wavelength.",
     "taught": "Coherence", "activity": "Same-frequency-but-random-phase comparison",
     "check": "Guided practice: distinguish coherent from merely equal-frequency sources"},
    {"id": "9.2.2", "text": "Define interference of light.",
     "simple": "Superposition of two coherent light waves producing bright and dark fringes.",
     "taught": "Interference", "activity": "Interference explorer with the intensity pattern computed live",
     "check": "Guided practice: define interference and explain why fringes appear"},
    {"id": "9.2.3", "text": "State conditions necessary for interference.",
     "simple": "Coherent sources, same frequency, comparable amplitude.",
     "taught": "Conditions for interference", "activity": "Checklist with a live pass/fail test",
     "check": "Guided practice: state and justify the three conditions"},
    {"id": "9.2.4", "text": "Explain Young's double slit experiment.",
     "simple": "Two slits split light into two coherent beams that interfere to give a fringe pattern.",
     "taught": "Young's experiment", "activity": "Optical arrangement with the two paths and their difference",
     "check": "Guided practice: explain the arrangement and why it proves interference"},
    {"id": "9.2.5", "text": "Derive relation for fringe spacing.",
     "simple": "dy = lambda L / d",
     "taught": "Fringe spacing", "activity": "Three-variable solver with the pattern drawn to scale",
     "check": "Guided practice: derive the fringe spacing and use it"},
    {"id": "9.2.6", "text": "Solve word problems related to fringe spacing.",
     "simple": "Numerical problems on dy, lambda L and d.",
     "taught": "Fringe-spacing problems", "activity": "Problem set with the arrangement drawn on every answer",
     "check": "Guided practice: solve fringe-spacing word problems"},
    {"id": "9.3.1", "text": "Describe construction and working of Michelson's interferometer.",
     "simple": "A beam splitter sends light down two arms and recombines it, so a tiny path change shifts the fringes.",
     "taught": "Michelson's interferometer", "activity": "Optical arrangement with both arms and the path difference",
     "check": "Guided practice: describe the construction and trace the two paths"},
    {"id": "9.3.2", "text": "Describe qualitatively about gravitational waves.",
     "simple": "Ripples in spacetime, predicted by Einstein and detected a century later.",
     "taught": "Gravitational waves", "activity": "Spacetime-rubber-sheet illustration of a binary system",
     "check": "Guided practice: describe gravitational waves qualitatively"},
    {"id": "9.3.3", "text": "State that a gravitational wave passing a mass creates distortion in spacetime.",
     "simple": "A passing wave stretches one direction and squeezes the perpendicular one.",
     "taught": "Spacetime distortion", "activity": "Ring of test masses before, during and after the wave",
     "check": "Guided practice: describe the distortion a wave leaves on a ring of masses"},
    {"id": "9.3.4", "text": "Describe use of interferometers in detecting gravitational waves.",
     "simple": "LIGO splits a laser into two arms 4 km long and measures an arm change of 10^-18 m.",
     "taught": "Detecting gravitational waves", "activity": "Sensitivity comparison across the whole EM spectrum",
     "check": "Guided practice: describe how an interferometer detects such a small change"},
    {"id": "9.4.1", "text": "Define diffraction of light.",
     "simple": "The spreading of light round an obstacle or through an opening, wider for longer wavelengths.",
     "taught": "Diffraction", "activity": "Single-slit pattern with minima marked",
     "check": "Guided practice: define diffraction and state its dependence on wavelength"},
    {"id": "9.4.2", "text": "Describe diffraction by diffraction grating.",
     "simple": "Many equally spaced slits produce sharp, intense principal maxima.",
     "taught": "Diffraction gratings", "activity": "Grating explorer over several orders",
     "check": "Guided practice: explain why a grating gives sharp maxima"},
    {"id": "9.4.3", "text": "Describe diffraction in a narrow slit.",
     "simple": "A central maximum twice as wide as the rest, with minima at a sin(theta) = m lambda.",
     "taught": "Single-slit diffraction", "activity": "Pattern for any slit width, minima labelled",
     "check": "Guided practice: locate the minima and read the central maximum width"},
    {"id": "9.4.4", "text": "Solve word problems related to diffraction.",
     "simple": "Numerical problems on slit width, wavelength and angle.",
     "taught": "Diffraction problems", "activity": "Problem set with the pattern drawn for each answer",
     "check": "Guided practice: solve diffraction word problems"},
    {"id": "9.5.1", "text": "State Bragg's law.",
     "simple": "2 d sin(theta) = m lambda for constructive reflection from crystal planes.",
     "taught": "Bragg's law", "activity": "Layer diagram with the 2d path difference shown",
     "check": "Guided practice: state Bragg's law and identify each term in it"},
    {"id": "9.5.2", "text": "Describe diffraction of X-rays through crystals.",
     "simple": "X-rays reflect off the atomic planes, and the pattern reveals the arrangement.",
     "taught": "X-ray diffraction", "activity": "Crystal-lattice diagram with the beam path traced",
     "check": "Guided practice: describe X-ray diffraction and what it reveals"},
    {"id": "9.5.3", "text": "Derive equation 2d sin(theta) = m lambda.",
     "simple": "The extra path the lower ray travels is 2d sin(theta), and constructive reflection needs m lambda.",
     "taught": "Deriving Bragg's law", "activity": "Derivation stepper with the geometry highlighted",
     "check": "Guided practice: derive the equation from the path difference"},
    {"id": "9.5.4", "text": "Solve word problems related to Bragg's law.",
     "simple": "Numerical problems on d, theta, lambda and the order m.",
     "taught": "Bragg problems", "activity": "Calculator with the plane spacing, angle and order all solved",
     "check": "Guided practice: solve Bragg's-law word problems"},
    {"id": "9.6.1", "text": "Describe unpolarised and polarised light.",
     "simple": "Unpolarised vibrates in every plane; polarised vibrates in one plane only.",
     "taught": "Polarisation", "activity": "Side-by-side vibration diagrams",
     "check": "Guided practice: distinguish polarised from unpolarised light"},
    {"id": "9.6.2", "text": "Explain polarisation with reference to transverse waves.",
     "simple": "Only transverse waves can be polarised, because they have a plane of vibration.",
     "taught": "Why only transverse waves", "activity": "Transverse and longitudinal compared for polarisability",
     "check": "Guided practice: explain why longitudinal waves cannot be polarised"},
    {"id": "9.6.3", "text": "Explain polarisation by reflection.",
     "simple": "At Brewster's angle the reflected light is completely plane-polarised.",
     "taught": "Polarisation by reflection", "activity": "Brewster angle diagram with the two rays at right angles",
     "check": "Guided practice: explain reflection polarisation and calculate the angle"},
    {"id": "9.6.4", "text": "Explain polarisation by a polaroid.",
     "simple": "A polaroid passes only the component along its transmission axis.",
     "taught": "Polaroid", "activity": "Wave through crossed polarisers with the surviving component shown",
     "check": "Guided practice: explain polaroid action and the three-polariser result"},
    {"id": "9.6.5", "text": "State Malus's law.",
     "simple": "I = I_0 cos^2(theta)",
     "taught": "Malus's law", "activity": "cos-squared curve with the transmission axis drawn",
     "check": "Guided practice: state and apply Malus's law"},
    {"id": "9.6.6", "text": "Solve word problems related to Malus's law.",
     "simple": "Numerical problems on the transmitted intensity at any angle.",
     "taught": "Malus problems", "activity": "Problem set with the percentage transmitted on every answer",
     "check": "Guided practice: solve Malus's-law word problems"},
    {"id": "9.6.7", "text": "Describe applications of polarisation in daily life.",
     "simple": "Sunglasses, photography, LCD screens and 3-D films all use it.",
     "taught": "Applications of polarisation", "activity": "Application table with the exploited property named",
     "check": "Guided practice: explain each application in terms of polarisation"},
]

STATIONS = [
    {"key": "overview", "label": "\U0001F5FA\uFE0F Your route & outcomes", "slos": []},
    {"key": "nature", "label": "\u2728 The nature of light", "slos": ["9.1.1", "9.1.2", "9.1.3"]},
    {"key": "conditions", "label": "\uD83E\uDDEA Coherence & conditions", "slos": ["9.2.1", "9.2.2", "9.2.3"]},
    {"key": "young", "label": "\uD83D\uDD2C Young's double slit", "slos": ["9.2.4", "9.2.5", "9.2.6"]},
    {"key": "michelson", "label": "\uD83D\uDD53 Michelson & gravitational waves", "slos": ["9.3.1", "9.3.2", "9.3.3", "9.3.4"]},
    {"key": "diffraction", "label": "\uD83D\uDC2F Diffraction & gratings", "slos": ["9.4.1", "9.4.2", "9.4.3", "9.4.4"]},
    {"key": "bragg", "label": "\uD83D\uDC8E Bragg's law & X-rays", "slos": ["9.5.1", "9.5.2", "9.5.3", "9.5.4"]},
    {"key": "polarisation", "label": "\uD83D\uDC76 Polarisation", "slos": ["9.6.1", "9.6.2", "9.6.3", "9.6.4"]},
    {"key": "malus", "label": "\uD83D\uDD2C Malus's law", "slos": ["9.6.5", "9.6.6"]},
    {"key": "uses", "label": "\uD83C\uDF0D Applications of polarisation", "slos": ["9.6.7"]},
    {"key": "worked", "label": "\uD83E\uDDEE Worked problems", "slos": []},
    {"key": "practice", "label": "\uD83E\uDDE0 Practice", "slos": []},
    {"key": "tutor", "label": "\uD83E\uDD16 Atlas Tutor (offline AI)", "slos": []},
    {"key": "references", "label": "\uD83D\uDCDA References", "slos": []},
]

BIG_IDEAS = [
    ("One piece of arithmetic runs through the whole chapter.",
     "bright when the path difference is m lambda, dark when it is (m + 1/2) lambda. Young's "
     "slits, a single slit, a grating, Michelson and X-ray diffraction are the same rule with "
     "different geometry in front of it."),
    ("Diffraction is unavoidable.",
     "Any opening has a finite width, so every experiment in this chapter has a blurred "
     "background under the fringes. Interference is the pattern; diffraction is the blur."),
    ("Polarity is a geometric fact, not a quantum one.",
     "Malus's law is cos squared because a polaroid passes a projection, not because "
     "anything is being absorbed selectively by some deep mechanism."),
]

TAG = "CHAPTER 9 \u00B7 OPEN"
INTRO = (
    "Twenty-eight outcomes and six sections \u2014 the longest chapter in the book, and the one "
    "where the mathematics is actually the easiest. Strip away the apparatus and every "
    "experiment here asks the same question: what is the path difference between two rays, and "
    "is it a whole number of wavelengths? There is one interference explorer that answers it "
    "for Young's slits, a single slit, a grating and Michelson alike."
)
ROUTE = ("The nature of light \u2192 Coherence \u2192 Young's double slit \u2192 Michelson and "
         "gravitational waves \u2192 Diffraction and gratings \u2192 Bragg's law \u2192 "
         "Polarisation \u2192 Malus's law \u2192 Applications \u2192 Worked problems \u2192 Practice.")
HONESTY_PILLS = [("Established scientific definitions", "info"),
                 ("Typical rather than certified values", "warn"),
                 ("Fringe patterns drawn from the formulas", "mute"),
                 ("Every trace computed by this app", "good")]

NOTES = [
    ("\u26A0 WATCH OUT", "A wave needs two coherent sources, not just two of the same frequency",
     "Two sodium lamps at the same frequency are still not coherent, because their phase "
     "difference wanders thousands of times a second, so any pattern is smeared into a uniform "
     "glow within a fraction of a second. That is why Young used two slits cut from the "
     "**same** wavefront."),
    ("\uD83C\uDFAF EXAM TIP", "Find the path difference before you touch a formula",
     "In every experiment in this chapter, draw the two rays and label the extra distance. "
     "If that extra distance is 1.5 lambda, the answer is dark, and no amount of arithmetic "
     "will change that."),
    ("\uD83D\uDD2E HONEST LIMIT", "Fringes drawn here are computed, not photographed",
     "Real patterns carry a diffraction envelope, imperfect coherence, polarisation leakage "
     "and detector noise. The curves in this chapter are computed from the ideal formulas so "
     "the structure is clear; a real double slit looks messier and more beautiful."),
]


# --------------------------------------------------------------------------
# 9.1  Nature of light
# --------------------------------------------------------------------------

LIGHT_THEORIES = [
    {"theory": "Newton's corpuscular theory (1672)",
     "claim": "Light is a stream of tiny particles.",
     "explained": "Straight-line travel and sharp shadows, why the speed is higher in a denser "
                  "medium, and reflection.",
     "failed_for": "Interference, diffraction, and why light bends the wrong way into water.",
     "verdict": "Necessarily wrong as a complete account, but not entirely without cause."},
    {"theory": "Huygens' wave theory (1678)",
     "claim": "Light is a wave in a continuous medium called the aether.",
     "explained": "Interference, diffraction and refraction, and the wavefront construction.",
     "failed_for": "Light travels perfectly well through a vacuum, where there is supposed to "
                   "be no aether.",
     "verdict": "Right about the physics, wrong about the medium."},
    {"theory": "Maxwell's electromagnetic theory (1864)",
     "claim": "Light is an electromagnetic wave needing no medium at all.",
     "explained": "The speed of light from electric and magnetic constants, the whole spectrum "
                  "including radio waves, and how light is produced and absorbed.",
     "failed_for": "It says nothing about light behaving as particles.",
     "verdict": "The correct classical description of light in transit."},
    {"theory": "Einstein's quantum theory (1905)",
     "claim": "Light is exchanged in packets called photons, each carrying energy hf.",
     "explained": "The photoelectric effect, where electrons are ejected only when the "
                  "frequency is high enough however weak the beam.",
     "failed_for": "Photons are not localised lumps travelling as little balls.",
     "verdict": "Necessary for detection, and it does not contradict Maxwell."},
    {"theory": "Wave-particle duality (today)",
     "claim": "Light is neither picture alone; quantum electrodynamics treats it as a "
              "quantum field whose excitations are photons.",
     "explained": "Interference appears in detection events one photon at a time, and the "
                  "pattern builds up photon by photon.",
     "failed_for": "Nothing — because the point is that both pictures are limits of one theory.",
     "verdict": "The modern position. 'Which is it?' is the wrong question to ask."},
]

HUYGENS_STEPS = [
    "Every point on a wavefront acts as a source of a new, tiny secondary wavelet.",
    "Each of those wavelets spreads out in all directions at the speed of the wave in that "
    "medium.",
    "After a short time, draw the new wavefront as the **envelope** that just touches all the "
    "secondary wavelets - the common tangent to the lot of them.",
    "The direction of that envelope is the new direction of travel, so the wavefront bends "
    "wherever it enters a new medium.",
]

HUYGENS_CONSEQUENCES = [
    {"application": "Reflection",
     "how": "The secondary wavelets from a mirror are all reflected back; their envelope runs "
            "back along the incident direction at the same angle.",
     "why": "Because every wavelet obeys the same law of reflection."},
    {"application": "Refraction",
     "how": "Wavelets in the new medium travel more slowly, so the envelope leans towards the "
            "normal.",
     "why": "Because the envelope must touch wavelets from all the old wavefront, which are now "
            "spreading at different speeds."},
    {"application": "Why a straight-edged object casts a shadow with a sharp edge",
     "how": "Only the wavelets from the un-obstructed part of the wavefront reach the screen, "
            "so the envelope stops short at the object's outline.",
     "why": "Because the envelope can only be built from wavelets that are not blocked."},
]

WAVEFRONT_NOTES = [
    {"question": "What exactly is a wavefront?",
     "answer": "A surface joining all the points reached by the wave at the same instant. In "
               "two dimensions you would draw it as a line; in three dimensions it is a "
               "surface."},
    {"question": "Which way does it travel?",
     "answer": "Always **normal** (perpendicular) to itself, at every point on it."},
    {"question": "How are circular wavefronts made?",
     "answer": "By dropping a pebble in at a point. The wavefronts are circles whose radius is "
               "the distance travelled, and their spacing shrinks as energy spreads out."},
    {"question": "How are straight wavefronts made?",
     "answer": "By a plane source such as a distant loudspeaker or a slit. The wavefronts are "
               "effectively parallel planes."},
]

COHERENCE_POINTS = [
    {"point": "Two sources at the same frequency are not enough",
     "detail": "Coherence needs a **constant** phase difference. Two ordinary lamps at the same "
               "frequency drift in and out of step many times a second, so any pattern is "
               "averaged away into a uniform glow."},
    {"point": "How to get true coherence",
     "detail": "Split **one** wavefront into two. Both parts then come from the same source "
               "and keep a fixed relationship. Young's two slits do exactly this."},
    {"point": "Coherence length",
     "detail": "Real sources have a finite coherence length - the path difference over which "
               "they stay coherent. It is long for a laser and very short for an incandescent "
               "bulb."},
    {"point": "Monochromatic means one wavelength",
     "detail": "'Mono-' (single) + 'chromatic' (colour). A monochromatic source emits one "
               "wavelength, so the fringes are clean. A white source gives a coloured fringe "
               "that is washed out unless the path difference is small."},
]

INTERFERENCE_CONDITIONS = [
    {"condition": "Coherent sources",
     "why": "Without a fixed phase difference the fringes move far faster than the eye can "
            "follow and average out to nothing.",
     "how": "Derive both beams from the same original wavefront."},
    {"condition": "Same (or nearly same) frequency",
     "why": "If the frequencies differ, the pattern is not stationary; it sweeps across the "
            "screen and blurs.",
     "how": "Use two slits in the same screen, or two lines in a single grating."},
    {"condition": "Comparable amplitude",
     "why": "If one beam is far stronger, the minima never reach zero and the fringes are faint "
            "and shallow.",
     "how": "Illuminate the two slits equally."},
    {"condition": "Path difference within the coherence length",
     "why": "Light scattered on the way from the source destroys the phase relationship over "
            "long distances.",
     "how": "Use a laser, and keep the arrangement compact."},
]

YOUNG_POINTS = [
    {"point": "Thomas Young, 1801, and it settled the argument",
     "detail": "He showed that light does interfere. Because this could not be explained by "
               "Newton's corpuscles, it was the first strong evidence for the wave nature of "
               "light."},
    {"point": "A single narrow source first",
     "detail": "A lit slit S provides a clean, single wavefront. Without it you would be "
               "adding two unrelated lamps, which do not interfere."},
    {"point": "The two slits are very close together",
     "detail": "Separated by a fraction of a millimetre, so the path difference to any point on "
               "the distant screen is small enough for the fringes to be visible."},
    {"point": "The screen must be far away",
     "detail": "At distance L the small angle approximation holds well, which is what lets the "
               "simple formula dy = lambda L / d work."},
    {"point": "White light gives coloured fringes",
     "detail": "Red fringes are furthest apart and blue closest, because dy is proportional to "
               "lambda. The central fringe is white, because there every wavelength is in step."},
]

FRINGE_NOTES = [
    {"quantity": "Fringe spacing dy", "formula": "dy = lambda L / d",
     "note": "Proportional to lambda and L, and inversely proportional to the slit separation d."},
    {"quantity": "Bright fringes", "formula": "y = n lambda L / d",
     "note": "n = 0, 1, 2, ... The zeroth is the central white (or bright) fringe."},
    {"quantity": "Dark fringes", "formula": "y = (n + 1/2) lambda L / d",
     "note": "They fall exactly halfway between the bright ones."},
    {"quantity": "Number of fringes across the screen",
     "formula": "N = width of screen / dy",
     "note": "The pattern is centred on the central fringe and fades towards the edges."},
]

MICHELSON_POINTS = [
    {"point": "The beam splitter",
     "detail": "A half-silvered mirror at 45 degrees. It transmits half the beam and reflects "
               "half, so two copies of the same light are made \u2014 perfectly coherent."},
    {"point": "The two arms",
     "detail": "One arm holds a fixed mirror, the other a mirror on a movable carriage. The "
               "movable mirror is the whole instrument: moving it changes the path length by "
               "twice the movement."},
    {"point": "Why the path changes by twice the movement",
     "detail": "The light travels out along the moving arm **and** back along it, so the "
               "round trip grows by 2x when the mirror moves x."},
    {"point": "Recombination",
     "detail": "The returning beams overlap at the beam splitter and interfere. The observer "
               "sees a circular fringe pattern, like contour lines on a map."},
    {"point": "One fringe per half a wavelength of movement",
     "detail": "Moving the mirror by lambda/2 shifts the path by a whole wavelength and one "
               "fringe passes the centre. This gives an enormously sensitive length measure."},
    {"point": "The null result",
     "detail": "Michelson and Morley looked for the 'ether wind' by comparing the round-trip "
               "times along the two arms. They found none \u2014 and that null result was one "
               "of the two pillars of special relativity."},
]

GRAVITATIONAL_NOTES = [
    {"point": "Predicted before it was ever detected",
     "detail": "Einstein's general relativity, published in 1915, predicted that accelerating "
               "mass would ripple through spacetime itself. Einstein himself doubted the "
               "measurement could ever be made."},
    {"point": "Not electromagnetic at all",
     "detail": "They are oscillations of spacetime, so they pass straight through matter "
               "without being absorbed or scattered. Electromagnetic waves cannot."},
    {"point": "Extremely weak",
     "detail": "Each passing wave changes a length by a part in 10^21. That is why the "
               "instruments are 4 km long and why the discovery took a century."},
    {"point": "What passes a mass does to it",
     "detail": "A wave stretches spacetime in one direction and squeezes it in the "
               "perpendicular direction, alternately, as it passes."},
    {"point": "Detected in 2015",
     "detail": "LIGO reported the merger of two black holes whose final oscillation lasted a "
               "third of a second and squeezed and stretched the 4 km arms."},
]

INTERFEROMETER_SENSITIVITY = [
    {"length": "separation between the nuclei in a crystal", "value": "1e-10 m",
     "note": "measured by X-ray diffraction"},
    {"length": "wavelength of visible light", "value": "5e-7 m", "note": "measured by interferometry"},
    {"length": "thickness of a human hair", "value": "7e-5 m", "note": "measured with a ruler"},
    {"length": "change in the LIGO arms from a passing wave", "value": "1e-18 m",
     "note": "a thousand billion billion times smaller than a proton radius"},
]

SINGLE_SLIT_NOTES = [
    {"feature": "Central maximum", "width": "2 lambda L / a",
     "note": "Twice as wide as every other bright band, because it is bounded by minima on "
             "both sides rather than by maxima."},
    {"feature": "Minima", "condition": "a sin(theta) = m lambda, m = 1, 2, 3, ...",
     "note": "There is **no** minimum at m = 0; the centre is the brightest point."},
    {"feature": "Secondary maxima", "condition": "approximately tan(theta) = (2m + 1) lambda / a",
     "note": "Far weaker than the central maximum, and close to the geometric minima."},
    {"feature": "Dependence", "condition": "wider for longer lambda, wider for narrower slit",
     "note": "Diffraction is unavoidable: every slit has a finite width, so every interference "
             "pattern sits on a blurred single-slit envelope."},
]

GRATING_NOTES = [
    {"point": "What a grating is",
     "detail": "Many thousands of equally spaced parallel slits, ruled or etched on glass. "
               "Typical gratings have around 5000 lines per millimetre."},
    {"point": "Why the maxima are sharp",
     "detail": "The maxima come from thousands of wavelets arriving in step. Away from that exact "
               "angle they scatter, so a grating separates wavelengths far better than a "
               "prism or a single slit."},
    {"point": "The grating equation",
     "detail": "d sin(theta) = m lambda, where d is the spacing between adjacent slits."},
    {"point": "Maximum order",
     "detail": "Only orders with m lambda <= d exist at all, because sin(theta) cannot exceed 1. "
               "Once m lambda > d the order simply is not there."},
    {"point": "Resolving power",
     "detail": "R = lambda / d(lambda) = m N. A grating with N lines resolves wavelengths "
               "differing by about 1/(mN) of their mean value."},
    {"point": "Where you meet them",
     "detail": "Spectrometers, CD and DVD players (a laser diode is chosen so the track pitch "
               "is a multiple of its wavelength), and astronomical spectrographs."},
]

BRAGG_GEOMETRY = [
    {"step": "1. Two rays leave the same point and reflect from the upper plane",
     "detail": "They leave in the same direction, so ray 1 simply grazes along the surface "
               "while ray 2 goes down to the next plane."},
    {"step": "2. Ray 2 travels an extra distance across the gap",
     "detail": "That extra length is **2 d sin(theta)**, where d is the plane spacing and theta "
               "is the glancing angle to the plane."},
    {"step": "3. For the reflections to add, that extra distance must be a whole wavelength",
     "detail": "Otherwise a crest lands on a trough and the two beams partially cancel, so the "
               "reflection is weak."},
    {"step": "4. That gives Bragg's law",
     "detail": "**2 d sin(theta) = m lambda**, with m = 1, 2, 3, ... the order of reflection."},
    {"step": "5. Note that theta is the glancing angle",
     "detail": "It is measured between the beam and the crystal *plane*, not the normal. That is "
               "why detectors are described as working at 2 theta, the angle between the "
               "incident and reflected beams."},
]

POLARISATION_TYPES = [
    {"type": "Unpolarised",
     "vibration": "in every possible plane at once",
     "appearance": "Looks bright from every direction",
     "note": "Ordinary light. Each photon is individually polarised, but the direction changes "
             "so fast that the average over any short interval is completely random."},
    {"type": "Plane-polarised",
     "vibration": "in one single plane",
     "appearance": "Bright from one direction and dark from the perpendicular one",
     "note": "Produced by a polaroid, by reflection at Brewster's angle, and by scattering at "
             "90 degrees."},
    {"type": "Circularly polarised",
     "vibration": "rotating steadily, tracing out a helix",
     "appearance": "Rotates if you turn a linear polaroid in front of your eye",
     "note": "Made by combining two plane-polarised beams at right angles and a quarter-cycle "
             "phase difference."},
    {"type": "Partially polarised",
     "vibration": "mostly in one plane, partly in all",
     "appearance": "Between fully polarised and unpolarised",
     "note": "Anything short of ideal, including most real polarisation experiments."},
]

POLARISATION_USES = [
    {"application": "Sunglasses",
     "how": "A sheet of stretched plastic that filters one plane, or a sheeting that reflects "
            "glare off a horizontal surface.",
     "why": "Glare from a road, water or a windscreen is mostly polarised, so it is blocked, "
            "while light scattered by the objects you want to see is much less so."},
    {"application": "Photography",
     "how": "A circular polariser screwed onto the lens.",
     "why": "It darkens blue skies and cuts reflections from leaves and wet stone, which is why "
            "a polariser is the first accessory many photographers buy."},
    {"application": "LCD screens",
     "how": "Two polarisers with a liquid crystal layer between them. The crystal rotates the "
            "polarisation by an amount set by the voltage across each pixel.",
     "why": "Changing the angle changes how much light passes the second polariser, so each "
            "pixel becomes a controllable dimmer."},
    {"application": "Three-dimensional films",
     "how": "Two images projected through polarisers at right angles; each eye sees one through "
            "its own polariser.",
     "why": "Each eye receives a different image, and the brain reads the pair as depth. "
            "Ordinary glasses would cancel the effect, so 3-D spectacles are polarised too."},
    {"application": "Stress analysis",
     "how": "Photoelasticity: a transparent plastic loaded in tension shows coloured fringes.",
     "why": "The strain changes the refractive index differently along two directions, so the "
            "material becomes a temporary analyser and fringes appear along the stress lines."},
]


# --------------------------------------------------------------------------
# Worked problems
# --------------------------------------------------------------------------

WORKED_PROBLEMS = [
    {"id": "WP1", "title": "Young's double slit - finding the wavelength",
     "level": "Foundation", "slos": ["9.2.5", "9.2.6"],
     "question": "In Young's experiment the slits are 0.50 mm apart and the screen is 1.20 m away. "
                 "The second bright fringe is 1.32 mm from the centre. Find the wavelength of light used.",
     "known": ["slit separation d = 0.50 mm = 5.0 x 10^-4 m",
               "screen distance L = 1.20 m",
               "bright fringe order n = 2, so y = 2 lambda L / d",
               "y = 1.32 mm = 1.32 x 10^-3 m"],
     "find": "the wavelength lambda",
     "equation": r"\lambda = \frac{y\,d}{n\,L}",
     "conversions": ["Both d and y are in millimetres and must be converted to metres. Getting "
                     "the slit separation wrong by a factor of a thousand is the standard slip."],
     "substitution": r"\lambda = \frac{(1.32\times10^{-3})(5.0\times10^{-4})}{2(1.20)}",
     "calculation": [
         "Step 1 \u2014 rearrange the bright-fringe condition y = n lambda L / d to give "
         "lambda = y d / (n L).",
         "Step 2 \u2014 substitute: lambda = (1.32e-3 x 5.0e-4) / (2 x 1.20) = 6.60e-7 / 2.40.",
         "Step 3 \u2014 lambda = 2.75 x 10^-7 m = 275 nm.",
         "Step 4 \u2014 is that plausible? The visible range is about 380 to 750 nm, so 275 nm "
         "is in the **ultraviolet**, and the experiment would have produced no visible fringes at all. "
         "A real examiner would have chosen numbers giving a visible answer, so this one is a "
         "check on the method rather than a realistic setup.",
         "Step 5 \u2014 the method is sound: to get a visible answer with these d and L, the "
         "second fringe would have to be at about 2.4 mm, not 1.32 mm.",
     ],
     "unit_check": r"\lambda = \frac{[L][L]}{[L]} = [L] = \mathrm{m}",
     "answer": "lambda = 2.75 x 10^-7 m (275 nm, i.e. ultraviolet)",
     "sig_fig_note": "All values are to two or three significant figures, so lambda = 2.8 x 10^-7 m.",
     "assumptions": ["The small-angle approximation holds: the fringe is 1.1 mm away on a screen "
                     "1.2 m distant, so the angle is about 0.05 degrees.",
                     "The slit separation is measured centre-to-centre."]},
    {"id": "WP2", "title": "Single-slit diffraction",
     "level": "Developing", "slos": ["9.4.3", "9.4.4"],
     "question": "Light of wavelength 600 nm passes through a slit 0.20 mm wide. Find the angle of "
                 "the first minimum, and the angular width of the central maximum.",
     "known": ["lambda = 600 nm = 6.0 x 10^-7 m", "slit width a = 0.20 mm = 2.0 x 10^-4 m",
               "Minima satisfy a sin(theta) = m lambda"],
     "find": "the angle of the first minimum, and the width of the central maximum",
     "equation": r"a\sin\theta = m\lambda, \qquad \text{width of central max} = \frac{2\lambda}{a}",
     "conversions": ["The wavelength is in nanometres and the slit in millimetres; both must "
                     "become metres before they are combined."],
     "substitution": r"\sin\theta_1 = \frac{1(6.0\times10^{-7})}{2.0\times10^{-4}} = 3.0\times10^{-3}",
     "calculation": [
         "Step 1 \u2014 first minimum, m = 1: sin(theta) = 6.0e-7/2.0e-4 = 3.0e-3.",
         "Step 2 \u2014 theta = arcsin(3.0e-3) = 0.172 degrees.",
         "Step 3 \u2014 the central maximum runs from the first minimum on one side to the "
         "first minimum on the other, so its angular width is **twice** that: 0.344 degrees.",
         "Step 4 \u2014 check with the width formula: 2 lambda / a = 2 x 6.0e-7 / 2.0e-4 = "
         "6.0e-3, and arcsin(6.0e-3) = 0.344 degrees. The two agree.",
         "Step 5 \u2014 note there is **no** minimum at m = 0. The centre is the brightest point, "
         "and that is why the central maximum is special.",
     ],
     "unit_check": r"\sin\theta = \frac{[L]}{[L]} \quad\text{dimensionless, as required}",
     "answer": "First minimum at 0.172 degrees; central maximum 0.344 degrees wide",
     "sig_fig_note": "Two significant figures throughout, so 0.17 degrees and 0.34 degrees.",
     "assumptions": ["The slit is illuminated uniformly across its width.",
                     "There is no refractive medium between the slit and the screen."]},
    {"id": "WP3", "title": "Bragg diffraction from a crystal",
     "level": "Challenge", "slos": ["9.5.3", "9.5.4"],
     "question": "X-rays of wavelength 154 pm are reflected from a crystal whose planes are 564 pm "
                 "apart. Calculate the glancing angle for first and second order reflection.",
     "known": ["lambda = 154 pm = 1.54 x 10^-10 m",
               "d = 564 pm = 5.64 x 10^-10 m",
               "Bragg's law: 2 d sin(theta) = m lambda"],
     "find": "theta for m = 1 and m = 2",
     "equation": r"\sin\theta = \frac{m\lambda}{2d}",
     "conversions": ["Picometres must be converted to metres. 1 pm = 1e-12 m."],
     "substitution": r"\sin\theta_1 = \frac{1.54\times10^{-10}}{2(5.64\times10^{-10})} = 0.1365",
     "calculation": [
         "Step 1 \u2014 first order: sin(theta) = lambda/(2d) = 1.54e-10/1.128e-9 = 0.1365.",
         "Step 2 \u2014 theta = arcsin(0.1365) = 7.85 degrees.",
         "Step 3 \u2014 second order: sin(theta) = 2(0.1365) = 0.2730, so theta = 15.84 degrees.",
         "Step 4 \u2014 fourth order would need sin(theta) = 4(0.1365) = 0.546, which is fine, but "
         "fifth order needs 0.683, sixth needs 0.819, and a **seventh** would need 0.9555 - "
         "just possible. An eighth would need 1.092, impossible since sin cannot exceed 1.",
         "Step 5 \u2014 that maximum order is a useful sanity check in any Bragg problem: "
         "m lambda <= 2 d, or the order simply does not exist.",
         "Step 6 \u2014 detectors are quoted at **2 theta**, so the first peak in a sodium chloride "
         "pattern appears at about 15.7 degrees - which is the familiar published value.",
     ],
     "unit_check": r"\sin\theta = \frac{[L]}{[L]} \quad\text{dimensionless}",
     "answer": "theta = 7.85 degrees for m = 1 and 15.84 degrees for m = 2",
     "sig_fig_note": "The wavelengths and spacing are to three figures, so the angles are quoted to three.",
     "assumptions": ["Bragg's law is satisfied exactly, as it is for a perfect crystal.",
                     "The angle is measured to the plane, not the normal."]},
    {"id": "WP4", "title": "Malus's law and crossed polarisers",
     "level": "Developing", "slos": ["9.6.5", "9.6.6"],
     "question": "Unpolarised light of intensity 400 W m^-2 passes through a polaroid and then "
                 "through a second polaroid whose axis is at 60 degrees to the first. Find the "
                 "intensity after each stage.",
     "known": ["I_0 = 400 W m^-2, unpolarised",
               "The first polaroid passes half of unpolarised light",
               "Malus's law: I = I_after_first cos^2(theta)",
               "theta = 60 degrees, so cos^2(60 degrees) = 0.25"],
     "find": "I after the first polaroid, and after the second",
     "equation": r"I = I_1\cos^2\theta, \qquad I_1 = \frac{I_0}{2}",
     "conversions": ["No unit conversion is needed; intensities stay in W m^-2."],
     "substitution": r"I = 400 \times \frac{1}{2} \times \cos^2 60^\circ = 200 \times 0.25",
     "calculation": [
         "Step 1 \u2014 the first polaroid passes exactly half the unpolarised intensity: "
         "I_1 = 400/2 = 200 W m^-2.",
         "Step 2 \u2014 apply Malus's law at 60 degrees: I = 200 x 0.25 = 50 W m^-2.",
         "Step 3 \u2014 the two steps are genuinely different and both are needed. The half comes "
         "from unpolarised input; the cos squared comes from the angle.",
         "Step 4 \u2014 a trap to avoid: dropping the cos squared would give 200 W m^-2, ten "
         "times too much. Malus's law only applies to **already polarised** light.",
         "Step 5 \u2014 note that the final intensity, 50 W m^-2, is an **eighth** of the "
         "original: half through the first polaroid, then a quarter through the second.",
     ],
     "unit_check": r"I = [M L^{-2} T^{-3}] = \mathrm{W\,m^{-2}}; \ \cos^2\theta \text{ is dimensionless}",
     "answer": "I = 200 W m^-2 after the first polaroid, 50 W m^-2 after the second",
     "sig_fig_note": "Three significant figures throughout, so 200 and 50 W m^-2.",
     "assumptions": ["The polaroids are ideal, with perfect transmission along their axis and "
                     "perfect absorption perpendicular to it.",
                     "The light reaching the second polaroid really is fully polarised."]},
    {"id": "WP5", "title": "Why an interferometer can see a gravitational wave",
     "level": "Challenge", "slos": ["9.3.1", "9.3.4"],
     "question": "An interferometer has two arms each 4.0 km long. A change in length of 1.0 x 10^-18 m "
                 "occurs in one arm. How many fringes does that produce, and what strain does it "
                 "correspond to?",
     "known": ["arm length L = 4.0 km = 4.0 x 10^3 m",
               "change in length dL = 1.0 x 10^-18 m",
               "One fringe passes for every lambda/2 of mirror movement"],
     "find": "the number of fringes, and the strain",
     "equation": r"N = \frac{2\,dL}{\lambda}, \qquad \text{strain} = \frac{dL}{L}",
     "conversions": ["The arm length must be in metres to compare with the change in length."],
     "substitution": r"N = \frac{2(1.0\times10^{-18})}{1.064\times10^{-6}}, \qquad "
                     r"\text{strain} = \frac{1.0\times10^{-18}}{4.0\times10^{3}}",
     "calculation": [
         "Step 1 \u2014 the mirror moves by dL/2 because the light makes the round trip: "
         "N = 2(1.0e-18)/1.064e-6 = 1.88 x 10^-12 fringes.",
         "Step 2 \u2014 that is a very small number of fringes, but a few thousandths of a "
         "fringe is detectable if the laser light is stable enough.",
         "Step 3 \u2014 strain: dL/L = 1.0e-18 / 4.0e3 = 2.5 x 10^-22.",
         "Step 4 \u2014 that is a part in 4 x 10^21. For comparison, a proton is about "
         "10^-15 m across, so the arm length changes by roughly a million billionth of a "
         "proton radius.",
         "Step 5 \u2014 why the arms are 4 km long: the requirement scales directly with length. "
         "Shorter arms would need proportionally larger strain to give the same signal, and "
         "nothing can provide that.",
     ],
     "unit_check": r"\text{strain} = \frac{[L]}{[L]} \text{ is dimensionless, as it must be}",
     "answer": "About 1.9 x 10^-12 fringes, corresponding to a strain of 2.5 x 10^-22",
     "sig_fig_note": "One significant figure each, since 1.0 x 10^-18 m is itself only known to that precision.",
     "assumptions": ["The wavelength used is 1064 nm (the LIGO laser).",
                     "The strain is uniform along the arm, which it effectively is for a wave "
                     "whose wavelength is far longer than the arm."]},
]

# --------------------------------------------------------------------------
# Practice questions
# --------------------------------------------------------------------------

PRACTICE_QUESTIONS = [
    {"id": "Q1", "category": "Nature of light", "type": "mcq", "slo": "9.1.1",
     "prompt": "Which observation forced Newton to abandon a purely corpuscular account of light?",
     "options": ["Straight-line travel", "Sharp shadows", "Interference",
                 "Reflection from a mirror"], "answer": 2,
     "hint": "Which of these can particles not do?",
     "explanation": "Particles passing through one another cannot produce bright and dark bands. "
                    "Newton's corpuscular theory explained straight lines, shadows and reflection "
                    "well but could not explain interference or diffraction."},
    {"id": "Q2", "category": "Nature of light", "type": "mcq", "slo": "9.1.1",
     "prompt": "Young's double-slit experiment was important because it...",
     "options": ["measured the speed of light", "gave the first strong evidence for the wave "
                 "nature of light", "discovered infrared radiation",
                 "proved light is a particle stream"], "answer": 1,
     "hint": "It settled a long-running argument.",
     "explanation": "It produced a clear interference pattern, which corpuscular theory cannot "
                    "explain. That was the first convincing evidence for the wave nature of light."},
    {"id": "Q3", "category": "Wavefronts", "type": "mcq", "slo": "9.1.2",
     "prompt": "A wavefront travels...",
     "options": ["parallel to its own surface at every point",
                 "perpendicular to itself at every point", "along the direction of the source",
                 "only in straight lines"], "answer": 1,
     "hint": "Think of the normal to a circle.",
     "explanation": "Always normal to itself at every point. For a circular wavefront from a "
                    "point source the wave therefore spreads out radially."},
    {"id": "Q4", "category": "Huygens", "type": "mcq", "slo": "9.1.3",
     "prompt": "Huygens' principle states that...",
     "options": ["light travels in straight lines", "every point on a wavefront acts as a source "
                 "of secondary wavelets", "waves bend only at edges",
                 "the speed of light is constant"], "answer": 1,
     "hint": "The principle builds the new wavefront from the old one.",
     "explanation": "Every point on a wavefront sends out a secondary wavelet; the new wavefront "
                    "is the envelope touching all of them. That construction gives reflection, "
                    "refraction and diffraction in one rule."},
    {"id": "Q5", "category": "Coherence", "type": "mcq", "slo": "9.2.1",
     "prompt": "Two sources are coherent when they...",
     "options": ["emit the same frequency", "keep a constant phase difference",
                 "have the same amplitude", "are close together"], "answer": 1,
     "hint": "Same frequency is necessary but not sufficient.",
     "explanation": "Coherence requires a **constant** phase difference. Two lamps at the same "
                    "frequency drift in and out of step, so their fringes smear into a uniform "
                    "glow within a fraction of a second."},
    {"id": "Q6", "category": "Coherence", "type": "mcq", "slo": "9.2.1",
     "prompt": "Young obtained two genuinely coherent sources by...",
     "options": ["using two identical lasers", "using two slits in the same screen",
                 "using two separate lamps", "using two candles"], "answer": 1,
     "hint": "Both beams must come from the same original wavefront.",
     "explanation": "A single source slit illuminates both apertures, so the two beams necessarily "
                    "keep a fixed phase relationship. Two separate lamps cannot do this, however "
                    "carefully they are matched."},
    {"id": "Q7", "category": "Conditions", "type": "mcq", "slo": "9.2.3",
     "prompt": "Which is NOT a necessary condition for interference to be observed?",
     "options": ["The sources must be coherent", "The sources must have the same frequency",
                 "The amplitudes must be comparable", "The sources must be monochromatic"],
     "answer": 3,
     "hint": "Three of these are essential; one is a refinement.",
     "explanation": "Coherence already requires a stable phase relationship. Monochromatic light "
                    "gives cleaner fringes because every wavelength has its own spacing, but white "
                    "light does produce interference near the centre."},
    {"id": "Q8", "category": "Interference", "type": "mcq", "slo": "9.2.2",
     "prompt": "Interference fringes disappear when...",
     "options": ["the slit separation increases", "the screen is moved further away",
                 "the sources are made incoherent", "the wavelength gets shorter"], "answer": 2,
     "hint": "The other three change the pattern; only one destroys it.",
     "explanation": "Incoherent sources give a phase difference that drifts, so the pattern "
                    "averages out. The other three change the fringe spacing, which is exactly "
                    "how you measure the wavelength."},

    {"id": "Q9", "category": "Young's experiment", "type": "numeric", "slo": "9.2.5",
     "prompt": "In Young's experiment the wavelength is 600 nm, the slit separation is 0.30 mm and "
               "the screen is 1.00 m away. Enter the fringe spacing in millimetres.",
     "answer": 2.0, "tolerance": 0.02, "unit": "mm",
     "hint": "dy = lambda L / d.",
     "explanation": "dy = (600e-9 x 1.00)/(0.30e-3) = 2.0e-3 m = 2.0 mm. Getting metres and "
                    "millimetres mixed up here gives a factor of a thousand error."},
    {"id": "Q10", "category": "Young's experiment", "type": "numeric", "slo": "9.2.5",
     "prompt": "In Young's experiment the wavelength is 500 nm and the fringe spacing is 2.5 mm. Enter "
               "the slit separation in millimetres if the screen is 1.20 m away.",
     "answer": 0.24, "tolerance": 0.005, "unit": "mm",
     "hint": "Rearrange dy = lambda L / d to give d = lambda L / dy.",
     "explanation": "d = (500e-9 x 1.20)/(2.5e-3) = 2.4e-4 m = 0.24 mm. Notice that increasing "
                    "the slit separation brings the fringes closer together."},
    {"id": "Q11", "category": "Young's experiment", "type": "numeric", "slo": "9.2.6",
     "prompt": "With the arrangement in the previous question, how far is the third bright fringe from "
               "the centre? Enter the number in millimetres.",
     "answer": 7.5, "tolerance": 0.05, "unit": "mm",
     "hint": "The nth bright fringe is at y = n x fringe spacing.",
     "explanation": "y_3 = 3 x 2.5 = 7.5 mm. Dark fringes fall halfway between the bright ones, "
                    "at 1.25 mm, 3.75 mm, 6.25 mm and so on."},
    {"id": "Q12", "category": "Young's experiment", "type": "mcq", "slo": "9.2.4",
     "prompt": "In Young's experiment the central fringe appears white with white light because...",
     "options": ["the source is white", "all wavelengths interfere constructively at zero path "
                 "difference", "the screen is reflecting light",
                 "the slits are coloured"], "answer": 1,
     "hint": "At the centre the path difference is zero for every wavelength.",
     "explanation": "Zero path difference means constructive interference for every wavelength at "
                    "once. Away from the centre the different wavelengths have different spacings "
                    "and separate into a spectrum."},

    {"id": "Q13", "category": "Michelson", "type": "mcq", "slo": "9.3.1",
     "prompt": "In Michelson's interferometer, moving the movable mirror by a distance x changes "
               "the optical path by...",
     "options": ["x", "2x", "x/2", "4x"], "answer": 1,
     "hint": "Count how many times the light passes the mirror.",
     "explanation": "2x, because the light travels out to the mirror and back again. That is why "
                    "moving the mirror by half a wavelength shifts one fringe."},
    {"id": "Q14", "category": "Gravitational waves", "type": "mcq", "slo": "9.3.2",
     "prompt": "Gravitational waves are...",
     "options": ["electromagnetic waves like light", "ripples in spacetime itself",
                 "sound waves in space", "particle emissions from stars"], "answer": 1,
     "hint": "They are not light and not sound.",
     "explanation": "They are oscillations of spacetime itself, which is why they pass straight "
                    "through matter without being scattered - a property no electromagnetic wave "
                    "has."},
    {"id": "Q15", "category": "Gravitational waves", "type": "mcq", "slo": "9.3.3",
     "prompt": "A gravitational wave passing a ring of freely falling masses causes the ring to...",
     "options": ["expand uniformly", "stretch in one direction and squeeze in the perpendicular "
                 "one alternately", "rotate steadily", "move bodily sideways"], "answer": 1,
     "hint": "The distortion is alternating in two perpendicular directions.",
     "explanation": "That alternating stretch-and-squeeze is exactly what LIGO looks for: a "
                    "measurable change in the separation between its end mirrors."},
    {"id": "Q16", "category": "Gravitational waves", "type": "numeric", "slo": "9.3.4",
     "prompt": "An interferometer arm is 4.0 km long and changes length by 1.0 x 10^-18 m. Enter the "
               "strain, the change as a fraction of the arm length.",
     "answer": 2.5e-22, "tolerance": 1e-24, "unit": "",
     "hint": "Strain is the change divided by the original length.",
     "explanation": "1.0e-18 / 4.0e3 = 2.5 x 10^-22, a part in four million million million. "
                    "That is why the arms have to be kilometres long."},

    {"id": "Q17", "category": "Diffraction", "type": "mcq", "slo": "9.4.1",
     "prompt": "Diffraction of light is...",
     "options": ["the splitting of white light into colours", "the spreading of light round an "
                 "obstacle or through an opening", "the reflection of light from a mirror",
                 "the bending of light at a glass surface"], "answer": 1,
     "hint": "One of these is dispersion, another reflection, another refraction.",
     "explanation": "Spreading past the edges. It is more pronounced for longer wavelengths and "
                    "narrower openings, which is why it is invisible in everyday life but "
                    "dominant when the opening is comparable to a wavelength."},
    {"id": "Q18", "category": "Diffraction", "type": "numeric", "slo": "9.4.3",
     "prompt": "Light of wavelength 500 nm passes through a slit 0.10 mm wide. Enter sin(theta) for "
               "the first minimum.",
     "answer": 0.005, "tolerance": 0.0002, "unit": "",
     "hint": "a sin(theta) = m lambda with m = 1.",
     "explanation": "sin(theta) = 500e-9/1.0e-4 = 5.0 x 10^-3. The angle is about 0.286 degrees."},
    {"id": "Q19", "category": "Diffraction", "type": "mcq", "slo": "9.4.3",
     "prompt": "The central maximum in a single-slit diffraction pattern is...",
     "options": ["the same width as the other bright bands", "twice as wide as the other bright "
                 "bands", "half as wide", "infinitely narrow"], "answer": 1,
     "hint": "It is bounded by minima rather than maxima.",
     "explanation": "Twice as wide, because it extends from the first minimum on one side to the "
                    "first minimum on the other, whereas every other band runs minimum to minimum."},
    {"id": "Q20", "category": "Diffraction", "type": "mcq", "slo": "9.4.2",
     "prompt": "A diffraction grating gives much sharper maxima than a single slit because...",
     "options": ["its slits absorb less light", "the maxima come from many wavelets arriving "
                 "together, and all others scatter",
                 "the wavelengths are longer", "the screen is closer"], "answer": 1,
     "hint": "Think about what happens to thousands of wavelets at a slight angle.",
     "explanation": "At the principal maxima thousands of wavelets arrive in step and reinforce; "
                    "a slight angle destroys that, so the maxima are extremely narrow. That is what "
                    "gives a grating its high resolving power."},
    {"id": "Q21", "category": "Diffraction", "type": "numeric", "slo": "9.4.2",
     "prompt": "A grating with 500 lines per millimetre is used with light of wavelength 600 nm. Enter "
               "the highest order m that exists.",
     "answer": 3.0, "tolerance": 0.01, "unit": "",
     "hint": "d = 1/(lines per mm). Only orders with m lambda <= d exist, so take the whole-number part.",
     "explanation": "d = 1/500 mm = 2e-6 m, so m lambda <= d gives m <= 2e-6/6e-7 = 3.33. The "
                    "highest order that actually exists is **m = 3**, and the fourth is "
                    "impossible because it would need sin(theta) > 1."},
    {"id": "Q22", "category": "Diffraction", "type": "mcq", "slo": "9.4.4",
     "prompt": "The diffraction pattern spreads more when...",
     "options": ["the wavelength is shorter", "the slit is narrower",
                 "the screen is further away", "the light is brighter"], "answer": 1,
     "hint": "Compare the wavelength with the slit width.",
     "explanation": "sin(theta) = lambda/a, so a narrower slit gives a larger angle. A shorter "
                    "wavelength narrows the pattern; screen distance only changes the linear size "
                    "on the screen, not the angles."},

    {"id": "Q23", "category": "Bragg's law", "type": "mcq", "slo": "9.5.1",
     "prompt": "Bragg's law for X-ray diffraction is...",
     "options": ["d sin(theta) = m lambda", "2 d sin(theta) = m lambda",
                 "2 d cos(theta) = m lambda", "d = m lambda"], "answer": 1,
     "hint": "Why does the factor of 2 appear?",
     "explanation": "2 d sin(theta) = m lambda. The factor of two comes from the round trip the "
                    "lower ray makes, down to the next plane and back up."},
    {"id": "Q24", "category": "Bragg's law", "type": "numeric", "slo": "9.5.4",
     "prompt": "X-rays of wavelength 100 pm reflect from planes 400 pm apart. Enter sin(theta) for "
               "first order reflection.",
     "answer": 0.125, "tolerance": 0.002, "unit": "",
     "hint": "sin(theta) = m lambda / (2 d).",
     "explanation": "sin(theta) = 100/(2 x 400) = 0.125, so theta = 7.18 degrees."},
    {"id": "Q25", "category": "Bragg's law", "type": "numeric", "slo": "9.5.3",
     "prompt": "For the same crystal, enter the highest order m that exists with 100 pm X-rays and "
               "400 pm plane spacing.",
     "answer": 8.0, "tolerance": 0.2, "unit": "",
     "hint": "The largest m with m lambda <= 2 d.",
     "explanation": "m max = 2d/lambda = 800/100 = 8. Orders beyond that would need sin(theta) > 1, "
                    "which is impossible."},
    {"id": "Q26", "category": "Bragg's law", "type": "mcq", "slo": "9.5.2",
     "prompt": "X-ray diffraction of a crystal reveals...",
     "options": ["the temperature of the crystal", "the arrangement of atoms within it",
                 "the speed of light in the crystal", "the charge on the atoms"], "answer": 1,
     "hint": "It is used to identify minerals and to work out DNA's structure.",
     "explanation": "The pattern of reflections is a fingerprint of the atomic arrangement. It is "
                    "how Rosalind Franklin's X-ray photograph led to the double helix, and how "
                    "minerals are identified today."},

    {"id": "Q27", "category": "Polarisation", "type": "mcq", "slo": "9.6.1",
     "prompt": "Plane-polarised light is light whose vibrations are...",
     "options": ["random in all planes", "in one single plane", "along the direction of travel",
                 "in every plane equally"], "answer": 1,
     "hint": "'Plane' refers to the plane of vibration.",
     "explanation": "In one single plane. Unpolarised light vibrates in every possible plane at "
                    "once, which is why it appears equally bright from every direction."},
    {"id": "Q28", "category": "Polarisation", "type": "mcq", "slo": "9.6.2",
     "prompt": "Which of these cannot be polarised?",
     "options": ["Light", "Water ripples", "Sound in air", "Radio waves"], "answer": 2,
     "hint": "Only transverse waves have a plane of vibration.",
     "explanation": "Sound in air is longitudinal: its particles vibrate along the direction of "
                    "travel, so there is no plane of vibration to select. Polarisation is "
                    "therefore impossible for longitudinal waves."},
    {"id": "Q29", "category": "Polarisation by reflection", "type": "numeric", "slo": "9.6.3",
     "prompt": "Light passes from air (n = 1.00) into glass (n = 1.50). Enter Brewster's angle in "
               "degrees.",
     "answer": 56.309932474020215, "tolerance": 0.2, "unit": "degrees",
     "hint": "tan(theta_B) = n2 / n1.",
     "explanation": "theta_B = arctan(1.50/1.00) = 56.3 degrees. At that angle the reflected and "
                    "refracted rays are at right angles, and the reflected light is completely "
                    "plane-polarised."},
    {"id": "Q30", "category": "Polarisation by reflection", "type": "mcq", "slo": "9.6.3",
     "prompt": "At Brewster's angle...",
     "options": ["all the light is reflected", "the reflected light is completely plane-polarised",
                 "the light is fully refracted", "the waves cancel completely"], "answer": 1,
     "hint": "Only one component of the vibration survives in the reflection.",
     "explanation": "The reflected light is completely plane-polarised, with the vibration in the "
                    "plane of incidence. This is why Polaroid sunglasses cut glare so much more "
                    "effectively than plain tinted lenses."},
    {"id": "Q31", "category": "Polaroid", "type": "numeric", "slo": "9.6.4",
     "prompt": "Unpolarised light of intensity 100 W m^-2 passes through a single ideal polaroid. "
               "Enter the intensity that emerges, in W m^-2.",
     "answer": 50.0, "tolerance": 0.5, "unit": "W m⁻²",
     "hint": "Half of unpolarised light passes through any ideal polaroid.",
     "explanation": "50 W m^-2. This halving is specific to unpolarised input; once the light is "
                    "polarised, Malus's law with cos squared takes over."},
    {"id": "Q32", "category": "Polaroid", "type": "mcq", "slo": "9.6.4",
     "prompt": "If a third polaroid is inserted at 45 degrees between two crossed polaroids, the "
               "view becomes...",
     "options": ["completely black, as before", "partially bright again",
                 "completely white", "unchanged in colour"], "answer": 1,
     "hint": "The middle polaroid re-orients the vibrations.",
     "explanation": "Partially bright again. The middle polaroid lets through the 45 degrees of "
                    "vibration it allows, and the final polaroid then passes half of *that*. This "
                    "is the clearest proof that what is happening is interference-like "
                    "reorientation, not simple filtering."},

    {"id": "Q33", "category": "Malus's law", "type": "numeric", "slo": "9.6.5",
     "prompt": "Polarised light of intensity 100 W m^-2 meets a polaroid whose axis is at 60 degrees "
               "to the vibration. Enter the intensity that passes, in W m^-2.",
     "answer": 25.0, "tolerance": 0.5, "unit": "W m⁻²",
     "hint": "I = I_0 cos^2(theta), and cos 60 degrees = 0.5.",
     "explanation": "100 x 0.25 = 25 W m^-2. The squaring matters: the transmitted intensity is "
                    "not proportional to cos but to cos squared."},
    {"id": "Q34", "category": "Malus's law", "type": "mcq", "slo": "9.6.5",
     "prompt": "Malus's law is I = I_0 cos^2(theta). At what angle does half the intensity pass?",
     "options": ["30 degrees", "45 degrees", "60 degrees", "90 degrees"], "answer": 1,
     "hint": "You need cos squared = 0.5.",
     "explanation": "45 degrees, since cos 45 = 0.707 and 0.707 squared = 0.5. At 60 degrees only "
                    "a quarter passes; at 90 degrees nothing does."},
    {"id": "Q35", "category": "Malus's law", "type": "numeric", "slo": "9.6.6",
     "prompt": "Unpolarised light of intensity 800 W m^-2 passes through two polaroids whose axes "
               "make an angle of 30 degrees. Enter the final intensity in W m^-2.",
     "answer": 300.0, "tolerance": 3.0, "unit": "W m⁻²",
     "hint": "Halve first, then apply cos squared.",
     "explanation": "The first polaroid gives 800/2 = 400 W m^-2. Malus's law then gives "
                    "400 x cos^2 30 = 400 x 0.75 = 300 W m^-2. Both steps are needed, and "
                    "forgetting the initial halving gives 600 - the single most common error."},
    {"id": "Q36", "category": "Applications", "type": "mcq", "slo": "9.6.7",
     "prompt": "Polarising sunglasses reduce glare mainly because...",
     "options": ["they are darker than ordinary sunglasses",
                 "glare from horizontal surfaces is largely polarised and is blocked",
                 "they absorb all blue light", "they magnify the scene"], "answer": 1,
     "hint": "Think about what happens to light reflecting off water or a road.",
     "explanation": "Light reflected from a horizontal surface is largely plane-polarised, so a "
                    "polaroid removes most of it while leaving the light scattered by the objects "
                    "you want to see largely untouched."},
    {"id": "Q37", "category": "Applications", "type": "mcq", "slo": "9.6.7",
     "prompt": "In an LCD screen, the liquid crystal layer between two polarisers is used to...",
     "options": ["change the polarisation by an amount set by each pixel's voltage",
                 "absorb light in the dark pixels", "generate the light",
                 "polarise the backlight before it enters"], "answer": 0,
     "hint": "The crystal rotates the polarisation; the second polariser then filters it.",
     "explanation": "The crystal's orientation depends on the voltage across each pixel, so it "
                    "rotates the polarisation by a controllable amount, and the second "
                    "polariser converts that rotation directly into brightness."},
    {"id": "Q38", "category": "Applications", "type": "mcq", "slo": "9.6.7",
     "prompt": "In a 3-D film, the two images are projected through polarisers...",
     "options": ["of the same orientation", "at right angles to each other",
                 "that rotate in time", "of opposite colour"], "answer": 1,
     "hint": "Each eye has its own filter.",
     "explanation": "At right angles. Each eye then receives only one image, and the brain reads "
                    "the pair as depth. That is why ordinary glasses ruin 3-D films while "
                    "polarised 3-D spectacles work."},
]

# --------------------------------------------------------------------------
# References
# --------------------------------------------------------------------------

REFERENCES = [
    {"short": "OpenStax University Physics Vol. 3",
     "title": "Chapters 1 and 5: The Nature of Light and Interference",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/university-physics-volume-3",
     "used_for": "Wavefronts, Huygens' principle, interference and the wave-particle discussion."},
    {"short": "OpenStax College Physics 2e",
     "title": "Chapter 27: Wave Optics",
     "org": "OpenStax, Rice University",
     "url": "https://openstax.org/details/books/college-physics-2e",
     "used_for": "Young's experiment, diffraction, gratings, polarisation and Malus's law."},
    {"short": "Nobel Prize in Physics 2017",
     "title": "For the first observation of gravitational waves",
     "org": "The Royal Swedish Academy of Sciences",
     "url": "https://www.nobelprize.org/prizes/physics/2017/summary/",
     "used_for": "The detection of gravitational waves and how interferometry made it possible."},
    {"short": "LIGO",
     "title": "Laser Interferometer Gravitational-Wave Observatory",
     "org": "LIGO Laboratory",
     "url": "https://www.ligo.caltech.edu/page/what-is-ligo",
     "used_for": "The instrument, its sensitivity and why the arms are 4 km long."},
    {"short": "AKU-EB syllabus",
     "title": "Physics HSSC Syllabus 2025, Part I, Topic 9",
     "org": "Aga Khan University Examination Board",
     "url": "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf",
     "used_for": "The official wording of outcomes 9.1.1 to 9.6.7."},
]

# --------------------------------------------------------------------------
# Malus's law — the numbers a calculator needs before it is ever used
# --------------------------------------------------------------------------

MALUS_TABLE = [
    {"theta_deg": 0, "fraction": 1.0,
     "note": "Axes parallel — every vibration already points the right way."},
    {"theta_deg": 30, "fraction": 0.75,
     "note": "cos 30 = 0.866, and 0.866 squared is 0.75. The square matters."},
    {"theta_deg": 45, "fraction": 0.5,
     "note": "Exactly half passes through a polaroid at 45 degrees."},
    {"theta_deg": 60, "fraction": 0.25,
     "note": "A quarter passes. Symmetric with 30 degrees, as it must be."},
    {"theta_deg": 90, "fraction": 0.0,
     "note": "Crossed axes — nothing at all gets through, and the view is black."},
]

# --------------------------------------------------------------------------
# Bragg's law — worked crystal data students can check their angle against
# --------------------------------------------------------------------------

BRAGG_EXAMPLES = [
    {"crystal": "Sodium chloride (NaCl)", "d": 5.64e-10,
     "note": "The classic first-order school case. d is the spacing between adjacent ion planes."},
    {"crystal": "Zinc blende (ZnS)", "d": 3.09e-10,
     "note": "Cube edge 5.41 A gives d = a/sqrt(3)."},
    {"crystal": "Copper", "d": 1.28e-10,
     "note": "A face-centred cubic metal; d = a/sqrt(4) with a = 3.61 A."},
    {"crystal": "Diamond", "d": 2.06e-10,
     "note": "Cubic edge 3.57 A, so d = a/sqrt(4)."},
    {"crystal": "Calcite (CaCO3)", "d": 3.04e-10,
     "note": "Real mineral identification goes on exactly this data — each mineral has its own set."},
]
