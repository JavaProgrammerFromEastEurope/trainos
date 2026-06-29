from dataclasses import dataclass

from .strategy_state import StrategyState


@dataclass(frozen=True)
class AdaptiveStrategy:

    name: 				str
    description: 	str
    state: StrategyState