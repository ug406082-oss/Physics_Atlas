"""Pure scientific helpers for Physics Atlas.

This module deliberately has NO dependency on Streamlit, pandas or numpy so
that every function can be unit-tested in isolation and reused by any future
chapter. Dimensions are represented as plain dictionaries mapping a base
dimension symbol to its exponent, for example ``{"M": 1, "L": 2, "T": -2}``.
"""

from __future__ import annotations

import math
import statistics

BASE_DIM_ORDER = ("M", "L", "T", "I", "Th", "N", "J")

BASE_DIM_LATEX = {
    "M": "M",
    "L": "L",
    "T": "T",
    "I": "I",
    "Th": r"\Theta",
    "N": "N",
    "J": "J",
}

BASE_DIM_NAME = {
    "M": "mass",
    "L": "length",
    "T": "time",
    "I": "electric current",
    "Th": "thermodynamic temperature",
    "N": "amount of substance",
    "J": "luminous intensity",
}

_SUPERSCRIPTS = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def _superscript(number: int) -> str:
    return str(number).translate(_SUPERSCRIPTS)


def normalise_dims(dims: dict | None) -> dict:
    """Return a copy of ``dims`` with zero exponents removed."""
    if not dims:
        return {}
    return {k: v for k, v in dims.items() if v}


def dims(**kwargs: int) -> dict:
    """Convenience constructor: ``dims(M=1, L=2, T=-2)``."""
    return normalise_dims(dict(kwargs))


def mul_dims(first: dict, second: dict) -> dict:
    """Dimensions of a product of two quantities."""
    result = dict(first)
    for key, value in second.items():
        result[key] = result.get(key, 0) + value
    return normalise_dims(result)


def div_dims(numerator: dict, denominator: dict) -> dict:
    """Dimensions of a quotient of two quantities."""
    result = dict(numerator)
    for key, value in denominator.items():
        result[key] = result.get(key, 0) - value
    return normalise_dims(result)


def pow_dims(base: dict, exponent: int) -> dict:
    """Dimensions of a quantity raised to an integer power."""
    return normalise_dims({k: v * exponent for k, v in base.items()})


def dims_equal(first: dict, second: dict) -> bool:
    """True when two dimensional expressions are identical."""
    return normalise_dims(first) == normalise_dims(second)


def is_dimensionless(dims: dict) -> bool:
    return not normalise_dims(dims)


def dim_latex(dims: dict) -> str:
    """Return a LaTeX dimension expression such as ``[M L^{2} T^{-2}]``."""
    parts = []
    for key in BASE_DIM_ORDER:
        exponent = normalise_dims(dims).get(key, 0)
        if not exponent:
            continue
        symbol = BASE_DIM_LATEX[key]
        if exponent == 1:
            parts.append(symbol)
        else:
            parts.append(rf"{symbol}^{{{exponent}}}")
    if not parts:
        return r"[\,]"
    return r"\left[" + "\\,".join(parts) + r"\right]"


def dim_unicode(dims: dict) -> str:
    """Return a Unicode dimension expression such as ``[M L² T⁻²]``."""
    parts = []
    for key in BASE_DIM_ORDER:
        exponent = normalise_dims(dims).get(key, 0)
        if not exponent:
            continue
        symbol = BASE_DIM_LATEX[key].replace(r"\Theta", "Θ")
        if exponent == 1:
            parts.append(symbol)
        else:
            parts.append(f"{symbol}{_superscript(exponent)}")
    if not parts:
        return "[dimensionless]"
    return "[" + " ".join(parts) + "]"


def check_homogeneity(lhs_terms: list[dict], rhs_terms: list[dict]) -> dict:
    """Check dimensional homogeneity of an equation.

    ``lhs_terms`` and ``rhs_terms`` are lists of dimensional expressions that
    are added or subtracted on each side. Every term on each side must share
    the same dimensions, and the two sides must match each other.
    """
    lhs_normalised = [normalise_dims(t) for t in lhs_terms]
    rhs_normalised = [normalise_dims(t) for t in rhs_terms]
    lhs_consistent = all(d == lhs_normalised[0] for d in lhs_normalised) if lhs_normalised else False
    rhs_consistent = all(d == rhs_normalised[0] for d in rhs_normalised) if rhs_normalised else False
    sides_match = bool(lhs_normalised and rhs_normalised and lhs_normalised[0] == rhs_normalised[0])
    return {
        "lhs_consistent": lhs_consistent,
        "rhs_consistent": rhs_consistent,
        "sides_match": sides_match,
        "homogeneous": lhs_consistent and rhs_consistent and sides_match,
    }


def solve_pendulum_exponents() -> dict:
    """Solve T = k m^a L^b g^c for the period of a simple pendulum.

    Equating dimensions gives:
        M: a = 0
        L: b + c = 0
        T: -2c = 1
    so a = 0, c = -1/2, b = 1/2, i.e. T is proportional to sqrt(L/g).
    """
    mass_exp = 0
    time_exp = -0.5
    length_exp = -time_exp
    return {
        "a": mass_exp,
        "b": length_exp,
        "c": time_exp,
        "result": "T ∝ sqrt(L / g)",
        "steps": [
            "Assume T = k · mᵃ · Lᵇ · gᶜ, where k is a dimensionless constant.",
            "Write dimensions: [T] = Mᵃ · Lᵇ · (L T⁻²)ᶜ = Mᵃ Lᵇ⁺ᶜ T⁻²ᶜ.",
            "Compare mass: a = 0 (the period does not depend on mass).",
            "Compare time: −2c = 1, so c = −½.",
            "Compare length: b + c = 0, so b = ½.",
            "Therefore T = k · sqrt(L / g). Dimensional analysis fixes the powers "
            "but cannot determine the dimensionless constant k (which is 2π for "
            "small oscillations of a simple pendulum).",
        ],
    }


def analyse_significant_figures(text: str) -> dict:
    """Count significant figures in a value written as text.

    Because trailing zeros carry meaning only as written, this function works
    on the *written* string rather than on a floating-point number.
    """
    if text is None or str(text).strip() == "":
        return {"valid": False, "count": 0, "ambiguous": False,
                "note": "Enter a value such as 0.00250, 1500, 1500. or 1.20e5."}
    raw = str(text).strip().replace(" ", "")
    raw = raw.replace("×", "x").replace("·", "x").replace("−", "-")
    mantissa, exponent = _split_exponent(raw)
    if mantissa in ("", "+", "-", "."):
        return {"valid": False, "count": 0, "ambiguous": False,
                "note": "That does not look like a number."}
    body = mantissa.lstrip("+-")
    digits_only = body.replace(".", "")
    if any(ch not in "0123456789" for ch in digits_only):
        return {"valid": False, "count": 0, "ambiguous": False,
                "note": "Use digits only, for example 3.60 or 2.5e6."}
    count, ambiguous = _count_from_mantissa(body)
    if count == 0:
        return {"valid": True, "count": 0, "ambiguous": True,
                "note": "A value written as zero carries no significant figures; "
                        "write 0.00 or 0.0 to show precision."}
    note = _sig_fig_note(body, ambiguous, exponent)
    return {"valid": True, "count": count, "ambiguous": ambiguous,
            "note": note, "mantissa": body, "exponent": exponent}


def _split_exponent(raw: str) -> tuple[str, str]:
    lowered = raw.lower()
    for marker in ("e", "x10", "*10", "×10"):
        idx = lowered.find(marker)
        if idx != -1:
            return raw[:idx], raw[idx + len(marker):]
    return raw, ""


def _count_from_mantissa(body: str) -> tuple[int, bool]:
    if "." in body:
        digits = body.replace(".", "").lstrip("0")
        if digits == "":
            return 0, True
        return len(digits), False
    stripped = body.lstrip("0")
    if stripped == "":
        return 0, True
    if stripped.endswith("0"):
        core = stripped.rstrip("0")
        return (len(core) if core else 1), True
    return len(stripped), False


def _sig_fig_note(body: str, ambiguous: bool, exponent: str) -> str:
    if ambiguous:
        return ("Ambiguous: trailing zeros before an unwritten decimal point may "
                "or may not be significant. Write a decimal point or use "
                "scientific notation to make the precision explicit.")
    if exponent:
        return "In scientific notation only the mantissa determines significant figures."
    if "." in body:
        return "Trailing zeros after a decimal point are significant."
    if body.lstrip("+-").startswith("0"):
        return "Leading zeros are never significant."
    return "All nonzero digits written are significant."


def round_to_sig_figs(value: float, sig_figs: int) -> float:
    """Round ``value`` to ``sig_figs`` significant figures."""
    if sig_figs < 1:
        raise ValueError("sig_figs must be at least 1")
    if value == 0 or not math.isfinite(value):
        return value
    exponent = math.floor(math.log10(abs(value)))
    decimals = sig_figs - 1 - exponent
    rounded = round(value, decimals)
    return rounded


def format_to_sig_figs(value: float, sig_figs: int) -> str:
    """Return a string for ``value`` shown with the requested significant figures."""
    if sig_figs < 1:
        raise ValueError("sig_figs must be at least 1")
    if value == 0:
        return "0"
    rounded = round_to_sig_figs(value, sig_figs)
    exponent = math.floor(math.log10(abs(value)))
    decimals = sig_figs - 1 - exponent
    if decimals < 0:
        rounded = round(rounded, decimals)
        return f"{int(round(rounded))}"
    return f"{rounded:.{decimals}f}"


def fractional_uncertainty(uncertainty: float, value: float) -> float:
    """Return |uncertainty / value|; returns ``inf`` for a zero value."""
    if value == 0:
        return math.inf
    return abs(uncertainty / value)


def percentage_uncertainty(uncertainty: float, value: float) -> float:
    """Return the uncertainty as a percentage of the value."""
    return fractional_uncertainty(uncertainty, value) * 100.0


def relative_uncertainty_quadrature(terms: list[tuple[float, float]]) -> float:
    """Independent-quantity (first-order) relative uncertainty.

    ``terms`` is a list of ``(exponent, relative_uncertainty)`` pairs for a
    quantity of the form ``k · x1^e1 · x2^e2 ...`` with independent inputs.
    Returns sqrt(sum((e_i · u_i/x_i)^2)).
    """
    total = 0.0
    for exponent, relative in terms:
        total += (exponent * relative) ** 2
    return math.sqrt(total)


def relative_uncertainty_maximum(terms: list[tuple[float, float]]) -> float:
    """Maximum (limiting) relative uncertainty: sum of |exponent · relative|."""
    return sum(abs(exponent) * abs(relative) for exponent, relative in terms)


def propagate_product(value: float, terms: list[tuple[float, float]],
                      method: str = "quadrature") -> dict:
    """Propagate uncertainty for a product/quotient.

    Returns absolute and relative uncertainties for the two supported methods.
    """
    if method == "maximum":
        relative = relative_uncertainty_maximum(terms)
    else:
        relative = relative_uncertainty_quadrature(terms)
    return {"relative": relative, "percentage": relative * 100.0,
            "absolute": abs(value) * relative, "method": method}


def uncertainty_from_absolute_terms(uncertainties: list[float],
                                    method: str = "quadrature") -> float:
    """Combine independent absolute uncertainties for a sum or difference."""
    if method == "maximum":
        return sum(abs(u) for u in uncertainties)
    return math.sqrt(sum(u * u for u in uncertainties))


def summary_statistics(values: list[float]) -> dict:
    """Mean, sample standard deviation and standard error of repeated readings."""
    clean = [v for v in values if v is not None and math.isfinite(v)]
    if not clean:
        return {"n": 0, "mean": None, "stdev": None, "stderr": None,
                "minimum": None, "maximum": None}
    mean = statistics.fmean(clean)
    stdev = statistics.stdev(clean) if len(clean) > 1 else 0.0
    stderr = stdev / math.sqrt(len(clean)) if clean else 0.0
    return {"n": len(clean), "mean": mean, "stdev": stdev, "stderr": stderr,
            "minimum": min(clean), "maximum": max(clean)}


def volume_of_sphere(diameter: float) -> float:
    """Volume of a sphere from its diameter (used in the ball-bearing practical)."""
    radius = diameter / 2.0
    return (4.0 / 3.0) * math.pi * radius ** 3


def density(mass: float, volume: float) -> float:
    """Density = mass / volume; returns ``inf`` for zero volume."""
    if volume == 0:
        return math.inf
    return mass / volume


def convert_prefix(value: float, from_factor: float, to_factor: float) -> float:
    """Convert between two SI prefixes using their multiplying factors."""
    if to_factor == 0:
        raise ValueError("to_factor must be non-zero")
    return value * from_factor / to_factor


def safe_divide(numerator: float, denominator: float) -> float | None:
    """Divide, returning ``None`` instead of raising for a zero denominator."""
    if denominator == 0:
        return None
    return numerator / denominator
