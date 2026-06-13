from __future__ import annotations

from typing import List
from trainos.kernel.command_bus.command 	import Command
from trainos.kernel.ai.decision.decision 	import Decision


class CommandGenerator:

    def generate(
        self,
        decisions: List[Decision],
    ) -> List[Command]:
        commands: List[Command] = []
        for decision in decisions:
            if decision.action 		== "initialize_state":
                commands.append(Command())
            elif decision.action 	== "trigger_recovery":
                commands.append(Command())
        return commands
