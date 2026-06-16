from trainos.kernel.behavior.htn.htn_task import (
    HTNTask,
)

from trainos.kernel.behavior.htn.htn_plan import (
    HTNPlan,
)

from trainos.kernel.behavior.htn.htn_planner import (
    HTNPlanner,
)


def test_htn():

    planner = HTNPlanner()
    task = HTNTask(name="mission")
    plan = planner.plan(task)

    assert isinstance(plan, HTNPlan)
    assert len(plan.tasks) == 1
    assert plan.tasks[0] is task
