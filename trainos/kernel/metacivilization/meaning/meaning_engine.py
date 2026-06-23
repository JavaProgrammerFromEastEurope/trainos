from .meaning import Meaning
from .meaning_type import MeaningType


class MeaningEngine:

    def determine(self) -> Meaning:
        return Meaning(type=MeaningType.CONTINUITY)
