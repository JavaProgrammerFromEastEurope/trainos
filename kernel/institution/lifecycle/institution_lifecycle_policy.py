from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionLifecyclePolicy:

    allow_suspend: 	bool
    allow_merge: 		bool
    allow_dissolve: bool