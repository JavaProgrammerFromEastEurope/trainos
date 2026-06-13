from dataclasses import dataclass
from typing import Callable, Optional

from trainos.kernel.lifecycle.kernel_service import KernelService


@dataclass
class Task:
    task_id: int
    callback: Callable[[], None]
    delay_seconds: float
    interval_seconds: Optional[float]
    repeat: bool
    next_fire: Optional[float] = None


class SchedulerService(KernelService):

    def __init__(self):
        super().__init__(
            name="scheduler",
            dependencies=(),
        ),
        self._running = False
        self._time = 0.0
        self._tasks: list[Task] = []
        self._id = 0

    # ---------------- LIFECYCLE ----------------

    def initialize(self) -> None:
        self._running = True

    def start(self) -> None:
        self._running = True

    def stop(self) -> None:
        self._running = False

    # ---------------- SCHEDULE ----------------
    def schedule(
        self,
        task,
        delay_seconds: float = 0.0,
        interval_seconds: float | None = None,
        repeat: bool = False,
    ) -> None:
        self._id += 1
        self._tasks.append(
            Task(
                task_id=self._id,
                callback=task,
                delay_seconds=delay_seconds,
                interval_seconds=interval_seconds,
                repeat=repeat,
                next_fire=None,
            )
        )

    # ---------------- UPDATE CORE ----------------
    def update(self, dt: float) -> None:
        if not self._running:
            return
        self._time += dt
        ready = []
        for task in list(self._tasks):
            # ---------------- WAIT PHASE ----------------
            if self._time < task.delay_seconds:
                continue
            # ---------------- FIRST EXECUTION (EXACTLY ONCE) ----------------
            if task.next_fire is None:
                task.next_fire = self._time  # ❗ ключевой фикс
                # execute ONLY if delay just reached in this tick window
                if self._time - dt < task.delay_seconds <= self._time:
                    ready.append(task)
                continue
            # ---------------- PERIODIC ----------------
            if task.interval_seconds is None:
                continue
            if self._time >= task.next_fire:
                ready.append(task)
                task.next_fire += task.interval_seconds
        # deterministic order
        ready.sort(key=lambda t: t.task_id)
        for task in ready:
            task.callback()
            if task.interval_seconds is None:
                self._tasks.remove(task)

    # ---------------- INTERNAL ----------------
    def _remove(self, task_id: int) -> None:
        self._tasks = [t for t in self._tasks if t.task_id != task_id]
