# kernel/time/sim_clock.py
from __future__ import annotations


class SimClock:

    def __init__(self) -> None:
        self._time = 0.0
        self._dt = 0.1

    def set_dt(self, dt: float) -> None:
        self._dt = dt

    def tick(self) -> float:
        self._time += self._dt
        return self._time

    @property
    def now(self) -> float:
        return self._time

    @property
    def dt(self) -> float:
        return self._dt
