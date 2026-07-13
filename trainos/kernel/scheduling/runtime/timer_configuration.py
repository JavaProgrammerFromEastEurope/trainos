from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TimerConfiguration:

    tick_interval_ms: int = 100