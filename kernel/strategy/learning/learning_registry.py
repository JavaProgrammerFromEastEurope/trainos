from __future__ import annotations

from .learning_event import LearningEvent


class LearningRegistry:

    def __init__(self) -> None:
        self._events: list[LearningEvent] = []

    def register(self, event: LearningEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[LearningEvent, ...]:
        return tuple(self._events)
