class ImprovementMetrics:

    def __init__(
        self,
    ) -> None:
        self.total_targets = 0

    def increment(
        self,
    ) -> None:
        self.total_targets += 1
