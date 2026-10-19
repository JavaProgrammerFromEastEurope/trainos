from dataclasses import dataclass

from .consumption_category import ConsumptionCategory
from .consumption_type import ConsumptionType


@dataclass(frozen=True, slots=True)
class ConsumptionDefinition:

    consumption_id: str
    name: str
    consumption_type: ConsumptionType
    category: ConsumptionCategory
