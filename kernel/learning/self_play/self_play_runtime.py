from .self_play_state import SelfPlayState


class SelfPlayRuntime:

    def __init__(
        self,
    ) -> None:
        self.state = SelfPlayState.IDLE
