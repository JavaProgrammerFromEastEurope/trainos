from __future__ import annotations

from .speciation_event import SpeciationEvent


class SpeciationRegistry:

    def __init__(self) -> None:
        self._events: list[SpeciationEvent] = []

    def register(self, event: SpeciationEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[SpeciationEvent, ...]:
        return tuple(self._events)
