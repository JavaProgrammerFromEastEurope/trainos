import pytest
from kernel.command.events.event_service import CommandEventService
from kernel.command.events.event_type import CommandEventType
from kernel.command.events.execution_event_adapter import ExecutionEventAdapter


def test_adapter_publishes_all_lifecycle_event_types_with_expected_payloads():
    service = CommandEventService()
    adapter = ExecutionEventAdapter(service)
    emitted = [
        adapter.command_created("cmd", "email"),
        adapter.command_started("cmd", "mail-handler"),
        adapter.progress_updated("cmd", 1, 3, False),
        adapter.command_retrying("cmd", 2, "temporary"),
        adapter.command_completed("cmd", {"ok": True}),
        adapter.command_failed("cmd", "boom", 3),
        adapter.command_cancelled("cmd", "requested"),
    ]
    assert [event.event_type for event in emitted] == list(CommandEventType)
    assert emitted[0].payload == {"command_type": "email"}
    assert emitted[1].payload == {"handler": "mail-handler"}
    assert emitted[2].payload == {"attempts": 1, "max_attempts": 3, "completed": False}
    assert emitted[3].payload == {"attempt": 2, "reason": "temporary"}
    assert emitted[4].payload == {"result": {"ok": True}}
    assert emitted[5].payload == {"error_message": "boom", "attempt": 3}
    assert emitted[6].payload == {"reason": "requested"}
    assert service.registry.get_events("cmd") == tuple(emitted)


def test_adapter_rejects_invalid_progress_and_retry_attempts():
    adapter = ExecutionEventAdapter(CommandEventService())
    for args in [("cmd", -1, 3, False), ("cmd", 0, 0, False), ("cmd", 4, 3, False)]:
        with pytest.raises(ValueError):
            adapter.progress_updated(*args)
    with pytest.raises(ValueError):
        adapter.command_retrying("cmd", 0)
