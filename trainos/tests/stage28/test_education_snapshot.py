from kernel.education.facilities.education_facility_status import (
    EducationFacilityStatus,
)
from kernel.education.programs.education_program_status import EducationProgramStatus
from kernel.education.runtime.education_lifecycle import EducationLifecycle
from kernel.education.skills.skill_level import SkillLevel
from kernel.education.snapshot.education_facility_snapshot import (
    EducationFacilitySnapshot,
)
from kernel.education.snapshot.education_program_snapshot import (
    EducationProgramSnapshot,
)
from kernel.education.snapshot.education_runtime_snapshot import (
    EducationRuntimeSnapshot,
)
from kernel.education.snapshot.education_snapshot import EducationSnapshot
from kernel.education.snapshot.education_snapshot_engine import (
    EducationSnapshotEngine,
)
from kernel.education.snapshot.skill_snapshot import SkillSnapshot
from kernel.education.snapshot.student_snapshot import StudentSnapshot
from kernel.education.students.student_status import StudentStatus


def test_education_snapshot():

    engine = EducationSnapshotEngine()

    snapshot = EducationSnapshot(
        snapshot_id="SNAP1",
        runtime=EducationRuntimeSnapshot(
            lifecycle=EducationLifecycle.RUNNING,
        ),
        students=(
            StudentSnapshot(
                student_id="S1",
                status=StudentStatus.STUDYING,
            ),
        ),
        skills=(
            SkillSnapshot(
                skill_id="SK1",
                level=SkillLevel.INTERMEDIATE,
            ),
        ),
        programs=(
            EducationProgramSnapshot(
                program_id="P1",
                status=EducationProgramStatus.ACTIVE,
            ),
        ),
        facilities=(
            EducationFacilitySnapshot(
                facility_id="F1",
                status=EducationFacilityStatus.OPERATIONAL,
            ),
        ),
    )
    result = engine.capture(snapshot)
    assert result is snapshot
