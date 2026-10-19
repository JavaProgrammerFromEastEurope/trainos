from dataclasses import dataclass

from .environment_state import EnvironmentState


@dataclass
class EnvironmentSnapshot:

    state: EnvironmentState
