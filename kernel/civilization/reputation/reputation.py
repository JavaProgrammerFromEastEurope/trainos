from dataclasses import dataclass

from .reputation_score import ReputationScore


@dataclass
class Reputation:

    score: ReputationScore
