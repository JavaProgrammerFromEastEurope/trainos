# kernel/scheduler/priority.py
from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class Priority(IntEnum):
    LOW = 10
    NORMAL = 20
    HIGH = 30
    CRITICAL = 40


@dataclass(slots=True)
class ScheduledTask:
    task_id: str
    priority: Priority
    timestamp: float
    payload: dict


# kernel/scheduler/task_queue.py

from __future__ import annotations

from heapq import heappush, heappop
from typing import Any

from trainos.kernel.scheduler.priority import ScheduledTask


class TaskQueue:

    def __init__(self) -> None:
        self._heap: list[tuple[int, float, ScheduledTask]] = []

    def push(self, task: ScheduledTask) -> None:

        heappush(
            self._heap,
            (-task.priority, task.timestamp, task),
        )

    def pop(self) -> ScheduledTask:

        _, _, task = heappop(self._heap)
        return task

    def empty(self) -> bool:
        return len(self._heap) == 0
