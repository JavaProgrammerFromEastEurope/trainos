from __future__ import annotations

from .task_executor import (
    TaskExecutor,
)


class TaskRuntime:

    def __init__(
        self,
    ) -> None:
        self.executor = TaskExecutor()
