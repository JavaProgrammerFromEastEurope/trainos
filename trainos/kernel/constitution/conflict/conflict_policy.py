from dataclasses import dataclass


@dataclass(frozen=True)
class ConstitutionalConflictPolicy:

    allow_balancing: bool