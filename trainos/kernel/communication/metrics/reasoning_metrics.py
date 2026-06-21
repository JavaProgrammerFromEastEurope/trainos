class ReasoningMetrics:

    def __init__(self) -> None:
        self.total_decisions = 0

    def increment(self) -> None:
        self.total_decisions += 1
