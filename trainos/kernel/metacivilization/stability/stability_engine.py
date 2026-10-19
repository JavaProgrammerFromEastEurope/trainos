from .drift_event import DriftEvent
from .stability_controller import StabilityController


class StabilityEngine:

    def __init__(self) -> None:
        self.controller = StabilityController()

    def process(self, event: DriftEvent) -> DriftEvent:
        return self.controller.evaluate(event)
