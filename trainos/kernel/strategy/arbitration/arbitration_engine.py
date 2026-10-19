from .arbitration_result import ArbitrationResult
from .goal_conflict import GoalConflict


class ArbitrationEngine:

    def resolve(self, conflict: GoalConflict) -> ArbitrationResult:
        if conflict.left.priority.value >= conflict.right.priority.value:
            return ArbitrationResult(selected=conflict.left)
        return ArbitrationResult(selected=conflict.right)
