class ResourceMetrics:

    def __init__(self) -> None:
        self.total_transfers = 0

    def increment(self) -> None:
        self.total_transfers += 1
