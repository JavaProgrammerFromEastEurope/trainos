from dataclasses import dataclass

from .htn_task import (
    HTNTask,
)


@dataclass
class HTNNode:

    task: HTNTask
