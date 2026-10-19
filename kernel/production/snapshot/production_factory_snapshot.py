from dataclasses import dataclass

from ..factories.factory_status import FactoryStatus


@dataclass(frozen=True, slots=True)
class ProductionFactorySnapshot:

    factory_id: str
    status: FactoryStatus