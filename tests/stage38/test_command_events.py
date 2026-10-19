from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
import pytest

from kernel.command.events.command_event import CommandEvent
from kernel.command.events.event_type import CommandEventType
from kernel.command.events.event_registry import EventRegistry


def test_event_creation_validation_immutability_and_bounded_registry():
    source_payload = {"attempt": 1}
    event = CommandEvent.create(
        "cmd-1", CommandEventType.COMMAND_CREATED, source_payload
    )
    source_payload["attempt"] = 99
    assert event.payload["attempt"] == 1
    assert event.timestamp.tzinfo is not None
    with pytest.raises(FrozenInstanceError):
        event.command_id = "other"
    with pytest.raises(ValueError):
        CommandEvent.create(" ", CommandEventType.COMMAND_CREATED)
    with pytest.raises(TypeError):
        CommandEvent.create("cmd", "command_created")
    registry = EventRegistry(max_events_per_command=2)
    events = [
        CommandEvent.create("cmd-1", CommandEventType.COMMAND_STARTED, {"n": n})
        for n in range(3)
    ]
    for item in events:
        registry.register(item)
    assert registry.get_events("cmd-1") == tuple(events[-2:])
    assert registry.get_latest("cmd-1") is events[-1]
    assert registry.get_events("missing") == ()
    registry.clear("cmd-1")
    assert registry.get_latest("cmd-1") is None
    registry.register(events[0])
    registry.clear()
    assert registry.get_events("cmd-1") == ()
    with pytest.raises(ValueError):
        EventRegistry(0)
