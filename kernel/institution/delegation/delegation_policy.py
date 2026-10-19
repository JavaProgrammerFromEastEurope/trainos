from dataclasses import dataclass


@dataclass(frozen=True)
class DelegationPolicy:

    require_existing_authority: bool
    forbid_self_delegation: 		bool
    allow_emergency_delegation: bool