from dataclasses import dataclass

from .goap_action import (
    GOAPAction,
)


@dataclass
class GOAPNode:

    action: GOAPAction
