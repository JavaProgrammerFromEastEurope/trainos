from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AuthorityPolicy:

    allow_decisions: bool 	= True
    allow_suspension: bool 	= True