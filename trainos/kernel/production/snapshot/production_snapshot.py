from dataclasses import dataclass

from .production_factory_snapshot import ProductionFactorySnapshot
from .production_job_snapshot import ProductionJobSnapshot
from .production_runtime_snapshot import ProductionRuntimeSnapshot


@dataclass(frozen=True, slots=True)
class ProductionSnapshot:

    snapshot_id: str
    runtime: 		ProductionRuntimeSnapshot
    factories: 	tuple[ProductionFactorySnapshot, ...]
    jobs: 			tuple[ProductionJobSnapshot, ...]