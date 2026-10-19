from __future__ import annotations

from .self_awareness import SelfAwareness


class SelfAwarenessRegistry:

    def __init__(self) -> None:
        self._awareness: list[SelfAwareness] = []

    def add(self, awareness: SelfAwareness) -> None:
        self._awareness.append(awareness)

    def awareness(self) -> tuple[SelfAwareness, ...]:
        return tuple(self._awareness)
