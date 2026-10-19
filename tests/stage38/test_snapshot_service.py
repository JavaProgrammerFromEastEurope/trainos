import pytest
from kernel.command.snapshots.snapshot_service import CommandSnapshotService


def test_snapshot_service_keeps_bounded_per_command_history_and_clears_correctly():
    service = CommandSnapshotService(max_history_per_command=2)
    snapshots = [
        service.capture(
            command_id="cmd-1",
            command_type="job",
            command_state=f"s{i}",
            attempt_count=i,
            execution_status="running",
        )
        for i in range(3)
    ]
    other = service.capture(
        command_id="cmd-2",
        command_type="job",
        command_state="created",
        attempt_count=0,
        execution_status="created",
    )
    assert service.get_history("cmd-1") == tuple(snapshots[-2:])
    assert service.get_latest("cmd-1") is snapshots[-1]
    assert service.get_latest("cmd-2") is other
    assert (
        service.get_history("missing") == () and service.get_latest("missing") is None
    )
    with pytest.raises(AttributeError):
        service.get_history("cmd-1").append(other)
    service.clear("cmd-1")
    assert service.get_history("cmd-1") == ()
    assert service.get_latest("cmd-2") is other
    service.clear()
    assert service.get_latest("cmd-2") is None
    with pytest.raises(ValueError):
        CommandSnapshotService(0)
