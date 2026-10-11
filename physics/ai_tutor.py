"""Atlas Tutor — an offline physics tutor that needs no API key.

Everything here runs on your own machine: there is no network call, no model
download and no account. The tutor combines three things:

1. a knowledge base written from this chapter's own content (``data.py``),
2. real calculators that call ``physics_core`` (significant figures,
   uncertainty, dimensional analysis), and
3. a unit-conversion engine built on the SI prefixes and standard factors.

It answers only what it actually knows and says so when it does not.
"""

from __future__ import annotations

import ast
import operator
import random
import re

import streamlit as st

from . import data as D
from . import physics_core as pc

# --------------------------------------------------------------------------
# 1. Knowledge base — plain-language answers taken from this chapter
# --------------------------------------------------------------------------
KB = [
    {"keys": ["physical quantity", "what is a physical quantity", "magnitude and unit",
              "magnitude", "number and unit"],
     "title": "Physical quantity",
     "answer": "A physical quantity is written as **a number (magnitude) + a unit**. "
               "Example: 9.81 m s⁻². The number 9.81 is the magnitude and m s⁻² is the unit. "
               "Either one on its own is not a measurement.",
     "slo": "1.1.1"},
    {"keys": ["unitless", "no unit", "without a unit", "why unit", "unit important", "unit matter"],
     "title": "Why the unit matters",
     "answer": "Without a unit, “5” could be 5 mm, 5 cm, 5 m or 5 km — those differ by a "
               "factor of 1 000 000. The unit carries the physical meaning, so it is never optional.",
     "slo": "1.1.1"},
    {"keys": ["appropriate value", "appropriate unit", "which unit", "choose unit",
              "best unit", "estimate", "order of magnitude"],
     "title": "Choosing an appropriate value",
     "answer": "Pick the unit that keeps the number near 1–100. Examples: a pencil → 15 cm; "
               "your mass → 50 kg; thickness of a coin → 2 mm; between cities → 200 km. "
               "An estimate is an educated guess; a measurement comes from an instrument and "
               "carries an uncertainty.",
     "slo": "1.1.2"},
    {"keys": ["base quantity", "base unit", "seven", "7 base", "si base", "fundamental"],
     "title": "The seven SI base quantities",
     "answer": "**Length → metre (m), Mass → kilogram (kg), Time → second (s), Electric current "
               "→ ampere (A), Thermodynamic temperature → kelvin (K), Amount of substance → mole "
               "(mol), Luminous intensity → candela (cd).**\n\nEverything else is built from these seven.",
     "slo": "1.1.3"},
    {"keys": ["derived unit", "derived quantity", "newton", "joule", "pascal", "watt", "force unit"],
     "title": "Derived units",
     "answer": "Derived units are products or quotients of base units. Examples: "
               "area → m², speed → m s⁻¹, **force → N = kg m s⁻²**, energy → J = kg m² s⁻², "
               "pressure → Pa = kg m⁻¹ s⁻². Special names like newton are only shorthand.",
     "slo": "1.1.4"},
    {"keys": ["dimension", "dimensions", "what is a dimension", "mlt", "m l t"],
     "title": "Dimensions",
     "answer": "A dimension tells the *kind* of quantity, not its size. The mechanical ones are "
               "**M** (mass), **L** (length) and **T** (time). Speed is always [L T⁻¹], force is "
               "[M L T⁻²], whatever unit you use.",
     "slo": "1.2.1"},
    {"keys": ["homogeneity", "homogeneous", "check equation", "equation correct",
              "dimensional check", "both sides"],
     "title": "Homogeneity of an equation",
     "answer": "An equation is homogeneous when both sides have the same dimensions and every "
               "added term matches. If the sides differ, the equation is definitely wrong. "
               "If they match, it is *possible* but not proven — dimensions cannot see "
               "numbers like 2π or ½.",
     "slo": "1.2.3"},
    {"keys": ["derive", "derivation", "pendulum", "find formula", "using dimensions", "unknown power"],
     "title": "Deriving a formula by dimensions",
     "answer": "Assume T = k·mᵃLᵇgᶜ, write dimensions, then compare powers. For a pendulum: "
               "mass gives a = 0, time gives −2c = 1 so c = −½, length gives b + c = 0 so b = ½. "
               "Result **T = k√(L/g)**. Dimensional analysis cannot find k (it is 2π for small "
               "oscillations).",
     "slo": "1.2.4"},
    {"keys": ["accuracy", "accurate"],
     "title": "Accuracy",
     "answer": "Accuracy is how close a measurement (or its average) is to the accepted reference "
               "value. A systematic error — like a zero error — destroys accuracy, and averaging "
               "does **not** fix it.",
     "slo": "1.3.1"},
    {"keys": ["precision", "precise"],
     "title": "Precision",
     "answer": "Precision is how closely repeated readings agree with each other. It is about "
               "spread, not about being right. You can be very precise and quite wrong: a ruler "
               "with a shifted zero gives tight but inaccurate readings.",
     "slo": "1.3.1"},
    {"keys": ["difference between accuracy and precision", "accuracy vs", "accuracy versus",
              "difference between precision"],
     "title": "Accuracy vs precision",
     "answer": "**Accuracy → close to the true value. Precision → readings close to each other.**\n\n"
               "• Accurate + precise: tight group on the centre.\n"
               "• Accurate, not precise: scattered but centred.\n"
               "• Precise, not accurate: tight group off to one side.\n"
               "• Neither: scattered and off centre.",
     "slo": "1.3.1"},
    {"keys": ["uncertainty", "why is there uncertainty", "error", "every measurement"],
     "title": "Why every measurement has uncertainty",
     "answer": "No instrument is perfect. The smallest division, the variation between readings, "
               "calibration, temperature, your reaction time and the method itself all add a small "
               "range. So a measurement is really *value ± uncertainty*, not a single point.",
     "slo": "1.4.2"},
    {"keys": ["significant figures", "sig fig", "sigfig", "significant figure", "sf"],
     "title": "Significant figures",
     "answer": "Significant figures record how a number was written. Rules: all non-zero digits "
               "count; leading zeros never count; zeros between non-zeros count; trailing zeros "
               "after a decimal point count; trailing zeros in a whole number (like 1500) are "
               "ambiguous — write 1.500 × 10³ instead. In multiplication keep the fewest sig figs "
               "of the inputs.",
     "slo": "1.4.1"},
    {"keys": ["propagation", "propagate", "combine uncertainty", "quadrature", "maximum method",
              "relative uncertainty", "percent uncertainty"],
     "title": "Combining uncertainty",
     "answer": "For Q = k·x₁ⁿ¹x₂ⁿ²… the relative uncertainties combine as\n\n"
               "• **Independent (quadrature):** ΔQ/Q = √(Σ (nᵢ·Δxᵢ/xᵢ)²)\n"
               "• **Maximum (limiting):** ΔQ/Q = Σ |nᵢ·Δxᵢ/xᵢ|\n\n"
               "The maximum method always gives the bigger interval. State which one your course "
               "uses and never mix them.",
     "slo": "1.4.1"},
    {"keys": ["source of uncertainty", "types of error", "systematic", "random",
              "zero error", "parallax"],
     "title": "Sources of uncertainty",
     "answer": "**Systematic** effects shift every reading one way (zero error, parallax, bad "
               "calibration) — they hurt accuracy and averaging will not remove them. "
               "**Random** effects scatter the readings (vibration, reaction time) — they hurt "
               "precision and averaging does reduce them.",
     "slo": "1.4.2"},
    {"keys": ["instrument", "resolution", "least count", "meter rule", "vernier", "micrometer",
              "stopwatch", "balance"],
     "title": "Instruments and resolution",
     "answer": "Resolution is the smallest change an instrument can show. A metre rule is 1 mm, a "
               "stopwatch commonly 0.01 s, a vernier caliper 0.01 mm. The reading uncertainty "
               "depends on the instrument and the method, so it must always be stated as an "
               "assumption — there is no single universal value.",
     "slo": "1.3.2"},
    {"keys": ["si prefix", "prefix", "kilo", "milli", "micro", "nano", "centi"],
     "title": "SI prefixes",
     "answer": "Prefixes multiply by powers of ten: **k = 10³, M = 10⁶, G = 10⁹**, and "
               "**m = 10⁻³, µ = 10⁻⁶, n = 10⁻⁹**. So 1 km = 1000 m and 1 mm = 0.001 m. "
               "When you square or cube a length, square or cube the factor too: "
               "1 cm² = 10⁻⁴ m².",
     "slo": "1.1.4"},
    {"keys": ["period of a pendulum", "pendulum formula", "2pi"],
     "title": "Period of a simple pendulum",
     "answer": "For small swings, **T = 2π√(L/g)**. The period does not depend on the mass, and "
               "g ≈ 9.81 m s⁻². Dimensional analysis only gives T ∝ √(L/g); the 2π comes from "
               "the real physics.",
     "slo": "1.2.4"},
    {"keys": ["what can you do", "help", "capabilities", "how do you work", "are you ai",
              "offline", "api"],
     "title": "What this tutor can do",
     "answer": "I run entirely in your browser window — no API key, no internet, no account. "
               "I can explain this chapter in simple words, convert units, count significant "
               "figures, combine uncertainties, check dimensions, do arithmetic and quiz you. "
               "Ask me things like *convert 90 km/h to m/s* or *how many sig figs in 0.00250*.",
     "slo": None},
]

GREETINGS = {
    "hi": "Hello! Ask me anything from Chapter 1 — units, dimensions, accuracy, uncertainty "
          "or significant figures.",
    "hello": "Hello! Ask me anything from Chapter 1 — units, dimensions, accuracy, uncertainty "
             "or significant figures.",
    "hey": "Hey! What shall we look at first?",
    "thanks": "Any time. Ask me another one.",
    "thank you": "Any time. Ask me another one.",
}

# --------------------------------------------------------------------------
# 2. Unit conversion engine
# --------------------------------------------------------------------------
# unit -> (dimension key, factor to the base unit of that dimension)
_UNITS = {
    "mm": ("L", 1e-3), "cm": ("L", 1e-2), "dm": ("L", 1e-1), "m": ("L", 1.0),
    "km": ("L", 1e3), "in": ("L", 0.0254), "ft": ("L", 0.3048),
    "mile": ("L", 1609.344), "yard": ("L", 0.9144), "µm": ("L", 1e-6), "um": ("L", 1e-6),
    "mg": ("M", 1e-6), "g": ("M", 1e-3), "kg": ("M", 1.0), "t": ("M", 1e3),
    "tonne": ("M", 1e3), "lb": ("M", 0.45359237), "u": ("M", 1.66053906660e-27),
    "ms": ("T", 1e-3), "s": ("T", 1.0), "min": ("T", 60.0), "h": ("T", 3600.0),
    "hr": ("T", 3600.0), "day": ("T", 86400.0), "year": ("T", 3.15576e7),
    "m/s": ("LT", 1.0), "ms-1": ("LT", 1.0), "km/h": ("LT", 1 / 3.6),
    "kmh": ("LT", 1 / 3.6), "kph": ("LT", 1 / 3.6), "mph": ("LT", 0.44704),
    "knot": ("LT", 0.514444),
    "m2": ("L2", 1.0), "m²": ("L2", 1.0), "cm2": ("L2", 1e-4), "cm²": ("L2", 1e-4),
    "mm2": ("L2", 1e-6), "mm²": ("L2", 1e-6), "km2": ("L2", 1e6), "km²": ("L2", 1e6),
    "m3": ("L3", 1.0), "m³": ("L3", 1.0), "cm3": ("L3", 1e-6), "cm³": ("L3", 1e-6),
    "l": ("L3", 1e-3), "litre": ("L3", 1e-3), "ml": ("L3", 1e-6),
    "n": ("MLT2", 1.0), "kn": ("MLT2", 1e3),
    "pa": ("ML-1T2", 1.0), "kpa": ("ML-1T2", 1e3), "bar": ("ML-1T2", 1e5),
    "atm": ("ML-1T2", 101325.0),
    "j": ("ML2T2", 1.0), "kj": ("ML2T2", 1e3), "cal": ("ML2T2", 4.184),
    "kwh": ("ML2T2", 3.6e6), "ev": ("ML2T2", 1.602176634e-19),
    "hz": ("T-1", 1.0), "khz": ("T-1", 1e3), "mhz": ("T-1", 1e6),
}

_ALIASES = {
    "kilometres": "km", "kilometer": "km", "kilometers": "km", "metres": "m",
    "meters": "m", "metre": "m", "meter": "m", "centimetres": "cm",
    "centimeters": "cm", "centimetre": "cm", "centimeter": "cm",
    "millimetres": "mm", "millimeters": "mm", "millimetre": "mm",
    "millimeter": "mm", "kilograms": "kg", "kilogram": "kg", "grams": "g",
    "gram": "g", "grammes": "g", "seconds": "s", "second": "s",
    "seconds.": "s", "minutes": "min", "minute": "min", "hours": "h",
    "hour": "h", "metres per second": "m/s", "meters per second": "m/s",
    "km per hour": "km/h", "km/hour": "km/h", "kph": "km/h",
    "newtons": "n", "newton": "n", "joules": "j", "joule": "j",
    "pascals": "pa", "litres": "l", "liter": "l", "liters": "l",
    "cubic centimetres": "cm3", "degrees celsius": "°c",
}

_TEMPERATURE = {"°c": "C", "c": "C", "celsius": "C", "°f": "F", "f": "F",
                "fahrenheit": "F", "k": "K", "kelvin": "K"}

_CONVERSION_RE = re.compile(
    r"(-?\d+(?:\.\d+)?)\s*([a-zA-Zµ°/²³²]+)\s*(?:to|in|into|as|=|->|→)\s*"
    r"([a-zA-Zµ°/²³²]+)"
)
_FIND_RE = re.compile(r"how\s+many\s+([a-zA-Zµ°/²³]+)\s+(?:are\s+)?in\s+"
                      r"(-?\d+(?:\.\d+)?)\s*([a-zA-Zµ°/²³]+)")


def _norm(token: str) -> str:
    token = token.strip().lower().replace(" ", "")
    token = token.replace("^", "").replace("**", "")
    return _ALIASES.get(token, _ALIASES.get(token.rstrip("s"), token))


def _to_temperature(token: str) -> str | None:
    return _TEMPERATURE.get(token.strip().lower())


def _convert_value(value: float, source: str, target: str) -> tuple[float, str] | None:
    source_n, target_n = _norm(source), _norm(target)

    if _to_temperature(source_n) and _to_temperature(target_n):
        scale = _to_temperature(source_n)
        kelvin = {"C": value + 273.15, "F": (value - 32) * 5 / 9 + 273.15,
                  "K": value}[scale]
        out = {"C": kelvin - 273.15, "F": (kelvin - 273.15) * 9 / 5 + 32,
               "K": kelvin}[_to_temperature(target_n)]
        return out, f"{value:g} {source_n} → {out:g} {target_n}"

    left, right = _UNITS.get(source_n), _UNITS.get(target_n)
    if not left or not right or left[0] != right[0]:
        return None
    base = value * left[1]
    return base / right[1], f"{value:g} {source_n} → {base / right[1]:g} {target_n}"


# --------------------------------------------------------------------------
# 3. Safe arithmetic (no eval of arbitrary code)
# --------------------------------------------------------------------------
_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg,
    ast.UAdd: operator.pos, ast.Mod: operator.mod,
}


def _evaluate(node):
    if isinstance(node, ast.Expression):
        return _evaluate(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.left), _evaluate(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.operand))
    raise ValueError("unsupported expression")


def _calculate(text: str) -> float | None:
    cleaned = text.strip().replace("×", "*").replace("÷", "/").replace("^", "**")
    cleaned = re.sub(r"\bpi\b", str(math_pi()), cleaned)
    if not re.fullmatch(r"[0-9+\-*/().\s e*]+", cleaned):
        return None
    if not re.search(r"[0-9]", cleaned) or not re.search(r"[+\-*/]", cleaned):
        return None
    try:
        value = _evaluate(ast.parse(cleaned, mode="eval"))
    except (SyntaxError, ValueError, ZeroDivisionError, TypeError):
        return None
    return float(value) if isinstance(value, (int, float)) else None


def math_pi() -> float:
    import math
    return math.pi


# --------------------------------------------------------------------------
# 4. The answer engine
# --------------------------------------------------------------------------
def _best_match(question: str, knowledge=None):
    """The highest-scoring knowledge-base entry for a question, or ``None``.

    Matching is deliberately plain substring scoring: no network, no model, no
    network request - just strings compared against strings. A match needs a
    score of at least 3, so a single loose word is not enough to trigger it.
    """
    text = question.lower()
    best, best_score = None, 0
    for entry in (KB if knowledge is None else knowledge):
        score = sum(3 for key in entry["keys"] if key in text)
        score += sum(1 for word in entry["keys"][0].split() if word in text)
        if score > best_score:
            best, best_score = entry, score
    return best if best_score >= 3 else None


def _chapter_tools(chapter: int):
    """The knowledge base and calculators belonging to one chapter."""
    import importlib

    from . import curriculum

    if chapter == 1:
        return KB, []
    try:
        module = importlib.import_module(f".tutor_kb.ch{chapter:02d}",
                                         package=__package__)
    except ModuleNotFoundError:
        return [], []
    return getattr(module, "KB", []), getattr(module, "CALCULATORS", [])


def _run_calculator(question: str, calculators):
    """Try each chapter calculator in turn and return the first reply that fits."""
    for tool in calculators:
        pattern = tool.get("pattern")
        if pattern is None:
            continue
        match = re.search(pattern, question)
        if match:
            try:
                return tool["reply"](*match.groups())
            except Exception as error:          # a bad entry must not break the tutor
                return f"That calculation did not work out ({error}). Try the numbers again."
    return None


def answer(question: str, chapter: int = 1) -> str:
    """Return a plain-language reply. Pure function apart from reading data.

    Shared calculators - units, significant figures, uncertainty, arithmetic and
    dimensional lookup - work in every chapter, because those tools are useful
    everywhere. On top of them the tutor consults the knowledge base belonging to
    the chapter the learner is actually in.
    """
    text = (question or "").strip()
    if not text:
        return f"Ask me something about Chapter {chapter}."

    lowered = text.lower().rstrip("?!.")
    if lowered in GREETINGS:
        return GREETINGS[lowered]

    # significant figures
    if re.search(r"sig(nificant)?\s*fig|how many (sf|significant)", lowered):
        digits = re.search(r"-?\d+(?:\.\d+)?", text)
        if digits:
            result = pc.analyse_significant_figures(digits.group(0))
            if result["valid"]:
                return (f"**{digits.group(0)} has {result['count']} significant "
                        f"figure{'s' if result['count'] != 1 else ''}.** {result['note']}")
        return ("Tell me the number, for example: *how many sig figs in 0.00250*.")

    # unit conversion
    match = _CONVERSION_RE.search(text)
    if match:
        value, source, target = float(match.group(1)), match.group(2), match.group(3)
    else:
        match = _FIND_RE.search(text)
        value = source = target = None
        if match:
            target, value, source = match.group(1), float(match.group(2)), match.group(3)
    if match:
        converted = _convert_value(value, source, target)
        if converted:
            out, _ = converted
            return (f"**{value:g} {source} = {out:g} {target}**\n\n"
                    "Worked as: change the first unit into the base unit, then change that "
                    "into the target unit. For area and volume the length factor is squared "
                    "or cubed.")
        return ("I cannot do that conversion — the two units measure different things, or "
                "I do not know one of them yet. Try *convert 90 km/h to m/s* or "
                "*convert 2.0 g to kg*.")

    # uncertainty given as "a ± b times/and c ± d"
    unc = re.match(r"^\s*(-?[\d.]+)\s*±\s*([\d.]+)\s*[x*·]\s*(-?[\d.]+)\s*±\s*([\d.]+)\s*$",
                   text)
    if unc:
        a, ua, b, ub = (float(unc.group(i)) for i in range(1, 5))
        product = a * b
        rel = pc.relative_uncertainty_quadrature([(1, ua / a), (1, ub / b)])
        worst = pc.relative_uncertainty_maximum([(1, ua / a), (1, ub / b)])
        return (f"**{a:g} × {b:g} = {product:g}**\n\n"
                f"Independent (quadrature): relative uncertainty = {rel:.4f} "
                f"→ **± {abs(product) * rel:.3g}** "
                f"({rel * 100:.2f} %).\n\n"
                f"Maximum (limiting): {worst:.4f} → **± {abs(product) * worst:.3g}** "
                f"({worst * 100:.2f} %).\n\n"
                f"The maximum method always gives the wider interval. Use one convention "
                f"and say which one you used.")

    # plain arithmetic
    if re.search(r"[\d)]\s*[-+*/^×÷]\s*[\d(]|\bsqrt\b", lowered):
        expr = lowered.replace("sqrt(", "0*(")
        calculated = _calculate(text)
        if "sqrt" in lowered:
            import math
            inner = re.search(r"sqrt\(\s*([\d.]+)\s*\)", lowered)
            if inner:
                return f"√{inner.group(1)} = {math.sqrt(float(inner.group(1))):.6g}"
        if calculated is not None:
            return f"**{text.strip()} = {calculated:.6g}**"

    # dimensional lookup
    dim_words = {"speed": pc.dims(L=1, T=-1), "velocity": pc.dims(L=1, T=-1),
                 "acceleration": pc.dims(L=1, T=-2), "force": pc.dims(M=1, L=1, T=-2),
                 "energy": pc.dims(M=1, L=2, T=-2), "work": pc.dims(M=1, L=2, T=-2),
                 "power": pc.dims(M=1, L=2, T=-3), "pressure": pc.dims(M=1, L=-1, T=-2),
                 "density": pc.dims(M=1, L=-3), "momentum": pc.dims(M=1, L=1, T=-1),
                 "area": pc.dims(L=2), "volume": pc.dims(L=3), "mass": pc.dims(M=1),
                 "length": pc.dims(L=1), "time": pc.dims(T=1)}
    if re.search(r"dimension(s)? of|what are the dimensions", lowered):
        for word, value in dim_words.items():
            if word in lowered:
                return (f"The dimensions of **{word}** are **{pc.dim_unicode(value)}**.\n\n"
                        f"Remember: M = mass, L = length, T = time. These never change, "
                        f"whatever unit you use.")
        return ("Tell me the quantity, e.g. *dimensions of force*. I know speed, velocity, "
                "acceleration, force, energy, work, power, pressure, density, momentum, "
                "area, volume, mass, length and time.")

    knowledge, calculators = _chapter_tools(chapter)

    reply = _run_calculator(text, calculators)
    if reply is not None:
        return reply

    hit = _best_match(lowered, knowledge)
    if hit:
        return hit["answer"]

    fallback = [entry["keys"][0] for entry in (knowledge or KB)[:6]]
    return ("I do not know that one yet, and I would rather say so than guess.\n\n"
            "Try asking about:\n"
            + "\n".join(f"• {s}" for s in fallback)
            + "\n\nor type *help* to see what I can calculate.")


def suggestions(chapter: int = 1) -> list[str]:
    """Example questions, starting with the ones that suit this chapter."""
    # These four are answered by the shared tools - unit conversion, significant
    # figures, uncertainty and dimensional lookup - which exist in every chapter.
    shared = [
        "Convert 90 km/h to m/s",
        "How many sig figs in 0.00250?",
        "Dimensions of force",
        "2.0 ± 0.1 x 3.0 ± 0.1",
    ]
    if chapter == 1:
        return ["What is a physical quantity?", "Accuracy vs precision?"] + shared + [
            "Why do all measurements have uncertainty?",
            "What are the seven SI base units?",
        ]
    knowledge, _ = _chapter_tools(chapter)
    return [entry["keys"][0] for entry in knowledge[:3]] + shared[:3]


def random_question(chapter: int = 1) -> str:
    """A practice question from this chapter that the learner has not seen yet."""
    from . import curriculum

    prefix = f"c{chapter}_"
    seen = {k[len(prefix):] for k in st.session_state.get(f"{prefix}practice_results", {})}
    pool = curriculum.chapter_data(chapter).PRACTICE_QUESTIONS
    unseen = [q for q in pool if q["id"] not in seen] or pool
    return random.choice(unseen)["prompt"]


# --------------------------------------------------------------------------
# 5. Chat interface
# --------------------------------------------------------------------------
def render(chapter: int = 1) -> None:
    """Draw the tutor's chat panel for one chapter."""
    log_key = f"chat_log_{chapter}"
    if log_key not in st.session_state:
        st.session_state[log_key] = [
            {"who": "tutor",
             "text": "Hi — I am the **Atlas Tutor**. I live inside this page: no API key, "
                     "no internet, no account. Ask me for a simple explanation, a unit "
                     "conversion, a significant-figure count or an uncertainty calculation."}
        ]

    st.markdown(
        f'<div class="atlas-card" style="border-color:#2dd4bf">'
        f'<div class="kicker">OFFLINE TUTOR · RUNS ON YOUR DEVICE</div>'
        f"<div class='body'>No API key and no network request are used. The answers come from "
        f"this chapter's own content and from the same formulas the rest of the app uses.</div>"
        f"</div>",
        unsafe_allow_html=True,
    )

    quick = st.columns(4)
    for column, prompt in zip(quick, suggestions(chapter)[:4]):
        if column.button(prompt, key=f"{log_key}_qs_{prompt}", use_container_width=True):
            st.session_state[log_key].append({"who": "user", "text": prompt})
            st.session_state[log_key].append({"who": "tutor",
                                              "text": answer(prompt, chapter)})

    for message in st.session_state[log_key]:
        role = "user" if message["who"] == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(message["text"])

    typed = st.chat_input("Ask the offline tutor…")
    if typed:
        st.session_state[log_key].append({"who": "user", "text": typed})
        with st.chat_message("user"):
            st.markdown(typed)
        reply = answer(typed, chapter)
        st.session_state[log_key].append({"who": "tutor", "text": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

    more = st.columns(3)
    if more[0].button("🎲 Quiz me", key=f"{log_key}_quiz", use_container_width=True):
        question = random_question(chapter)
        st.session_state[log_key].append({"who": "user", "text": "Quiz me"})
        st.session_state[log_key].append(
            {"who": "tutor", "text": f"**Quick check.** {question}"})
    if more[1].button("🧹 Clear chat", key=f"{log_key}_clear", use_container_width=True):
        st.session_state[log_key] = []
        st.rerun()
    if more[2].button("💡 More ideas", key=f"{log_key}_more", use_container_width=True):
        st.session_state[log_key].append(
            {"who": "tutor",
             "text": "More things I can do:\n"
                     "• *convert 2.0 g to kg*\n"
                     "• *how many sig figs in 1500*\n"
                     "• *dimensions of pressure*\n"
                     "• *12.5 * 4.2*\n"
                     "• *What is homogeneity?*"})
