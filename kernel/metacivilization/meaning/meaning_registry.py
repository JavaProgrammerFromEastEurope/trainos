from __future__ import annotations

from .meaning import Meaning


class MeaningRegistry:

    def __init__(self) -> None:
        self._meanings: list[Meaning] = []

    def add(self, meaning: Meaning) -> None:
        self._meanings.append(meaning)

    def meanings(self) -> tuple[Meaning, ...]:
        return tuple(self._meanings)
