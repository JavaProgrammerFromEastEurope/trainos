from kernel.integration.routing.integration_route import (
    IntegrationRoute,
)

from kernel.integration.routing.route_target import (
    RouteTarget,
)

from kernel.integration.routing.routing_engine import (
    RoutingEngine,
)


def test_routing():

    routes = [
        IntegrationRoute(
            route_id="R1",
            event_name="ResidentCreated",
            target=RouteTarget.HEALTHCARE,
        ),
        IntegrationRoute(
            route_id="R2",
            event_name="ResidentCreated",
            target=RouteTarget.SECURITY,
        ),
    ]

    result = RoutingEngine().route(
        "ResidentCreated",
        routes,
    )

    assert len(result) == 2