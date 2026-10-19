from .meta_state import MetaState


class MetaRuntime:

    def __init__(
        self,
    ) -> None:
        self.state = MetaState.IDLE
