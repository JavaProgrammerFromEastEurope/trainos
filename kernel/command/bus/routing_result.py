from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RoutingResult:

    success: bool
    handler_id: str
