class TaskMetrics:

    def __init__(
        self,
    ) -> None:
        self.executed = 0

    def increment(
        self,
    ) -> None:
        self.executed += 1
