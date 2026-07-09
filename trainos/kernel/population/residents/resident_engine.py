from .resident import Resident
from .resident_status import ResidentStatus


class ResidentEngine:

    def activate(
        self,
        resident: Resident,
    ) -> Resident:
        return Resident(
            resident_id=resident.resident_id,
            name=resident.name,
            resident_type=resident.resident_type,
            status=ResidentStatus.ACTIVE,
        )

    def retire(
        self,
        resident: Resident,
    ) -> Resident:
        return Resident(
            resident_id=resident.resident_id,
            name=resident.name,
            resident_type=resident.resident_type,
            status=ResidentStatus.RETIRED,
        )
