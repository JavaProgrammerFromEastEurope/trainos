class LifelongMetrics:

    def __init__(self) -> None:
        self.total_sessions = 0

    def increment(self) -> None:
        self.total_sessions += 1
