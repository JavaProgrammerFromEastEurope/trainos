from dataclasses import dataclass


@dataclass(frozen=True)
class EconomyPolicy:

    allow_runtime_restart: 	bool
    immutable_history: 			bool