from __future__ import annotations

from .constitutional_diff import ConstitutionalDiff


class DiffRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalDiff] = []

    def register(
        self,
        diff: ConstitutionalDiff,
    ) -> None:
        self._entries.append(diff)

    def entries(
        self,
    ) -> tuple[ConstitutionalDiff, ...]:
        return tuple(self._entries)
