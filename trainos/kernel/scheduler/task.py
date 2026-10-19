# kernel/scheduler/task.py

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Any


class TaskState(Enum):
    PENDING 		= "pending"
    RUNNING 		= "running"
    COMPLETED 	= "completed"
    FAILED 			= "failed"


@dataclass(slots=True)
class Task:
    task_id: str
    name: str
    priority: int
    payload: dict[str, Any]
    state: TaskState = TaskState.PENDING
