# kernel/scheduler/event_scheduler.py
from __future__ import annotations

from trainos.kernel.events.event_bus 			import EventBus
from trainos.kernel.scheduler.task_queue 	import TaskQueue
from trainos.kernel.scheduler.priority 		import ScheduledTask


class EventScheduler:

    def __init__(self, event_bus: EventBus) -> None:
        self._bus = event_bus
        self._queue = TaskQueue()

    def schedule(self, task: ScheduledTask) -> None:
        self._queue.push(task)

    def update(self, now: float) -> None:
        while not self._queue.empty():
            task = self._queue.pop()
            self._bus.publish(event=task.payload["event"])
