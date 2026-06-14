from dataclasses import dataclass

from .component import Component


@dataclass
class GoalComponent(Component):

    goal: str = ""
