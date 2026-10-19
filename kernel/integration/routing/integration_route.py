from dataclasses import dataclass

from .route_target import RouteTarget


@dataclass(frozen=True, slots=True)
class IntegrationRoute:

    route_id: 	str
    event_name: str
    target: RouteTarget