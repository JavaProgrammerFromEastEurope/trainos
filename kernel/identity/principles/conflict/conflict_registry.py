from __future__ import annotations

from .conflict_resolution import PrincipleConflictResolution


class PrincipleConflictRegistry:

    def __init__(self) -> None:
        self._resolutions: list[PrincipleConflictResolution] = []

    def register(self, resolution: PrincipleConflictResolution) -> None:
        self._resolutions.append(resolution)

    def resolutions(self) -> tuple[PrincipleConflictResolution, ...]:
        return tuple(self._resolutions)
