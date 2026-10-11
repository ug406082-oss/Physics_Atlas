"""The app must teach the published syllabus, not an approximation of it.

Every chapter's learning outcomes are compared against
:mod:`physics.syllabus_xi`, which was transcribed from the AKU-EB Physics HSSC
Syllabus 2025 PDF. If these tests fail, the app has drifted from the book and a
learner is being taught something the board does not ask for - or is missing
something it does.
"""

from __future__ import annotations

import pytest

from physics import curriculum, syllabus_xi

PUBLISHED = {
    1: 13, 2: 10, 3: 12, 4: 20, 5: 8,
    6: 18, 7: 22, 8: 19, 9: 28, 10: 35,
}
TOTAL = 185


def test_the_syllabus_module_itself_is_intact():
    assert len(syllabus_xi.OUTCOMES) == TOTAL
    assert len({row["id"] for row in syllabus_xi.OUTCOMES}) == TOTAL
    for number, expected in PUBLISHED.items():
        assert len(syllabus_xi.chapter_ids(number)) == expected, number
    for row in syllabus_xi.OUTCOMES:
        assert row["text"].strip(), row["id"]
        assert row["topic"].strip(), row["id"]
        assert row["id"].startswith(f"{row['id'].split('.')[0]}.")


def test_every_chapter_matches_the_published_outcome_count():
    for number, expected in PUBLISHED.items():
        assert len(curriculum.slo_ids(number)) == expected, number


def test_no_outcome_exists_that_the_syllabus_does_not_publish():
    published = {row["id"] for row in syllabus_xi.OUTCOMES}
    for number in range(1, 11):
        for sid in curriculum.slo_ids(number):
            assert sid in published, f"chapter {number} teaches {sid}, which is not in the syllabus"


def test_no_published_outcome_is_missing_from_the_app():
    for number in range(1, 11):
        published = set(syllabus_xi.chapter_ids(number))
        taught = set(curriculum.slo_ids(number))
        assert published == taught, (
            f"chapter {number}: missing {sorted(published - taught)}, "
            f"invented {sorted(taught - published)}"
        )


def test_the_wordings_are_the_published_wordings():
    by_id = {row["id"]: row for row in syllabus_xi.OUTCOMES}
    for number in range(1, 11):
        for slo in curriculum.outcomes(number):
            assert slo["text"] == by_id[slo["id"]]["text"], slo["id"]


@pytest.mark.parametrize("number", range(1, 11))
def test_every_outcome_is_taught_by_exactly_one_station(number):
    published = syllabus_xi.chapter_ids(number)
    taught = [sid for station in curriculum.chapter_data(number).STATIONS
              for sid in station["slos"]]
    assert sorted(taught) == sorted(published)
    assert len(taught) == len(set(taught)), "an outcome is taught by two stations"


@pytest.mark.parametrize("number", range(1, 11))
def test_every_outcome_is_practised(number):
    published = set(syllabus_xi.chapter_ids(number))
    practised = {q["slo"] for q in curriculum.chapter_data(number).PRACTICE_QUESTIONS}
    assert published <= practised, sorted(published - practised)


@pytest.mark.parametrize("number", range(1, 11))
def test_worked_problems_are_anchored_to_published_outcomes(number):
    published = set(syllabus_xi.chapter_ids(number))
    for problem in curriculum.chapter_data(number).WORKED_PROBLEMS:
        assert set(problem["slos"]) <= published, problem["id"]


def test_formative_outcomes_are_marked_as_such():
    """Seven outcomes are FA: not examined, but still taught."""
    marked = {row["id"] for row in syllabus_xi.OUTCOMES if row["formative"]}
    assert marked, "the syllabus marks formative outcomes; none were found"
    for number in range(1, 11):
        data = curriculum.chapter_data(number)
        assert hasattr(data, "SLOS")


def test_the_reconstructed_outcomes_are_all_reachable():
    for sid in syllabus_xi.REVIEWED:
        assert any(row["id"] == sid for row in syllabus_xi.OUTCOMES), sid
