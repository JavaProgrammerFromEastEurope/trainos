from dataclasses import dataclass

from .existential_risk_level import ExistentialRiskLevel


@dataclass
class ExistentialRisk:

    level: ExistentialRiskLevel
