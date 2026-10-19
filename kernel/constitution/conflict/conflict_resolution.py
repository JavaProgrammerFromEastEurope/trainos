from dataclasses import dataclass


@dataclass(frozen=True)
class ConstitutionalConflictResolution:

    winning_article: str
    explanation: str