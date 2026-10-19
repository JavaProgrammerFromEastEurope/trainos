# kernel/stability/clock_stability.py

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ClockStability:
    previous_time: float = 0.0

    def validate(
        self,
        current_time: float,
    ) -> bool:
        if current_time < self.previous_time:
            return False
        self.previous_time = current_time
        return True
