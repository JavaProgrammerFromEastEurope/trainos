from dataclasses import dataclass

from kernel.healthcare.treatments.treatment_status import TreatmentStatus


@dataclass(frozen=True, slots=True)
class TreatmentSnapshot:

    treatment_id: str
    status: TreatmentStatus