from dataclasses import dataclass


@dataclass(frozen=True)
class IdentityPolicy:

    allow_role_change: 		bool
    require_registration: bool