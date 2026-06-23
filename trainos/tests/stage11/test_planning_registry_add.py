from trainos.kernel.metacivilization.planning.long_term_plan import LongTermPlan
from trainos.kernel.metacivilization.planning.planning_horizon import PlanningHorizon
from trainos.kernel.metacivilization.planning.planning_registry import PlanningRegistry


def test_planning_registry_add():

    registry = PlanningRegistry()

    plan = LongTermPlan(horizon=PlanningHorizon.LONG)

    registry.add(plan)

    assert registry.plans() == (plan,)