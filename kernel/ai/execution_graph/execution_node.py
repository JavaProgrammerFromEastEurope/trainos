from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionNode:
    id: str
    payload: dict[str, Any]
    dependencies: list[str] = field(
        default_factory=list,
    )
