from decimal import Decimal

from .resource_inventory import ResourceInventory
from .inventory_transaction import InventoryTransaction
from .inventory_policy import InventoryPolicy


class ResourceInventoryEngine:

    def __init__(self, policy: InventoryPolicy | None = None) -> None:
        self._policy = policy or InventoryPolicy(
            allow_negative_stock=False, strict_validation=True
        )

    def apply(
        self, inventory: ResourceInventory, tx: InventoryTransaction
    ) -> ResourceInventory:
        if inventory.resource_id != tx.resource_id:
            raise ValueError("Resource mismatch")
        new_quantity = inventory.quantity + tx.delta
        if not self._policy.allow_negative_stock and new_quantity < Decimal("0"):
            raise ValueError("Negative stock not allowed")
        return ResourceInventory(
            resource_id=inventory.resource_id, quantity=new_quantity
        )
