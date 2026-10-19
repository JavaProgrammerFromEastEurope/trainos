# kernel/scheduler/event_scheduler.py
from __future__ import annotations

from kernel.events.event_bus import EventBus
from kernel.scheduler.priority import ScheduledTask
from kernel.scheduler.task_queue import TaskQueue


class EventScheduler:
    """Publish scheduled events when their timestamp becomes due."""

    def __init__(self, event_bus: EventBus) -> None:
        self._bus = event_bus
        self._queue = TaskQueue()

    def schedule(self, task: ScheduledTask) -> None:
        if not isinstance(task, ScheduledTask):
            raise TypeError("task must be a ScheduledTask")
        self._queue.push(task)

    def update(self, now: float) -> None:
        while True:
            task = self._queue.pop_due(now)
            if task is None:
                return
            if "event" not in task.payload:
                raise ValueError("scheduled task payload must contain 'event'")
            self._bus.publish(task.payload["event"])
