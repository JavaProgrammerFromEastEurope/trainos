from decimal import Decimal

from kernel.resources.reservation.reservation_engine import ReservationEngine
from kernel.resources.reservation.reservation_request import ReservationRequest


def test_reservation_engine():

    engine = ReservationEngine()

    request = ReservationRequest(
        request_id="R1",
        resource_id="water",
        requester_id="citizen-1",
        quantity=Decimal("10"),
    )

    result = engine.reserve(request)

    assert result.approved is True
    assert result.reserved_quantity == Decimal("10")