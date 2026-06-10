# kernel/scheduler/kernel_scheduler.py

from __future__ import annotations

import heapq
from typing import Dict

from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState
from trainos.kernel.scheduler.task import Task
from trainos.kernel.scheduler.task import TaskState
from trainos.kernel.scheduler.task_executor import TaskExecutor


class KernelScheduler(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="scheduler",
            startup_priority=30,
            dependencies=("clock",),
        )

        self._executors: Dict[str, TaskExecutor] = {}
        self._queue: list[tuple[int, int, Task]] = []
        self._sequence 				= 0
        self._submitted_tasks = 0
        self._completed_tasks = 0
        self._failed_tasks = 0

    def initialize(self) -> None:

        self._executors.clear()
        self._queue.clear()
        self._sequence = 0

        self._submitted_tasks = 0
        self._completed_tasks = 0
        self._failed_tasks = 0

        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:

        self._set_state(ServiceState.STARTING)
        self._set_state(ServiceState.RUNNING)

    def stop(self) -> None:

        self._set_state(ServiceState.STOPPING)
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:

        self._executors.clear()
        self._queue.clear()

    def register_executor(
        self,
        task_name: str,
        executor: TaskExecutor,
    ) -> None:

        self._executors[task_name] = executor

    def submit(self, task: Task) -> None:

        heapq.heappush(
            self._queue,
            (
                -task.priority,
                self._sequence,
                task,
            ),
        )

        self._sequence += 1
        self._submitted_tasks += 1

    def update(self, dt: float) -> None:

        if self.state != ServiceState.RUNNING:
            return
        while self._queue:
            _, _, task = heapq.heappop(self._queue)
            executor = self._executors.get(task.name)
            if executor is None:
                task.state = TaskState.FAILED
                self._failed_tasks += 1
                continue
            try:
                task.state = TaskState.RUNNING
                executor.execute(task)
                task.state = TaskState.COMPLETED
                self._completed_tasks += 1
            except Exception:
                task.state = TaskState.FAILED
                self._failed_tasks += 1

    @property
    def queue_size(self) -> int:
        return len(self._queue)

    @property
    def submitted_tasks(self) -> int:
        return self._submitted_tasks

    @property
    def completed_tasks(self) -> int:
        return self._completed_tasks

    @property
    def failed_tasks(self) -> int:
        return self._failed_tasks

    def health_check(self) -> bool:
        return not self.failed and self.queue_size < 100000
