from .improvement_target import ImprovementTarget


class AdaptationEngine:

    def adapt(self) -> ImprovementTarget:
        return ImprovementTarget(name="navigation")
