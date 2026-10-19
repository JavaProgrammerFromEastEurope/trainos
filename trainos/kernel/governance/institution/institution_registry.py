from __future__ import annotations

from .governance_institution import GovernanceInstitution


class InstitutionRegistry:

    def __init__(self) -> None:
        self._institutions: list[GovernanceInstitution] = []

    def register(self, institution: GovernanceInstitution) -> None:
        self._institutions.append(institution)

    def institutions(self) -> tuple[GovernanceInstitution, ...]:
        return tuple(self._institutions)
