from dataclasses import dataclass


@dataclass(frozen=True)
class LifecyclePolicy:

    allow_reactivation: bool
    allow_state_skip: 	bool