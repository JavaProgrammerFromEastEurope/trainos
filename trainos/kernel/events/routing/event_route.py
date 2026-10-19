from dataclasses import dataclass

from .routing_policy import RoutingPolicy


@dataclass(frozen=True, slots=True)
class EventRoute:

    route_id: str
    policy: RoutingPolicy