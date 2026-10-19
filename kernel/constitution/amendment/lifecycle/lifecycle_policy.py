from dataclasses import dataclass


@dataclass(frozen=True)
class LifecyclePolicy:

    allow_backward_transition: 	bool
    require_terminal_state: 		bool