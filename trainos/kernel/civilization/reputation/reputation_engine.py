from .reputation import Reputation
from .reputation_score import ReputationScore


class ReputationEngine:

    def evaluate(self) -> Reputation:
        return Reputation(
            score=ReputationScore.NORMAL,
        )
