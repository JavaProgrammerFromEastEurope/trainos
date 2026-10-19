from kernel.core.registry.base_registry import BaseRegistry

from kernel.persistence.engine.persistence_engine import PersistenceEngine


class PersistenceEngineRegistry(
    BaseRegistry[PersistenceEngine],
):
    pass
