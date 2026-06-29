from dataclasses import dataclass

from .cognition_state import CognitionState


@dataclass(frozen=True)
class CognitionSnapshot:

    state: CognitionState
