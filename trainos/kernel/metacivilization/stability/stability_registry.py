from __future__ import annotations

from .drift_event import DriftEvent


class StabilityRegistry:

    def __init__(self) -> None:
        self._events: list[DriftEvent] = []

    def register(self, event: DriftEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[DriftEvent, ...]:
        return tuple(self._events)
