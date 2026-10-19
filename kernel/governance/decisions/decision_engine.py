from .decision import Decision
from .decision_status import DecisionStatus


class DecisionEngine:

    def approve(
        self,
        decision: Decision,
    ) -> Decision:
        return Decision(
            decision_id=decision.decision_id,
            authority_id=decision.authority_id,
            title=decision.title,
            decision_type=decision.decision_type,
            status=DecisionStatus.APPROVED,
        )

    def execute(
        self,
        decision: Decision,
    ) -> Decision:
        return Decision(
            decision_id=decision.decision_id,
            authority_id=decision.authority_id,
            title=decision.title,
            decision_type=decision.decision_type,
            status=DecisionStatus.EXECUTED,
        )
