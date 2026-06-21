class SocialMemoryMetrics:

    def __init__(self) -> None:
        self.total_events = 0

    def increment(self) -> None:
        self.total_events += 1
