from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ResidentPolicy:

    allow_employment: 	bool = True
    allow_consumption: 	bool = True
    allow_relocation: 	bool = True