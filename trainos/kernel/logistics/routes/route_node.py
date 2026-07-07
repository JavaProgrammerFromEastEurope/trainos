from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RouteNode:

    node_id: 			str
    warehouse_id: str
    order: 				int