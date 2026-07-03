from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class BudgetItem:

    item_id: 		str
    budget_id: 	str
    category: 	str
    planned_amount: Decimal