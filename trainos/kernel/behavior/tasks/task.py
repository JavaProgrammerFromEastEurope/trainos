from __future__ import annotations

from .task_result import (
    TaskResult,
)

from .task_status import (
    TaskStatus,
)


class Task:

    def execute(
        self,
    ) -> TaskResult:
        return TaskResult(
            TaskStatus.SUCCESS,
        )
