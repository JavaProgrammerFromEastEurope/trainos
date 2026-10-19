from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EducationProgramPolicy:

    allow_completion: bool 		= True
    allow_cancellation: bool 	= True