from decimal import Decimal

from kernel.economy.budget.budget_item import BudgetItem
from kernel.economy.budget.budget_engine import BudgetEngine


def test_budget_allocate():

    item = BudgetItem(
        item_id="MED",
        budget_id="FY2027",
        category="Healthcare",
        planned_amount=Decimal("500"),
    )

    engine = BudgetEngine()

    allocation = engine.allocate(
        item,
        Decimal("200"),
    )

    assert allocation.allocated_amount == Decimal("200")
