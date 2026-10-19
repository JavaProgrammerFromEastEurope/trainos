from __future__ import annotations

from .task_assignment import (
    TaskAssignment,
)


class CoordinationHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[TaskAssignment] = []

    def add(
        self,
        assignment: TaskAssignment,
    ) -> None:
        self._history.append(assignment)

    def records(
        self,
    ) -> tuple[TaskAssignment, ...]:
        return tuple(self._history)
