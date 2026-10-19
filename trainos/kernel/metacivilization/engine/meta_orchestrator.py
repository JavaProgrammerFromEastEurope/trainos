from .meta_state import MetaState
from .meta_decision import MetaDecision


class MetaOrchestrator:

    def decide(self, state: MetaState) -> MetaDecision:
        return MetaDecision(
            description="stabilize civilization trajectory",
        )
