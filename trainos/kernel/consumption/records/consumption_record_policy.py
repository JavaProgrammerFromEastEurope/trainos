from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumptionRecordPolicy:

    require_positive_quantity: bool = True