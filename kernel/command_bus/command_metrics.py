from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CommandMetrics:

    total_executed: int = 0
    success_count: 	int = 0
    error_count: 		int = 0
    last_command: 	str | None = None

    def record_success(self, command_name: str) -> None:
        self.total_executed += 1
        self.success_count 	+= 1
        self.last_command 	= command_name

    def record_error(self, command_name: str) -> None:
        self.total_executed += 1
        self.error_count 		+= 1
        self.last_command 	= command_name

    def success_rate(self) -> float:
        if self.total_executed == 0:
            return 0.0
        return self.success_count / self.total_executed