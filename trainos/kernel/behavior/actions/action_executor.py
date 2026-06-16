from __future__ import annotations

from .action import (
    Action,
)

from .action_context import (
    ActionContext,
)

from .action_result import (
    ActionResult,
)


class ActionExecutor:

    def execute(
        self,
        action: Action,
        context: ActionContext,
    ) -> ActionResult:
        return action.execute(
            context,
        )
