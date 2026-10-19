from dataclasses import dataclass


@dataclass(frozen=True)
class JurisdictionPolicy:

    require_registered_institution: bool
    allow_multiple_domains: bool