from __future__ import annotations

from .task_assignment import (
    TaskAssignment,
)


class CoordinationGraph:

    def __init__(
        self,
    ) -> None:
        self._assignments: list[TaskAssignment] = []

    def add(
        self,
        assignment: TaskAssignment,
    ) -> None:
        self._assignments.append(assignment)

    def assignments(
        self,
    ) -> tuple[TaskAssignment, ...]:
        return tuple(self._assignments)
