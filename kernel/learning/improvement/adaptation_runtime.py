from .adaptation_state import AdaptationState


class AdaptationRuntime:

    def __init__(
        self,
    ) -> None:
        self.state = AdaptationState.IDLE
