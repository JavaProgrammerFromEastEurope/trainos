from .feedback_event import FeedbackEvent


class FeedbackEngine:

    def propagate(self, event: FeedbackEvent) -> FeedbackEvent:
        adjusted_intensity = event.intensity * 1.1
        return FeedbackEvent(
            origin=event.origin,
            signal=event.signal,
            intensity=adjusted_intensity,
        )