from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class CommandInspectionNode:

    command_name: str
    timestamp: 		float
    success: 			bool
    metadata: 		dict[str, Any]
