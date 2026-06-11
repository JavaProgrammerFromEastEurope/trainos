# kernel/time/time_service.py

from __future__ import annotations

from trainos.kernel.lifecycle.kernel_service import (
    KernelService,
    ServiceState,
)
from trainos.kernel.time.simulation_time import SimulationTime


class TimeService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="time",
            dependencies=("clock",),
        )

        self._elapsed_seconds = 0.0
        self._tick_count = 0

    @property
    def elapsed_seconds(self) -> float:
        return self._elapsed_seconds

    @property
    def tick_count(self) -> int:
        return self._tick_count

    @property
    def simulation_time(self) -> SimulationTime:
        return SimulationTime(
            elapsed_seconds=self._elapsed_seconds,
            tick_count=self._tick_count,
        )

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.RUNNING)

    def update(self, dt: float) -> None:
        self._elapsed_seconds += dt
        self._tick_count += 1

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        self._elapsed_seconds = 0.0
        self._tick_count = 0

    def reset(self) -> None:
        self._elapsed_seconds = 0.0
        self._tick_count = 0
