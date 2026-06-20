class MetaMetrics:

    def __init__(
        self,
    ) -> None:
        self.total_updates = 0

    def increment(
        self,
    ) -> None:
        self.total_updates += 1
