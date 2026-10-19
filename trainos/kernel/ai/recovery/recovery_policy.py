from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RecoveryPolicy:
    max_retries: int = 3
    rollback_on_failure: bool = True
    continue_on_failure: bool = False
