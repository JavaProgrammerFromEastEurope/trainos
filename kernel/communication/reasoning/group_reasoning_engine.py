from .decision_result import DecisionResult


class GroupReasoningEngine:

    def reason(self) -> DecisionResult:
        return DecisionResult(decision="navigation")
