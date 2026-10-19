# kernel/stability/scheduler_reentrancy_guard.py

from __future__ import annotations


class SchedulerReentrancyGuard:

    def __init__(self) -> None:
        self._inside_update = False

    @property
    def locked(self) -> bool:
        return self._inside_update

    def enter(self) -> bool:
        if self._inside_update:
            return False
        self._inside_update = True
        return True

    def leave(self) -> None:
        self._inside_update = False

    def reset(self) -> None:
        self._inside_update = False
