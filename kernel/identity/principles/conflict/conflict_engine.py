from .conflict_resolution import (
    PrincipleConflictResolution,
)
from .principle_conflict import PrincipleConflict


class PrincipleConflictEngine:

    def resolve(
        self,
        conflict: PrincipleConflict,
    ) -> PrincipleConflictResolution:
        return PrincipleConflictResolution(winner=conflict.left)
