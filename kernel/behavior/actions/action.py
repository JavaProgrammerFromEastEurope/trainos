from __future__ import annotations

from .action_context import (
    ActionContext,
)

from .action_result import (
    ActionResult,
)

from .action_status import (
    ActionStatus,
)


class Action:

    def execute(
        self,
        context: ActionContext,
    ) -> ActionResult:
        return ActionResult(
            status=ActionStatus.SUCCESS,
        )
