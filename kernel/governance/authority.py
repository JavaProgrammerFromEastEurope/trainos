from dataclasses import dataclass

from .authority_level import AuthorityLevel


@dataclass(frozen=True)
class GovernanceAuthority:

    name: 	str
    level: AuthorityLevel