from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorityPolicy:

    require_registered_institution: 	bool
    single_authority_per_institution: bool