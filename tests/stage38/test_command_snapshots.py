from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
import pytest

from kernel.command.snapshots.command_snapshot import CommandSnapshot
from kernel.command.command.command_status import CommandStatus
from kernel.command.execution.execution_status import ExecutionStatus


def test_snapshot_serialization_validation_and_enum_normalization():
    snapshot = CommandSnapshot.create(
        command_id="cmd-1",
        command_type="email",
        command_state=CommandStatus.ACCEPTED,
        attempt_count=2,
        execution_status=ExecutionStatus.RUNNING,
        active_handler="mail",
        error_message=None,
    )
    data = snapshot.to_dict()
    assert data["command_state"] == "accepted"
    assert data["execution_status"] == "running"
    assert data["attempt_count"] == 2 and data["active_handler"] == "mail"
    assert datetime.fromisoformat(data["timestamp"]).tzinfo is not None
    with pytest.raises(FrozenInstanceError):
        snapshot.command_id = "other"
    with pytest.raises(ValueError):
        CommandSnapshot.create(
            command_id="",
            command_type="email",
            command_state="created",
            attempt_count=0,
            execution_status="created",
        )
    with pytest.raises(ValueError):
        CommandSnapshot.create(
            command_id="cmd",
            command_type="email",
            command_state="created",
            attempt_count=-1,
            execution_status="created",
        )
    with pytest.raises(ValueError):
        CommandSnapshot(
            "cmd",
            "email",
            "created",
            0,
            "created",
            None,
            datetime.now().replace(tzinfo=None),
        )
