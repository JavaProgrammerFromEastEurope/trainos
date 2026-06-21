from .adaptation_plan import AdaptationPlan


class AdaptationEngine:

    def adapt(self) -> AdaptationPlan:
        return AdaptationPlan(
            description="increase hydroponics capacity",
        )
