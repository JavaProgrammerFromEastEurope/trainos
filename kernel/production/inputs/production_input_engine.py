from .production_input_result import ProductionInputResult
from .production_input_check import ProductionInputCheck


class ProductionInputEngine:

    def validate(
        self, checks: tuple[ProductionInputCheck, ...]
    ) -> ProductionInputResult:
        missing = []
        for check in checks:
            if check.available_quantity < check.required_quantity:
                missing.append(check.resource_id)
        return ProductionInputResult(
            approved=len(missing) == 0,
            missing_resources=tuple(missing),
        )
