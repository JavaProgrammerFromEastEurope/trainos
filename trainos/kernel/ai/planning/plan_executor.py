from __future__ import annotations

from trainos.kernel.ai.command_generation.decision_to_command_pipeline import (
    DecisionToCommandPipeline,
)
from trainos.kernel.command_bus.command_bus import CommandBus
from trainos.kernel.command_bus.command_context import CommandContext


class PlanExecutor:

    def __init__(
        self,
        bus: CommandBus,
    ) -> None:
        self._bus = bus
        self._pipeline = DecisionToCommandPipeline()

    def execute(self, plan):
        context = CommandContext()
        for step in plan.steps:
            cmd = self._pipeline.execute([])
            for c in cmd:
                self._bus.send(c, context)
