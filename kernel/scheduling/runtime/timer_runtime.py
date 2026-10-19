from dataclasses import dataclass

from .timer_status import TimerStatus


@dataclass(frozen=True, slots=True)
class TimerRuntime:

    runtime_id: str
    tick: 			int = 0
    status: TimerStatus = TimerStatus.CREATED