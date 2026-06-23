from .cross_system_event import CrossSystemEvent


class InteractionEngine:

    def propagate(self, event: CrossSystemEvent) -> CrossSystemEvent:
        return CrossSystemEvent(
            source_system=event.source_system,
            target_system=event.target_system,
            payload=event.payload,
        )
