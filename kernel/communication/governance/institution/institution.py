from dataclasses import dataclass

from .institution_type import InstitutionType


@dataclass
class Institution:
    type: InstitutionType
