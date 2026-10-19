from __future__ import annotations

from abc import ABC, abstractmethod

from .command import Command
from .command_context import CommandContext
from .command_result 	import CommandResult


class CommandHandler(ABC):

    @abstractmethod
    def execute(
        self,
        command: Command,
        context: CommandContext,
    ) -> CommandResult:
        pass