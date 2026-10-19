from __future__ import annotations

from .action import (
    Action,
)

from .action_type import (
    ActionType,
)


class ActionRegistry:

    def __init__(
        self,
    ) -> None:
        self._actions: dict[
            ActionType,
            Action,
        ] = {}

    def register(
        self,
        action_type: ActionType,
        action: Action,
    ) -> None:
        self._actions[action_type] = action

    def get(
        self,
        action_type: ActionType,
    ) -> Action | None:
        return self._actions.get(
            action_type,
        )
