from .budget_engine import BudgetEngine


class BudgetRuntime:

    def __init__(self) -> None:
        self._engine = BudgetEngine()

    def initialize(self) -> None:
        pass

    def update(self, *args, **kwargs):
        return self._engine.allocate(*args, **kwargs)

    def shutdown(self) -> None:
        pass
