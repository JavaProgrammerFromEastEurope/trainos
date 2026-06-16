class UtilityMetrics:

    def __init__(
        self,
    ) -> None:
        self.evaluations = 0

    def increment(
        self,
    ) -> None:
        self.evaluations += 1
