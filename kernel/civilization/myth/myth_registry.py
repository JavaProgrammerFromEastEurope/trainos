from __future__ import annotations

from .myth import Myth


class MythRegistry:

    def __init__(self) -> None:
        self._myths: list[Myth] = []

    def add(self, myth: Myth) -> None:
        self._myths.append(myth)

    def myths(self) -> tuple[Myth, ...]:
        return tuple(self._myths)
