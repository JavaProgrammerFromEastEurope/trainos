from trainos.kernel.metacivilization.existential_risk.existential_risk import ExistentialRisk
from trainos.kernel.metacivilization.existential_risk.existential_risk_level import ExistentialRiskLevel
from trainos.kernel.metacivilization.existential_risk.existential_risk_registry import ExistentialRiskRegistry


def test_existential_risk_registry_add():

    registry = ExistentialRiskRegistry()
    risk = ExistentialRisk(level=ExistentialRiskLevel.MODERATE)
    registry.add(risk)

    assert registry.risks() == (risk,)