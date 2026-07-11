from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PatientPolicy:

    allow_treatment: bool = True
    allow_discharge: bool = True