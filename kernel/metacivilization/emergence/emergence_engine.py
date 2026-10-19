from .emergence_event import EmergenceEvent
from .emergence_pattern import EmergencePattern


class EmergenceEngine:

    def process(self, event: EmergenceEvent) -> EmergencePattern:
        return EmergencePattern(
            name=event.pattern,
            stability=event.strength,
        )
