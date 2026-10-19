from __future__ import annotations

from .reflection import Reflection


class ReflectionRegistry:

    def __init__(self) -> None:
        self._reflections: list[Reflection] = []

    def add(self, reflection: Reflection) -> None:
        self._reflections.append(reflection)

    def reflections(self) -> tuple[Reflection, ...]:
        return tuple(self._reflections)
