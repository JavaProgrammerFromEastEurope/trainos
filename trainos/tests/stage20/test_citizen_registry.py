from kernel.society.identity.identity_role 		import IdentityRole
from kernel.society.registry.citizen_record 	import CitizenRecord
from kernel.society.registry.citizen_registry import CitizenRegistry


def test_register_citizen():

    registry = CitizenRegistry()

    citizen = CitizenRecord(
        entity_id="A-104",
        role=IdentityRole.CITIZEN,
        active=True,
    )

    registry.register_citizen(citizen)
    stored = registry.get("A-104")

    assert stored == citizen
