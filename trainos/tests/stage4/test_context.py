from trainos.kernel.command_bus.command_context import CommandContext


def test_context():
    ctx = CommandContext()
    assert ctx.correlation_id is not None
    assert ctx.trace_id 			is not None
