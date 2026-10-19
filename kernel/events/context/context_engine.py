from .context_state import ContextState
from .event_context import EventContext


class ContextEngine:

    def activate(
        self,
        context: EventContext,
    ) -> EventContext:
        return EventContext(
            event_id=context.event_id,
            metadata=context.metadata,
            state=ContextState.ACTIVE,
        )

    def close(
        self,
        context: EventContext,
    ) -> EventContext:
        return EventContext(
            event_id=context.event_id,
            metadata=context.metadata,
            state=ContextState.CLOSED,
        )
