from .prediction import Prediction
from .prediction_horizon import PredictionHorizon


class PredictionEngine:

    def predict(self, description: str) -> Prediction:
        return Prediction(
            description=description,
            horizon=PredictionHorizon.SHORT_TERM,
        )
