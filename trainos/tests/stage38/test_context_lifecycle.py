import pytest
from dataclasses import FrozenInstanceError

from kernel.command.context.command_context import CommandContext
from kernel.command.context.command_metadata import CommandMetadata
from kernel.command.context.context_engine import ContextEngine
from kernel.command.context.context_state import ContextState


def test_context_metadata_validation_and_lifecycle_preserve_metadata():
    metadata = CommandMetadata("runtime-1", "scheduler-1", 4, "corr-1", "api")
    context = CommandContext("cmd-1", metadata)
    engine = ContextEngine()
    active = engine.activate(context)
    closed = engine.close(active)
    assert active.state is ContextState.ACTIVE
    assert closed.state is ContextState.CLOSED
    assert active.metadata is metadata and closed.metadata is metadata
    assert active.command_id == closed.command_id == "cmd-1"
    with pytest.raises(FrozenInstanceError):
        metadata.tick = 5
    with pytest.raises(ValueError):
        CommandMetadata("runtime", "scheduler", -1, "corr", "api")
    for bad in [
        ("", "scheduler", "corr", "api"),
        ("runtime", "", "corr", "api"),
        ("runtime", "scheduler", "", "api"),
        ("runtime", "scheduler", "corr", ""),
    ]:
        with pytest.raises(ValueError):
            CommandMetadata(*bad[:2], 0, *bad[2:])
