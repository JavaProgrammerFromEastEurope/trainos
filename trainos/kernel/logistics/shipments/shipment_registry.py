from kernel.core.registry.base_registry import BaseRegistry

from .shipment import Shipment


class ShipmentRegistry(
    BaseRegistry[Shipment],
):
    pass
