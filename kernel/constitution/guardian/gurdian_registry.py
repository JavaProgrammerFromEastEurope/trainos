from __future__ import annotations

from .constitutional_guardian import ConstitutionalGuardian


class GuardianRegistry:

    def __init__(self) -> None:
        self._guardians: list[ConstitutionalGuardian] = []

    def register(
        self,
        guardian: ConstitutionalGuardian,
    ) -> None:
        self._guardians.append(guardian)

    def guardians(
        self,
    ) -> tuple[ConstitutionalGuardian, ...]:
        return tuple(self._guardians)
