# kernel/clock/tick.py

from __future__ 	import annotations
from dataclasses 	import dataclass


@dataclass(frozen=True, slots=True)
class Tick:
    tick_number: int
    dt: float
    simulation_time: float
