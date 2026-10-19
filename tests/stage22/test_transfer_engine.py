from decimal import Decimal

from kernel.resources.transfer.transfer_engine import TransferEngine
from kernel.resources.transfer.transfer_request import TransferRequest
from kernel.resources.transfer.transfer_status import TransferStatus


def test_transfer_engine():

    engine = TransferEngine()

    request = TransferRequest(
        request_id="T1",
        resource_id="water",
        source_owner_id="government",
        destination_owner_id="citizen-1",
        quantity=Decimal("15"),
    )

    result = engine.transfer(request)

    assert result.status == TransferStatus.COMPLETED
    assert result.transferred_quantity == Decimal("15")