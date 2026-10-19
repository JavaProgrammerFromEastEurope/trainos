from .meta_state import MetaState
from .meta_cycle import MetaCycle
from .meta_orchestrator import MetaOrchestrator


class MetaCivilizationEngine:

    def __init__(self) -> None:
        self.cycle = MetaCycle()
        self.orchestrator = MetaOrchestrator()

    def step(self, state: MetaState):
        tick = self.cycle.tick()
        decision = self.orchestrator.decide(state)
        return {
            "tick": tick,
            "decision": decision,
        }
