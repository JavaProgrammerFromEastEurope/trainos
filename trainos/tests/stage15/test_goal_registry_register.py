from trainos.kernel.strategy.goals.goal import Goal
from trainos.kernel.strategy.goals.goal_id import GoalId
from trainos.kernel.strategy.goals.goal_priority import GoalPriority
from trainos.kernel.strategy.goals.goal_registry import GoalRegistry


def test_goal_registry_register():

    registry = GoalRegistry()
    goal = Goal(
        id=GoalId("goal-1"),
        description="increase food production",
        priority=GoalPriority.HIGH,
    )
    registry.register(goal)
    assert registry.goals() == (goal,)
