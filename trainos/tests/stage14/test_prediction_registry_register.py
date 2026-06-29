from trainos.kernel.intelligence.prediction.prediction import Prediction
from trainos.kernel.intelligence.prediction.prediction_horizon import PredictionHorizon
from trainos.kernel.intelligence.prediction.prediction_registry import (
    PredictionRegistry,
)


def test_prediction_registry_register():

    registry = PredictionRegistry()
    prediction = Prediction(
        description="water shortage",
        horizon=PredictionHorizon.SHORT_TERM,
    )
    registry.register(prediction)
    assert registry.predictions() == (prediction,)
