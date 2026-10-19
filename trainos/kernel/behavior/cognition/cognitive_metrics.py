class CognitiveMetrics:

    def __init__(
        self,
    ) -> None:
        self.cycles = 0

    def increment(
        self,
    ) -> None:
        self.cycles += 1
