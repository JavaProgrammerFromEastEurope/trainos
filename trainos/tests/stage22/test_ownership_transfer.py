from kernel.resources.ownership.ownership_engine import OwnershipEngine
from kernel.resources.ownership.ownership_type import OwnershipType
from kernel.resources.ownership.resource_ownership import ResourceOwnership


def test_ownership_transfer():

    engine = OwnershipEngine()

    ownership = ResourceOwnership(
        ownership_id="OWN1",
        resource_id="water",
        owner_id="government",
        owner_type=OwnershipType.GOVERNMENT,
        quantity=100,
    )

    transferred = engine.transfer(
        ownership,
        "citizen-1",
    )

    assert transferred.owner_id == "citizen-1"