from kernel.command.events import (
    CommandEventService,
    CommandEventType,
    ExecutionDiagnosticMonitor,
)


def publish(service, *, execution_id="exec-1", code="invalid_transition", severity="critical", message="bad transition", **extra):
    payload = {
        "diagnostic_type": "execution_integrity",
        "execution_id": execution_id,
        "code": code,
        "severity": severity,
        "message": message,
        **extra,
    }
    return service.publish(execution_id, CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC, payload)


def test_monitor_aggregates_counts_and_latest_per_execution_code():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service)
    publish(service, message="first", sequence=1)
    publish(service, message="updated", sequence=2)
    publish(service, execution_id="exec-2", code="invalid_progress", severity="error")

    snapshot = monitor.snapshot()
    assert snapshot.total_events == 3
    assert snapshot.malformed_events == 0
    assert snapshot.critical_count == 2
    assert snapshot.error_count == 1
    assert len(snapshot.recent_findings) == 2
    latest = next(item for item in snapshot.recent_findings if item.execution_id == "exec-1")
    assert latest.message == "updated"
    assert latest.sequence == 2
    monitor.close()


def test_monitor_bounds_retained_findings_but_keeps_cumulative_counts():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service, max_findings=2)
    for i in range(4):
        publish(service, execution_id=f"exec-{i}", code=f"code-{i}", severity="error")
    snapshot = monitor.snapshot()
    assert snapshot.total_events == 4
    assert len(snapshot.recent_findings) == 2
    assert snapshot.error_count == 4
    monitor.close()


def test_monitor_counts_malformed_events_without_retaining_them():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service)
    service.publish("exec-1", CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC, {
        "diagnostic_type": "execution_integrity",
        "execution_id": "exec-1",
        "code": "bad",
        "severity": "urgent-unknown",
        "message": "bad severity",
    })
    snapshot = monitor.snapshot()
    assert snapshot.total_events == 0
    assert snapshot.malformed_events == 1
    assert snapshot.recent_findings == ()
    monitor.close()


def test_monitor_unsubscribes_on_close_and_close_is_idempotent():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service)
    publish(service)
    monitor.close()
    monitor.close()
    publish(service, execution_id="exec-2")
    assert monitor.snapshot().total_events == 1


def test_monitor_rejects_invalid_capacity_and_event_service():
    try:
        ExecutionDiagnosticMonitor(CommandEventService(), max_findings=0)
    except ValueError:
        pass
    else:
        raise AssertionError("zero capacity must be rejected")
    try:
        ExecutionDiagnosticMonitor(object())
    except TypeError:
        pass
    else:
        raise AssertionError("invalid event service must be rejected")
