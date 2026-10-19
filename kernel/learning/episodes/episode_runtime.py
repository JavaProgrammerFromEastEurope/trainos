from .episode_state import (
    EpisodeState,
)


class EpisodeRuntime:

    def __init__(
        self,
    ) -> None:
        self.state = EpisodeState.RUNNING
