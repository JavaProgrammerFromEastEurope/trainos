# kernel/scheduler/scheduled_task.py

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Any


@dataclass(slots=True)
class ScheduledTask:
    task_id: int
    callback: Callable[[], Any]
    delay_seconds: float 		= 0.0
    interval_seconds: float = 0.0
    repeat: bool 						= False
    elapsed_seconds: float 	= 0.0
    priority: int 					= 0
    enabled: bool 					= True
    metadata: dict[str, Any] = field(default_factory=dict)

    def should_run(self) -> bool:
        if not self.enabled:
            return False
        return self.elapsed_seconds >= self.delay_seconds

    def advance(self, dt: float) -> None:
        self.elapsed_seconds += dt

    def execute(self) -> None:
        self.callback()
        if self.repeat:
            self.elapsed_seconds = max(
                0.0,
                self.elapsed_seconds - self.interval_seconds,
            )
        else:
            self.enabled = False
