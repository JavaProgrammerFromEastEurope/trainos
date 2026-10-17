from kernel.behavior.actions.action import (
    Action,
)

from kernel.behavior.actions.action_context import ActionContext
from kernel.behavior.actions.action_status import ActionStatus


def test_actions():

    action = Action()
    result = action.execute(ActionContext())

    assert result.status == ActionStatus.SUCCESS
