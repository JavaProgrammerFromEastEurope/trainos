from decimal import Decimal

from kernel.consumption.requests.consumption_request import ConsumptionRequest
from kernel.consumption.requests.consumption_request_engine import ConsumptionRequestEngine
from kernel.consumption.requests.consumption_request_priority import ConsumptionRequestPriority
from kernel.consumption.requests.consumption_request_status import ConsumptionRequestStatus


def test_consumption_request_engine():

    engine = ConsumptionRequestEngine()

    request = ConsumptionRequest(
        request_id="REQ1",
        consumer_id="C1",
        resource_id="water",
        quantity=Decimal("100"),
        priority=ConsumptionRequestPriority.HIGH,
        status=ConsumptionRequestStatus.CREATED,
    )

    approved = engine.approve(request)
    assert approved.status == ConsumptionRequestStatus.APPROVED

    rejected = engine.reject(request)
    assert rejected.status == ConsumptionRequestStatus.REJECTED