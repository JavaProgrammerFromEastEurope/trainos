from .reinforcement_state import ReinforcementState


class ReinforcementRuntime:

    def __init__(
        self,
    ) -> None:
        self.state = ReinforcementState.IDLE
