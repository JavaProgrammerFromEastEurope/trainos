from dataclasses import dataclass


@dataclass(frozen=True)
class GovernancePolicy:

    allow_reform: bool