from dataclasses import dataclass

from .lifecycle_state import LifecycleState


@dataclass
class Lifecycle:

    state: LifecycleState = LifecycleState.CREATED

    def transition(self, new_state: LifecycleState) -> None:
        self.state = new_state
