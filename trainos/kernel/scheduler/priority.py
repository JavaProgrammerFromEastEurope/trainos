# kernel/scheduler/priority.py
from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Any


class Priority(IntEnum):
    LOW = 10
    NORMAL = 20
    HIGH = 30
    CRITICAL = 40


@dataclass(slots=True)
class ScheduledTask:
    task_id: str
    priority: Priority
    timestamp: float
    payload: dict[str, Any]
