from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import time
import uuid


@dataclass
class CommandContext:

    timestamp: float 		= field(default_factory=time.time)
    correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    trace_id: str 			= field(default_factory=lambda: str(uuid.uuid4()))
    metadata: dict[str, Any] = field(default_factory=dict)

    user_id:		str | None = None
    session_id: str | None = None
