from .tradition import Tradition
from .tradition_type import TraditionType


class TraditionEngine:

    def create(self) -> Tradition:
        return Tradition(
            type=TraditionType.FOOD_RESERVE,
        )
