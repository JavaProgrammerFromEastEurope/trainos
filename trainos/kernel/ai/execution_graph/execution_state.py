from __future__ import annotations

from dataclasses import dataclass
from .execution_status import (
    ExecutionStatus,
)


@dataclass
class ExecutionState:
  
    node_id: str
    status: ExecutionStatus
