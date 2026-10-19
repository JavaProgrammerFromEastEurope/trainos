from __future__ import annotations

from dataclasses import dataclass, field
import time


@dataclass
class CommandRecord:

    command_name: str
    payload: 		object
    timestamp: 	float = field(default_factory=time.time)
    success: 		bool = True
    error: 			str | None = None