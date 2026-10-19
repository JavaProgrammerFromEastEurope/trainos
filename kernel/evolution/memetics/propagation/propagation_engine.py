from .propagation_event import PropagationEvent


class PropagationEngine:

    def propagate(
        self,
        event: PropagationEvent,
    ) -> PropagationEvent:
        return PropagationEvent(
            meme=event.meme,
            source=event.source,
            target=event.target,
        )
