from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class PlanStep:
    name: str
    payload: dict[str, Any]
    depends_on: list[str]
