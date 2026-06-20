from .improvement_target import (
    ImprovementTarget,
)


class ImprovementEngine:

    def target(
        self,
    ) -> ImprovementTarget:

        return ImprovementTarget(
            name="navigation",
        )