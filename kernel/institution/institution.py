from dataclasses import dataclass

from .institution_type import InstitutionType


@dataclass(frozen=True)
class Institution:

    institution_id: str
    name: str
    institution_type: InstitutionType