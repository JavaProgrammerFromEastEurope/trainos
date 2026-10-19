from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EmploymentPolicy:

    allow_assignment: 	bool = True
    require_profession: bool = True