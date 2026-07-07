from kernel.core.registry.base_registry import BaseRegistry

from .delivery_job import DeliveryJob


class DeliveryJobRegistry(
    BaseRegistry[DeliveryJob],
):
    pass