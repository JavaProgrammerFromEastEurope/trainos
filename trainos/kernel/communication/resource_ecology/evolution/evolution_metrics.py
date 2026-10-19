class EvolutionMetrics:

    def __init__(self) -> None:
        self.total_adaptations = 0

    def increment(self) -> None:
        self.total_adaptations += 1
