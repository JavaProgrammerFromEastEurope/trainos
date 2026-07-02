from dataclasses import dataclass


@dataclass(frozen=True)
class RegistryPolicy:

    allow_duplicate_roles: 	bool
    require_active_flag: 		bool