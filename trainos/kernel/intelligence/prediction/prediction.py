from dataclasses import dataclass

from .prediction_horizon import PredictionHorizon


@dataclass
class Prediction:

    description: str
    horizon: PredictionHorizon