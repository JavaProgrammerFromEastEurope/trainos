from __future__ import annotations

from .constitutional_ratification import ConstitutionalRatification


class RatificationRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalRatification] = []

    def register(
        self,
        ratification: ConstitutionalRatification,
    ) -> None:
        self._entries.append(ratification)

    def entries(
        self,
    ) -> tuple[ConstitutionalRatification, ...]:
        return tuple(self._entries)
