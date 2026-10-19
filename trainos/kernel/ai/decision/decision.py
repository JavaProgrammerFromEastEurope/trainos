from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Decision:
    action: 		str
    confidence: float
    payload: 		dict[str, Any]