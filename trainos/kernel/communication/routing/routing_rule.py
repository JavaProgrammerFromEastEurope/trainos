from dataclasses import dataclass


@dataclass
class RoutingRule:

    source: str
    destination: str
