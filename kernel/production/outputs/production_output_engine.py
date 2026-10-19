from .production_output import ProductionOutput
from .production_output_result import ProductionOutputResult


class ProductionOutputEngine:

    def produce(
        self,
        outputs: tuple[ProductionOutput, ...],
    ) -> ProductionOutputResult:
        return ProductionOutputResult(
            completed=True,
            outputs=outputs,
        )
