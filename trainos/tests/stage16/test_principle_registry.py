from trainos.kernel.identity.principles.principle_registry import PrincipleRegistry
from trainos.kernel.identity.principles.civilization_principle import CivilizationPrinciple
from trainos.kernel.identity.principles.principle_type import PrincipleType


def test_principle_registry():
    registry = PrincipleRegistry()

    principle = CivilizationPrinciple(
        name="Protect train integrity",
        description="System stability principle",
        type=PrincipleType.STRATEGIC
    )

    registry.register(principle)

    assert len(registry.principles()) == 1