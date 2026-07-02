from dataclasses import dataclass


@dataclass(frozen=True)
class AmendmentPolicy:

    require_target: 			bool
    require_description: 	bool