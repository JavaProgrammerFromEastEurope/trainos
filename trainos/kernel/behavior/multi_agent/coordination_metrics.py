class CoordinationMetrics:

    def __init__(
        self,
    ) -> None:
        self.assignments = 0

    def increment(
        self,
    ) -> None:
        self.assignments += 1
