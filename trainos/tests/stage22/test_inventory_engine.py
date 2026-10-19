from decimal import Decimal

from kernel.resources.inventory.inventory_transaction import InventoryTransaction
from kernel.resources.inventory.resource_inventory import ResourceInventory
from kernel.resources.inventory.resource_inventory_engine import ResourceInventoryEngine


def test_inventory_engine():

    engine = ResourceInventoryEngine()

    inventory = ResourceInventory(
        resource_id="water",
        quantity=Decimal("100"),
    )

    tx = InventoryTransaction(
        transaction_id="TX1",
        resource_id="water",
        delta=Decimal("25"),
        reason="production",
    )

    result = engine.apply(inventory, tx)

    assert result.quantity == Decimal("125")
