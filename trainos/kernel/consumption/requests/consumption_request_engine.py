from .consumption_request 				import ConsumptionRequest
from .consumption_request_status 	import ConsumptionRequestStatus


class ConsumptionRequestEngine:

    def approve(
        self,
        request: ConsumptionRequest,
    ) -> ConsumptionRequest:
        return ConsumptionRequest(
            request_id=request.request_id,
            consumer_id=request.consumer_id,
            resource_id=request.resource_id,
            quantity=request.quantity,
            priority=request.priority,
            status=ConsumptionRequestStatus.APPROVED,
        )

    def reject(
        self,
        request: ConsumptionRequest,
    ) -> ConsumptionRequest:
        return ConsumptionRequest(
            request_id=request.request_id,
            consumer_id=request.consumer_id,
            resource_id=request.resource_id,
            quantity=request.quantity,
            priority=request.priority,
            status=ConsumptionRequestStatus.REJECTED,
        )