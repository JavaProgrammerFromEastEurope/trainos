from kernel.behavior.goap.goap_goal import GOAPGoal
from kernel.behavior.goap.goap_plan import GOAPPlan
from kernel.behavior.goap.goap_planner import GOAPPlanner


def test_goap():

    planner = GOAPPlanner()
    plan = planner.plan(GOAPGoal(name="recharge"))

    assert isinstance(plan, GOAPPlan)
    assert len(plan.actions) == 0
