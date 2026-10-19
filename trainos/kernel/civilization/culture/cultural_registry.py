from __future__ import annotations

from .cultural_event import CulturalEvent


class CulturalRegistry:

    def __init__(self) -> None:
        self._events: list[CulturalEvent] = []

    def add(self, event: CulturalEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[CulturalEvent, ...]:
        return tuple(self._events)
