from __future__ import annotations

from .destiny import Destiny


class DestinyRegistry:

    def __init__(self) -> None:
        self._destinies: list[Destiny] = []

    def add(self, destiny: Destiny) -> None:
        self._destinies.append(destiny)

    def destinies(self) -> tuple[Destiny, ...]:
        return tuple(self._destinies)
