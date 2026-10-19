from kernel.education.programs.education_program import EducationProgram
from kernel.education.programs.education_program_engine import EducationProgramEngine
from kernel.education.programs.education_program_status import EducationProgramStatus
from kernel.education.programs.education_program_type import EducationProgramType


def test_education_program_engine():

    engine = EducationProgramEngine()
    program = EducationProgram(
        program_id="P1",
        student_id="S1",
        name="Engineering Program",
        program_type=EducationProgramType.TECHNICAL,
        status=EducationProgramStatus.PLANNED,
    )

    active = engine.start(program)
    assert active.status == EducationProgramStatus.ACTIVE

    completed = engine.complete(active)
    assert completed.status == EducationProgramStatus.COMPLETED