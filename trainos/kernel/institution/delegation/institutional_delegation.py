from dataclasses import dataclass

from .delegation_scope import DelegationScope


@dataclass(frozen=True)
class InstitutionalDelegation:

    from_institution: str
    to_institution: 	str
    scope: DelegationScope