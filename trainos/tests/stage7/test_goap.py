from trainos.kernel.behavior.goap.goap_goal import GOAPGoal
from trainos.kernel.behavior.goap.goap_plan import GOAPPlan
from trainos.kernel.behavior.goap.goap_planner import GOAPPlanner


def test_goap():

    planner = GOAPPlanner()
    plan = planner.plan(GOAPGoal(name="recharge"))

    assert isinstance(plan, GOAPPlan)
    assert len(plan.actions) == 0
