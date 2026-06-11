# kernel/runtime/runtime_state.py

from __future__ import annotations

from enum 	import Enum


class RuntimeState(Enum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED 	= "paused"
    STOPPED = "stopped"
