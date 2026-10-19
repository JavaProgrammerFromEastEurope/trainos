from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RoutePolicy:

    allow_loop_routes: bool 		= False
    require_active_route: bool 	= True