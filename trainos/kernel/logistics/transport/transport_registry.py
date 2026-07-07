from kernel.core.registry.base_registry import BaseRegistry

from .transport_unit import TransportUnit


class TransportRegistry(
    BaseRegistry[TransportUnit],
):
    pass
