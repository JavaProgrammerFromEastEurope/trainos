from trainos.kernel.communication.resource_ecology.logistics.logistic_engine import (
    LogisticsEngine,
)
from trainos.kernel.communication.resource_ecology.logistics.transfer_route import (
    TransferRoute,
)


def test_logistics_engine_plan_route():
    engine = LogisticsEngine()
    route = engine.plan_route()
    expected = TransferRoute(path=["A", "B", "C"])

    assert route == expected
