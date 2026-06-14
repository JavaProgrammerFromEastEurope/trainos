from dataclasses import dataclass

from .component import Component


@dataclass
class MemoryComponent(Component):

    capacity: int = 128
