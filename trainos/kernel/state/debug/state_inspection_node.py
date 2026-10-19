from __future__ import annotations

from dataclasses import (
    dataclass,
)


@dataclass(frozen=True, slots=True)
class StateInspectionNode:
    key: str
    value: object
    value_type: str
