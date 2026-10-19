from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ConsumptionPolicy:

    policy_id: 	str
    allow_consumption: 		bool = True
    daily_limit: Decimal | None = None
    allow_emergency_override: bool = False
    require_government_approval: bool = False