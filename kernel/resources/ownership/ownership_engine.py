from .resource_ownership import ResourceOwnership
from .ownership_policy import OwnershipPolicy


class OwnershipEngine:

    def __init__(
        self,
        policy: OwnershipPolicy | None = None,
    ) -> None:
        self._policy = policy or OwnershipPolicy(
            allow_transfer=True, enforce_exclusive_ownership=True
        )

    def transfer(
        self,
        ownership: ResourceOwnership,
        new_owner_id: str,
    ) -> ResourceOwnership:
        if not self._policy.allow_transfer:
            raise ValueError("Transfer not allowed")
        return ResourceOwnership(
            ownership_id=ownership.ownership_id,
            resource_id=ownership.resource_id,
            owner_id=new_owner_id,
            owner_type=ownership.owner_type,
            quantity=ownership.quantity,
        )
