# kernel/time/simulation_time.py

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SimulationTime:
    elapsed_seconds: float
    tick_count: int
