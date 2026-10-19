from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StateHistoryRecord:
    tick: int
    key: str
    old_value: object
    new_value: object
