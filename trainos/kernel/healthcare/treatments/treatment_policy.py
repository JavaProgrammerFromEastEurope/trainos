from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TreatmentPolicy:

    allow_completion: bool 		= True
    allow_cancellation: bool 	= True