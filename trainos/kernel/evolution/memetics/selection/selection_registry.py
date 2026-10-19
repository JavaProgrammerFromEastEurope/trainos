from __future__ import annotations

from .selection_event import SelectionEvent


class SelectionRegistry:

    def __init__(self) -> None:
        self._events: list[SelectionEvent] = []

    def register(self, event: SelectionEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[SelectionEvent, ...]:
        return tuple(self._events)
