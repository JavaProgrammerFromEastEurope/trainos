from kernel.strategy.arbitration.arbitration_registry import ArbitrationRegistry
from kernel.strategy.arbitration.arbitration_result import ArbitrationResult
from kernel.strategy.goals.goal import Goal
from kernel.strategy.goals.goal_id import GoalId
from kernel.strategy.goals.goal_priority import GoalPriority


def test_arbitration_registry_register():

    registry = ArbitrationRegistry()
    goal = Goal(
        id=GoalId("goal-1"),
        description="save energy",
        priority=GoalPriority.HIGH,
    )
    result = ArbitrationResult(selected=goal)
    registry.register(result)
    assert registry.results() == (result,)
