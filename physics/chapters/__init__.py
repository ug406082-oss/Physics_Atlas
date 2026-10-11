"""One data module and one user-interface module per chapter.

``chNN_data`` holds nothing but content - learning outcomes, reference tables,
worked problems and practice questions - and imports nothing from Streamlit, so
the whole curriculum can be imported and checked by a bare Python interpreter.

``chNN`` builds that chapter's :class:`~physics.engine.ChapterSpec` and hands it
to the engine. It is imported only when a learner actually opens the chapter.
"""

from __future__ import annotations

__all__ = ["ch01", "ch01_data", "ch02", "ch02_data", "ch03", "ch03_data",
           "ch04", "ch04_data", "ch05", "ch05_data", "ch06", "ch06_data",
           "ch07", "ch07_data", "ch08", "ch08_data", "ch09", "ch09_data",
           "ch10", "ch10_data"]
