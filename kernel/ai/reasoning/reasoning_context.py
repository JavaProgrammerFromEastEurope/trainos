from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ReasoningContext:

    state: dict[str, Any]

    memory: dict[str, Any] = field(
        default_factory=dict,
    )

    goals: list[str] = field(
        default_factory=list,
    )