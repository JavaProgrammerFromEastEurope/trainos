from kernel.core.registry.base_registry import BaseRegistry

from .reservation import Reservation


class ReservationRegistry(
    BaseRegistry[Reservation],
):
    pass
