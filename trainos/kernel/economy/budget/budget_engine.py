from decimal import Decimal

from .allocation import Allocation
from .budget_item import BudgetItem


class BudgetEngine:

    def allocate(
        self,
        item: BudgetItem,
        amount: Decimal,
    ) -> Allocation:
        return Allocation(
            allocation_id="AUTO",
            item_id=item.item_id,
            allocated_amount=amount,
        )
