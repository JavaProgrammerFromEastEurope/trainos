from .constraint import Constraint


class ConstraintEngine:

    def validate(
        self,
        constraint: Constraint,
    ) -> bool:
        return constraint.immutable
