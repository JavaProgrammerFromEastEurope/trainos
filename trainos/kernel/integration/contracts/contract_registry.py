from kernel.core.registry.base_registry import BaseRegistry

from .integration_contract import IntegrationContract


class ContractRegistry(
    BaseRegistry[IntegrationContract],
):
    pass
