from dataclasses import dataclass

from trainos.kernel.strategy.goals.goal import Goal


@dataclass(frozen=True)
class ArbitrationResult:

    selected: Goal