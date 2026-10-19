from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DecisionContext:

    state_snapshot: dict[str, Any]
    history: list[Any] 					= field(default_factory=list)
    metrics: dict[str, Any] 		= field(default_factory=dict)
    constraints: dict[str, Any] = field(default_factory=dict)