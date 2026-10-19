from .drift_event import DriftEvent


class StabilityController:

    def evaluate(self, event: DriftEvent) -> DriftEvent:
        corrected = event.deviation * 0.8
        return DriftEvent(
            source=event.source,
            deviation=corrected,
        )
