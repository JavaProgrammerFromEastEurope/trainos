from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass
class StateObserver:

    key: str
    callback: Callable[
        [str, object, object],
        None,
    ]
