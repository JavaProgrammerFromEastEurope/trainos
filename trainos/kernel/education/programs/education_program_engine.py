from .education_program import EducationProgram
from .education_program_status import EducationProgramStatus


class EducationProgramEngine:

    def start(
        self,
        program: EducationProgram,
    ) -> EducationProgram:
        return EducationProgram(
            program_id=program.program_id,
            student_id=program.student_id,
            name=program.name,
            program_type=program.program_type,
            status=EducationProgramStatus.ACTIVE,
        )

    def complete(
        self,
        program: EducationProgram,
    ) -> EducationProgram:
        return EducationProgram(
            program_id=program.program_id,
            student_id=program.student_id,
            name=program.name,
            program_type=program.program_type,
            status=EducationProgramStatus.COMPLETED,
        )
