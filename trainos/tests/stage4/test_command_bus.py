from trainos.kernel.command_bus.command_bus import CommandBus
from trainos.kernel.command_bus.command_service import CommandService


def test_command_bus():

    service = CommandService()
    bus = CommandBus(service)

    class Cmd:
        pass

    class Handler:
        def execute(self, c, ctx):
            return "done"

    service.register(Cmd, Handler())
    result = bus.send(Cmd())
    assert result.data == "done"
