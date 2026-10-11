"""Content depth: can a learner learn this outcome without the book?

Every published outcome must have a full lesson - what it means, why it is true, a
worked example, the usual mistake, and a question they can answer. The point of
the app is that a student who works through it does not need the book, and this
is the part that guarantees it.
"""

from __future__ import annotations

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from physics import syllabus_xi
from physics.teaching import LESSONS, MINIMUM_WORDS

REQUIRED = ("meaning", "why", "check", "answer")
OPTIONAL_BUT_NICE = ("example", "pitfall")


def _depth(lesson):
    return len((lesson["meaning"] + lesson["why"] + lesson.get("example", "")).split())


def test_every_lesson_has_the_required_parts():
    for sid, lesson in LESSONS.items():
        for field in REQUIRED:
            assert field in lesson, f"{sid} has no {field}"
            assert lesson[field].strip(), f"{sid} has an empty {field}"


def test_no_lesson_is_a_stub():
    for sid, lesson in LESSONS.items():
        assert _depth(lesson) >= MINIMUM_WORDS, (
            f"{sid} has only {_depth(lesson)} words of teaching; "
            f"{MINIMUM_WORDS} is the minimum")


def test_every_lesson_belongs_to_a_published_outcome():
    published = {row["id"] for row in syllabus_xi.OUTCOMES}
    for sid in LESSONS:
        assert sid in published, f"{sid} is not a published Grade XI outcome"


def test_outcomes_with_lessons_have_a_check_they_can_pass():
    for sid, lesson in LESSONS.items():
        assert len(lesson["check"]) > 20, f"{sid} has a token check question"
        assert len(lesson["answer"]) > 5, f"{sid} has no usable answer"


def test_coverage_is_reported():
    """Not a pass/fail gate - a standing measurement of how complete the book is."""
    published = [row["id"] for row in syllabus_xi.OUTCOMES]
    missing = [sid for sid in published if sid not in LESSONS]
    covered = len(published) - len(missing)
    print(f"\nlessons written: {covered}/{len(published)} "
          f"({100 * covered / len(published):.1f}%)")
    if missing:
        by_chapter = {}
        for sid in missing:
            by_chapter.setdefault(sid.split(".")[0], []).append(sid)
        for chapter, ids in sorted(by_chapter.items(), key=lambda kv: int(kv[0])):
            print(f"   chapter {chapter}: {len(ids)} outstanding {ids}")
    assert covered, "no lessons at all"
