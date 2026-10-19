from dataclasses import dataclass

from .jurisdiction_domain import JurisdictionDomain


@dataclass(frozen=True)
class InstitutionalJurisdiction:

    institution_id: str
    domain: JurisdictionDomain