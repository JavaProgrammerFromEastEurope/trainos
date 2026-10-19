from __future__ import annotations

from .constitutional_justification import ConstitutionalJustification


class JustificationRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalJustification] = []

    def register(self, justification: ConstitutionalJustification) -> None:
        self._entries.append(justification)

    def entries(self) -> tuple[ConstitutionalJustification, ...]:
        return tuple(self._entries)
