from .runtime_tick 	import RuntimeTick
from .runtime_cycle import RuntimeCycle


class RecursiveRuntimeEngine:

    def __init__(self) -> None:
        self._cycle = RuntimeCycle()

    def step(self) -> RuntimeTick:
        index = self._cycle.next_tick()
        return RuntimeTick(index=index)
