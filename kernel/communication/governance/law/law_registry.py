from __future__ import annotations

from .law import (
    Law,
)


class LawRegistry:

    def __init__(self) -> None:
        self._laws: list[Law] = []

    def add(self, law: Law) -> None:
        self._laws.append(law)

    def laws(self) -> tuple[Law, ...]:
        return tuple(self._laws)
