from .transfer_request import TransferRequest
from .transfer_result import TransferResult
from .transfer_status import TransferStatus


class TransferEngine:

    def transfer(
        self,
        request: TransferRequest,
    ) -> TransferResult:
        return TransferResult(
            transfer_id=request.request_id,
            transferred_quantity=request.quantity,
            status=TransferStatus.COMPLETED,
        )
