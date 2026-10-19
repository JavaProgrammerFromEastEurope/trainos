from dataclasses import dataclass

from .education_configuration import EducationConfiguration


@dataclass(slots=True)
class EducationContext:

    configuration: EducationConfiguration