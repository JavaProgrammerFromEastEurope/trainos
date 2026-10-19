from .myth import Myth
from .myth_type import MythType


class MythEngine:

    def create(self) -> Myth:
        return Myth(type=MythType.SURVIVAL)
