from dataclasses import dataclass

from .authority_level import AuthorityLevel


@dataclass(frozen=True)
class ConstitutionalAuthority:

    institution_id: str
    level: AuthorityLevel