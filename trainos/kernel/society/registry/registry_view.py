from dataclasses import dataclass


@dataclass(frozen=True)
class RegistryView:

    total_citizens: 	int
    active_citizens: 	int