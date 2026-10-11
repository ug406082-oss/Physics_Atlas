"""Session progress tracking for the learning outcomes of every chapter.

Each chapter keeps its own tally so that mastering one chapter never inflates
another. Everything lives in ``st.session_state`` for the current browser
session only - no personal data is stored and nothing is sent anywhere.
"""

from __future__ import annotations

import streamlit as st

from . import curriculum

# Status levels, in increasing order of mastery.
NOT_STARTED = "Not started"
EXPLORED = "Explored"
PRACTISED = "Practised"
MASTERED = "Mastered"

_ORDER = {NOT_STARTED: 0, EXPLORED: 1, PRACTISED: 2, MASTERED: 3}

_KEY = "slo_progress_{}"


def _store(chapter: int) -> dict:
    """The mastery tally for one chapter, created on first use."""
    key = _KEY.format(chapter)
    if key not in st.session_state:
        st.session_state[key] = {
            slo_id: {"viewed": False, "correct": 0, "wrong": 0}
            for slo_id in curriculum.slo_ids(chapter)
        }
    return st.session_state[key]


def mark_viewed(chapter: int, slo_ids) -> None:
    """Record that the teaching station for these outcomes has been opened."""
    store = _store(chapter)
    for slo_id in slo_ids:
        if slo_id in store:
            store[slo_id]["viewed"] = True


def record_answer(chapter: int, slo_id: str, correct: bool) -> None:
    """Record one practice answer for an outcome of this chapter."""
    store = _store(chapter)
    if slo_id not in store:
        return
    store[slo_id]["viewed"] = True
    if correct:
        store[slo_id]["correct"] += 1
    else:
        store[slo_id]["wrong"] += 1


def status_of(chapter: int, slo_id: str) -> str:
    """The mastery level earned so far for one outcome.

    ``Mastered`` needs at least one correct answer and at least as many correct
    answers as wrong ones, so a single lucky guess after several misses does
    not count.
    """
    entry = _store(chapter).get(slo_id, {})
    correct = entry.get("correct", 0)
    wrong = entry.get("wrong", 0)
    if correct >= 1 and correct >= wrong:
        return MASTERED
    if correct + wrong >= 1:
        return PRACTISED
    if entry.get("viewed"):
        return EXPLORED
    return NOT_STARTED


def level_of(chapter: int, slo_id: str) -> int:
    """The status as a number from 0 (not started) to 3 (mastered)."""
    return _ORDER[status_of(chapter, slo_id)]


def is_mastered(chapter: int, slo_id: str) -> bool:
    return status_of(chapter, slo_id) == MASTERED


def counts(chapter: int) -> dict:
    """How many of this chapter's outcomes sit at each status."""
    tally = {NOT_STARTED: 0, EXPLORED: 0, PRACTISED: 0, MASTERED: 0}
    for slo_id in curriculum.slo_ids(chapter):
        tally[status_of(chapter, slo_id)] += 1
    return tally


def mastered_count(chapter: int) -> int:
    return counts(chapter)[MASTERED]


def touched_count(chapter: int) -> int:
    tally = counts(chapter)
    return tally[EXPLORED] + tally[PRACTISED] + tally[MASTERED]


def fraction_mastered(chapter: int) -> float:
    ids = curriculum.slo_ids(chapter)
    return mastered_count(chapter) / len(ids) if ids else 0.0


def outcome_count(chapter: int) -> int:
    return len(curriculum.slo_ids(chapter))


def reset(chapter: int) -> None:
    """Forget everything recorded for one chapter."""
    st.session_state.pop(_KEY.format(chapter), None)


def badge(status: str) -> str:
    """HTML pill for a status, using the theme classes."""
    colour = {
        MASTERED: "good",
        PRACTISED: "info",
        EXPLORED: "warn",
        NOT_STARTED: "mute",
    }[status]
    return f'<span class="pill pill-{colour}">{status.upper()}</span>'


# --------------------------------------------------------------------------
# Book-wide totals, used by the chapter picker
# --------------------------------------------------------------------------

def book_counts() -> dict:
    """Status totals across every chapter that has been opened."""
    tally = {NOT_STARTED: 0, EXPLORED: 0, PRACTISED: 0, MASTERED: 0}
    for entry in curriculum.CHAPTERS:
        if _KEY.format(entry["number"]) not in st.session_state:
            continue
        for status, value in counts(entry["number"]).items():
            tally[status] += value
    return tally


def book_mastered() -> int:
    return book_counts()[MASTERED]


def book_outcomes() -> int:
    """Every outcome in the syllabus."""
    return sum(len(curriculum.slo_ids(entry["number"])) for entry in curriculum.CHAPTERS)
