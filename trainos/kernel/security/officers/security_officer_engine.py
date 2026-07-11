from .security_officer import SecurityOfficer
from .security_officer_status import SecurityOfficerStatus


class SecurityOfficerEngine:

    def dispatch(
        self,
        officer: SecurityOfficer,
    ) -> SecurityOfficer:
        return SecurityOfficer(
            officer_id=officer.officer_id,
            resident_id=officer.resident_id,
            status=SecurityOfficerStatus.RESPONDING,
        )

    def return_to_duty(
        self,
        officer: SecurityOfficer,
    ) -> SecurityOfficer:
        return SecurityOfficer(
            officer_id=officer.officer_id,
            resident_id=officer.resident_id,
            status=SecurityOfficerStatus.ON_DUTY,
        )
