from .optimization_plan import OptimizationPlan


class OptimizationEngine:

    def optimize(self) -> OptimizationPlan:
        return OptimizationPlan(
            description="rebalance hydroponics output",
        )
