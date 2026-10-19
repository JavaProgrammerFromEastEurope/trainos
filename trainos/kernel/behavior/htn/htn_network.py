from __future__ import annotations

from .htn_task import HTNTask


class HTNNetwork:

    def __init__(
        self,
    ) -> None:
        self._tasks: list[HTNTask] = []

    def add(
        self,
        task: HTNTask,
    ) -> None:
        self._tasks.append(task)

    def tasks(
        self,
    ) -> tuple[HTNTask, ...]:
        return tuple(self._tasks)
