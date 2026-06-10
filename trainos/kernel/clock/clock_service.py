# kernel/clock/clock_service.py

from __future__ import annotations

import time

from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState


class ClockService(KernelService):

    def __init__(self) -> None:

        super().__init__(
            name="clock",
            startup_priority=1,
            dependencies=(),
        )

        self._start_time 		= 0.0
        self._current_time 	= 0.0
        self._delta_time 		= 0.0
        self._last_tick 		= 0.0

    def initialize(self) -> None:

        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:

        self._set_state(ServiceState.STARTING)

        self._start_time 		= time.time()
        self._last_tick 		= self._start_time
        self._current_time 	= self._start_time
        self._set_state(ServiceState.RUNNING)

    def update(self, dt: float) -> None:
        now = time.time()
        self._delta_time 		= now - self._last_tick
        self._current_time 	= now
        self._last_tick 		= now

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPING)
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        pass

    def health_check(self) -> bool:
        return not self.failed

    @property
    def now(self) -> float:
        return self._current_time

    @property
    def delta(self) -> float:
        return self._delta_time

    @property
    def uptime(self) -> float:
        return self._current_time - self._start_time
