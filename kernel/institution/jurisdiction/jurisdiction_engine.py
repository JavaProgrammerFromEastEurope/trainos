from .institutional_jurisdiction import InstitutionalJurisdiction


class JurisdictionEngine:

    def assign(
        self, jurisdiction: InstitutionalJurisdiction
    ) -> InstitutionalJurisdiction:
        return jurisdiction
