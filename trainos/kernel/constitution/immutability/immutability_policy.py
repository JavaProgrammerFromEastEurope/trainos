from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutabilityPolicy:

    allow_override: bool