"""Physics Atlas — an interactive Grade XI physics field guide.

Run locally with:  streamlit run streamlit_app.py
Entry point for Streamlit Community Cloud.

Screens
-------
1. Chapter picker  — the only thing on the first screen.
2. Chapter world   — the learning stations for one chapter.
3. Mastery report  — what you now know, shown when you leave the chapter.
"""

from __future__ import annotations

import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from physics import chapter1
from physics import data as D
from physics import progress as P
from physics import visuals as V
from physics.theme import inject_css, metric_row, pill

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
# Screen 1 — the chapter picker (the whole first screen)
# --------------------------------------------------------------------------
def _chapter_home():
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

    columns = st.columns(2)
    for index, chapter in enumerate(D.CHAPTERS):
        column = columns[index % 2]
        with column:
            _chapter_card(chapter)
            st.write("")


def _chapter_card(chapter: dict) -> None:
    if chapter["available"]:
        state = (pill("OPEN NOW", "good") + pill("13 OUTCOMES", "info")
                 + pill("OFFLINE AI TUTOR", "warn"))
        css_class = "chapter-card live"
        button_label = f"Enter Chapter {chapter['number']} →"
        disabled = False
    else:
        state = pill("LOCKED", "mute")
        css_class = "chapter-card locked"
        button_label = "Coming soon"
        disabled = True

    st.markdown(
        f'<div class="{css_class}">'
        f'<div><div class="chapter-no">CHAPTER {chapter["number"]:02d}</div>'
        f'<div class="chapter-title">{chapter["title"]}</div>'
        f'<div class="chapter-blurb">{chapter["blurb"]}</div></div>'
        f"<div style='margin-top:10px'>{state}</div>"
        f"</div>",
        unsafe_allow_html=True,
    )
    if st.button(button_label, key=f"open_{chapter['number']}", use_container_width=True,
                 type="primary" if chapter["available"] else "secondary",
                 disabled=disabled):
        st.session_state["active_chapter"] = chapter["number"]
        st.session_state["view"] = "chapter"
        st.rerun()


# --------------------------------------------------------------------------
# Screen 2 — the chapter world
# --------------------------------------------------------------------------
def _chapter_world():
    chapter = next(c for c in D.CHAPTERS if c["number"] == ACTIVE)
    top = st.columns([1, 4, 1])
    with top[0]:
        if st.button("← Leave chapter", key="leave_top", use_container_width=True):
            st.session_state["view"] = "report"
            st.rerun()
    with top[1]:
        st.markdown(
            f'<div style="text-align:center"><span class="chapter-no">CHAPTER '
            f'{chapter["number"]:02d}</span> '
            f'<span style="color:#eef6ff;font-weight:700">{chapter["title"]}</span></div>',
            unsafe_allow_html=True,
        )
    with top[2]:
        st.markdown(
            f'<div style="text-align:right">{pill(f"{P.mastered_count()}/13 mastered", "info")}'
            f"</div>", unsafe_allow_html=True,
        )

    chapter1.render()

    st.divider()
    bottom = st.columns([1, 2, 1])
    with bottom[1]:
        if st.button("🎓 Leave chapter — show what I learned", key="leave_bottom",
                     use_container_width=True, type="primary"):
            st.session_state["view"] = "report"
            st.rerun()


# --------------------------------------------------------------------------
# Screen 3 — the mastery report shown on the way out
# --------------------------------------------------------------------------
def _mastery_report():
    tally = P.counts()
    st.markdown(
        """
        <div style="text-align:center;padding:8px 0">
          <div class="kicker">CHAPTER 1 · EXIT REPORT</div>
          <h1 style="margin:.15rem 0">What you now know</h1>
          <p style="color:#9fb4cc;margin:0">
            Every outcome from the syllabus, in plain words, with the status you earned.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    ring_col, meter_col = st.columns([1, 2])
    with ring_col:
        st.markdown(
            V.progress_ring(P.fraction_mastered(), f"{P.mastered_count()} of {len(D.SLOS)} outcomes"),
            unsafe_allow_html=True,
        )
    with meter_col:
        metric_row([
            ("Mastered", str(tally[P.MASTERED])),
            ("Practised", str(tally[P.PRACTISED])),
            ("Explored", str(tally[P.EXPLORED])),
            ("Not started", str(tally[P.NOT_STARTED])),
        ])
        if P.mastered_count() == len(D.SLOS):
            st.success("Outstanding — you have mastered all 13 outcomes of Chapter 1.")
        else:
            remaining = len(D.SLOS) - P.mastered_count()
            st.info(f"{remaining} outcome{'s' if remaining != 1 else ''} still to master. "
                    "Answer one practice question correctly for each one, then come back.")

    st.subheader("Your outcome report")
    for slo in D.SLOS:
        status = P.status_of(slo["id"])
        st.markdown(
            f'<div class="atlas-card">'
            f'<div style="display:flex;gap:14px;align-items:flex-start;flex-wrap:wrap">'
            f'<div class="mono" style="color:#5eead4;font-weight:700;min-width:70px">'
            f'{slo["id"]}</div>'
            f'<div style="flex:1;min-width:280px">'
            f'<div style="color:#eef6ff;font-weight:600;font-size:1.02rem">{slo["simple"]}</div>'
            f'<div style="color:#9fb4cc;font-size:.82rem;margin-top:6px">'
            f'<b>You studied it in:</b> {slo["taught"]} &nbsp;·&nbsp; '
            f'<b>Official wording:</b> {slo["text"]}</div></div>'
            f'<div style="min-width:120px;text-align:right">{P.badge(status)}</div>'
            f'</div></div>',
            unsafe_allow_html=True,
        )

    st.write("")
    back, revise = st.columns(2)
    with back:
        if st.button("← Back to the chapter world", key="report_back", use_container_width=True):
            st.session_state["view"] = "chapter"
            st.rerun()
    with revise:
        if st.button("⛳ Go to the chapter picker", key="report_home", use_container_width=True,
                     type="primary"):
            st.session_state["view"] = "chapters"
            st.rerun()


# --------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------
if VIEW == "chapter":
    _chapter_world()
elif VIEW == "report":
    _mastery_report()
else:
    _chapter_home()
