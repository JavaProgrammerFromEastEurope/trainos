from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RetryState:

    attempts: int = 0

    def increment(self) -> None:
        self.attempts += 1
