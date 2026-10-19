from .goal_engine import GoalEngine


class GoalRuntime:

    def __init__(self) -> None:
        self._engine = GoalEngine()

    def initialize(self) -> None:
        pass

    def update(self, goal):
        return self._engine.activate(goal)

    def shutdown(self) -> None:
        pass
