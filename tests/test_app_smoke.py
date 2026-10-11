"""Smoke tests that actually execute the Streamlit app in-process.

Uses Streamlit's official AppTest harness, which runs the real script and
collects any exceptions. This exercises the chapter picker, the chapter world
and the exit report.
"""

from pathlib import Path

import pytest

from streamlit.testing.v1 import AppTest

from physics import curriculum as D

APP = str(Path(__file__).resolve().parents[1] / "streamlit_app.py")


def test_chapter_picker_without_exception():
    at = AppTest.from_file(APP, default_timeout=60)
    at.run()
    assert not at.exception, at.exception
    assert any("Enter Chapter 1" in b.label for b in at.button)


def test_locked_chapters_are_disabled():
    """Only chapters that have not been written yet show as locked."""
    at = AppTest.from_file(APP, default_timeout=60)
    at.run()
    disabled = [b for b in at.button if b.disabled]
    assert len(disabled) == len(D.CHAPTERS) - sum(1 for c in D.CHAPTERS if c["available"])


def test_chapter_world_runs_without_exception():
    at = AppTest.from_file(APP, default_timeout=60)
    at.session_state["view"] = "chapter"
    at.run()
    assert not at.exception, at.exception
    assert len(at.tabs) >= 9


@pytest.mark.parametrize("number", [c["number"] for c in D.CHAPTERS if c["available"]])
def test_every_open_chapter_renders(number):
    at = AppTest.from_file(APP, default_timeout=90)
    at.session_state["view"] = "chapter"
    at.session_state["active_chapter"] = number
    at.run()
    assert not at.exception, at.exception
    assert len(at.tabs) >= 9


@pytest.mark.parametrize("number", [c["number"] for c in D.CHAPTERS if c["available"]])
def test_every_open_chapter_reports(number):
    at = AppTest.from_file(APP, default_timeout=90)
    at.session_state["view"] = "report"
    at.session_state["active_chapter"] = number
    at.run()
    assert not at.exception, at.exception
    assert any("chapter picker" in b.label.lower() for b in at.button)


def test_mastery_report_runs_without_exception():
    at = AppTest.from_file(APP, default_timeout=60)
    at.session_state["view"] = "report"
    at.run()
    assert not at.exception, at.exception
    assert any("chapter picker" in b.label.lower() for b in at.button)
