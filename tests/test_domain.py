"""Unit tests for core rules. Expected results come from the scenario brief
(customer-kit/scenarios/repair-shop.md), not from the code under test."""

import pytest

from benchbolt.domain import (
    InquiryInput,
    Status,
    TransitionError,
    check_transition,
    validate_inquiry,
)


def make(**overrides: str) -> InquiryInput:
    base = {"rider_label": "Rider-001", "bike_type": "city", "problem": "Flat rear tire"}
    base.update(overrides)
    return InquiryInput(**base)


# --- Story 1: intake validation -------------------------------------------


def test_valid_inquiry_has_no_errors() -> None:
    assert validate_inquiry(make()) == []


@pytest.mark.parametrize("problem", ["", "   ", "\n\t"])
def test_blank_problem_rejected(problem: str) -> None:
    assert "problem: required" in validate_inquiry(make(problem=problem))


def test_unsupported_bike_type_rejected() -> None:
    assert validate_inquiry(make(bike_type="unicycle"))


@pytest.mark.parametrize(("length", "ok"), [(1, True), (240, True), (241, False)])
def test_problem_length_boundary(length: int, ok: bool) -> None:
    assert (validate_inquiry(make(problem="x" * length)) == []) is ok


@pytest.mark.parametrize(("length", "ok"), [(0, True), (40, True), (41, False)])
def test_preferred_day_boundary(length: int, ok: bool) -> None:
    assert (validate_inquiry(make(preferred_day="d" * length)) == []) is ok


# --- Story 3: decision rules -----------------------------------------------


@pytest.mark.parametrize(
    ("current", "target"),
    [
        (Status.PENDING_REVIEW, Status.ACCEPTED),
        (Status.PENDING_REVIEW, Status.DECLINED),
        (Status.ACCEPTED, Status.COMPLETED),
    ],
)
def test_allowed_transitions(current: Status, target: Status) -> None:
    check_transition(current, target)  # does not raise


@pytest.mark.parametrize(
    ("current", "target"),
    [
        (Status.PENDING_REVIEW, Status.COMPLETED),  # must accept first
        (Status.DECLINED, Status.ACCEPTED),  # terminal
        (Status.COMPLETED, Status.PENDING_REVIEW),  # terminal
        (Status.ACCEPTED, Status.DECLINED),
    ],
)
def test_rejected_transitions(current: Status, target: Status) -> None:
    with pytest.raises(TransitionError):
        check_transition(current, target)
