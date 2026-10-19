from kernel.governance.decisions.decision import Decision
from kernel.governance.decisions.decision_engine import DecisionEngine
from kernel.governance.decisions.decision_status import DecisionStatus
from kernel.governance.decisions.decision_type import DecisionType


def test_decision_engine():

    engine = DecisionEngine()
    decision = Decision(
        decision_id="D1",
        authority_id="A1",
        title="Emergency",
        decision_type=DecisionType.EMERGENCY,
        status=DecisionStatus.PROPOSED,
    )

    approved = engine.approve(decision)
    assert approved.status == DecisionStatus.APPROVED

    executed = engine.execute(approved)
    assert executed.status == DecisionStatus.EXECUTED
