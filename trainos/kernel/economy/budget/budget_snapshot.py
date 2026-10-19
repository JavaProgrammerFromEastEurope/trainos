from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class BudgetSnapshot:

    planned_total: 		Decimal
    allocated_total: 	Decimal