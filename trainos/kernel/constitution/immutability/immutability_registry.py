from __future__ import annotations

from .constitutional_immutability import ConstitutionalImmutability


class ImmutabilityRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalImmutability] = []

    def register(
        self,
        entry: ConstitutionalImmutability,
    ) -> None:
        self._entries.append(entry)

    def entries(
        self,
    ) -> tuple[ConstitutionalImmutability, ...]:
        return tuple(self._entries)
