from .existential_risk import ExistentialRisk
from .existential_risk_level import ExistentialRiskLevel


class ExistentialRiskEngine:

    def evaluate(self) -> ExistentialRisk:
        return ExistentialRisk(
            level=ExistentialRiskLevel.MODERATE,
        )
