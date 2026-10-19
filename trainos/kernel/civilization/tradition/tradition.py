from dataclasses import dataclass

from .tradition_type import TraditionType


@dataclass
class Tradition:

    type: TraditionType