from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TimerSnapshot:

    tick: int