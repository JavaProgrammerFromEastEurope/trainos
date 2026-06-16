from dataclasses import dataclass

from .goap_action import (
    GOAPAction,
)


@dataclass
class GOAPPlan:

    actions: list[GOAPAction]
