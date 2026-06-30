from dataclasses import dataclass


@dataclass(frozen=True)
class PrinciplePolicy:

    allow_modification: bool