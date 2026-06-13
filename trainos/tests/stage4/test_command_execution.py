from trainos.kernel.command_bus.command import Command
from trainos.kernel.command_bus.command_handler import CommandHandler
from trainos.kernel.command_bus.command_service import CommandService
from trainos.kernel.command_bus.command_context import CommandContext
from trainos.kernel.command_bus.command_result import CommandResult


class DummyCommand(Command):
    pass


class DummyHandler(CommandHandler):
    def execute(self, command, context):
        return CommandResult(True, "ok")


def test_command_execution():

    service = CommandService()
    service.register(DummyCommand, DummyHandler())
    result = service.execute(DummyCommand(), CommandContext())
    assert result.success is True
    assert result.data == "ok"
