from dataclasses import dataclass


@dataclass(frozen=True)
class IdentityPolicy:

    mutable: bool
