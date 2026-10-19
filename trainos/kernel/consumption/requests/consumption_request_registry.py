from kernel.core.registry.base_registry import BaseRegistry

from .consumption_request import ConsumptionRequest


class ConsumptionRequestRegistry(
    BaseRegistry[ConsumptionRequest],
):
    pass
