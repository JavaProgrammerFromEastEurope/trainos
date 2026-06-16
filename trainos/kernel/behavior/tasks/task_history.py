from __future__ import annotations

from .task_result import (
    TaskResult,
)


class TaskHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[TaskResult] = []

    def add(
        self,
        result: TaskResult,
    ) -> None:
        self._history.append(
            result,
        )

    def records(
        self,
    ) -> tuple[TaskResult, ...]:
        return tuple(
            self._history,
        )
