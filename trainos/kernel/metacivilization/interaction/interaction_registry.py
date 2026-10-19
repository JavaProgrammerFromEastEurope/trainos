from __future__ import annotations

from .cross_system_event import CrossSystemEvent


class InteractionRegistry:

    def __init__(self) -> None:
        self._events: list[CrossSystemEvent] = []

    def emit(self, event: CrossSystemEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[CrossSystemEvent, ...]:
        return tuple(self._events)