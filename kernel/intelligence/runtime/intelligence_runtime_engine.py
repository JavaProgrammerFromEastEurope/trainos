from .intelligence_cycle import IntelligenceCycle


class IntelligenceRuntimeEngine:

    def __init__(self) -> None:
        self._index = 0

    def next_cycle(self) -> IntelligenceCycle:
        self._index += 1
        return IntelligenceCycle(index=self._index)
