from dataclasses import dataclass

from .hierarchy_level import HierarchyLevel


@dataclass(frozen=True)
class ConstitutionalHierarchy:

    rule_name: str
    level: HierarchyLevel