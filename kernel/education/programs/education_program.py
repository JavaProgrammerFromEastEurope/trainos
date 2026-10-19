from dataclasses import dataclass

from .education_program_status import EducationProgramStatus
from .education_program_type import EducationProgramType


@dataclass(frozen=True, slots=True)
class EducationProgram:

    program_id: str
    student_id: str
    name: 			str
    program_type: EducationProgramType
    status: EducationProgramStatus