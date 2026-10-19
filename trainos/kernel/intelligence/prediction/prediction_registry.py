from __future__ import annotations

from .prediction import Prediction


class PredictionRegistry:

    def __init__(self) -> None:
        self._predictions: list[Prediction] = []

    def register(self, prediction: Prediction) -> None:
        self._predictions.append(prediction)

    def predictions(self) -> tuple[Prediction, ...]:
        return tuple(self._predictions)
