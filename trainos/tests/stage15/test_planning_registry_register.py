from trainos.kernel.strategy.planning.plan_step import PlanStep
from trainos.kernel.strategy.planning.planning_registry import PlanningRegistry
from trainos.kernel.strategy.planning.strategic_plan import StrategicPlan


def test_planning_registry_register():

    registry = PlanningRegistry()
    plan = StrategicPlan(
        name="Food Plan",
        description="Increase food reserves",
        steps=(
            PlanStep(
                name="Expand hydroponics",
                description="Build new sector",
            ),
        ),
    )
    registry.register(plan)
    assert registry.plans() == (plan,)
