from dataclasses import dataclass

from .law_type import LawType


@dataclass
class Law:
    type: LawType
