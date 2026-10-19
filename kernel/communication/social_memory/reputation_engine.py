from .reputation_score import ReputationScore


class ReputationEngine:

    def evaluate(self) -> ReputationScore:
        return ReputationScore(value=1.0)
