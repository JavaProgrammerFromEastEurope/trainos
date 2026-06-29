from .learning_engine import LearningEngine


class LearningRuntime:

    def __init__(self) -> None:
        self._engine = LearningEngine()

    def initialize(self) -> None:
        pass

    def update(self, event):
        return self._engine.process(event)

    def shutdown(self) -> None:
        pass
