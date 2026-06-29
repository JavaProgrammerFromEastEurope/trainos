from trainos.kernel.strategy.goals.goal import Goal
from trainos.kernel.strategy.goals.goal_engine import GoalEngine
from trainos.kernel.strategy.goals.goal_id import GoalId
from trainos.kernel.strategy.goals.goal_priority import GoalPriority


def test_goal_engine_activate():

    engine = GoalEngine()
    goal = Goal(
        id=GoalId("goal-1"),
        description="repair reactor",
        priority=GoalPriority.CRITICAL,
    )
    assert engine.activate(goal) == goal
