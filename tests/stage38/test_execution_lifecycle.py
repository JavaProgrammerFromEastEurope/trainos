from dataclasses import FrozenInstanceError
import pytest

from kernel.command.execution.command_execution import CommandExecution
from kernel.command.execution.execution_engine import ExecutionEngine
from kernel.command.execution.execution_progress import ExecutionProgress
from kernel.command.execution.execution_status import ExecutionStatus


def test_execution_start_and_complete_are_immutable_state_transitions():
    progress = ExecutionProgress(attempts=1, max_attempts=3, completed=False)
    original = CommandExecution("exec-1", "cmd-1", progress)
    engine = ExecutionEngine()
    started = engine.start(original)
    completed = engine.complete(started)
    assert original.status is ExecutionStatus.CREATED
    assert started.status is ExecutionStatus.RUNNING
    assert completed.status is ExecutionStatus.COMPLETED
    assert started.progress is progress and completed.progress is progress
    assert completed.execution_id == original.execution_id
    with pytest.raises(FrozenInstanceError):
        started.status = ExecutionStatus.FAILED
    with pytest.raises(ValueError):
        CommandExecution(" ", "cmd", progress)
    with pytest.raises(TypeError):
        CommandExecution("exec", "cmd", object())
