from dataclasses import dataclass

from .action_type import (
    ActionType,
)


@dataclass
class ActionRecord:
    action: ActionType
