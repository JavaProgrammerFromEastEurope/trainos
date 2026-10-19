from .reservation_request import ReservationRequest
from .reservation_result 	import ReservationResult


class ReservationEngine:

    def reserve(
        self,
        request: ReservationRequest,
    ) -> ReservationResult:
        return ReservationResult(
            reservation_id=request.request_id,
            approved=True,
            reserved_quantity=request.quantity,
        )
