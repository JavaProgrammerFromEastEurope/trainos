from decimal import Decimal

from kernel.resources.consumption.consumption_engine import ConsumptionEngine
from kernel.resources.consumption.consumption_request import ConsumptionRequest


def test_consumption_engine():

    engine = ConsumptionEngine()

    request = ConsumptionRequest(
        request_id="C1",
        resource_id="water",
        consumer_id="citizen-1",
        quantity=Decimal("2"),
    )

    result = engine.consume(request)

    assert result.approved is True
    assert result.consumed_quantity == Decimal("2")