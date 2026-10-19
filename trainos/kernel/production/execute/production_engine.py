from .production_context import ProductionContext
from .production_executor import ProductionExecutor
from .production_pipeline import ProductionPipeline
from .production_policy import ProductionPolicy


class ProductionEngine:

    def __init__(
        self,
        policy: ProductionPolicy | None = None,
    ) -> None:
        self._policy = policy or ProductionPolicy()
        self._executor = ProductionExecutor()
        self._pipeline = ProductionPipeline()

    def run(self, context: ProductionContext) -> None:
        self._pipeline.run(context)
        self._executor.execute(context)