from dataclasses import dataclass, field

from .lifecycle import Lifecycle


@dataclass
class BaseContext:

    lifecycle: Lifecycle = field(default_factory=Lifecycle)
