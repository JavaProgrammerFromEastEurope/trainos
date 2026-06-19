class LearningMetrics:

    def __init__(self) -> None:
        self.samples = 0

    def increment(self) -> None:
        self.samples += 1