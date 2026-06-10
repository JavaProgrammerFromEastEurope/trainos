# kernel/clock/simulation_clock.py

from __future__ import annotations
from trainos.kernel.clock.tick import Tick
from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState


class SimulationClock(KernelService):

    def __init__(
        self,
        fixed_dt: float = 0.1,
    ) -> None:
        super().__init__(
            name="clock",
            startup_priority=0,
            dependencies=(),
        )
        self._fixed_dt = fixed_dt
        self._tick_number = 0
        self._simulation_time = 0.0
        self._current_tick = Tick(
            tick_number=0,
            dt=fixed_dt,
            simulation_time=0.0,
        )

    @property
    def fixed_dt(self) -> float:
        return self._fixed_dt

    @property
    def tick_number(self) -> int:
        return self._tick_number

    @property
    def simulation_time(self) -> float:
        return self._simulation_time

    @property
    def current_tick(self) -> Tick:
        return self._current_tick

    def initialize(self) -> None:
        self._tick_number = 0
        self._simulation_time = 0.0
        self._current_tick = Tick(
            tick_number=0,
            dt=self._fixed_dt,
            simulation_time=0.0,
        )
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.STARTING)
        self._set_state(ServiceState.RUNNING)

    def update(self, dt: float | None = None) -> None:
        if self.state != ServiceState.RUNNING:
            return
        delta_time = self._fixed_dt if dt is None else dt
        self._tick_number += 1
        self._simulation_time += delta_time
        self._current_tick = Tick(
            tick_number=self._tick_number,
            dt=delta_time,
            simulation_time=self._simulation_time,
        )
        self.set_uptime(self._simulation_time)

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPING)
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        self._tick_number = 0
        self._simulation_time = 0.0
        self._current_tick = Tick(
            tick_number=0,
            dt=self._fixed_dt,
            simulation_time=0.0,
        )

    def health_check(self) -> bool:
        return not self.failed and self.fixed_dt > 0.0

    def reset(self) -> None:
        self._tick_number = 0
        self._simulation_time = 0.0
        self._current_tick = Tick(
            tick_number=0,
            dt=self._fixed_dt,
            simulation_time=0.0,
        )

    def advance(self, ticks: int) -> None:
        if ticks <= 0:
            return
        for _ in range(ticks):
            self.update()

    def seconds_to_ticks(self, seconds: float) -> int:
        return int(seconds / self._fixed_dt)

    def ticks_to_seconds(self, ticks: int) -> float:
        return ticks * self._fixed_dt
