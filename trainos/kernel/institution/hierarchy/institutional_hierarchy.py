from dataclasses import dataclass

from .hierarchy_relation import HierarchyRelation


@dataclass(frozen=True)
class InstitutionalHierarchy:

    relations: tuple[HierarchyRelation, ...]
