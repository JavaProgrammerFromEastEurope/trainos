from dataclasses import dataclass


@dataclass(frozen=True)
class HierarchyRelation:

    parent_id: 	str
    child_id: 	str