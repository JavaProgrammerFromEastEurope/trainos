from dataclasses import dataclass, field
import time
from typing import Any


@dataclass
class Event:
    event_type: str
    payload: Any
    timestamp: float = field(default_factory=lambda: time.time())
