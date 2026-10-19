from .router import Router


class RoutingEngine:

    def __init__(self):
        self.router = Router()

    def route(
        self,
        event_name: str,
        routes,
    ):
        return self.router.resolve(event_name, routes)
