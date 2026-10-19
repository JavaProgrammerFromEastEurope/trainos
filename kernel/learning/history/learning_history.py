from __future__ import annotations

from ..experience.experience import (
    Experience,
)


class LearningHistory:

    def __init__(self) -> None:
        self._history: list[Experience] = []

    def add(
        self,
        exp: Experience,
    ) -> None:
        self._history.append(exp)

    def all(self) -> tuple:
        return tuple(self._history)
