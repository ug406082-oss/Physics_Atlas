# Physics Atlas

Physics Atlas is a complete, interactive Grade XI Physics learning web app built with Streamlit. It provides a polished, chapter-based learning environment focused on **Physical Quantities and Measurement** (Chapter 1) with a roadmap for the remaining chapters.

## Features

- **Chapter-only first screen**: the home screen is nothing but the chapter picker — choose a chapter and step into its world.
- **Chapter world**: nine interactive stations (route & outcomes, units, dimensions, accuracy, uncertainty, worked problems, practice, offline tutor, references) with a live mastery meter.
- **Exit report**: when you leave a chapter, you get a full report showing every student learning outcome (SLO) in plain words with the status you earned.
- **Offline AI tutor** ("Atlas Tutor"): a helper that needs **no API key and no internet**. It answers from the chapter's own content and from real calculators — unit conversion, significant figures, uncertainty propagation, dimensional lookup and arithmetic.
- **Illustrative SVG diagrams**: magnitude-vs-unit scale, SI base-unit wheel, dimensional balance beam, error bullseye, uncertainty number line, significant-figure highlighter, derived-unit builder and a zoomable reading ruler.
- **Simple language** throughout, with the official SLO wording kept alongside.
- **Comprehensive Chapter 1**: covers all 13 SLOs for Physical Quantities and Measurement.
- **Interactive tools**: estimation activities, SI unit explorer, dimensional analysis, accuracy vs precision simulator, uncertainty calculator and significant-figures tool.
- **Worked examples and guided practice**: step-by-step numerical problems plus 24 practice questions with hints, explanations and session progress.
- **Scientific references**: BIPM SI Brochure, NIST SP 811, JCGM GUM and OpenStax College Physics 2e.

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

## Project Structure

```
Physics_Atlas/
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .streamlit/
    └── config.toml     # Streamlit configuration
```

## Deployment to Streamlit Community Cloud

1. Create a new GitHub repository (e.g., `physics-atlas`) - do not reuse Enzyme Atlas
2. Push all files in this `Physics_Atlas/` directory to that repository
3. Go to [share.streamlit.io](https://share.streamlit.io)
4. Sign in with GitHub and click "New app"
5. Connect your `physics-atlas` repository
6. Set the main file path to `streamlit_app.py`
7. Select the correct branch (usually `main`)
8. Click "Deploy"

## Scientific References

1. BIPM - SI Brochure: https://www.bipm.org/en/publications/si-brochure
2. NIST SP 811 - Guide for the Use of the International System of Units: https://www.nist.gov/pml/special-publication-811
3. JCGM - Guide to the Expression of Uncertainty in Measurement (GUM): https://www.bipm.org/en/committees/jc/jcgm/publications
4. OpenStax College Physics 2e: https://openstax.org/details/books/college-physics-2e

## Notes

- This is an independent project; it does not modify or depend on Enzyme Atlas
- Chapter 1 (Physical Quantities and Measurement) is fully implemented
- Chapters 2-10 are marked as coming soon/locked as placeholders
- All calculations are for educational purposes; simulated data is clearly labeled
