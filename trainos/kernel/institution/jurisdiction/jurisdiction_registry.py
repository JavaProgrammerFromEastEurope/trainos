from __future__ import annotations

from .institutional_jurisdiction import InstitutionalJurisdiction


class JurisdictionRegistry:

    def __init__(self) -> None:
        self._jurisdictions: dict[str, tuple[InstitutionalJurisdiction, ...]] = {}

    def register(self, jurisdiction: InstitutionalJurisdiction) -> None:
        current = self._jurisdictions.get(jurisdiction.institution_id, ())
        self._jurisdictions[jurisdiction.institution_id] = current + (jurisdiction,)

    def get(self, institution_id: str) -> tuple[InstitutionalJurisdiction, ...]:
        return self._jurisdictions.get(institution_id, ())
