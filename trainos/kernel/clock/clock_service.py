# kernel/clock/clock_service.py

from __future__ import annotations

from trainos.kernel.clock.clock_state import ClockState
from trainos.kernel.lifecycle.kernel_service import (
    KernelService,
    ServiceState,
)


class ClockService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="clock",
            dependencies=(),
        )

        self._tick_count = 0
        self._uptime_seconds = 0.0
        self._delta_time = 0.0

    @property
    def tick_count(self) -> int:
        return self._tick_count

    @property
    def uptime_seconds(self) -> float:
        return self._uptime_seconds

    @property
    def delta_time(self) -> float:
        return self._delta_time

    @property
    def state_snapshot(self) -> ClockState:
        return ClockState(
            tick_count=self._tick_count,
            uptime_seconds=self._uptime_seconds,
            delta_time=self._delta_time,
        )

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.RUNNING)

    def update(self, dt: float) -> None:
        self._delta_time = dt
        self._uptime_seconds += dt
        self._tick_count += 1

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        self._tick_count = 0
        self._uptime_seconds = 0.0
        self._delta_time = 0.0
