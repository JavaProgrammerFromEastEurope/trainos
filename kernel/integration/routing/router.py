from .integration_route import IntegrationRoute


class Router:

    def resolve(
        self,
        event_name: str,
        routes: list[IntegrationRoute],
    ) -> list[IntegrationRoute]:
        return [route for route in routes if route.event_name == event_name]
