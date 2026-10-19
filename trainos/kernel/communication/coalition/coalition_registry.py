from __future__ import annotations

from .coalition import Coalition


class CoalitionRegistry:

    def __init__(self) -> None:
        self._coalitions: list[Coalition] = []

    def add(self, coalition: Coalition) -> None:
        self._coalitions.append(coalition)

    def coalitions(self) -> tuple[Coalition, ...]:
        return tuple(self._coalitions)
