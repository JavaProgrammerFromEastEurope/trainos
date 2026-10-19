from __future__ import annotations

from .task import (
    Task,
)

from .task_result import (
    TaskResult,
)


class TaskExecutor:

    def execute(
        self,
        task: Task,
    ) -> TaskResult:
        return task.execute()
