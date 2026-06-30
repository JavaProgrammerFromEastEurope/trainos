from dataclasses import dataclass

from trainos.kernel.identity.principles.civilization_principle import (
    CivilizationPrinciple,
)


@dataclass(frozen=True)
class PrincipleConflict:

    left: CivilizationPrinciple
    right: CivilizationPrinciple
