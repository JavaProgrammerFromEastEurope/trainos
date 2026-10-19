from __future__ import annotations

from .meta_memetic_event import MetaMemeticEvent


class MetaMemeticRegistry:

    def __init__(self) -> None:
        self._events: list[MetaMemeticEvent] = []

    def register(self, event: MetaMemeticEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[MetaMemeticEvent, ...]:
        return tuple(self._events)
