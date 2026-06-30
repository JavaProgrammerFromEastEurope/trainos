from dataclasses import dataclass

from trainos.kernel.identity.principles.civilization_principle import (
    CivilizationPrinciple,
)


@dataclass(frozen=True)
class PrincipleConflictResolution:
    winner: CivilizationPrinciple