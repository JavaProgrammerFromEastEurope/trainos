from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RuntimeMetrics:
    tick_count: int = 0
    uptime_seconds: float = 0.0
    active_services: int = 0

    @property
    def fps(self) -> float:
        if self.uptime_seconds <= 0:
            return 0.0
        return self.tick_count / self.uptime_seconds
