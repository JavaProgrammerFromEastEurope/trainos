from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumptionPolicy:

    require_inventory_check: 	bool
    allow_negative_inventory: bool