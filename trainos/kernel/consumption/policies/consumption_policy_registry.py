from kernel.core.registry.base_registry import BaseRegistry

from .consumption_policy import ConsumptionPolicy


class ConsumptionPolicyRegistry(
    BaseRegistry[ConsumptionPolicy],
):
    pass
