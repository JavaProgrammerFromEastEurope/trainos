from dataclasses import dataclass

from .task_status import (
    TaskStatus,
)


@dataclass
class TaskResult:
    status: TaskStatus
