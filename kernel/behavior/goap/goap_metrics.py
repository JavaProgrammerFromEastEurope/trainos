class GOAPMetrics:

    def __init__(
        self,
    ) -> None:
        self.generated = 0

    def increment(
        self,
    ) -> None:
        self.generated += 1
