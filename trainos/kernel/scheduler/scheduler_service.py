from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import Callable, Optional

from trainos.kernel.lifecycle.kernel_service import KernelService, ServiceState


@dataclass(order=True)
class ScheduledTask:
    sort_index: tuple = field(init=False, repr=False)

    priority: int
    task_id: int = field(compare=False)
    callback: Callable[[], None] = field(compare=False)

    delay_seconds: float = field(compare=False)
    interval_seconds: Optional[float] = field(compare=False)
    repeat: bool = field(compare=False)

    next_fire: float = field(default=0.0, compare=False)

    def __post_init__(self):
        self.sort_index = (-self.priority, self.task_id)


class SchedulerService(KernelService):

	def __init__(self) -> None:
			super().__init__(name="scheduler")

			self._heap: list[ScheduledTask] = []
			self._next_id = 1
			self._time = 0.0
			self._running = False

	# ---------------- lifecycle ----------------

	def initialize(self) -> None:
			self._set_state(ServiceState.INITIALIZED)

	def start(self) -> None:
			self._running = True
			self._set_state(ServiceState.RUNNING)

	def stop(self) -> None:
			self._running = False
			self._set_state(ServiceState.STOPPED)

	# ---------------- scheduling ----------------

	def schedule(
			self,
			callback: Callable[[], None],
			delay_seconds: float = 0.0,
			interval_seconds: Optional[float] = None,
			repeat: bool = False,
			priority: int = 0,
	) -> int:

			task_id = self._next_id
			self._next_id += 1

			task = ScheduledTask(
					priority=priority,
					task_id=task_id,
					callback=callback,
					delay_seconds=delay_seconds,
					interval_seconds=interval_seconds,
					repeat=repeat,
					next_fire=delay_seconds,
			)

			heapq.heappush(self._heap, task)

			return task_id

	def cancel(self, task_id: int) -> None:
			self._heap = [t for t in self._heap if t.task_id != task_id]
			heapq.heapify(self._heap)

	# ---------------- core update ----------------

	def update(self, dt: float) -> None:

			if not self._running:
					return

			self._time += dt

			ready = []

			for task in list(self._heap):

					# ---------------- DELAY GATE ----------------
					if self._time < task.delay_seconds:
							continue

					# ---------------- FIRST FIRE LOGIC ----------------
					if not hasattr(task, "_started"):
							task._started = True
							task.next_fire = task.delay_seconds
							continue  # IMPORTANT: no execution in same tick

					# ---------------- PERIODIC ----------------
					if task.interval_seconds is None:
							ready.append(task)
							continue

					if self._time >= task.next_fire:
							ready.append(task)

			# deterministic ordering
			ready.sort(key=lambda t: (-t.priority, t.task_id))

			for task in ready:

					task.callback()

					if task.interval_seconds is None:
							self._remove(task.task_id)
							continue

					task.next_fire += task.interval_seconds