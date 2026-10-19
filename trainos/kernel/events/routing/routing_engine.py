from .router import Router


class RoutingEngine:

    def __init__(self):
        self.router = Router()

    def route(
        self,
        subscribers,
        event,
    ):
        return [
            subscriber
            for subscriber in subscribers
            if self.router.matches(subscriber, event)
        ]
