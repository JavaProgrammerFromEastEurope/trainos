from trainos.kernel.ai.decision.decision_context import DecisionContext
from trainos.kernel.ai.decision.decision_engine import DecisionEngine


def test_decision_engine():

    engine = DecisionEngine()
    context = DecisionContext(state_snapshot={})

    decisions = engine.analyze(context)
    assert len(decisions) == 1
    assert decisions[0].action == "initialize_state"
