from .consumption_request import ConsumptionRequest
from .consumption_result 	import ConsumptionResult


class ConsumptionEngine:

    def consume(
        self,
        request: ConsumptionRequest,
    ) -> ConsumptionResult:
        return ConsumptionResult(
            consumption_id=request.request_id,
            consumed_quantity=request.quantity,
            approved=True,
        )
