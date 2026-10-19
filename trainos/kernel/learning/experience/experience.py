from dataclasses import dataclass


@dataclass
class Experience:

    state: dict
    action: str
    reward: float
    next_state: dict
