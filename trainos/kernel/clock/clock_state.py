# kernel/clock/clock_state.py

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ClockState:
    tick_count: int
    uptime_seconds: float
    delta_time: float
