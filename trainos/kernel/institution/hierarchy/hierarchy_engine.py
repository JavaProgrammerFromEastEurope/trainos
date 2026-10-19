from .institutional_hierarchy import InstitutionalHierarchy


class HierarchyEngine:

    def build(
        self,
        hierarchy: InstitutionalHierarchy,
    ) -> InstitutionalHierarchy:
        return hierarchy