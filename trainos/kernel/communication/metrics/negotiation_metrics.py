class NegotiationMetrics:

    def __init__(self) -> None:
        self.total_negotiations = 0

    def increment(self) -> None:
        self.total_negotiations += 1
