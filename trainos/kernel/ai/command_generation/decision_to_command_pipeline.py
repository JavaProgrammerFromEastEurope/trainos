from __future__ import annotations

from typing import List

from trainos.kernel.ai.decision.decision import Decision
from .command_generator import CommandGenerator
from trainos.kernel.command_bus.command import Command


class DecisionToCommandPipeline:

    def __init__(self) -> None:
        self._generator = CommandGenerator()

    def execute(
        self,
        decisions: List[Decision],
    ) -> List[Command]:
        return self._generator.generate(decisions)
