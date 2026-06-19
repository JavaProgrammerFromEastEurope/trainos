class PolicyMetrics:

    def __init__(
        self,
    ) -> None:
        self.total_versions = 0

    def increment(
        self,
    ) -> None:
        self.total_versions += 1
