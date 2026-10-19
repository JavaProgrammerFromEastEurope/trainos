class MemoryMetrics:

    def __init__(self) -> None:
        self.total_writes = 0

    def increment(self) -> None:
        self.total_writes += 1
