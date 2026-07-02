from __future__ import annotations

from .conflict_resolution import ConstitutionalConflictResolution


class ConstitutionalConflictRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalConflictResolution] = []

    def register(
        self,
        resolution: ConstitutionalConflictResolution,
    ) -> None:
        self._entries.append(resolution)

    def entries(self) -> tuple[ConstitutionalConflictResolution, ...]:
        return tuple(self._entries)
