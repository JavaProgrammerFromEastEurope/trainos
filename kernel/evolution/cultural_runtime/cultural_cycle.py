class CulturalCycle:

    def __init__(self) -> None:
        self._tick = 0

    def next_tick(self) -> int:
        self._tick += 1
        return self._tick