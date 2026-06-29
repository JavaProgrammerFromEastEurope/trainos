from __future__ import annotations

from .conflict_resolution import PreferenceResolution


class ConflictRegistry:

    def __init__(self) -> None:
        self._resolutions: list[PreferenceResolution] = []

    def register(self, resolution: PreferenceResolution) -> None:
        self._resolutions.append(resolution)

    def resolutions(self) -> tuple[PreferenceResolution, ...]:
        return tuple(self._resolutions)
