from __future__ import annotations

from dataclasses import dataclass

from .task import (
    Task,
)


@dataclass
class TaskNode:
    task: Task
