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


def test_repeated_diagnostics_track_first_seen_latest_event_and_occurrences():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service)
    first = publish(service, message="first", sequence=1)
    second = publish(service, message="second", sequence=2)

    snapshot = monitor.snapshot()
    assert snapshot.total_events == 2
    finding = snapshot.recent_findings[0]
    assert finding.event_id == second.event_id
    assert finding.message == "second"
    assert finding.sequence == 2
    assert finding.occurrences == 2
    assert finding.repeated is True
    assert finding.first_seen_iso == first.timestamp.isoformat()
    assert finding.timestamp_iso == second.timestamp.isoformat()
    assert snapshot.repeated_groups_count == 1
    assert snapshot.repeated_occurrences_count == 1
    monitor.close()


def test_execution_summary_isolated_by_execution_and_severity():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service)
    publish(service, execution_id="exec-1", code="same", severity="critical")
    publish(service, execution_id="exec-1", code="same", severity="error")
    publish(service, execution_id="exec-1", code="other", severity="warning")
    publish(service, execution_id="exec-2", code="same", severity="error")

    summary = monitor.summary_for_execution("exec-1")
    assert summary.execution_id == "exec-1"
    assert summary.retained_groups == 2
    assert summary.repeated_groups == 1
    assert summary.retained_occurrences == 3
    assert summary.repeated_occurrences == 1
    assert dict(summary.severity_counts) == {"error": 1, "warning": 1}
    assert monitor.summary_for_execution("exec-2").retained_groups == 1
    monitor.close()


def test_recurrence_metadata_is_bounded_with_retained_groups():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service, max_findings=2)
    publish(service, execution_id="old", code="repeat")
    publish(service, execution_id="old", code="repeat")
    publish(service, execution_id="new-1", code="a")
    publish(service, execution_id="new-2", code="b")

    snapshot = monitor.snapshot()
    assert snapshot.total_events == 4
    assert len(snapshot.recent_findings) == 2
    assert all(item.execution_id != "old" for item in snapshot.recent_findings)
    assert snapshot.repeated_groups_count == 0
    assert monitor.summary_for_execution("old").retained_groups == 0
    monitor.close()


def test_unhashable_or_unknown_severity_is_counted_as_malformed():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service)
    for severity in ([], "urgent-unknown"):
        service.publish("exec-1", CommandEventType.EXECUTION_INTEGRITY_DIAGNOSTIC, {
            "diagnostic_type": "execution_integrity",
            "execution_id": "exec-1",
            "code": "bad",
            "severity": severity,
            "message": "bad severity",
        })
    snapshot = monitor.snapshot()
    assert snapshot.total_events == 0
    assert snapshot.malformed_events == 2
    assert snapshot.recent_findings == ()
    monitor.close()


def test_execution_summary_rejects_blank_identifier():
    service = CommandEventService()
    monitor = ExecutionDiagnosticMonitor(service)
    for value in ("", "   ", None, 12):
        try:
            monitor.summary_for_execution(value)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid execution_id must be rejected")
    monitor.close()
