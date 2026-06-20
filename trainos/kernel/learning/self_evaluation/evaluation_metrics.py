class EvaluationMetrics:

    def __init__(
        self,
    ) -> None:
        self.total_evaluations = 0

    def increment(
        self,
    ) -> None:
        self.total_evaluations += 1
