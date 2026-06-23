from .awareness_level import AwarenessLevel
from .self_awareness 	import SelfAwareness


class SelfAwarenessEngine:

    def evaluate(self) -> SelfAwareness:
        return SelfAwareness(level=AwarenessLevel.NORMAL)
