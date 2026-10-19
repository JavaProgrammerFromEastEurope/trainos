from __future__ import annotations

from .civilization_identity import CivilizationIdentity


class IdentityRegistry:

    def __init__(self) -> None:
        self._identities: list[CivilizationIdentity] = []

    def register(self, identity: CivilizationIdentity) -> None:
        self._identities.append(identity)

    def identities(self) -> tuple[CivilizationIdentity, ...]:
        return tuple(self._identities)
