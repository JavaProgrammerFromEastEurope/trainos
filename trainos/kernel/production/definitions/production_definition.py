from dataclasses import dataclass

from .production_type import ProductionType
from .production_category import ProductionCategory


@dataclass(frozen=True, slots=True)
class ProductionDefinition:

    production_id: str
    name: str
    production_type: ProductionType
    category: ProductionCategory