from trainos.kernel.ai.goals.goal import Goal
from trainos.kernel.ai.goals.goal_manager import GoalManager


def test_goal_system():
    manager = GoalManager()
    goal = Goal(id="goal_1", description="test")
    manager.add(goal)
    assert manager.get("goal_1") is goal
