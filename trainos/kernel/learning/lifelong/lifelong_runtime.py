from .lifelong_state import LifelongState


class LifelongRuntime:

    def __init__(self) -> None:
        self.state = LifelongState.STOPPED
