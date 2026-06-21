class RoutingMetrics:

    def __init__(self) -> None:
        self.total_routes = 0

    def increment(self) -> None:
        self.total_routes += 1
