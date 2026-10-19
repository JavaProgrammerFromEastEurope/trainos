from __future__ import annotations

from .propagation_event import PropagationEvent


class PropagationRegistry:

    def __init__(self) -> None:
        self._events: list[PropagationEvent] = []

    def register(self, event: PropagationEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[PropagationEvent, ...]:
        return tuple(self._events)
