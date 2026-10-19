from __future__ import annotations

from .emergence_pattern import EmergencePattern


class EmergenceRegistry:

    def __init__(self) -> None:
        self._patterns: list[EmergencePattern] = []

    def register(self, pattern: EmergencePattern) -> None:
        self._patterns.append(pattern)

    def patterns(self) -> tuple[EmergencePattern, ...]:
        return tuple(self._patterns)
