class SelfPlayMetrics:

    def __init__(
        self,
    ) -> None:
        self.total_matches = 0

    def increment(
        self,
    ) -> None:
        self.total_matches += 1