# kernel/scheduler/task_queue.py
from __future__ import annotations

from heapq import heapify, heappop, heappush
from itertools import count

from kernel.scheduler.priority import ScheduledTask


class TaskQueue:
    """Priority queue ordered by descending priority, then timestamp, then FIFO."""

    def __init__(self) -> None:
        self._sequence = count()
        self._heap: list[tuple[int, float, int, ScheduledTask]] = []

    def push(self, task: ScheduledTask) -> None:
        heappush(
            self._heap,
            (-int(task.priority), task.timestamp, next(self._sequence), task),
        )

    def pop(self) -> ScheduledTask:
        _, _, _, task = heappop(self._heap)
        return task

    def empty(self) -> bool:
        return not self._heap

    def __len__(self) -> int:
        return len(self._heap)

    def peek(self) -> ScheduledTask | None:
        """Return the next task without removing it, or None when empty."""
        return self._heap[0][3] if self._heap else None

    def pop_due(self, now: float) -> ScheduledTask | None:
        """Pop the highest-priority task whose timestamp is at or before now.

        Future tasks remain in place, and equal-priority/equal-timestamp tasks
        retain FIFO ordering through their insertion sequence.
        """
        due_indices = [
            index
            for index, (_, timestamp, _, _) in enumerate(self._heap)
            if timestamp <= now
        ]
        if not due_indices:
            return None

        index = min(due_indices, key=lambda item: self._heap[item][:3])
        _, _, _, task = self._heap[index]
        last = self._heap.pop()
        if index < len(self._heap):
            self._heap[index] = last
            heapify(self._heap)
        return task
