from dataclasses import dataclass

from ..runtime.production_lifecycle import ProductionLifecycle


@dataclass(frozen=True, slots=True)
class ProductionRuntimeSnapshot:

    lifecycle: ProductionLifecycle