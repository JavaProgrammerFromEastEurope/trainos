from __future__ import annotations

from .institutional_delegation import InstitutionalDelegation


class DelegationRegistry:

    def __init__(self) -> None:
        self._delegations: dict[tuple[str, str], InstitutionalDelegation] = {}

    def register(self, delegation: InstitutionalDelegation) -> None:
        key = (delegation.from_institution, delegation.to_institution)
        self._delegations[key] = delegation

    def get(
        self, from_institution: str, to_institution: str
    ) -> InstitutionalDelegation | None:
        return self._delegations.get((from_institution, to_institution))

    def delegations(self) -> tuple[InstitutionalDelegation, ...]:
        return tuple(self._delegations.values())
