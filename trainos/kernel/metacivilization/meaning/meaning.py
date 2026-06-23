from dataclasses import dataclass

from .meaning_type import MeaningType


@dataclass
class Meaning:

    type: MeaningType