from dataclasses import dataclass


@dataclass(frozen=True)
class HierarchyPolicy:

    enforce_priority: bool