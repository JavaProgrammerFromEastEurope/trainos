from kernel.logistics.routes.route import Route
from kernel.logistics.routes.route_engine import RouteEngine
from kernel.logistics.routes.route_node import RouteNode
from kernel.logistics.routes.route_status import RouteStatus


def test_route_engine():

    engine = RouteEngine()
    route = Route(
        route_id="R1",
        name="North Route",
        status=RouteStatus.AVAILABLE,
        nodes=(
            RouteNode(
                node_id="1",
                warehouse_id="WH1",
                order=1,
            ),
            RouteNode(
                node_id="2",
                warehouse_id="WH2",
                order=2,
            ),
        ),
    )
    result = engine.validate(route)
    assert result is route
