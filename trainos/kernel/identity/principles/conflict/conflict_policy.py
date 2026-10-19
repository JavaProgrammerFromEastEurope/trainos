from dataclasses import dataclass


@dataclass(frozen=True)
class PrincipleConflictPolicy:

    allow_dynamic_resolution: bool