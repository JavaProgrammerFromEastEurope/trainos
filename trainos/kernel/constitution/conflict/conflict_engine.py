from .constitutional_conflict import ConstitutionalConflict
from .conflict_resolution import ConstitutionalConflictResolution


class ConstitutionalConflictEngine:

    def resolve(
        self,
        conflict: ConstitutionalConflict,
    ) -> ConstitutionalConflictResolution:
        return ConstitutionalConflictResolution(
            winning_article=conflict.left_article,
            explanation="Priority hierarchy applied.",
        )
