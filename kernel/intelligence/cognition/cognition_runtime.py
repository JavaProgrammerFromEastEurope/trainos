from .cognition_engine import CognitionEngine


class CognitionRuntime:

    def __init__(self) -> None:
        self._engine = CognitionEngine()

    def step(self):
        return self._engine.evaluate()
