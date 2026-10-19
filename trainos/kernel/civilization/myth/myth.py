from dataclasses import dataclass

from .myth_type import MythType


@dataclass
class Myth:

    type: MythType
