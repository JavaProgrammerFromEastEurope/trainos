from dataclasses import dataclass


@dataclass(frozen=True)
class IntelligenceMetrics:

    reasoning_events: int
    predictions: 			int
    hypotheses: 			int