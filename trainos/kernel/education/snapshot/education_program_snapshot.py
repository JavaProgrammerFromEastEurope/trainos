from dataclasses import dataclass

from kernel.education.programs.education_program_status import (
    EducationProgramStatus,
)


@dataclass(frozen=True, slots=True)
class EducationProgramSnapshot:

    program_id: str
    status: EducationProgramStatus