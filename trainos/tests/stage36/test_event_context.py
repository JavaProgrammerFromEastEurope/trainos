from kernel.events.context.event_context import EventContext
from kernel.events.context.event_metadata import EventMetadata
from kernel.events.context.context_engine import ContextEngine
from kernel.events.context.context_state import ContextState


def test_event_context():

    context = EventContext(
        event_id="EVENT-006",
        metadata=EventMetadata(
            publisher_id="PUB-1",
            runtime_id="RUN-1",
            tick=50,
            correlation_id="CORR-001",
        ),
    )

    result = ContextEngine().activate(context)
    assert result.state == ContextState.ACTIVE
    assert result.metadata.tick == 50
    assert result.metadata.correlation_id == "CORR-001"
