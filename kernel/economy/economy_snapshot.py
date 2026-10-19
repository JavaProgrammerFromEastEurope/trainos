from dataclasses import dataclass

from .economy_state import EconomyState


@dataclass(frozen=True)
class EconomySnapshot:

    state: EconomyState
    registered_services: int