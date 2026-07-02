from __future__ import annotations

from .civil_identity import CivilIdentity


class IdentityRegistry:

    def __init__(self) -> None:
        self._identities: dict[str, CivilIdentity] = {}

    def register(self, identity: CivilIdentity) -> None:
        self._identities[identity.entity_id] = identity

    def get(self, entity_id: str) -> CivilIdentity | None:
        return self._identities.get(entity_id)

    def all(self) -> tuple[CivilIdentity, ...]:
        return tuple(self._identities.values())
