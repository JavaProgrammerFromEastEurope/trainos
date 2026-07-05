from decimal import Decimal

from kernel.resources.allocation.allocation_engine import AllocationEngine
from kernel.resources.allocation.allocation_request import AllocationRequest


def test_allocation_engine():

    engine = AllocationEngine()

    request = AllocationRequest(
        request_id="A1",
        resource_id="water",
        receiver_id="citizen-1",
        quantity=Decimal("20"),
    )

    result = engine.allocate(request)

    assert result.approved is True
    assert result.approved_quantity == Decimal("20")
