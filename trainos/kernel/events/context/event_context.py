from dataclasses import dataclass

from .context_state import ContextState
from .event_metadata import EventMetadata


@dataclass(frozen=True, slots=True)
class EventContext:

    event_id: str
    metadata: EventMetadata
    state: ContextState = ContextState.CREATED