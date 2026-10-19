from dataclasses import dataclass

from .route_node import RouteNode
from .route_status import RouteStatus


@dataclass(frozen=True, slots=True)
class Route:

    route_id: str
    name: 		str
    nodes: 		tuple[RouteNode, ...]
    status: RouteStatus