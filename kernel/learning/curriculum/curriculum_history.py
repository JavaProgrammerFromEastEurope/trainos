from __future__ import annotations

from .lesson import (
    Lesson,
)


class CurriculumHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[Lesson] = []

    def add(
        self,
        lesson: Lesson,
    ) -> None:
        self._history.append(lesson)

    def lessons(
        self,
    ) -> tuple[Lesson, ...]:
        return tuple(self._history)
