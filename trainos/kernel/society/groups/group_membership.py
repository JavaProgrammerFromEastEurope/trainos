from dataclasses import dataclass


@dataclass(frozen=True)
class GroupMembership:

    entity_id: 	str
    group_id: 	str