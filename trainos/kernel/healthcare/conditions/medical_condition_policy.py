from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MedicalConditionPolicy:

    allow_treatment: bool 	= True
    allow_monitoring: bool 	= True