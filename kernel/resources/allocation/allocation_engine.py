from decimal import Decimal

from .allocation_policy 	import AllocationPolicy
from .allocation_request 	import AllocationRequest
from .allocation_result 	import AllocationResult


class AllocationEngine:

    def __init__(
        self,
        policy: AllocationPolicy | None = None,
    ) -> None:
        self._policy = policy or AllocationPolicy(
            allow_partial_allocation=False,
            require_available_inventory=True,
        )

    def allocate(
        self,
        request: AllocationRequest,
    ) -> AllocationResult:
        return AllocationResult(
            allocation_id=request.request_id,
            resource_id=request.resource_id,
            receiver_id=request.receiver_id,
            approved_quantity=request.quantity,
            approved=True,
        )
