from dataclasses import dataclass


@dataclass
class PredictionPolicy:

    confidence_threshold: float