from .value_assessment import ValueAssessment


class ValueEngine:

    def evaluate(self, outcome: str) -> ValueAssessment:
        return ValueAssessment(outcome=outcome, scores=())
