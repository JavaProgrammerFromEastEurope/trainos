from .treatment 				import Treatment
from .treatment_status 	import TreatmentStatus


class TreatmentEngine:

    def start(
        self,
        treatment: Treatment,
    ) -> Treatment:
        return Treatment(
            treatment_id=treatment.treatment_id,
            condition_id=treatment.condition_id,
            name=treatment.name,
            treatment_type=treatment.treatment_type,
            status=TreatmentStatus.ACTIVE,
        )

    def complete(
        self,
        treatment: Treatment,
    ) -> Treatment:
        return Treatment(
            treatment_id=treatment.treatment_id,
            condition_id=treatment.condition_id,
            name=treatment.name,
            treatment_type=treatment.treatment_type,
            status=TreatmentStatus.COMPLETED,
        )
