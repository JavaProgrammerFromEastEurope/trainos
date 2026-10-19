from __future__ import annotations

from .opponent import (
    Opponent,
)


class OpponentPool:

    def __init__(
        self,
    ) -> None:
        self._opponents: list[Opponent] = []

    def add(
        self,
        opponent: Opponent,
    ) -> None:
        self._opponents.append(opponent)

    def all(
        self,
    ) -> tuple[Opponent, ...]:
        return tuple(self._opponents)
