"""Physics Atlas — an interactive Grade XI physics field guide.

Run locally with:  streamlit run streamlit_app.py
Entry point for Streamlit Community Cloud.

Screens
-------
1. Chapter picker  — the only thing on the first screen.
2. Chapter world   — the learning stations for one chapter.
3. Mastery report  — what you now know, shown when you leave the chapter.

Everything here is routed through :mod:`physics.curriculum` and
:mod:`physics.engine`, so adding a chapter means adding two files under
``physics/chapters`` and nothing in this file at all.
"""

import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from physics import curriculum, engine, progress as P, visuals as V
from physics.theme import GREEN, MUTED, inject_css, metric_row, pill

st.set_page_config(
    page_title="Physics Atlas | Grade XI Physics",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()

VIEW = st.session_state.setdefault("view", "chapters")
ACTIVE = st.session_state.setdefault("active_chapter", 1)


# --------------------------------------------------------------------------
# Screen 1: the chapter picker
# --------------------------------------------------------------------------

def _chapter_home() -> None:
    st.markdown(
        """
        <div style="text-align:center;padding:10px 0 4px">
          <div class="kicker">PHYSICS ATLAS · GRADE XI</div>
          <h1 style="margin:.15rem 0">Choose a chapter</h1>
          <p style="color:#9fb4cc;font-size:1.02rem;margin:0">
            Enter a chapter, explore it as a world of interactive stations, and leave knowing
            every learning outcome.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    totals = P.book_counts()
    total_outcomes = P.book_outcomes()
    head, ring = st.columns([3, 1])
    with head:
        metric_row([
            ("Chapters", str(len(curriculum.CHAPTERS))),
            ("Learning outcomes", str(total_outcomes)),
            ("Mastered so far", str(totals[P.MASTERED])),
            ("Explored or better", str(total_outcomes - totals[P.NOT_STARTED])),
        ])
    with ring:
        st.markdown(
            V.progress_ring(P.book_mastered() / total_outcomes if total_outcomes else 0.0,
                            "of the whole book"),
            unsafe_allow_html=True,
        )

    columns = st.columns(2)
    for index, slot in enumerate(engine.chapter_slots()):
        with columns[index % 2]:
            _chapter_card(slot)
            st.write("")


def _go(target: str, chapter: int | None = None) -> None:
    """Navigation callback for every button in the app.

    The destination is set here, in the callback, rather than after the button
    and then followed by ``st.rerun()``. Streamlit already reruns the script
    after a button is pressed, and a callback runs *before* that rerun, so the
    new screen renders on the first pass.

    These buttons must NOT be wrapped in ``@st.fragment``. A widget inside a
    fragment reruns only that fragment, so the router at the bottom of this file
    would never re-execute and the screen would never change - "Enter chapter"
    would do nothing. A button in the main script gets an app-wide rerun, so the
    callback's state change is picked up by the router on the same pass.

    Nor can this callback ask for the rerun itself: on streamlit 1.40.2
    ``st.rerun()`` inside a widget callback is swallowed with "Calling
    st.rerun() within a callback is a no-op" (``session_state._call_callbacks``),
    so it would neither rerun the app nor navigate.
    """
    if chapter is not None:
        st.session_state["active_chapter"] = chapter
    st.session_state["view"] = target


def _chapter_card(slot: dict) -> None:
    number = slot["number"]
    outcomes = slot.get("slo_count")
    if slot["available"]:
        state = (pill("OPEN NOW", "good")
                 + pill(f"{outcomes} OUTCOMES" if outcomes else "OUTCOMES", "info")
                 + pill(f"{slot['stations']} STATIONS" if slot.get("stations") else "STATIONS", "warn")
                 + pill("OFFLINE AI TUTOR", "mute"))
        css_class = "chapter-card live"
        button_label = f"Enter Chapter {number} →"
        disabled = False
    else:
        state = pill("LOCKED", "mute")
        css_class = "chapter-card locked"
        button_label = "Coming soon"
        disabled = True

    done = P.mastered_count(number) if slot["available"] else 0
    if done and outcomes:
        state += pill(f"{done}/{outcomes} MASTERED", "good")

    st.markdown(
        f'<div class="{css_class}">'
        f'<div><div class="chapter-no">CHAPTER {number:02d}</div>'
        f'<div class="chapter-title">{slot["title"]}</div>'
        f'<div class="chapter-blurb">{slot["blurb"]}</div></div>'
        f"<div style='margin-top:10px'>{state}</div>"
        f"</div>",
        unsafe_allow_html=True,
    )
    st.button(button_label, key=f"open_{number}", use_container_width=True,
              type="primary" if slot["available"] else "secondary",
              disabled=disabled, on_click=_go, args=("chapter", number))


# --------------------------------------------------------------------------
# Screen 2: the chapter world
# --------------------------------------------------------------------------

def _leave_chapter(key: str, label: str, primary: bool = False) -> None:
    """One of the two ways out of a chapter.

    Deliberately not a fragment: see ``_go``. The chapter world re-renders on
    the way to the report, which costs one pass over the chapter's stations.
    """
    st.button(label, key=key, use_container_width=True,
              type="primary" if primary else "secondary",
              on_click=_go, args=("report",))


def _chapter_world() -> None:
    entry = curriculum.chapter(ACTIVE)
    spec = curriculum.chapter_ui(ACTIVE).SPEC
    mastered = P.mastered_count(ACTIVE)
    total = len(spec.slos)

    top = st.columns([1, 2, 1])
    with top[0]:
        _leave_chapter("leave_top", "← Leave chapter")
    with top[1]:
        st.write("")
    with top[2]:
        st.markdown(
            pill(f"{mastered}/{total} mastered", GREEN if mastered else MUTED),
            unsafe_allow_html=True,
        )

    curriculum.chapter_ui(ACTIVE).render()

    st.divider()
    bottom = st.columns([1, 2, 1])
    with bottom[1]:
        _leave_chapter("leave_bottom",
                       "🎓 Leave chapter — show what I learned", primary=True)

    st.caption(f"Chapter {entry['number']} of {len(curriculum.CHAPTERS)} · "
               f"{total} learning outcomes · "
               "nothing is saved beyond this browser session.")



# --------------------------------------------------------------------------
# Screen 3: the exit report
# --------------------------------------------------------------------------

def _mastery_report() -> None:
    spec = curriculum.chapter_ui(ACTIVE).SPEC
    engine.exit_report(spec)

    st.divider()
    bottom = st.columns([1, 2, 1])
    with bottom[0]:
        _back_to_chapter()
    with bottom[2]:
        _leave_view("report_home", "⛳ Go to the chapter picker", "chapters")


def _leave_view(key: str, label: str, target: str,
                primary: bool = False) -> None:
    """Switch to another screen. Not a fragment - see ``_go``."""
    st.button(label, key=key, use_container_width=True,
              type="primary" if primary else "secondary",
              on_click=_go, args=(target,))


def _back_to_chapter() -> None:
    """The report's only control.

    It used to call ``_leave_view``, which was itself a fragment; nesting one
    fragment inside another gives the inner one an identity derived from the
    outer's. Both are now plain functions, so neither problem applies.
    """
    st.button("← Back to the chapter world", key="report_back",
              use_container_width=True, type="secondary",
              on_click=_go, args=("chapter",))


# --------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------

if VIEW == "chapter":
    _chapter_world()
elif VIEW == "report":
    _mastery_report()
else:
    _chapter_home()
