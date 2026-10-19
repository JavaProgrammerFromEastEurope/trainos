from __future__ import annotations

from .budget import Budget


class BudgetRegistry:

    def __init__(self) -> None:
        self._budgets: dict[str, Budget] = {}

    def register(
        self,
        budget: Budget,
    ) -> None:
        self._budgets[budget.budget_id] = budget

    def get(
        self,
        budget_id: str,
    ) -> Budget | None:
        return self._budgets.get(budget_id)

    def all(
        self,
    ) -> tuple[Budget, ...]:
        return tuple(self._budgets.values())
