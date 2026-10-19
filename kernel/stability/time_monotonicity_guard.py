# kernel/stability/time_monotonicity_guard.py

from __future__ import annotations


class TimeMonotonicityGuard:

    def __init__(self) -> None:
        self._last_time = 0.0

    @property
    def last_time(self) -> float:
        return self._last_time

    def validate(
        self,
        current_time: float,
    ) -> bool:
        if current_time < self._last_time:
            return False
        self._last_time = current_time
        return True

    def reset(self) -> None:
        self._last_time = 0.0
