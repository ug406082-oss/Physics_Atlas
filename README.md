# Physics Atlas

Physics Atlas is a complete, interactive **Grade XI Physics** learning web app built with Streamlit. It covers the **whole AKU-EB Physics HSSC Syllabus 2025, Part I** — all ten chapters and all **185 student learning outcomes** — as ten separate learning environments, each with its own apparatus, diagrams and tutor.

Everything runs **offline**. There is no API key, no account and no network call anywhere in the app.

## What is in the book

| # | Chapter | Outcomes | Stations | Worked | Practice |
|---|---------|---------:|---------:|-------:|---------:|
| 1 | Physical Quantities and Measurement | 13 | 9 | 6 | 24 |
| 2 | Scalars and Vectors | 10 | 13 | 6 | 30 |
| 3 | Motion in One Dimension | 12 | 14 | 8 | 28 |
| 4 | Motion in Two Dimensions | 20 | 15 | 6 | 39 |
| 5 | Deformation in Solids | 8 | 13 | 5 | 23 |
| 6 | Fluids Dynamics | 18 | 14 | 5 | 28 |
| 7 | Oscillations | 22 | 15 | 4 | 37 |
| 8 | Waves | 19 | 16 | 5 | 30 |
| 9 | Physical Optics | 28 | 15 | 5 | 38 |
| 10 | Thermodynamics | 35 | 19 | 8 | 62 |
| | **Total** | **185** | **143** | **58** | **339** |

All **185** published outcomes, in the published wording. The authoritative list lives in
`physics/syllabus_xi.py`, transcribed from the AKU-EB PDF, and
`tests/test_syllabus_fidelity.py` fails the build if any chapter teaches an outcome the board
does not publish, misses one it does, or changes the wording.

The twelve topic-wise practical experiments the board lists (Vernier callipers, screw gauge,
spherometer, parallelogram method strip, ticker-timer, free fall, pendulum, sonometer,
resonance tube, and the two calorimetry methods) appear as their own station in each chapter,
with apparatus, method, formula, data-table columns and the theory behind each.

Chapters are deliberately uneven in depth, because the syllabus is. Chapter 5 has five outcomes and Chapter 10 has thirty-five; each chapter carries its own identity — its own simulator, its own diagrams and its own worked problems — rather than a chapter being a re-skin of another.

## Features

- **Chapter-only first screen.** The home screen is nothing but the chapter picker; choose a chapter and step into its world.
- **Chapter world.** Every chapter is split into stations (route & outcomes, the teaching content, worked problems, practice, offline tutor, references) with a live mastery meter and a per-chapter exit report.
- **Exit report.** When you leave a chapter you get every one of its outcomes in plain words with the status you earned — mastered, explored, or not started.
- **Offline AI tutor ("Atlas Tutor").** A per-chapter knowledge base plus real calculators — gas laws, rms speed, Carnot efficiency, Fringe spacing, work on a P–V diagram, uncertainty propagation and more. No API key, no internet.
- **Interactive simulations.** Not illustrations: a vector workbench, a projectile studio, a stress–strain tester, a Bernoulli bench, a pendulum rig, a Michelson interferometer, a Carnot cycle you can move the reservoirs on, and more.
- **Illustrative SVG diagrams.** Every diagram is computed from the same formulas the core module uses, so the picture and the number can never drift apart.
- **Worked problems and guided practice.** 58 fully worked problems and 311 practice questions, every one anchored to a specific outcome, with hints and explanations that say *why*, not just what.
- - **Every outcome has a full lesson.** Content is organised by station, and a station covers up to six
  outcomes, so every station also ends with an outcome-by-outcome review: what the board asks, what it
  means in plain terms, why it is true, a worked example, the usual mistake, and a question with a
  revealable answer. That is 185 lessons and about 12 400 words of dedicated explanation in
  `physics/teaching.py`, so a learner never has to remember which station an outcome came from.
- **Diagrams cannot silently clip.** SVG has no line wrapping, so a label wider than its viewBox is
  clipped in the browser. `common._svg` measures every label against the box and wraps what would not
  fit, and `tools/check_diagrams.py` measures all 41 diagrams and reports any that overflow.
- **Every interactive station says what to do with it.** A `how_to()` line opens each station that has controls, and `tests/test_interactive_guidance.py` fails the build if one ever ships without it.
- **Simple language**, with the official outcome wording kept alongside.

## Architecture

The important design rule is that **content is separated from presentation**, so every number can be tested without a browser.

```
physics/
├── board.py            # which board and syllabus this is built against
├── curriculum.py       # the chapter registry — the single source of truth
├── engine.py           # shared station engine, guidance blocks, fragments, reports
├── progress.py         # per-chapter session progress
├── ai_tutor.py         # chapter-aware tutor routing
├── core/               # pure formulas; no Streamlit, no I/O, fully testable
│   ├── measurement.py vectors.py motion1d.py motion2d.py
│   ├── solids.py fluids.py oscillations.py waves.py optics.py thermo.py
├── chapters/           # pure content: outcomes, stations, questions, references
│   └── chNN_data.py    #   ... and chNN.py for the chapter's interface
├── visuals/            # per-chapter SVG builders, all @st.cache_data
└── tutor_kb/           # per-chapter tutor knowledge and calculators
```

`physics/core/` never imports Streamlit. That is what allows the whole of the physics to be checked by a plain Python interpreter.

## Performance

- **`@st.cache_data`** wraps every diagram builder and the chapter-slot list. Streamlit re-executes the whole script on every interaction, so anything expensive is memoised behind a stable key.
- **`@st.fragment`** wraps every station renderer, centrally, in `engine._as_fragment()`. `st.tabs` renders *every* tab body each time, so without this a single slider drag would rebuild the entire chapter. Station fragments are given deterministic names (`station_<key>`) because Streamlit derives fragment identity from module + qualname, and several renderers are lambdas that would otherwise all share the qualname `<lambda>`.
- Navigation controls on the app shell are their own small fragments too, so leaving a chapter does not force the chapter to re-render first.

Together these cut an interaction from "rebuild the whole book" to "rebuild the one station you are touching".

## Quick Start (Local)

1. Clone or download this repository to your local machine
2. Navigate to the project directory:

```bash
cd Physics_Atlas
```

3. Create and activate a virtual environment:

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

4. Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Run the app:

```bash
streamlit run streamlit_app.py
```

6. Open your browser to `http://localhost:8501`

To stop the app, press `Ctrl+C` in the terminal.

## Tests

```bash
pytest tests/ -q
```

The pure-physics and curriculum suites need no browser. `tests/test_app_smoke.py` drives the real Streamlit app through `AppTest` and needs the full dependency set installed.

There is also a stubbed end-to-end renderer that needs no Streamlit at all, which is useful in a restricted environment:

```bash
python tools/smoke_app.py
```

It renders every station of every open chapter and reports how many `@cache_data` and `@st.fragment` decorations were exercised.

## Project Structure

```
Physics_Atlas/
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── physics/              # all the code, as described above
├── tests/                # pure-physics, curriculum and app smoke tests
├── tools/smoke_app.py    # stubbed end-to-end renderer
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

## Deployment to Streamlit Community Cloud

1. Create a new GitHub repository (e.g., `physics-atlas`)
2. Push all files in this `Physics_Atlas/` directory to that repository
3. Go to [share.streamlit.io](https://share.streamlit.io)
4. Sign in with GitHub and click "New app"
5. Connect your `physics-atlas` repository
6. Set the main file path to `streamlit_app.py`
7. Select the correct branch (usually `main`)
8. Click "Deploy"

## Scientific References

1. BIPM — SI Brochure: https://www.bipm.org/en/publications/si-brochure
2. NIST SP 811 — Guide for the Use of the International System of Units: https://www.nist.gov/pml/special-publication-811
3. JCGM — Guide to the Expression of Uncertainty in Measurement (GUM): https://www.bipm.org/en/committees/jc/jcgm/publications
4. OpenStax University Physics, Vols. 1–3: https://openstax.org/details/books/university-physics-volume-1
5. Nobel Prize in Physics 2017 (gravitational waves): https://www.nobelprize.org/prizes/physics/2017/summary/
6. AKU-EB Physics HSSC Syllabus 2025, Part I: https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf

## Notes

- This is an independent project; it does not modify or depend on Enzyme Atlas.
- **All ten chapters are fully implemented.** Nothing is locked or stubbed.
- All calculations are for educational purposes; simulated data is clearly labelled, and idealisations (ideal gases, reversible processes) are stated explicitly wherever they are used.
- Nothing is saved beyond the browser session.