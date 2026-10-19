from .emergence_event import EmergenceEvent


class EmergenceDetector:

    def detect(self, signal: str) -> EmergenceEvent | None:
        if "pattern" in signal:
            return EmergenceEvent(
                source="system",
                pattern="unknown_behavior",
                strength=0.7,
            )
        return None
