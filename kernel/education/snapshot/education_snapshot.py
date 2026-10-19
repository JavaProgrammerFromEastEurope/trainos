from dataclasses import dataclass

from .education_facility_snapshot import EducationFacilitySnapshot
from .education_program_snapshot import EducationProgramSnapshot
from .education_runtime_snapshot import EducationRuntimeSnapshot
from .skill_snapshot import SkillSnapshot
from .student_snapshot import StudentSnapshot


@dataclass(frozen=True, slots=True)
class EducationSnapshot:

    snapshot_id: str
    runtime: 		EducationRuntimeSnapshot
    students: 	tuple[StudentSnapshot, ...]
    skills: 		tuple[SkillSnapshot, ...]
    programs: 	tuple[EducationProgramSnapshot, ...]
    facilities: tuple[EducationFacilitySnapshot, ...]