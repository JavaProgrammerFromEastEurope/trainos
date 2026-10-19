from dataclasses import dataclass

from .destiny_type import DestinyType


@dataclass
class Destiny:

    type: DestinyType