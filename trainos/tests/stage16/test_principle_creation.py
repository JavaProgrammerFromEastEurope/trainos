from trainos.kernel.identity.principles.civilization_principle import (
    CivilizationPrinciple,
)
from trainos.kernel.identity.principles.principle_type import PrincipleType


def test_principle_creation():
    principle = CivilizationPrinciple(
        name="Never abandon passengers",
        description="Core survival principle",
        type=PrincipleType.ABSOLUTE,
    )

    assert principle.name == "Never abandon passengers"
    assert principle.type == PrincipleType.ABSOLUTE
