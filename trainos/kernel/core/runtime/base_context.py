from dataclasses import dataclass

from .lifecycle import Lifecycle


@dataclass
class BaseContext:

    lifecycle: Lifecycle = Lifecycle()
