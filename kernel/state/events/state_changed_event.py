from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
)
class StateChangedEvent:
    key: str
    old_value: object
    new_value: object
