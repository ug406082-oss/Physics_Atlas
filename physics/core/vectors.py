"""Chapter 2 - Scalars and Vectors.

A vector is carried around as a plain ``(x, y)`` tuple of Cartesian components.
Angles are in degrees everywhere they cross a user interface, and radians
internally, because that is how they are measured in the syllabus.

Nothing here imports Streamlit, pandas or NumPy.
"""

from __future__ import annotations

import math

__all__ = [
    "add", "subtract", "scale", "magnitude", "angle_of", "as_tuple",
    "components_from_polar", "polar_from_components", "negate",
    "dot_product", "dot_commutativity_error", "dot_distributivity_error",
    "cross_product", "cross_anticommutativity_error", "angle_between",
    "cross_direction", "project", "perpendicular_component", "resolve",
    "unit_vector", "is_perpendicular", "is_parallel", "momentum",
    "work", "format_vector",
]


# --------------------------------------------------------------------------
# Basic vector algebra
# --------------------------------------------------------------------------

def as_tuple(value) -> tuple:
    """Coerce a vector given as a list, tuple or dict into an ``(x, y)`` tuple."""
    if isinstance(value, dict):
        return float(value["x"]), float(value["y"])
    x, y = value
    return float(x), float(y)


def add(first, second) -> tuple:
    """Component-wise sum ``A + B``."""
    ax, ay = as_tuple(first)
    bx, by = as_tuple(second)
    return ax + bx, ay + by


def subtract(first, second) -> tuple:
    """Component-wise difference ``A - B``."""
    ax, ay = as_tuple(first)
    bx, by = as_tuple(second)
    return ax - bx, ay - by


def negate(vector) -> tuple:
    """``-A``."""
    x, y = as_tuple(vector)
    return -x, -y


def scale(vector, factor: float) -> tuple:
    """``k * A``."""
    x, y = as_tuple(vector)
    return x * factor, y * factor


def magnitude(vector) -> float:
    """The size (magnitude) of a vector: ``sqrt(x^2 + y^2)``."""
    x, y = as_tuple(vector)
    return math.hypot(x, y)


def angle_of(vector) -> float:
    """Direction of a vector measured counter-clockwise from the +x axis.

    Returns degrees in the range 0 <= theta < 360. The zero vector has no
    direction, so its angle is reported as 0.0 and callers should check
    :func:`magnitude` first.
    """
    x, y = as_tuple(vector)
    if x == 0.0 and y == 0.0:
        return 0.0
    return math.degrees(math.atan2(y, x)) % 360.0


def unit_vector(vector) -> tuple:
    """A vector of magnitude 1 pointing the same way. Returns ``(0.0, 0.0)``
    when the input has no magnitude."""
    size = magnitude(vector)
    if size == 0.0:
        return 0.0, 0.0
    return scale(vector, 1.0 / size)


def components_from_polar(size: float, angle_deg: float) -> tuple:
    """Resolve a vector of given magnitude and direction into components.

    ``Ax = A cos(theta)`` and ``Ay = A sin(theta)``, with theta measured from
    the positive x axis.
    """
    radians = math.radians(angle_deg)
    return size * math.cos(radians), size * math.sin(radians)


def polar_from_components(vector) -> tuple:
    """The inverse of :func:`components_from_polar`: returns ``(A, theta)``."""
    return magnitude(vector), angle_of(vector)


# --------------------------------------------------------------------------
# Scalar (dot) product
# --------------------------------------------------------------------------

def dot_product(first, second) -> float:
    """The scalar product ``A . B = Ax Bx + Ay By = A B cos(theta)``.

    The result is a scalar. It is positive when the angle between the vectors
    is acute, negative when it is obtuse, and zero when they are perpendicular.
    """
    ax, ay = as_tuple(first)
    bx, by = as_tuple(second)
    return ax * bx + ay * by


def dot_commutativity_error(first, second) -> float:
    """``|A.B - B.A|``. Should be zero for any pair of vectors."""
    return abs(dot_product(first, second) - dot_product(second, first))


def dot_distributivity_error(first, second, third) -> float:
    """``|A.(B + C) - A.B - A.C|``. Should be zero for any three vectors."""
    return abs(dot_product(first, add(second, third))
               - dot_product(first, second) - dot_product(first, third))


def project(vector, onto) -> tuple:
    """The scalar projection of ``A`` on ``B``: ``A . B_hat``.

    This is the length of the shadow of ``A`` that falls on the direction of
    ``B``. It is negative when the two point more than 90 degrees apart.
    """
    return dot_product(vector, unit_vector(onto))


def perpendicular_component(vector, onto) -> tuple:
    """The vector left after removing the component of ``A`` along ``B``."""
    return subtract(vector, scale(unit_vector(onto), project(vector, onto)))


def resolve(vector, onto) -> dict:
    """Split ``A`` into a part along ``B`` and the remaining perpendicular part."""
    along_scalar = project(vector, onto)
    along_vector = scale(unit_vector(onto), along_scalar)
    across = perpendicular_component(vector, onto)
    return {
        "along": along_vector,
        "across": across,
        "along_scalar": along_scalar,
        "across_scalar": magnitude(across),
        "angle": angle_between(vector, onto),
    }


# --------------------------------------------------------------------------
# Vector (cross) product
# --------------------------------------------------------------------------

def cross_product(first, second) -> float:
    """The z-component of the vector product ``A x B = A B sin(theta) n``.

    In the xy plane the cross product points along the z axis, so only its
    magnitude and sense are kept: positive means out of the page towards the
    observer (anticlockwise from ``A`` to ``B``), negative means into the page.
    """
    ax, ay = as_tuple(first)
    bx, by = as_tuple(second)
    return ax * by - ay * bx


def cross_anticommutativity_error(first, second) -> float:
    """``|A x B + B x A|``. Should be zero, because ``A x B = -(B x A)``."""
    return abs(cross_product(first, second) + cross_product(second, first))


def cross_direction(value: float) -> str:
    """Plain-language sense of a cross product."""
    if value > 1e-12:
        return "out of the page, anticlockwise from the first vector to the second"
    if value < -1e-12:
        return "into the page, clockwise from the first vector to the second"
    return "zero - the two vectors are parallel, so there is no perpendicular component"


def angle_between(first, second) -> float:
    """The angle separating two vectors, in degrees, from 0 to 180."""
    a, b = magnitude(first), magnitude(second)
    if a == 0.0 or b == 0.0:
        return 0.0
    cosine = max(-1.0, min(1.0, dot_product(first, second) / (a * b)))
    return math.degrees(math.acos(cosine))


def is_perpendicular(first, second, tolerance: float = 1e-9) -> bool:
    """True when the scalar product vanishes, i.e. the vectors are at 90 degrees."""
    return abs(dot_product(first, second)) <= tolerance


def is_parallel(first, second, tolerance: float = 1e-9) -> bool:
    """True when the vectors are along the same line (same or opposite sense)."""
    a, b = magnitude(first), magnitude(second)
    if a == 0.0 or b == 0.0:
        return False
    ratio = dot_product(first, second) / (a * b)
    return abs(abs(ratio) - 1.0) <= tolerance


# --------------------------------------------------------------------------
# Every-day uses that tie Chapter 2 to later chapters
# --------------------------------------------------------------------------

def momentum(mass: float, velocity) -> tuple:
    """Momentum ``p = m v`` - a vector because velocity is a vector."""
    return scale(velocity, mass)


def work(force, displacement) -> float:
    """Work ``W = F . d = F d cos(theta)``.

    Positive when the force has a component along the displacement, negative
    when it opposes the motion.
    """
    return dot_product(force, displacement)


def format_vector(vector) -> str:
    """Human-readable ``(x, y)`` for the interface."""
    x, y = as_tuple(vector)
    return f"({x:.3g}, {y:.3g})"
