class EpisodeMetrics:

    def __init__(
        self,
    ) -> None:
        self.completed = 0

    def increment(
        self,
    ) -> None:
        self.completed += 1
