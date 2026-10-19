from .command import Command
from .command_status import CommandStatus


class CommandEngine:

    def accept(
        self,
        command: Command,
    ) -> Command:

        return Command(
            command_id=command.command_id,
            name=command.name,
            priority=command.priority,
            status=CommandStatus.ACCEPTED,
        )


    def execute(
        self,
        command: Command,
    ) -> Command:

        return Command(
            command_id=command.command_id,
            name=command.name,
            priority=command.priority,
            status=CommandStatus.EXECUTED,
        )
