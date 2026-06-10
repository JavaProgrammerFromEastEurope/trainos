# kernel/scheduler/interrupt_controller.py
from __future__ import annotations

from collections import defaultdict
from trainos.kernel.scheduler.priority import Priority


class InterruptController:

    def __init__(self) -> None:
        self._handlers = defaultdict(list)

    def register(self, priority: Priority, handler) -> None:
        self._handlers[priority].append(handler)

    def trigger(self, priority: Priority, context: dict) -> None:
        for p in sorted(self._handlers.keys(), reverse=True):
            if p >= priority:
                for h in self._handlers[p]:
                    h(context)
