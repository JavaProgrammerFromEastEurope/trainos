from dataclasses import dataclass

from .education_category import EducationCategory
from .education_type import EducationType


@dataclass(frozen=True, slots=True)
class EducationDefinition:

    education_id: str
    name: 				str
    education_type: EducationType
    category: EducationCategory