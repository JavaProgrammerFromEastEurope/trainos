from dataclasses import dataclass

from .action_status import (
    ActionStatus,
)


@dataclass
class ActionResult:
    status: ActionStatus
    message: str = ""
