from dataclasses import dataclass

from .production_configuration import ProductionConfiguration


@dataclass(slots=True)
class ProductionContext:

    configuration: ProductionConfiguration