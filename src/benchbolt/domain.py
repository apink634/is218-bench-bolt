"""Core rules for Bench & Bolt repair inquiries.

No Flask or SQLite imports here: these rules are pure so they can be unit
tested quickly and reused by the web layer and the store.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class Status(StrEnum):
    PENDING_REVIEW = "Pending review"
    ACCEPTED = "Accepted"
    DECLINED = "Declined"
    COMPLETED = "Completed"


# Workflow state boundary: a plain table, not the OO State pattern.
ALLOWED_TRANSITIONS: dict[Status, frozenset[Status]] = {
    Status.PENDING_REVIEW: frozenset({Status.ACCEPTED, Status.DECLINED}),
    Status.ACCEPTED: frozenset({Status.COMPLETED}),
    Status.DECLINED: frozenset(),  # terminal
    Status.COMPLETED: frozenset(),  # terminal
}

BIKE_TYPES = frozenset({"city", "road", "other"})
PROBLEM_MAX = 240
PREFERRED_DAY_MAX = 40


class TransitionError(ValueError):
    """Raised when a status change is not allowed."""


@dataclass(frozen=True)
class InquiryInput:
    rider_label: str
    bike_type: str
    problem: str
    preferred_day: str = ""


def validate_inquiry(data: InquiryInput) -> list[str]:
    """Return a list of field errors. An empty list means the input is valid."""
    errors: list[str] = []
    if not data.rider_label.strip():
        errors.append("rider_label: required")
    if data.bike_type not in BIKE_TYPES:
        errors.append("bike_type: must be city, road or other")
    problem = data.problem.strip()
    if not problem:
        errors.append("problem: required")
    elif len(data.problem) > PROBLEM_MAX:
        errors.append(f"problem: at most {PROBLEM_MAX} characters")
    if len(data.preferred_day) > PREFERRED_DAY_MAX:
        errors.append(f"preferred_day: at most {PREFERRED_DAY_MAX} characters")
    return errors


def check_transition(current: Status, target: Status) -> None:
    """Raise TransitionError unless current -> target is allowed."""
    if target not in ALLOWED_TRANSITIONS[current]:
        raise TransitionError(f"Cannot move from {current.value} to {target.value}")
