from dataclasses import dataclass

from .component import Component


@dataclass
class HealthComponent(Component):

    value: float = 100.0
