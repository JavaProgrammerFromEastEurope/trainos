from __future__ import annotations

from .principle_reflection import PrincipleReflection


class ReflectionRegistry:

    def __init__(self) -> None:
        self._reflections: list[PrincipleReflection] = []

    def register(self, reflection: PrincipleReflection) -> None:
        self._reflections.append(reflection)

    def reflections(self) -> tuple[PrincipleReflection, ...]:
        return tuple(self._reflections)
