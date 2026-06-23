from trainos.kernel.metacivilization.goals.goal import Goal
from trainos.kernel.metacivilization.goals.goal_type import GoalType
from trainos.kernel.metacivilization.goals.goal_registry import GoalRegistry


def test_goal_registry_add():

    registry = GoalRegistry()

    goal = Goal(type=GoalType.SURVIVAL)

    registry.add(goal)

    assert registry.goals() == (goal,)