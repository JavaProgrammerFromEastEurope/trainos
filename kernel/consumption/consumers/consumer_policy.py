from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumerPolicy:

    allow_consumption: 			bool = True
    allow_emergency_supply: bool = True