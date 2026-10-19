from dataclasses import dataclass


@dataclass(frozen=True)
class GroupPolicy:

    allow_multiple_membership: 	bool
    immutable_group_ids: 				bool