class EconomyMetrics:

    def __init__(self) -> None:
        self.total_trades = 0

    def increment(self) -> None:
        self.total_trades += 1
