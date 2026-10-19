from dataclasses import dataclass

from .economy_state import EconomyState


@dataclass
class EconomyContext:

    state: EconomyState = EconomyState.CREATED