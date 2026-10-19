from .cultural_cycle 	import CulturalCycle
from .cultural_tick 	import CulturalTick


class CulturalRuntimeEngine:

    def __init__(self) -> None:
        self._cycle = CulturalCycle()

    def step(self) -> CulturalTick:
        return CulturalTick(index=self._cycle.next_tick())
