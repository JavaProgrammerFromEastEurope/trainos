from kernel.command.events import (
    CommandEventService,
    CommandEventType,
    ExecutionIntegrityEventAdapter,
)
from kernel.command.execution.command_execution import CommandExecution
from kernel.command.execution.execution_audit_store import ExecutionAuditStore
from kernel.command.execution.execution_progress import ExecutionProgress
from kernel.command.execution.execution_status import ExecutionStatus


def execution(status, *, completed=False):
    return CommandExecution(
        execution_id="exec-stage48",
        command_id="cmd-stage48",
        progress=ExecutionProgress(attempts=0, max_attempts=1, completed=completed),
        status=status,
    )


def finding(code="invalid_transition", execution_id="exec-stage48"):
    return {
        "code": code,
        "execution_id": execution_id,
        "message": f"Detected {code}",
        "sequence": 2,
    }


def test_clean_store_publishes_no_events(tmp_path):
    service = CommandEventService()
    with ExecutionAuditStore(tmp_path / "clean.sqlite3") as store:
        store.append(execution(ExecutionStatus.CREATED))
        store.append(execution(ExecutionStatus.RUNNING))
        before = store.get_history("exec-stage48")
        result = ExecutionIntegrityEventAdapter(service).verify_and_publish(store)
        assert result.findings_count == 0
        assert result.published_events == ()
        assert result.successful
        assert store.get_history("exec-stage48") == before
    assert service.registry.get_events("exec-stage48") == ()


def test_findings_publish_as_structured_events_with_severity():
    service = CommandEventService()
    result = ExecutionIntegrityEventAdapter(service).publish_findings([
        finding("invalid_transition"),
        finding("invalid_progress"),
    ])
    assert result.successful
    assert result.findings_count == 2
    assert len(result.published_events) == 2
    first, second = result.published_events
    assert first.event_type is CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC
    assert first.command_id == "exec-stage48"
    assert first.payload["diagnostic_type"] == "execution_integrity"
    assert first.payload["severity"] == "critical"
    assert first.payload["sequence"] == 2
    assert second.payload["severity"] == "error"
    assert service.registry.get_events("exec-stage48") == (first, second)


def test_publish_exception_is_reported_and_later_findings_are_attempted(monkeypatch):
    service = CommandEventService()
    original_publish = service.publish
    calls = []

    def flaky_publish(**kwargs):
        calls.append(kwargs["payload"]["code"])
        if kwargs["payload"]["code"] == "invalid_transition":
            raise RuntimeError("event store unavailable")
        return original_publish(**kwargs)

    monkeypatch.setattr(service, "publish", flaky_publish)
    result = ExecutionIntegrityEventAdapter(service).publish_findings([
        finding("invalid_transition"), finding("invalid_progress")
    ])
    assert calls == ["invalid_transition", "invalid_progress"]
    assert len(result.publish_failures) == 1
    assert "event store unavailable" in result.publish_failures[0]["error"]
    assert len(result.published_events) == 1
    assert not result.successful


def test_subscriber_errors_are_reported_without_blocking_other_subscribers():
    service = CommandEventService()
    seen = []

    def broken(_event):
        raise RuntimeError("observer unavailable")

    service.dispatcher.subscribe(CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC, broken)
    service.dispatcher.subscribe(CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC, seen.append)
    result = ExecutionIntegrityEventAdapter(service).publish_findings([finding()])
    assert len(result.published_events) == 1
    assert len(result.subscriber_failures) == 1
    assert "observer unavailable" in result.subscriber_failures[0]["error"]
    assert seen == list(result.published_events)
    assert not result.successful


def test_adapter_rejects_malformed_findings():
    adapter = ExecutionIntegrityEventAdapter(CommandEventService())
    try:
        adapter.publish_findings([{"code": "invalid_transition"}])
    except ValueError as exc:
        assert "execution_id, code and message" in str(exc)
    else:
        raise AssertionError("malformed finding must be rejected")
