# kernel/scheduler/task_executor.py

from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from kernel.scheduler.task import Task


class TaskExecutor(ABC):

    @abstractmethod
    def execute(self, task: Task) -> None: ...
