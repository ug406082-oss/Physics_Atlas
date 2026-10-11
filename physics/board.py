"""The examination board and syllabus this app is built against.

Kept in its own tiny module so that :mod:`physics.curriculum` and every chapter
data file can import it without creating a circular dependency.
"""

from __future__ import annotations

BOARD = "AKU-EB (Aga Khan University Examination Board)"
SYLLABUS = "Physics HSSC Syllabus 2025, Part I (Grade XI)"
SYLLABUS_SOURCE = "https://files.akuebresources.com/2025/07/Physics-XI-XII-Syllabus-2025.pdf"
PART = "Part I"
GRADE = "Grade XI"
