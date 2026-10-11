# Syllabus fidelity: what to check by hand

Source: `Physics-XI-XII-Syllabus-2025.pdf`, AKU-EB, latest revision January 2025.
The authoritative outcome list now lives in `physics/syllabus_xi.py` and every
chapter data file is checked against it by `tests/test_syllabus_fidelity.py`.

## Totals

| Chapter | Outcomes in the PDF |
|---|---|
| 1 Physical Quantities and Measurement | 13 |
| 2 Scalars and Vectors | 10 |
| 3 Motion in One Dimension | 12 |
| 4 Motion in Two Dimensions | 20 |
| 5 Deformation in Solids | 8 |
| 6 Fluids Dynamics | 18 |
| 7 Oscillations | 22 |
| 8 Waves | 19 |
| 9 Physical Optics | 28 |
| 10 Thermodynamics | 35 |
| **Total** | **185** |

## Outcomes needing a human check

The PDF stores these as embedded formula glyphs that no text extractor can read.
Each was reconstructed from its sub-topic and its paired outcome, and is listed in
`syllabus_xi.REVIEWED`. Please confirm these against the PDF.

| Outcome | Reconstructed as | Why it was lost |
|---|---|---|
| 3.2.1 | state the law of conservation of linear momentum | text block dropped between columns |
| 5.4.2 | interpret force extension graph for a deformed material | merged into 5.4.3 |
| 6.1.2 | solve word problems using W = rho g V | formula is a glyph |
| 6.1.4 | solve word problems using the law of floatation for a floating body | text block dropped |
| 6.4.1 | state Bernoulli's equation, P + (1/2) rho v^2 + rho g h = constant | formula is a glyph |
| 7.2.3 | derive expression for instantaneous displacement, velocity and acceleration in terms of angular frequency | text block dropped |
| 7.5.2 | solve word problems related to the given expression for energy conservation in S.H.M. | formula is a glyph |
| 8.5.1 | describe the Doppler effect | text block dropped |
| 8.5.2 | derive the relation between original and apparent frequency in the three cases | list items dropped |
| 8.5.4 | describe the change in frequency and wavelength of light waves due to relative motion (red and blue shifts) | truncated to "waves" |
| 9.4.3 | describe the diffraction pattern produced by a grating and the role of the number of lines | text block dropped |
| 9.5.1 | state Bragg's law, 2 d sin(theta) = m lambda | formula is a glyph |
| 9.5.3 | derive the equation 2 d sin(theta) = m lambda | formula is a glyph |
| 9.5.4 | solve word problems related to the given equation | formula is a glyph |
| 9.6.5 | state Malus's law, I = I0 cos^2 theta | text block dropped |
| 10.2.1 | state Boyle's law and Charles's law | formula is a glyph |
| 10.2.2 | describe that a gas obeying PV = nRT is an ideal gas | formula is a glyph |
| 10.6.2 | explain the molar specific heat of a gas at constant volume and at constant pressure, Cv and Cp | formula is a glyph |
| 10.11.1 | explain entropy as a measure of the number of microscopic arrangements (microstates) | text block dropped |

## Cognitive levels

Each outcome carries the syllabus's own level: `R` remember, `U` understand,
`A` apply, `An` analyse, `E` evaluate, `C` create, `*` unmarked. Seven outcomes
are marked **FA** (formative assessment, not examined).

## Syllabus areas the app does not yet cover

- Topic-wise practical activities and their apparatus lists (Vernier callipers,
  screw gauge, spherometer, ticker-timer, free-fall apparatus, pendulum).
- The assessment scheme: MCQ / CRQ / ERQ split and the cognitive marks
  distribution (Remember 0-15 %, Understand 45-60 %, Apply and beyond 25-40 %).
