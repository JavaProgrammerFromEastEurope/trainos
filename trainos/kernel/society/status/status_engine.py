from .civil_status import CivilStatus


class StatusEngine:

    def evaluate(
        self,
        status: CivilStatus,
    ) -> CivilStatus:
        return status
