from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class MemoryRecord:
    key: str
    value: Any
