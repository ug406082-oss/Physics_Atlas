"""The shared chapter engine.

A chapter is described by a :class:`ChapterSpec`. The engine turns that
description into a chapter world: an introduction, a live mastery meter, a row
of station tabs and - on the way out - a full report of every learning outcome.

The engine deliberately supplies *building blocks*, not a fixed template. Each
chapter picks the stations it needs, writes its own teaching renderers and its
own diagrams, and reuses only the pieces that are genuinely the same everywhere:
the outcome strip, the worked-problem stepper, the practice grader, the
references list and the exit report. Two chapters should never read as the same
page with the words swapped.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd
import streamlit as st
from streamlit import cache_data

from . import curriculum, progress as P
from .theme import (AMBER, CYAN, GREEN, MUTED, ROSE, TEAL, VIOLET, card,
                    metric_row, pill, section_intro)

__all__ = [
    "Station", "ChapterSpec", "render", "exit_report", "number_or_none",
    "slo_strip", "overview_station", "worked_problems", "practice",
    "references", "render_question", "guidance", "WATCH_OUT", "EXAM_TIP",
    "HONEST_LIMIT", "WHY_IT_MATTERS", "TRY_IT", "slo_cards",
]


# --------------------------------------------------------------------------
# Description of a chapter
# --------------------------------------------------------------------------

@dataclass
class Station:
    """One tab of the chapter world.

    ``slos`` lists the outcome identifiers that station teaches. Opening the tab
    marks them as explored.
    """

    key: str
    label: str
    renderer: object
    slos: list = field(default_factory=list)


@dataclass
class ChapterSpec:
    """Everything the engine needs to build one chapter world."""

    number: int
    title: str
    blurb: str
    tag: str
    intro: str
    stations: list
    slos: list
    key_prefix: str
    big_ideas: list
    worked_problems: list
    practice_questions: list
    references: list
    tutor: object
    route: str = ""
    honesty_pills: list = field(default_factory=list)
    notes: list = field(default_factory=list)

    def ids(self):
        return [row["id"] for row in self.slos]


# --------------------------------------------------------------------------
# Guidance blocks
#
# Every station may drop these in. They are the difference between a page of
# facts and a lesson, so they are part of the engine rather than something each
# chapter reinvents.
# --------------------------------------------------------------------------

WATCH_OUT = "⚠ WATCH OUT"
EXAM_TIP = "🎯 EXAM TIP"
HONEST_LIMIT = "🔬 HONEST LIMIT"
WHY_IT_MATTERS = "💡 WHY IT MATTERS"
TRY_IT = "🧪 TRY IT"


def guidance(kind: str, title: str, body: str) -> None:
    """Draw one guidance block in a consistent, recognisable style."""
    colours = {
        WATCH_OUT: (ROSE, "rgba(251,113,133,.10)"),
        EXAM_TIP: (AMBER, "rgba(251,191,36,.10)"),
        HONEST_LIMIT: (VIOLET, "rgba(167,139,250,.10)"),
        WHY_IT_MATTERS: (CYAN, "rgba(34,211,238,.10)"),
        TRY_IT: (GREEN, "rgba(52,211,153,.10)"),
    }
    colour, tint = colours.get(kind, (MUTED, "rgba(148,163,184,.10)"))
    st.markdown(
        f'<div style="border:1px solid {colour}55;background:{tint};border-radius:14px;'
        f'padding:13px 17px;margin:8px 0 14px">'
        f'<div class="kicker" style="color:{colour}">{kind}</div>'
        f'<div style="color:#f1f7ff;font-weight:600;margin:.2rem 0 .25rem">{title}</div>'
        f'<div class="body" style="color:#c6d6ea;font-size:.94rem">{body}</div></div>',
        unsafe_allow_html=True,
    )


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def number_or_none(text):
    """Parse a learner's typed answer, returning ``None`` when it is not a number."""
    try:
        return float(str(text).strip())
    except (TypeError, ValueError):
        return None


def _fmt(value, places: int = 3) -> str:
    """Format a number for display without a trail of zeros."""
    try:
        return f"{float(value):.{places}g}"
    except (TypeError, ValueError):
        return str(value)


def slo_strip(spec: ChapterSpec) -> None:
    """The live mastery meter shown under the chapter introduction."""
    total = len(spec.slos)
    st.progress(
        P.fraction_mastered(spec.number),
        text=f"Outcomes mastered: {P.mastered_count(spec.number)} of {total} · "
             f"explored {P.touched_count(spec.number)} of {total} · "
             f"leave the chapter to see your full report",
    )


def slo_cards(spec: ChapterSpec) -> None:
    """One card per learning outcome, each showing the status earned so far."""
    for slo in spec.slos:
        status = P.status_of(spec.number, slo["id"])
        st.markdown(
            f'<div class="atlas-card" style="padding:14px 18px;margin:6px 0">'
            f'<div style="display:flex;gap:14px;align-items:flex-start;flex-wrap:wrap">'
            f'<div class="mono" style="color:#5eead4;font-weight:700;min-width:64px">'
            f'{slo["id"]}</div>'
            f'<div style="flex:1;min-width:260px"><div style="color:#eef6ff;font-weight:600">'
            f'{slo["simple"]}</div>'
            f'<div style="color:#9fb4cc;font-size:.82rem;margin-top:4px">Official wording: '
            f'{slo["text"]}</div></div>'
            f'<div>{P.badge(status)}</div></div></div>',
            unsafe_allow_html=True,
        )


# --------------------------------------------------------------------------
# Shared stations
# --------------------------------------------------------------------------

def overview_station(spec: ChapterSpec) -> None:
    """The opening station: the big ideas, the honesty labels and the outcome list.

    Chapters pass their own ``big_ideas`` and ``notes``, so the shape is shared
    but the content is entirely theirs.
    """
    if spec.big_ideas:
        card(
            f"The big ideas of Chapter {spec.number}",
            "".join(f"<p><b>{i}. {heading}</b> {body}</p>"
                    for i, (heading, body) in enumerate(spec.big_ideas, start=1)),
            "START HERE",
        )
    if spec.honesty_pills:
        st.markdown(" ".join(pill(text, kind) for text, kind in spec.honesty_pills),
                    unsafe_allow_html=True)
        st.caption("Every box in this chapter carries one of these labels, so you "
                   "always know where the information came from.")

    if spec.notes:
        for kind, title, body in spec.notes:
            guidance(kind, title, body)

    st.subheader(f"Your {len(spec.slos)} outcomes")
    st.caption(
        "This is what you must be able to do by the end of the chapter. As you open "
        "each station and answer practice questions, the status below changes. Leaving "
        "the chapter shows you this list as a full report."
    )
    slo_cards(spec)

    if spec.route:
        card("Suggested route", f"<p>{spec.route}</p>", "STUDY PLAN")


def worked_problems(spec: ChapterSpec) -> None:
    """Step-by-step worked problems, revealed a stage at a time."""
    if not spec.worked_problems:
        st.info("No worked problems are stored for this chapter yet.")
        return
    st.caption("Work through these with a pencil and paper. Drag the slider to reveal "
               "each stage only when you need it.")
    for problem in spec.worked_problems:
        with st.expander(f"{problem['id']} · {problem['title']}  ({problem['level']})"):
            st.markdown(f"### {problem['title']}")
            st.markdown(f"**Question.** {problem['question']}")
            reveal = st.slider("Reveal solution stages", 0, 3, 0,
                               key=f"{spec.key_prefix}wp_step_{problem['id']}")
            left, right = st.columns(2)
            with left:
                st.markdown("**What you are given**")
                for item in problem["known"]:
                    st.markdown(f"- {item}")
                st.markdown(f"**{problem['find']}**")
                st.markdown("**Equation**")
                st.latex(problem["equation"])
            with right:
                st.markdown("**Before you calculate**")
                for item in problem["conversions"]:
                    st.markdown(f"- {item}")
                st.markdown("**Substitution**")
                st.latex(problem["substitution"])
            if reveal >= 1:
                st.markdown("**Step-by-step calculation**")
                for i, step in enumerate(problem["calculation"], start=1):
                    st.markdown(f"{i}. {step}")
            if reveal >= 2:
                st.markdown("**Unit and dimensional check**")
                st.latex(problem["unit_check"])
                st.success(f"**Answer:** {problem['answer']}")
            if reveal >= 3:
                st.info(f"**On significant figures:** {problem['sig_fig_note']}")
                st.markdown("**Assumptions**")
                for item in problem["assumptions"]:
                    st.markdown(f"- {item}")
    st.caption("All the answers in this station are computed by the app, not typed in by hand.")


def render_question(spec: ChapterSpec, q: dict) -> None:
    """Render and grade one practice question."""
    st.markdown(f"---\n**{q['id']} · {q['category']} · SLO {q['slo']}**")
    st.markdown(q["prompt"])

    results_key = f"{spec.key_prefix}practice_results"
    st.session_state.setdefault(results_key, {})
    key = f"{spec.key_prefix}ans_{q['id']}"
    checked_key = f"{spec.key_prefix}checked_{q['id']}"
    hint_key = f"{spec.key_prefix}hint_{q['id']}"

    if q["type"] == "mcq":
        st.radio("Choose one", q["options"], key=key, index=None,
                 label_visibility="collapsed")
    else:
        st.text_input(f"Your answer ({q.get('unit', 'number')})", key=key,
                      placeholder="type a number")

    button_col, _ = st.columns([1, 5])
    with button_col:
        if st.button("Check", key=f"{spec.key_prefix}chk_{q['id']}"):
            st.session_state[checked_key] = True
    if st.button("Show hint", key=f"{spec.key_prefix}hintbtn_{q['id']}"):
        st.session_state[hint_key] = True

    if st.session_state.get(hint_key):
        st.info(f"**Hint.** {q['hint']}")
    if not st.session_state.get(checked_key):
        if q["type"] == "numeric" and st.session_state.get(key):
            st.caption("Press Check when you are ready.")
        return

    response = st.session_state.get(key)
    if q["type"] == "mcq":
        if response is None:
            st.warning("Choose an option first, then press Check.")
            return
        is_correct = response == q["options"][q["answer"]]
    else:
        typed = number_or_none(response)
        if typed is None:
            st.warning("That does not look like a number. Type digits only, then press Check.")
            return
        is_correct = abs(typed - q["answer"]) <= q.get("tolerance", 0)

    results = st.session_state[results_key]
    first_time = q["id"] not in results
    results[q["id"]] = bool(is_correct)
    if first_time:
        P.record_answer(spec.number, q["slo"], bool(is_correct))

    if is_correct:
        st.success(f"Correct. {q['explanation']}")
    elif q["type"] == "mcq":
        st.error(f"Not yet. The best answer is “{q['options'][q['answer']]}”. {q['explanation']}")
    else:
        st.error(f"Not yet. The expected answer is about {_fmt(q['answer'])} "
                 f"{q.get('unit', '')}. {q['explanation']}")


def practice(spec: ChapterSpec) -> None:
    """The guided-practice station, with a skill filter and a running score."""
    questions = spec.practice_questions
    if not questions:
        st.info("No practice questions are stored for this chapter yet.")
        return

    results_key = f"{spec.key_prefix}practice_results"
    st.session_state.setdefault(results_key, {})

    categories = sorted({q["category"] for q in questions})
    chosen = st.multiselect("Filter by skill (leave empty for all)", categories,
                            key=f"{spec.key_prefix}pr_cats")
    shown = [q for q in questions if not chosen or q["category"] in chosen]

    results = st.session_state[results_key]
    correct = sum(1 for ok in results.values() if ok)
    answered = len(results)
    metric_row([
        ("Questions shown", str(len(shown))),
        ("Answered this session", str(answered)),
        ("Correct", str(correct)),
        ("Accuracy", f"{(100 * correct / answered):.0f}%" if answered else "—"),
    ])
    if st.button("Reset my answers for this session", key=f"{spec.key_prefix}pr_reset"):
        st.session_state[results_key] = {}
        P.reset(spec.number)
        st.rerun()

    with st.expander("My outcome status so far", expanded=False):
        status_frame = pd.DataFrame([
            {"Outcome": slo["id"], "What it means": slo["simple"],
             "Status": P.status_of(spec.number, slo["id"])}
            for slo in spec.slos
        ])
        st.dataframe(status_frame, use_container_width=True, hide_index=True)

    for q in shown:
        render_question(spec, q)


def references(spec: ChapterSpec) -> None:
    """Where this chapter's content came from."""
    if not spec.references:
        st.info("No references are stored for this chapter yet.")
        return
    for ref in spec.references:
        st.markdown(
            f'<div class="atlas-card" style="padding:14px 18px;margin:6px 0">'
            f'<div class="kicker">{ref["short"]}</div>'
            f'<div style="color:#f1f7ff;font-weight:600;margin:.2rem 0">{ref["title"]}</div>'
            f'<div style="color:#9fb4cc;font-size:.86rem">{ref["org"]}</div>'
            f'<div style="color:#c6d6ea;font-size:.88rem;margin-top:6px">'
            f'<b>Used for:</b> {ref["used_for"]}</div>'
            f'<div style="margin-top:6px"><a href="{ref["url"]}">Open the source</a></div>'
            f"</div>",
            unsafe_allow_html=True,
        )
    card(
        "How to read these labels",
        "<p>Sources marked <b>established science</b> are definitions agreed "
        "internationally. Sources marked <b>curriculum convention</b> are the "
        "simplifications this syllabus chooses, stated openly so you can tell them "
        "apart. Simulated figures are generated by the app so you can experiment "
        "safely; they are never presented as measurements of a real object.</p>",
        "SOURCING",
    )
    st.caption("This app runs entirely offline. It never calls a network service, "
               "and it holds no API key.")


# --------------------------------------------------------------------------
# Entry points
# --------------------------------------------------------------------------

def _as_fragment(renderer, key: str):
    """Wrap a station renderer so it reruns on its own.

    Streamlit re-executes the whole script on every interaction, and ``st.tabs``
    renders *every* tab body each time, so a single slider drag would otherwise
    rebuild every station in the chapter. Making each station a fragment means
    only the station the learner is touching reruns.

    Streamlit derives a fragment's identity from ``module`` + ``qualname`` plus
    the delta path and the script hash. Several of the renderers here are
    lambdas that would all share the qualname ``<lambda>``, so the wrapper is
    given a deterministic name built from the station key. That keeps the
    identity stable across reruns, which is what preserves widget state.
    """
    if getattr(renderer, "__atlas_fragment__", False):
        return renderer

    def station_body(*args, **kwargs):
        return renderer(*args, **kwargs)

    station_body.__qualname__ = f"station_{key}"
    station_body.__module__ = __name__
    wrapped = st.fragment(station_body)
    wrapped.__atlas_fragment__ = True
    return wrapped


@cache_data(show_spinner=False)
def chapter_slots():
    """The chapter picker's slot list, including each chapter's outcome and
    station counts.

    Importing eight chapter modules just to print two numbers on a card is the
    slowest part of drawing the first screen, so it is cached. Building a new
    button flushes the cache for the picker only.
    """
    return curriculum.chapter_slots()


def render(spec: ChapterSpec) -> None:
    """Build the whole chapter world for one chapter."""
    P.mark_viewed(spec.number, spec.ids())
    section_intro(spec.tag, spec.title, spec.intro)
    slo_strip(spec)

    def _safe_label(s):
    return s.encode("ascii", "replace").decode("ascii")

tabs = st.tabs([_safe_label(station.label) for station in spec.stations])
    for tab, station in zip(tabs, spec.stations):
        with tab:
            P.mark_viewed(spec.number, station.slos)
            _as_fragment(station.renderer, station.key)()


def exit_report(spec: ChapterSpec) -> None:
    """The full outcome report shown when a learner leaves a chapter."""
    tally = P.counts(spec.number)
    total = len(spec.slos)

    st.markdown(
        f'<div style="text-align:center;padding:6px 0 2px">'
        f'<div class="kicker">CHAPTER {spec.number:02d} · EXIT REPORT</div>'
        f'<h1 style="margin:.15rem 0">What you now know</h1>'
        f'<p style="color:#9fb4cc;margin:0">{spec.title}</p></div>',
        unsafe_allow_html=True,
    )
    st.write("")

    ring_col, meter_col = st.columns([1, 2])
    with ring_col:
        from . import visuals as V
        st.markdown(V.progress_ring(P.fraction_mastered(spec.number),
                                    f"{P.mastered_count(spec.number)} of {total} outcomes"),
                    unsafe_allow_html=True)
    with meter_col:
        metric_row([
            ("Mastered", tally[P.MASTERED]),
            ("Practised", tally[P.PRACTISED]),
            ("Explored", tally[P.EXPLORED]),
            ("Not started", tally[P.NOT_STARTED]),
        ])
        remaining = total - P.mastered_count(spec.number)
        if remaining == 0:
            st.success(f"Outstanding — you have mastered all {total} outcomes of "
                       f"Chapter {spec.number}.")
        else:
            st.info(f"{remaining} outcome{'s' if remaining != 1 else ''} still to master. "
                    "Go back into the chapter, open the stations that cover them, and "
                    "answer the practice questions until the status turns green.")

    st.subheader("Your outcome report")
    for slo in spec.slos:
        status = P.status_of(spec.number, slo["id"])
        st.markdown(
            f'<div class="atlas-card" style="padding:14px 18px;margin:6px 0">'
            f'<div style="display:flex;gap:14px;align-items:flex-start;flex-wrap:wrap">'
            f'<div class="mono" style="color:#5eead4;font-weight:700;min-width:64px">'
            f'{slo["id"]}</div>'
            f'<div style="flex:1;min-width:260px">'
            f'<div style="color:#eef6ff;font-weight:600">{slo["simple"]}</div>'
            f'<div style="color:#9fb4cc;font-size:.82rem;margin-top:4px">'
            f'<b>You studied it in:</b> {slo["taught"]} · '
            f'<b>Official wording:</b> {slo["text"]}</div></div>'
            f'<div>{P.badge(status)}</div></div></div>',
            unsafe_allow_html=True,
        )
