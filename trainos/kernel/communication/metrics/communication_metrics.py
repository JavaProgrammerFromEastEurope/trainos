class CommunicationMetrics:

    def __init__(self) -> None:
        self.total_messages = 0

    def increment(self) -> None:
        self.total_messages += 1
