from trainos.kernel.identity.principles.principle_engine import PrincipleEngine
from trainos.kernel.identity.principles.civilization_principle import CivilizationPrinciple


def test_principle_engine():
    engine = PrincipleEngine()

    principle = CivilizationPrinciple(
        name="Maintain order",
        description="Operational stability",
        type="strategic"
    )

    result = engine.establish(principle)

    assert result == principle