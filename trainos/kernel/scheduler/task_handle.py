# kernel/scheduler/task_handle.py

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TaskHandle:
    task_id: int
