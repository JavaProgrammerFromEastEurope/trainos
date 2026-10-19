from kernel.core.registry.base_registry import BaseRegistry

from .persistence_contract import PersistenceContract


class PersistenceRegistry(
    BaseRegistry[PersistenceContract],
):
    pass
