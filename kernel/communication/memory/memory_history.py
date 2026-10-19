from __future__ import annotations

from .memory_event import MemoryEvent


class MemoryHistory:

    def __init__(self) -> None:
        self._events: list[MemoryEvent] = []

    def add(self, event: MemoryEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[MemoryEvent, ...]:
        return tuple(self._events)
