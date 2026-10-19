from dataclasses import dataclass

from .production_output import ProductionOutput


@dataclass(frozen=True, slots=True)
class ProductionOutputResult:

    completed: bool
    outputs: tuple[ProductionOutput, ...]