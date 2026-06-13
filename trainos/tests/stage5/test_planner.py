from trainos.kernel.ai.decision.decision import Decision
from trainos.kernel.ai.planning.planner import Planner


def test_planner():

    planner = Planner()

    decisions = [Decision(action="initialize_state",
                          confidence=1.0, payload={})]
    plan = planner.build(decisions)
    assert len(plan.steps) == 1
    assert plan.steps[0].name == "init_state"
