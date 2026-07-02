from kernel.society.groups.civil_group import CivilGroup
from kernel.society.groups.group_membership import GroupMembership
from kernel.society.groups.group_registry import GroupRegistry


def test_register_group_membership():

    registry = GroupRegistry()

    group = CivilGroup(
        group_id="MED-01",
        name="Medical Team",
    )

    registry.register_group(group)

    membership = GroupMembership(
        entity_id="A-104",
        group_id="MED-01",
    )

    registry.register_membership(membership)

    assert registry.group("MED-01") == group
    assert membership in registry.memberships()
