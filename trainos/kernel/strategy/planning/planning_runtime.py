from .planning_engine import PlanningEngine


class PlanningRuntime:

    def __init__(self) -> None:
        self._engine = PlanningEngine()

    def initialize(self) -> None:
        pass

    def update(self, plan):
        return self._engine.build(plan)

    def shutdown(self) -> None:
        pass
