from .learning_rate import LearningRate


class LearningRateController:

    def current(
        self,
    ) -> LearningRate:
        return LearningRate(value=0.001)
