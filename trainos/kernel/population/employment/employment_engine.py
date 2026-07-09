from .employment import Employment
from .employment_status import EmploymentStatus


class EmploymentEngine:

    def activate(
        self,
        employment: Employment,
    ) -> Employment:
        return Employment(
            employment_id=employment.employment_id,
            resident_id=employment.resident_id,
            profession_id=employment.profession_id,
            organization_id=employment.organization_id,
            employment_type=employment.employment_type,
            status=EmploymentStatus.ACTIVE,
        )

    def terminate(
        self,
        employment: Employment,
    ) -> Employment:
        return Employment(
            employment_id=employment.employment_id,
            resident_id=employment.resident_id,
            profession_id=employment.profession_id,
            organization_id=employment.organization_id,
            employment_type=employment.employment_type,
            status=EmploymentStatus.TERMINATED,
        )