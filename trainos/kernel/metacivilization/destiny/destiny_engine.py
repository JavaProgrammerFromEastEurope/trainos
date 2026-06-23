from .destiny import Destiny
from .destiny_type import DestinyType


class DestinyEngine:

    def determine(self) -> Destiny:
        return Destiny(type=DestinyType.HARMONY)
