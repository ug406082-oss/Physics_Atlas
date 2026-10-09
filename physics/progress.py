"""Session progress tracking for the 13 Chapter 1 learning outcomes.

Everything lives in ``st.session_state`` for the current browser session only.
No personal data is stored or sent anywhere.
"""

from __future__ import annotations

import streamlit as st

from . import data as D

# Status levels, in increasing order of mastery.
NOT_STARTED = "Not started"
EXPLORED = "Explored"
PRACTISED = "Practised"
MASTERED = "Mastered"

_ORDER = {NOT_STARTED: 0, EXPLORED: 1, PRACTISED: 2, MASTERED: 3}


def _store() -> dict:
    if "slo_progress" not in st.session_state:
        st.session_state["slo_progress"] = {
            s["id"]: {"viewed": False, "correct": 0, "wrong": 0} for s in D.SLOS
        }
    return st.session_state["slo_progress"]


def mark_viewed(slo_ids) -> None:
    """Record that the teaching station for these outcomes has been opened."""
    store = _store()
    for slo_id in slo_ids:
        if slo_id in store:
            store[slo_id]["viewed"] = True


def record_answer(slo_id: str, correct: bool) -> None:
    """Record one guided-practice answer for an outcome."""
    store = _store()
    if slo_id not in store:
        return
    store[slo_id]["viewed"] = True
    if correct:
        store[slo_id]["correct"] += 1
    else:
        store[slo_id]["wrong"] += 1


def status_of(slo_id: str) -> str:
    entry = _store().get(slo_id, {})
    correct = entry.get("correct", 0)
    wrong = entry.get("wrong", 0)
    if correct >= 1 and correct >= wrong:
        return MASTERED
    if correct + wrong >= 1:
        return PRACTISED
    if entry.get("viewed"):
        return EXPLORED
    return NOT_STARTED


def level_of(slo_id: str) -> int:
    return _ORDER[status_of(slo_id)]


def is_mastered(slo_id: str) -> bool:
    return status_of(slo_id) == MASTERED


def counts() -> dict:
    tally = {NOT_STARTED: 0, EXPLORED: 0, PRACTISED: 0, MASTERED: 0}
    for slo in D.SLOS:
        tally[status_of(slo["id"])] += 1
    return tally


def mastered_count() -> int:
    return counts()[MASTERED]


def touched_count() -> int:
    tally = counts()
    return tally[EXPLORED] + tally[PRACTISED] + tally[MASTERED]


def fraction_mastered() -> float:
    return mastered_count() / len(D.SLOS)


def reset() -> None:
    st.session_state.pop("slo_progress", None)


def badge(status: str) -> str:
    """HTML pill for a status, using the theme classes."""
    colour = {
        MASTERED: "good",
        PRACTISED: "info",
        EXPLORED: "warn",
        NOT_STARTED: "mute",
    }[status]
    return f'<span class="pill pill-{colour}">{status.upper()}</span>'
