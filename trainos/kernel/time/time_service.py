from __future__ import annotations

from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState
from trainos.kernel.time.sim_clock import SimClock


class TimeService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="time",
            startup_priority=2,
            dependencies=("clock",),
        )
        self._clock = SimClock()

    @property
    def clock(self) -> SimClock:
        return self._clock

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.STARTING)
        self._set_state(ServiceState.RUNNING)

    def update(self, dt: float) -> None:
        self._clock.tick()

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPING)
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        pass

    def health_check(self) -> bool:
        return not self.failed
