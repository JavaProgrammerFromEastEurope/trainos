from __future__ import annotations

from .tradition import Tradition


class TraditionRegistry:

    def __init__(self) -> None:
        self._traditions: list[Tradition] = []

    def add(self, tradition: Tradition) -> None:
        self._traditions.append(tradition)

    def traditions(self) -> tuple[Tradition, ...]:
        return tuple(self._traditions)
