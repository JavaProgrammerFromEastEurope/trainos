from dataclasses import dataclass


@dataclass(frozen=True)
class HierarchyPolicy:

    prevent_cycles: bool
    single_parent: 	bool