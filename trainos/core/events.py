from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Event:
    type: str
    payload: dict[str, Any]
    timestamp: datetime = datetime.utcnow()
