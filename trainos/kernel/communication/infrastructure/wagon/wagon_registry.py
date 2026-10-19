from __future__ import annotations

from .wagon import Wagon


class WagonRegistry:

    def __init__(self) -> None:
        self._wagons: list[Wagon] = []

    def add(self, wagon: Wagon) -> None:
        self._wagons.append(wagon)

    def wagons(self) -> tuple[Wagon, ...]:
        return tuple(self._wagons)
