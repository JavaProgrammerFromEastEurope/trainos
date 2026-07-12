from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RoutingSnapshot:
    routes: int
